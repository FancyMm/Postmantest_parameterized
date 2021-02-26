import requests

class Authorization:
  # access_token获取值
  def authorization(self,inData,getToken=True):
    url = 'http://api.jiguangxiu.vrshow.com/auth-service/auth/password'
    payload = inData
    headers = {
      'clientId': '10000001',
      'clientSecret': 'E10ADC3949BA59ABBE56E057F20F883E',
      'nonceStr': '637311946905191469',
      'sign': 'A9B7B8135C795221710B1ABF3FE22FC6',
      'Authorization': 'Basic MTAwMDAwMDE6RTEwQURDMzk0OUJBNTlBQkJFNTZFMDU3RjIwRjg4M0U=',
      'Content-Type': 'application/x-www-form-urlencoded',
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    #
    # print(response.text.encode('utf8'))
    # print(response.json()['access_token'])
    if getToken:  # 获取token
      return response.json()['access_token']
    else:
      return response.json()  # 返回是字典格式

#测试下
if __name__ == '__main__':
    testData={'username':'小雪','password':'123456'}
    #实例化对象
    res=Authorization().authorization(testData)
    # res=Authorization().authorization(testData,getToken=False)
    print(res)

