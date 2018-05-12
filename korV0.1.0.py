import requests
import json

response = requests.get("https://tradingeconomics.com/united-states/indicators")
jsonResponse = ((response.text.split('angular.callbacks._3('))[0].split(');')[0])
data = json.loads(jsonResponse)
print(data["grid_layout"])
grid_data = data["grid_layout"]



#for grid_item in grid_data:
#    print("Brand:", grid_item["brand"])
#    print("Product Name:", grid_item["name"])
#    print("Current Price: Rs", grid_item["offer_price"])
#    print("==================")
