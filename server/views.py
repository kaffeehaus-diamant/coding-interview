import random

from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render


def index(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    return render(request, 'server/index.html')


def products(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    result = [
        {'name': 'Zeckenschlinge', 'brand': '3iX', 'location': 'G072', 'status': 'new', 'bestBefore': None,
         'quantity': 1440, 'productId': 1,
         'image': 'https://images-na.ssl-images-amazon.com/images/I/81nfHPn5JpL._SL75_.jpg'},
        {'name': 'Zeckenschlinge', 'brand': '3iX', 'location': 'G072', 'status': 'reserved', 'bestBefore': None,
         'quantity': 204, 'productId': 1,
         'image': 'https://images-na.ssl-images-amazon.com/images/I/81nfHPn5JpL._SL75_.jpg'},
        {'name': 'DROPS Chocolate Drops Vollmilch, 750g', 'brand': 'Xucker', 'location': 'G072', 'status': 'new',
         'bestBefore': '2023-07-01', 'quantity': 400, 'productId': 3,
         'image': 'https://images-na.ssl-images-amazon.com/images/I/81HHUeGWquL._SL75_.jpg'},
        {'name': 'DROPS Chocolate Drops Vollmilch, 750g', 'brand': 'Xucker', 'location': 'G072', 'status': 'new',
         'bestBefore': '2025-02-28', 'quantity': 650, 'productId': 3,
         'image': 'https://images-na.ssl-images-amazon.com/images/I/81HHUeGWquL._SL75_.jpg'},
        {'name': 'DROPS Chocolate Drops Vollmilch, 750g', 'brand': 'Xucker', 'location': 'G072', 'status': 'reserved',
         'bestBefore': '2023-07-01', 'quantity': 150, 'productId': 3,
         'image': 'https://images-na.ssl-images-amazon.com/images/I/81HHUeGWquL._SL75_.jpg'},
        {'name': 'DROPS Chocolate Drops Vollmilch, 750g', 'brand': 'Xucker', 'location': 'G072', 'status': 'reserved',
         'bestBefore': '2025-02-28', 'quantity': 250, 'productId': 3,
         'image': 'https://images-na.ssl-images-amazon.com/images/I/81HHUeGWquL._SL75_.jpg'},
        {'name': 'Xylit Schokolade Tafel "Vollmilch", 80g, 1 VE = 10 Stück', 'brand': 'Xucker', 'location': 'G072',
         'status': 'new', 'bestBefore': '2024-06-13', 'quantity': 117, 'productId': 4,
         'image': 'https://m.media-amazon.com/images/I/71O-S0-WI3L._AC_UY218_.jpg'},
        {'name': 'Xylit Schokolade Tafel "Vollmilch", 80g, 1 VE = 10 Stück', 'brand': 'Xucker', 'location': 'G072',
         'status': 'new', 'bestBefore': '2025-08-17', 'quantity': 225, 'productId': 4,
         'image': 'https://m.media-amazon.com/images/I/71O-S0-WI3L._AC_UY218_.jpg'},
        {'name': 'Xylit Schokolade Tafel "Vollmilch", 80g, 1 VE = 10 Stück', 'brand': 'Xucker', 'location': 'G072',
         'status': 'reserved', 'bestBefore': '2023-07-01', 'quantity': 280, 'productId': 4,
         'image': 'https://m.media-amazon.com/images/I/71O-S0-WI3L._AC_UY218_.jpg'},
        {'name': 'Erfrischender Ingwer Orange, 32,4g', 'brand': 'Teekanne', 'location': 'G072', 'status': 'new',
         'bestBefore': '2024-05-17', 'quantity': 2000, 'productId': 5,
         'image': 'https://images-na.ssl-images-amazon.com/images/I/51BQxXy%2BnNL._SL75_.jpg'},
        {'name': 'Erfrischender Ingwer Orange, 32,4g', 'brand': 'Teekanne', 'location': 'G072', 'status': 'reserved',
         'bestBefore': '2024-05-17', 'quantity': 640, 'productId': 5,
         'image': 'https://images-na.ssl-images-amazon.com/images/I/51BQxXy%2BnNL._SL75_.jpg'},
        {'name': 'Erfrischender Ingwer Orange, 32,4g', 'brand': 'Teekanne', 'location': 'G072', 'status': 'reserved',
         'bestBefore': '2023-12-31', 'quantity': 180, 'productId': 5,
         'image': 'https://images-na.ssl-images-amazon.com/images/I/51BQxXy%2BnNL._SL75_.jpg'},
        {'name': 'Erfrischender Ingwer Orange, 32,4g', 'brand': 'Teekanne', 'location': 'G072', 'status': 'reserved',
         'bestBefore': '2023-09-06', 'quantity': 180, 'productId': 5,
         'image': 'https://images-na.ssl-images-amazon.com/images/I/51BQxXy%2BnNL._SL75_.jpg'},
        {'name': 'Erfrischender Ingwer Orange, 32,4g', 'brand': 'Teekanne', 'location': 'G072', 'status': 'damaged',
         'bestBefore': '2024-05-17', 'quantity': 17, 'productId': 5,
         'image': 'https://images-na.ssl-images-amazon.com/images/I/51BQxXy%2BnNL._SL75_.jpg'},
        {'name': 'Ländertee Schwedische Blaubeere, 45g', 'brand': 'Teekanne', 'location': 'G072', 'status': 'new',
         'bestBefore': '2022-02-12', 'quantity': 860, 'productId': 10,
         'image': 'https://images-na.ssl-images-amazon.com/images/I/51a81kA8j2L._SL75_.jpg'},
        {'name': 'Ländertee Schwedische Blaubeere, 45g', 'brand': 'Teekanne', 'location': 'G072', 'status': 'new',
         'bestBefore': '2025-05-15', 'quantity': 430, 'productId': 10,
         'image': 'https://images-na.ssl-images-amazon.com/images/I/51a81kA8j2L._SL75_.jpg'},
        {'name': 'Ländertee Schwedische Blaubeere, 45g', 'brand': 'Teekanne', 'location': 'G072', 'status': 'new',
         'bestBefore': '2023-03-23', 'quantity': 610, 'productId': 10,
         'image': 'https://images-na.ssl-images-amazon.com/images/I/51a81kA8j2L._SL75_.jpg'},
        {'name': 'Ländertee Schwedische Blaubeere, 45g', 'brand': 'Teekanne', 'location': 'G072', 'status': 'new',
         'bestBefore': '2024-04-14', 'quantity': 250, 'productId': 10,
         'image': 'https://images-na.ssl-images-amazon.com/images/I/51a81kA8j2L._SL75_.jpg'},
        {'name': 'Ländertee Schwedische Blaubeere, 45g', 'brand': 'Teekanne', 'location': 'G072', 'status': 'new',
         'bestBefore': '2025-09-30', 'quantity': 940, 'productId': 10,
         'image': 'https://images-na.ssl-images-amazon.com/images/I/51a81kA8j2L._SL75_.jpg'},
    ]
    random.shuffle(result)
    return JsonResponse(result, safe=False)
