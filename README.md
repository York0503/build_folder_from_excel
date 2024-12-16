# 依照excel指定欄位建立資料夾

# config.ini 參數介紹
- 1.Excel_1: "Excel_"不變，後方請輸入資料編號(如1、2、3、4...)
- 2.file_path: excel file path
- 3.sheet_name: excel分頁名稱
- 4.column_name: 創建資料夾的名稱列表，請輸入該列表title

參考範例
```
[Excel_1]
file_path = input_Excel/Product_CHT_ENG_Reference.xlsx
sheet_name = Drinks
column_name = item_name (EN)
```
