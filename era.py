import json
import requests

api_key='325508beeb37434f8bcf8e29'
api_url=f'https://v6.exchangerate-api.com/v6/{api_key}/latest/'

sat_doviz=input("Satmak istediğiniz döviz türü nedir?:")#USD TRY gibi
al_doviz=input("Almak istediğiniz döviz türü nedir?:")#USD TRY gibi

miktar_doviz=int(input(f"Satmak istediğiniz {sat_doviz} miktarını girin:"))
get_datas=requests.get(api_url+sat_doviz)
get_datas_fromJson=json.loads(get_datas.text)

print(f"alacağınız tutar:{miktar_doviz*get_datas_fromJson['conversion_rates'][al_doviz]} {al_doviz}")
