# -*- coding: utf-8 -*-
"""
Name:         002.按条件拆分Excel表.py
Description:  猿友汇技术团队出品
Author:       laoxu
Date:         2022/11/13 9:46 PM
Version:      V1.0
"""
import pandas as pd

filePath = "todofiles/Excel拆分模拟数据.xlsx"
datas = pd.read_excel(filePath)
companyList = list(datas["公司"].drop_duplicates())

for item in companyList:
    writer = pd.ExcelWriter(f"./tempdata/{item}.xlsx")
    tempData = datas[datas["公司"] == item]
    tempData.to_excel(writer, index=False)
    writer.close()

print('Ok')
