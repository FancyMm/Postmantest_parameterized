import xlrd
from xlutils.copy import copy
import json
from lib.apiLib.user import User
import pytest

# 获取excel数据---请求体+预期结果

def get_excel_data(sheetName,caseName):
    '''
        :param sheetName: 表名
        :param caseName: 用例名
        :return: 一个列表嵌套元组   [(请求体1，期望数据1),(请求体2，期望数据2)]
    '''
    resList = []
    excelDir = '../data/postmantest.xls'
        # 1- 打开excel对象---formatting_info=True  保持样式
    # workBook = xlrd.open_workbook(excelDir,formatting_info=True)
    workBook = xlrd.open_workbook(excelDir)
        # 2- 对某一个sheet操作
    workSheet = workBook.sheet_by_name(sheetName)
        # 3- 获取值  第6列 和第8列
    # print(workSheet.col_values(1))
    # print(workSheet.cell(1,10))
    # print(workSheet.cell(1, 13))
    # 获取第11列内容,值
    # cols = workSheet.col_values(10)
    # cols = workSheet.col_values(13)
    # print(cols)
    # print(type(cols))
    # # 获取单元格内容
    # data = workSheet.cell(1, 10)
    # print(type(data)) #<class 'xlrd.sheet.Cell'>
        # 4- 获取数据
    idx = 0
    #从第0行开始操作-也可以从第1行（根据实际sheet）
    for one in workSheet.col_values(0):
        # 说明这条用例是我们需要的
        if caseName in one:
            # 请求体--单元格数据--cell(行号，列号)0从0开始
            reqBody = workSheet.cell(idx, 10).value
            # print(type(reqBody))
            # return reqBody
            # return json.loads(reqBody)
            # 期望数据
            respData = workSheet.cell(idx, 13).value
            # print(type(respData))
            # return respData
            # 每一行数据增加返回list里
            # 字符串--转化--字典  字典 = json.loads(json数据)
            resList.append((json.loads(reqBody),json.loads(respData)))  # 字符串格式--不能使用键去取值
            # resList.append(respData)
            # [('',''),()]
        idx += 1
        # 每次遍历一次，就准备操做下一行
    return resList

if __name__ == '__main__':
    res = get_excel_data('1-查询用户','cz')
    for one in res:
        print(one)

