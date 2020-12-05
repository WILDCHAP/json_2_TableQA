# 代码 8-1
import numpy as np
import pandas as pd
import os
import json

class SaveJson(object):

    def save_file(self, path, item):

        # 先将字典对象转化为可写入文本的字符串
        item = json.dumps(item,ensure_ascii=False)

        try:
            if not os.path.exists(path):
                with open(path, "w", encoding='utf-8') as f:
                    f.write(item + "\n")
                    print("^_^ write success")
            else:
                with open(path, "a", encoding='utf-8') as f:
                    f.write(item + "\n")
                    print("^_^ write success")
        except Exception as e:
            print("write error==>", e)
def db2json(inputfile,outputpath):  ##  r'C:\Users\wxjzy007\Desktop\NCP.csv'  “test1.json”
    ##inputfile = r'C:\Users\wxjzy007\Desktop\NCP.csv' ## 输入的数据文件
    data = pd.read_csv(inputfile) ## 读取数据

    rows=data.values.tolist()  #dataframe转ndarray，再转二维数组
    name=inputfile.split('\\')[-1].split('.')[0]   #获取表名，注意转义
    title=""
    header=np.array(data.columns).tolist()
    common=""
    id=name

    types=[]
    row=rows[0]
    print(row)

    for i in row:
        if(isinstance(i,str)):
            types.append("text")
        else:
            types.append("real")

    item={}  ##dict
    item["rows"]=rows
    item["name"]=name
    item["title"]=title
    item["header"]=header
    item["common"]=common
    item["id"]=id
    item["types"]=types

    # 保存的文件名
    ##outputpath = "test1.json"

    s = SaveJson()

    # 测试代码，循环写入三行，没有空行
    for i in range(3):
        s.save_file(outputpath, item)

#db2json(r'C:\Users\wxjzy007\Desktop\NCP.csv',"test2.json")