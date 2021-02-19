import json
import pandas as pd
from itertools import zip_longest

completelist, finalelist = [] , []
itemValue = 'pricePerUnit'
listKeys = ['instanceType', 'memory', 'vcpu', 'storage', 'networkPerformance', 'tenancy']

with open('/Users/mahdifrid/Desktop/PricingCloud/file.json', 'r') as data : 
    json_data = json.load(data)

# function get instance type
for i in range(len(json_data)):
    listsUnits = {}
    instanceType = (json_data[i]["product"]["attributes"])
    for key, value in instanceType.items():
        for keyInstance in listKeys :
            if key in keyInstance:
                listsUnits.update({key:value}) 
    completelist.append(listsUnits)


# function get pricing list            
for i in range(len(json_data)):
    listUnitsmatch = {}
    listPricesinstance = {}
    termsInstance = (json_data[i]["terms"]["OnDemand"])
    pricingItems = [dict_pricing['priceDimensions'] for dict_pricing in termsInstance.values()]  
    princingUnit = json.dumps(pricingItems)
    unitDict = json.loads(princingUnit)
    for element in unitDict:
        for key, value in element.items():
            listPricesinstance = value
    for key, value in listPricesinstance.items():
        if key in itemValue:
            listUnitsmatch.update(value)
    finalelist.append(listUnitsmatch)

listec2Instance = [{**u, **v} for u, v in zip_longest(completelist, finalelist, fillvalue={})]
print(json.dumps(listec2Instance, indent=4))