# -*- coding: utf-8 -*-
"""
Name:         001.将Pdf中的表格读取到Excel.py
Description:  猿友汇技术团队出品
Author:       laoxu
Date:         2022/10/29 5:36 PM
Version:      V1.0
"""
import pdfplumber
import pandas

with pdfplumber.open("todofiles/2022年某价格表.pdf") as pdf:
    page = pdf.pages[0]
    table = page.extract_table()
    temp = pandas.DataFrame(table[1:], columns=table[0])
    temp.to_excel("test.xlsx")
    print("ok")































# if __name__ == '__main__':
#     print('Hi, This is 001.将Pdf中的表格读取到Excel.py')
#
