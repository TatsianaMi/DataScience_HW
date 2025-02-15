import pandas as pd
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
    
    path = kagglehub.dataset_download("habedi/developer-salary-survey-data-norway-2024")
    df = pd.read_csv(path+'/salaries.csv')
    return df