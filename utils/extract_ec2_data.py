import json
import pandas as pd
from itertools import zip_longest

def load_data(filepath) :
    with open(filepath, 'r') as data : 
        json_data = json.load(data)
    return json_data

def aws_get_ec2_description(data):
    listKeys = ['instanceType', 'memory', 'vcpu', 'storage', 'networkPerformance', 'tenancy']
    completelist = []
    for i in range(len(data)):
        listsUnits = {}
        instanceType = (data[i]["product"]["attributes"])
        for key, value in instanceType.items():
            for keyInstance in listKeys :
                if key in keyInstance:
                    listsUnits.update({key:value}) 
        completelist.append(listsUnits)
    return completelist


def aws_ec2_ondemand_price(data):
    itemValue = 'pricePerUnit'
    finalelist = []     
    for i in range(len(data)):
        listUnitsmatch = {}
        listPricesinstance = {}
        termsInstance = (data[i]["terms"]["OnDemand"])
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
    return finalelist
    