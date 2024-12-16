import pandas as pd
import os
from datetime import datetime
import configparser
import logging
from datetime import datetime


# 讀取 config.ini 檔案
config = configparser.ConfigParser()
config.read("config.ini", encoding="utf-8")

# 獲取共用設定
log_folder = config["General"]["log_folder"]
output_folder = config["General"]["output_folder"]

# 根據日期生成日誌檔案名稱並添加路徑
log_filename = os.path.join(log_folder, datetime.now().strftime("%Y-%m-%d.log"))

# 設定日誌配置
logging.basicConfig(
    filename = log_filename,
    level = logging.ERROR,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    encoding = "utf-8"
)

# 確保 log 資料夾存在
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

try:
    # 遍歷配置檔案中的所有 Excel 組
    for section in config.sections():
        if section.startswith("Excel_"):
            file_path = config[section]["file_path"]
            sheet_name = config[section]["sheet_name"]
            column_name = config[section]["column_name"]

            # 建立根資料夾（output_folder）下的工作表資料夾
            sheet_folder = os.path.join(output_folder, sheet_name)
            if not os.path.exists(sheet_folder):
                os.makedirs(sheet_folder)
                print(f"工作表資料夾 '{sheet_folder}' 已建立")
            else:
                print(f"工作表資料夾 '{sheet_folder}' 已存在")

            # 載入 Excel 檔案
            try:
                # 確保載入 Excel 資料夾存在
                if not os.path.exists(file_path):
                    logging.error(f"無法讀取 Excel 檔案 '{file_path}'\n{section} 指定資料夾不存在\n")
                    print(f"無法讀取 Excel 檔案 '{file_path}'\n'{section}' 指定資料夾不存在\n")
                    continue
                df = pd.read_excel(file_path, sheet_name=sheet_name, engine="openpyxl")
            except Exception as e:
                logging.error(f"無法讀取 Excel 檔案 '{file_path}' 或工作表 '{sheet_name}': {e}\n")
                print(f"無法讀取 Excel 檔案 '{file_path}' 或工作表 '{sheet_name}': {e}")
                continue

            # 確保指定欄位存在
            if column_name in df.columns:
                folder_names = df[column_name].dropna().unique()  # 獲取不重複且非空的資料夾名稱
                for folder_name in folder_names:
                    folder_name = str(folder_name).strip()
                    full_path = os.path.join(sheet_folder, folder_name)
                    try:
                        if not os.path.exists(full_path):
                            os.makedirs(full_path)
                            print(f"資料夾 '{full_path}' 已建立")
                        else:
                            print(f"資料夾 '{full_path}' 已存在")
                    except Exception as e:
                        logging.error(f"無法建立資料夾 '{full_path}': {e}\n")
                        print(f"無法建立資料夾 '{full_path}', 已記錄於日誌")
            else:
                logging.error(f"指定欄位 '{column_name}' 不存在於工作表 '{sheet_name}' 中\n")
                print(f"指定欄位 '{column_name}' 不存在於工作表 '{sheet_name}' 中")
except Exception as e:
    logging.error(f"Exception error")
    print(f"Exception error")