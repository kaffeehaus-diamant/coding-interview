from collections import defaultdict
from contextlib import AbstractContextManager
from contextlib import contextmanager
from datetime import timedelta
import os
import re
import time
from typing import NamedTuple

from django.db import connection


class QueryStatistics:
    @classmethod
    @contextmanager
    def measure(cls) -> AbstractContextManager['QueryStatistics']:
        stats = QueryStatistics()
        try:
            with connection.execute_wrapper(stats._measure_queries):
                yield stats
        finally:
            stats._total_duration += stats.current_duration

    def __init__(self):
        self._stats = defaultdict(lambda: _QueryStatisticsEntry(count=0, duration=0))
        self._total_duration = 0
        self._start = time.monotonic()

    def _measure_queries(self, execute, sql: str, params, many, context) -> None:
        start = time.monotonic()
        try:
            return execute(sql, params, many, context)
        finally:
            duration = time.monotonic() - start
            self._stats[self._normalize_query(sql)] += duration

    @classmethod
    def _normalize_query(cls, sql: str) -> str:
        normalized_whitespace = re.sub(r'\s+', ' ', sql.strip())
        normalized_params = re.sub(r'\( ?%s(, ?%s)* ?\)', '(%s, ...)', normalized_whitespace)
        return normalized_params

    @property
    def current_duration(self) -> float:
        return time.monotonic() - self._start

    @property
    def total_duration(self) -> float:
        return self._total_duration

    @property
    def total_query_duration(self) -> float:
        return sum(stats.duration for stats in self._stats.values())

    @property
    def total_query_count(self) -> int:
        return sum(stats.count for stats in self._stats.values())

    @property
    def unique_query_count(self):
        return len(self._stats)

    def dump(self) -> None:
        try:
            terminal_width, _ = os.get_terminal_size()
        except OSError:
            terminal_width = 78

        self._print_details(terminal_width)
        self._print_summary()

    def _print_details(self, print_width: int) -> None:
        print_width = max(20, print_width - 6)

        for query, stats in sorted(self._stats.items(), key=lambda pair: pair[1]):
            print(f'{stats.count:,} similar queries in {stats.duration:.1f}s:')
            for start in range(0, len(query), print_width):
                print('    ', query[start:start + print_width])

    def _print_summary(self):
        if self._stats:
            sql_rate = self.total_query_duration / self.total_duration if self.total_duration else float('NaN')
            print(f'Executed {self.total_query_count:,} ({self.unique_query_count:,} unique) queries'
                  f' in {self.total_duration:.1f}s (sql time: {self.total_query_duration:.1f}s; {sql_rate:.1%}).')


class _QueryStatisticsEntry(NamedTuple):
    count: int
    duration: float

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return _QueryStatisticsEntry(count=self.count + 1, duration=self.duration + other)
        elif isinstance(other, timedelta):
            return _QueryStatisticsEntry(count=self.count + 1, duration=self.duration + other.total_seconds())
        elif hasattr(other, 'count') and hasattr(other, 'duration'):
            return _QueryStatisticsEntry(count=self.count + other.count, duration=self.duration + other.duration)
        else:
            return NotImplemented

    __radd__ = __add__
