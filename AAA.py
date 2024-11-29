import logging

# 設定日誌配置，使用 UTF-8 編碼以支援中文
logging.basicConfig(
    filename="error.log",         # 日誌檔案名稱
    level=logging.ERROR,          # 只記錄錯誤級別的訊息
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"              # 指定 UTF-8 編碼
)

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logging.error("錯誤：不能除以零")
    except Exception as e:
        logging.error("未知錯誤：%s", e)

# 測試程式
divide(10, 0)  # 觸發除以零錯誤
divide("10", 2)  # 觸發其他錯誤
