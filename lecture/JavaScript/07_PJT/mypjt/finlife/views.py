from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import DepositProducts, DepositOptions
from .serializers import DepositProductsSerializer, DepositOptionsSerializer
import requests
from django.http import JsonResponse
from django.db.models import Max

BASE_URL = 'https://finlife.fss.or.kr/finlife/main/contents.do?menuNo=700029'

# Create your views here.
@api_view(['GET'])
def api_test(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth': settings.API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    response = requests.get(URL, params=params).json()
    return JsonResponse({'response': response})


# requests 모듈을 활용하여 정기예금 상품 목록 데이터를 가져와
# 정기예금 상품 목록과 옵션목록을 DB에 저장 (GET)  

# @api_view(['GET'])
# def save_deposit_products(request):
#     URL = BASE_URL + 'depositProductsSearch.json'
#     params = {
#         'auth': settings.API_KEY,
#         'topFinGrpNo': '020000',
#         'pageNo': 1
#     }
#     response = requests.get(URL, params=params).json()
#     for item in response['result']['baseList']:
#         serializer = DepositProductsSerializer(data=item)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#     for item in response['result']['optionList']: 
#         for key in item.keys():      
#             if item[key] is None:
#                 item[key] = -1
#         serializer = DepositOptionsSerializer(data=item)
#         product = DepositProducts.objects.get(fin_prdt_cd=item['fin_prdt_cd'])
        
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(fin_prdt_cd = product)    

@api_view(['GET'])
def save_deposit_products(request):
    api_key = settings.API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1&type=json'
    requestData = requests.get(url)
    jsonData = None
    if requestData.status_code == 200:
        jsonData = requestData.json()
        product_list = jsonData.get('result').get('baseList') 
        for item in product_list:
            serializer = DepositProductsSerializer(data=item)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            
        option_list = jsonData.get('result').get('optionList')
        for item in option_list:
            product = DepositProducts.objects.get(fin_prdt_cd=item.get('fin_prdt_cd'))
            item['intr_rate'] = -1 if item.get('intr_rate') == None else item.get('intr_rate')
            item['intr_rate2'] = -1 if item.get('intr_rate2') == None else item.get('intr_rate2')
            
            serializer = DepositOptionsSerializer(data=item)
            print(serializer)
            if serializer.is_valid(raise_exception=True):
                serializer.save(fin_prdt_cd=product)
    
    return JsonResponse({'message': 'okay'})



@api_view(['GET', 'POST'])
def deposit_products(request):
    
    # GET: 전체 정기예금 상품 목록 반환
    if request.method == 'GET':
        products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(products, many=True)
        return Response(serializer.data)
    
    # POST: 상품 데이터 저장
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


# 특정 상품의 옵션 리스트 반환 (GET)
@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
    options = product.options.all()
    serializer = DepositOptionsSerializer(options, many=True)
    return Response(serializer.data)

# 가입 기간에 상관없이 금리가 가장 높은 상품과 해당 상품의 옵션 리스트 출력 (GET)
@api_view(['GET'])
def top_rate(request):
    top_product = DepositOptions.objects.aggregate(intr_rate2=Max("intr_rate2"))
    # print(top_product)
    option = DepositOptions.objects.filter(intr_rate2=top_product['intr_rate2']).first()
    # print(option)
    product = DepositProducts.objects.get(id = option.fin_prdt_cd_id)
    options = product.options.all()
    serializer_product = DepositProductsSerializer(product)
    serializer_option = DepositOptionsSerializer(options, many=True)
    return Response({
        'deposit_product': serializer_product.data,
        'options' : serializer_option.data,
    })