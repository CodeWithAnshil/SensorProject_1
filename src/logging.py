import logging
import os
from datetime import datetime


LOG_File = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

Log_path =  os.path.join(os.getcwd(),"logs",LOG_File)

os.makedirs(Log_path,exist_ok=True)

LOG_File_Path = os.path.join(Log_path,LOG_File)

logging.basicConfig(
  filename=LOG_File_Path,
  format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
  level=logging.INFO
)

