import json

listsUnits = {}
completelist = []
itemValue = 'pricePerUnit'
listKeys = ['instanceType', 'memory', 'vcpu', 'storage', 'networkPerformance', 'tenancy']

with open('/Users/mahdifrid/Desktop/file.json', 'r') as data : 
    json_data = json.load(data)

instanceType = (json_data["product"]["attributes"])
for key, value in instanceType.items():
    for keyInstance in listKeys :
        if key in keyInstance:
            completelist.append("{}: {}".format(key, value)) 


termsInstance = (json_data["terms"]["OnDemand"])
pricingItems = [dict_pricing['priceDimensions'] for dict_pricing in termsInstance.values()]

princingUnit = json.dumps(pricingItems)
unitDict = json.loads(princingUnit)
for element in unitDict:
    for key, value in element.items():
        listsUnits = value

for key, value in listsUnits.items():
    if key in itemValue:
        completelist.append("{}: {}".format(key, value)) 

print(completelist)
print(len(completelist))

#print((json_data["product"]["attributes"]["instanceType"])+": "+(json_data["product"]["attributes"]["memory"])+ ".RAM")

