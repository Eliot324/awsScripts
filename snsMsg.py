
import boto3

ak='' #accesskey
sak=''  #secret AccessKEy

client = boto3.client(
                      "sns",
                      aws_access_key_id=ak,
                      aws_secret_access_key=sak,
                      region_name="us-east-1"
                      )


while True:
    
    client.publish(
                   PhoneNumber='',
                   Message=''
                   )
