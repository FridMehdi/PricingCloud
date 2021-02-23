from utils.extract_ec2_data import *
from utils.load_ec2_data import *  
from utils.s3_ec2_data import * 
import json
from typing import Optional, List
from fastapi import FastAPI, Query
from starlette.responses import FileResponse

app = FastAPI()


@app.get("/ec2/Ondemand/{region_id}/")
def read_ec2_Ondemand(region_id: str = None,list_ec2_instances: Optional[List[str]]= Query(None)):
    bucketName = 'ec2pricing'
    #Create Bucket to store files 
    make_bucket(bucketName)
    
    #Get Prices and infos about EC2 instances from Api AWS 
    data = get_products(region_id, list_ec2_instances)

    #Load data from OBS and convert, extract data needed

    ec2_description = aws_get_ec2_description(data)
    ec2_payg_prices = aws_ec2_ondemand_price(data)
    
    #Merge EC2 data with prices 
    prices_ec2 = [{**u, **v} for u, v in zip_longest(ec2_description, ec2_payg_prices, fillvalue={})]

    #Load finale data to OBS
    with open ('jsonfiles/data.json', 'w') as outfile_ec2 : 
        json.dump(prices_ec2, outfile_ec2)
    
    upload_file_to_bucket(bucketName,'jsonfiles/data.json')
    download_file_from_bucket(bucketName,'data.json','jsonfiles/instances_EC2.json')
    return FileResponse("jsonfiles/instances_EC2.json", media_type='application/octet-stream',filename="instances_EC2.json")    