import subprocess
import pandas as pd
import json
import requests

def azure_get_vm_pricing(data):
    d = data['Items']
    listKeys = ['armSkuName','reservationTerm', 'retailPrice', 'unitPrice', 'productName', 'unitOfMeasure']
    completelist = []
    for i in range(len(d)):
        listsUnits = {}
        instanceType = (d[i])
        for key, value in instanceType.items():
            for item in listKeys :
                if key in item:
                    listsUnits.update({key:value}) 
        completelist.append(listsUnits)
    return completelist

def azure_get_vm_pricing_1Year(data):
    finalelist = []
    for item in data :
        for key, val in item.items():
            if val == "1 Year":
                finalelist.append(item)
    return finalelist

def main():
    res = requests.get("https://prices.azure.com/api/retail/prices?$filter= armSkuName eq 'Standard_F8' and armRegionName eq 'francecentral' and priceType eq 'Reservation'")
    json_data = json.loads(res.text)
    data = (azure_get_vm_pricing(json_data))
    finaldata = (azure_get_vm_pricing_1Year(data))
    print(finaldata)
    
    
    
if __name__ == "__main__":
    # execute only if run as a script
    main()
