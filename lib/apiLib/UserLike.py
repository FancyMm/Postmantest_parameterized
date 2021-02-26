import requests
from lib.apiLib.authorization import Authorization

# access_token获取值
token = Authorization().authorization({'username': '小雪', 'password': '123456'}, getToken=True)

class UserLike:
      # 资源点赞
      def adduserlike(self,getToken=True):
        url = 'http://api.jiguangxiu.vrshow.com/user-app-service/user/like'
        payload = {'resourceType':1, 'resourceId':'37213978799247360', 'userId': 68007388434796544}
        headers = {
            'clientId': '10000001',
            'clientSecret': 'E10ADC3949BA59ABBE56E057F20F883E',
            'nonceStr': '637311946905191469',
            'sign': 'A9B7B8135C795221710B1ABF3FE22FC6',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer' + ' ' +token
        }
        res = requests.post(url,headers=headers,json=payload)
        print(res.json())
        # 打印请求响应体的单个字段值
        print(res.json()['desc'])
        print(res.json()['code'])
        # 打印请求的响应
        print(res.content.decode())
        # print(res.status_code)
        # print(res.headers)
        # print(headers)
        # 断言响应状态码
        # assert res.status_code == 100 , "status_code为200"

      # 资源取消点赞
      def deluserlike(self, getToken=True):
        url = 'http://api.jiguangxiu.vrshow.com/user-app-service/user/like'
        payload = {'resourceType': 1,'resourceIdList': ['37213978799247360']}
        headers = {
              'clientId': '10000001',
              'clientSecret': 'E10ADC3949BA59ABBE56E057F20F883E',
              'nonceStr': '637311946905191469',
              'sign': 'A9B7B8135C795221710B1ABF3FE22FC6',
              'Content-Type': 'application/json',
              'Authorization': 'Bearer' + ' ' + token
          }
        response = requests.delete(url, headers=headers, json=payload )
        print(response.json())
        # print(response.status_code)

#测试下
if __name__ == '__main__':
        token = Authorization().authorization({'username':'小雪','password':'123456'}, getToken=True)
        print(token)
        # 实例化对象
        res = UserLike().adduserlike()
        res = UserLike().deluserlike( )