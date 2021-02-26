import requests
from lib.apiLib.authorization import Authorization

# access_token获取值
token = Authorization().authorization({'username': '小雪', 'password': '123456'}, getToken=True)

class User:
  # 用户查询
  def user(self,inData,getToken=True):
    url = "http://api.jiguangxiu.vrshow.com/user-app-service/user"
    content = inData
    headers = {
        'clientId': '10000001',
        'clientSecret': 'E10ADC3949BA59ABBE56E057F20F883E',
        'nonceStr': '637311946905191469',
        'sign': 'A9B7B8135C795221710B1ABF3FE22FC6',
        'Authorization': 'Bearer' + ' ' + token,
    }
    response = requests.request("GET", url, headers=headers, params=content)
    print(response.json())
    return response.json()  # 返回字典类型
    # print(response.status_code)


  # 用户性别修改
  def gender(self, getToken=True):
      url = 'http://api.jiguangxiu.vrshow.com/user-app-service/user/gender'
      payload = {'userId': '68007388434796544', 'sex': 2}
      headers = {
          'clientId': '10000001',
          'clientSecret': 'E10ADC3949BA59ABBE56E057F20F883E',
          'nonceStr': '637311946905191469',
          'sign': 'A9B7B8135C795221710B1ABF3FE22FC6',
          'Content-Type': 'application/json',
          'Authorization': 'Bearer' + ' ' + token
      }
      res = requests.put(url, headers=headers, json=payload)
      # print(res.json())
      # print(res.status_code)
      # print(res.headers)
      # print(headers)

  # 用户生日修改
  def birthday(self, getToken=True):
      url = 'http://api.jiguangxiu.vrshow.com/user-app-service/user/birthday'
      payload = {'userId': '68007388434796544', 'birthday': '2020-12-22'}
      headers = {
          'clientId': '10000001',
          'clientSecret': 'E10ADC3949BA59ABBE56E057F20F883E',
          'nonceStr': '637311946905191469',
          'sign': 'A9B7B8135C795221710B1ABF3FE22FC6',
          'Content-Type': 'application/json',
          'Authorization': 'Bearer' + ' ' + token
      }
      res = requests.request("put",url, headers=headers, json=payload)
      print(res.json())
      # print(res.status_code)

  # 用户地区修改
  def address(self, getToken=True):
      url = 'http://api.jiguangxiu.vrshow.com/user-app-service/user/address'
      payload = {'userId': '68007388434796544', 'provinceCode': '518000','provinceName':'广东省','cityCode':'518000',"cityName":"深圳市","areaCode":"440300",
                 "areaName":"龙岗区","streetCode":"518064","streetName":"布吉街道","address":"粤海街道高新南七道"}
      headers = {
          'clientId': '10000001',
          'clientSecret': 'E10ADC3949BA59ABBE56E057F20F883E',
          'nonceStr': '637311946905191469',
          'sign': 'A9B7B8135C795221710B1ABF3FE22FC6',
          'Content-Type': 'application/json',
          'Authorization': 'Bearer' + ' ' + token
      }
      res = requests.request("put",url, headers=headers, json=payload)
      print(res.json())
      # print(res.status_code)

#测试下
if __name__ == '__main__':
    token = Authorization().authorization({'username':'小雪','password':'123456'}, getToken=True)
    #实例化对象
    res = User().user(token)
    res = User().gender()
    res = User().birthday()
    res = User().address()

