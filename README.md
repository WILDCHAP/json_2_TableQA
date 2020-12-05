# json_2_TableQA
sqlite数据表导出json转为TableQA格式json

请根据自己表的表头等字段更新json2json_line32-37，并修改文件名  
本代码只能对**单表**进行修改  
处理文件只包括表内容(数据，字段等)，需要问题转换成TableQA请参见[auto_question_TableQA](https://github.com/WILDCHAP/auto_question_TableQA)

原json是利用[Navicat 15 for SQLite](https://www.navicat.com.cn/company/press/111-press20081120a)导出  

TableQA格式如下：  
```json
{
    "id":"a1b2c3d4", # 表格id
    "name":"Table_a1b2c3d4", # 表格名称
    "title":"表1：2019年新开工预测 ", # 表格标题
    "header":[ # 表格所包含的列名
        "300城市土地出让",
        "规划建筑面积(万㎡)",
        ……
    ],
    "types":[ # 表格列所相应的类型
        "text",
        "real",
        ……
    ],
    "rows":[ # 表格每一行所存储的值
        [
            "2009年7月-2010年6月",
            168212.4,
            ……
        ]
    ]
}
```
