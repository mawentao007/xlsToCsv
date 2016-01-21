#coding:utf-8
__author__ = 'marvin'
import xlrd
import csv
import re
import os




def readXls(fname):
    data = xlrd.open_workbook(fname)
    table = data.sheets()[0]
    codeLine = table.row_values(0)
    code = extractCode(str(codeLine))
    return code,table         #返回的证券代码，表，行数


def extractCode(inputStr):
    valid = re.compile(ur"\d+\.?[A-Z]+",re.UNICODE)
    return valid.search(inputStr).group(0)


def writeTitleRow(fileToWrite):
    title = ["证券代码"," ","公告日期","被参控公司","参控关系","投资额","参股比例(%)","被参控公司注册资本","被参控股公司总资产",
             "被参控股公司净利润(元)","被参控公司主营业务","是否合并报表","未并入合并报表原因"]
    writer = csv.writer(file(fileToWrite, 'a'))
    writer.writerow(title)


def writeToCsv(code,table,fileToWrite):
    writer = csv.writer(file(fileToWrite, 'a'))
    nrows = table.nrows
    for i in range(3,nrows-2):  #丢弃前三行和最后两行
        data = [x.encode("utf-8") for x in table.row_values(i) if not type(x) == float]
        data.insert(0,code)
        writer.writerow(data)



def getAllFile(path):
    return os.listdir(path)



if __name__=="__main__":
    fileToWrite = "answer.csv"
    p = "com"
    writeTitleRow(fileToWrite)
    for f in getAllFile(p):
        code,table = readXls(str(os.path.join(p,f)))
    #code,table = readXls(str(os.path.join(p,"000001.xlsx")))
        writeToCsv(code,table,fileToWrite)

