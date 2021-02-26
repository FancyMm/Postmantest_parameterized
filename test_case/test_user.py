import pytest
import requests
from lib.apiLib.user import User
from lib.apiLib.UserLike import UserLike
import os
# from tools.ExcelDataCtl import get_excel_data
from lib.apiLib.user import User
from tools.ExcelDataCtl import get_excel_data
import xlrd
from xlutils.copy import copy
import allure
'''
从excel获取请求体/响应的预期结果
'''
class TestUser:
    # def test_user(self):
    #     #2- 调用用户的接口代码
    #     res = User().user()#获取响应数据---字典格式
    #     #3- 预期结果--excel里与实际结果对比
    #     assert '查询成功' == '成功' ,"desc为查询成功"
    #
    # def test_userLike(self):
    #     res = UserLike().adduserlike()
    #     # assert 200 == 250, "status_code为200"
    #     # assert '处理成功' == '成功', "desc为处理成功"real_result
    #     assert '资源已点赞' == '资源已点赞'
    @allure.feature('用户查询')
    @pytest.mark.parametrize('inBody,expData', get_excel_data('1-查询用户', 'cz'))  # 数据驱动---如果自己开发--一定会写一个for
    def test_user(self, inBody, expData):
        # 2- 调用登录的接口代码
        res = User().user(inBody,getToken=True)  # 获取响应数据---字典格式
        # print(res['code'])
        # print(expData)
        # 3- 预期结果--excel里与实际结果对比     assert 实际结果==期望结果  ; 在封装的类中，请求完，需return返回字典类型
        assert res['desc'] == expData['desc']
if __name__ == '__main__':
    #1- 框架执行后的结果数据

    # pytest.main(['test_user.py','-s','--html=../report/xt.html'])
    # pytest.main(['test_user.py', '-s','--alluredir = ../report/allure'])

    pytest.main(['test_user.py', '-s', '--alluredir', '../report/tmp'])
    os.system('allure generate ../report/tmp -c -o ../report/html --clean')  # ../report/tmp 为存放报告的源文件目录 -c	在生成报告之前先清理之前的报告目录  -o 指定生成报告的文件夹
#2- 使用allure  应用，去打开这个结果数据-并且 浏览器访问（使用火狐/谷歌--设置默认浏览器）
    os.system('allure serve ../report/tmp')