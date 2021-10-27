import random

from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render


def index(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    return render(request, 'server/index.html')



def products(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    result = [
        {'name': 'Zeckenschlinge', 'brand': '3iX', 'location': 'G072', 'status': 'new', 'bestBefore': None, 'quantity': 1440, 'productId': 1, 'image': 'https://images-na.ssl-images-amazon.com/images/I/81nfHPn5JpL._SL75_.jpg'},
        {'name': 'Zeckenschlinge', 'brand': '3iX', 'location': 'G072', 'status': 'reserved', 'bestBefore': None,'quantity': 204, 'productId': 1, 'image': 'https://images-na.ssl-images-amazon.com/images/I/81nfHPn5JpL._SL75_.jpg'},
        {'name': 'Weihnachts Cashew, 100g', 'brand': 'Lindt', 'location': 'G072', 'status': 'new', 'bestBefore': '2022-10-18', 'quantity': 129, 'productId': 2, 'image': ''},
        {'name': 'DROPS Chocolate Drops Vollmilch, 750g', 'brand': 'Xucker', 'location': 'G072', 'status': 'new', 'bestBefore': '2023-07-01', 'quantity': 400, 'productId': 3, 'image': 'https://images-na.ssl-images-amazon.com/images/I/81HHUeGWquL._SL75_.jpg'},
        {'name': 'DROPS Chocolate Drops Vollmilch, 750g', 'brand': 'Xucker', 'location': 'G072', 'status': 'new', 'bestBefore': '2025-02-28', 'quantity': 650, 'productId': 3, 'image': 'https://images-na.ssl-images-amazon.com/images/I/81HHUeGWquL._SL75_.jpg'},
        {'name': 'DROPS Chocolate Drops Vollmilch, 750g', 'brand': 'Xucker', 'location': 'G072', 'status': 'reserved', 'bestBefore': '2023-07-01', 'quantity': 150, 'productId': 3, 'image': 'https://images-na.ssl-images-amazon.com/images/I/81HHUeGWquL._SL75_.jpg'},
        {'name': 'DROPS Chocolate Drops Vollmilch, 750g', 'brand': 'Xucker', 'location': 'G072', 'status': 'reserved', 'bestBefore': '2025-02-28', 'quantity': 250, 'productId': 3, 'image': 'https://images-na.ssl-images-amazon.com/images/I/81HHUeGWquL._SL75_.jpg'},
        {'name': 'Erfrischender Ingwer Orange, 32,4g', 'brand': 'Teekanne', 'location': 'G072', 'status': 'new', 'bestBefore': '2024-05-17', 'quantity': 2000, 'productId': 4, 'image': 'https://images-na.ssl-images-amazon.com/images/I/51BQxXy%2BnNL._SL75_.jpg'},
        {'name': 'Erfrischender Ingwer Orange, 32,4g', 'brand': 'Teekanne', 'location': 'G072', 'status': 'reserved', 'bestBefore': '2024-05-17', 'quantity': 640, 'productId': 4, 'image': 'https://images-na.ssl-images-amazon.com/images/I/51BQxXy%2BnNL._SL75_.jpg'},
        {'name': 'Erfrischender Ingwer Orange, 32,4g', 'brand': 'Teekanne', 'location': 'G072', 'status': 'reserved', 'bestBefore': '2023-12-31', 'quantity': 180, 'productId': 4, 'image': 'https://images-na.ssl-images-amazon.com/images/I/51BQxXy%2BnNL._SL75_.jpg'},
        {'name': 'Erfrischender Ingwer Orange, 32,4g', 'brand': 'Teekanne', 'location': 'G072', 'status': 'reserved', 'bestBefore': '2023-09-06', 'quantity': 180, 'productId': 4, 'image': 'https://images-na.ssl-images-amazon.com/images/I/51BQxXy%2BnNL._SL75_.jpg'},
        {'name': 'Erfrischender Ingwer Orange, 32,4g', 'brand': 'Teekanne', 'location': 'G072', 'status': 'damaged', 'bestBefore': '2024-05-17', 'quantity': 17, 'productId': 4, 'image': 'https://images-na.ssl-images-amazon.com/images/I/51BQxXy%2BnNL._SL75_.jpg'},
    ]
    random.shuffle(result)
    return JsonResponse(result, safe=False)
