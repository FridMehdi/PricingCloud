from extract_ec2_data import *
from load_ec2_data import *  
from s3_ec2_data import * 
import json
from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

# if __name__ == "__main__":
#     bucketName = 'ec2pricing'
#     region = 'EU (Paris)'
#     finalelist = [] 
#     #Create Bucket to store files 
#     make_bucket(bucketName)
    
#     #Get Prices and infos about EC2 instances from Api AWS 
#     data = get_products(region)

#     #Load data from OBS and convert, extract data needed

#     ec2_description = aws_get_ec2_description(data)
#     ec2_payg_prices = aws_ec2_ondemand_price(data)
    
#     #Merge EC2 data with prices 
#     prices_ec2 = [{**u, **v} for u, v in zip_longest(ec2_description, ec2_payg_prices, fillvalue={})]

#     #Load finale data to OBS
#     with open ('jsonfiles/data.json', 'w') as outfile_ec2 : 
#         json.dump(prices_ec2, outfile_ec2)
    
#     upload_file_to_bucket(bucketName,'jsonfiles/data.json')
#     download_file_from_bucket(bucketName,'data.json','jsonfiles/instances_EC2.json')