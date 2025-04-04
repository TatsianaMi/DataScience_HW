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

def fromKaggelhubCSV(kagglehub_path: str, csv_file_name: str):
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d Time %H:%M:%S+00:00")
    logger.info(f"Fetching file by url on {timestamp} UTC")
    
    path = kagglehub.dataset_download(kagglehub_path)
    df = pd.read_csv(path+'/'+csv_file_name)
    return df

