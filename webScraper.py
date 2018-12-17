from bs4 import BeautifulSoup
import boto3
import requests
import datetime
from decimal import *
import datetime
import time
strings = time.strftime("%Y,%m,%d,%H,%M,%S")
print(strings)
ACCESS_KEY_ID = ''
ACCESS_SECRET_KEY = ''

headers = {
    "User-Agent": "my web scraping program. contact me at EMAIL@gmail.com"
}



page_response = requests.get("https://www.investing.com/commodities/gold", headers=headers, timeout=5)


page_content = BeautifulSoup(page_response.content, "html.parser")
var=page_content.find(id="ENTER id or change what your looking for").text.strip()

var = var.replace(',', '') #replaces , so you can strip prices like 34,00 to 34000
var= Decimal(var)

dynamodb = boto3.resource('dynamodb', region_name='us-east-2', endpoint_url="https://dynamodb.us-east-2.amazonaws.com", aws_access_key_id=ACCESS_KEY_ID,
                          aws_secret_access_key=ACCESS_SECRET_KEY)
#write to dynamo

dynamoTable = dynamodb.Table('TABLE NAME')
dynamoTable.put_item(
                     Item= {
                     "Name": strings,
                     "Value": var
                     
                     }
                     )

