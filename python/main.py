import imp
from google.cloud import storage
from datetime import datetime
from time import sleep
from common_utils import is_not_empty

import os

bucket_name = os.environ['GCS_BUCKET_NAME']
file_name = os.environ['BUCKET_FILENAME']
wait_time = int(os.environ['WAIT_TIME'])

gcs_client = storage.Client()

while True:
    vdate = datetime.now()
    
    try:
        bucket = gcs_client.bucket(bucket_name)
        blob = bucket.blob(file_name)
        line = "Written at {}".format(vdate.isoformat())

        with blob.open(mode='w') as f:
            f.write(line)
    except Exception as e:
        print("Unexpected error : {}".format(e))
    
    print(line)
    sleep(wait_time)
