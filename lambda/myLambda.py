import boto3
import time
import tempfile
from boto3 import client

#Following lambda triggers when an object is uploaded to the s3 bucket, and populates the dynamodb Table.
def lambda_handler(event, context):
    myBucketName = ''
    #print(event['Records']['key'])
    #print(context)
    conn = client('s3')
    #dynamodb = boto3.resource('dynamodb')
    #table = dynamodb.Table('ixcloud-phase1-d')
    
    
    eventKey = event['Records'][0]['s3']['object']['key']
    k = conn.head_object(Bucket = 'ixia-product-update', Key = eventKey)
    #m = k["Metadata"]
    #bno = m['buildno']
    #print (bno)
    
    file= open("/tmp/latest_upload.txt","w+")
    #file.write("%s" % bno)
    timestamp = time.time()
    file.write("%s" %timestamp)
    file.close()

    #object_path = m['packagename'] + "/version_info.txt"
    object_path =  "/version_info.txt"
    conn.upload_file("/tmp/latest_upload.txt", 'ixia-product-update', object_path)
    """
    try:
        table.put_item(
           Item={
                'guid': str(event['Records'][0]['eventTime']),
                'buildno': m['buildno'],
                'channel': m['channel'],
                'releasetrack': m['releasetrack'],
                'packagename': m['packagename'],
                's3objectname': eventKey
                
            }
        )        
    except:
        print('Error while trying to write DB')
    """ 
    
