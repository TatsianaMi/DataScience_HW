import requests
import pandas as pd
from .utils.serviceDataAPI import DataAPI
from datetime import datetime
from datetime import timezone
import kagglehub

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel("INFO")

def fromCSV():
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d Time %H:%M:%S+00:00")
    logger.info(f"Fetching file by url on {timestamp} UTC")
    
    path = kagglehub.dataset_download("beridzeg45/diamonds-prices-prediction")
    print("Path to dataset files:", path)
    df = pd.read_csv(path+'/diamonds (cleaned).csv')
    return df

def fromAPI():
  api_key = "API-KEY"
  file_name="TEST-FILE-NAME"
  api = DataAPI(api_token=api_key)
  response = api.get_file(file_name)
  if "error" in response:
        logger.error(f"Unable to retrieve file: {response['error']}")
        sys.exit(1)
  return pd.json_normalize(response)