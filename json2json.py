import json
import pandas as pd
import numpy as np

from db2json import SaveJson
# 文件名和下面的生成路径自己改
filename = 'Table_financial_statements_dev.json'

# 从文件读取JSON格式的字符串，并将其转化为字典
with open(filename, 'r', encoding='UTF-8') as f:
    json_file = json.load(f)
    print("读取JSON文件中的内容：")
    print(len(json_file))

# 记录集合==>list[dict, dict...]
bb=json_file["RECORDS"]

# 列内容
rows = []

# 每次取出bb中一行数据，只取出他的值放入list中，再把这个list加入rows
for temp_dict in bb:
    temp_list = []
    for val in temp_dict.values():
        temp_list.append(val)
    rows.append(temp_list)
    if len(rows) % 10000 == 0:
        print(len(rows))

item={}  ##dict
item["rows"] = rows
item["name"] = "Table_financial_statements"
item["title"] = "上市公司财报"
item["header"] = ["数据id", "股票代码", "报表名称", "时间", "数据项名称", "数据值", "单位"]
item["common"] = ""
item["id"] = "financial_statements"
item["types"] = ["text", "text", "text", "text", "text", "text", "text"]

# 保存的文件名
outputpath = "Table_financial_statements_dev_new.json"

s = SaveJson()


s.save_file(outputpath, item)