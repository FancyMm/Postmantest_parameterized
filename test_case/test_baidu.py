import requests
import pytest

class TestAssert():
    def test_assert(self):
        r = requests.get('http://www.baidu.com')
        assert r.status_code == 100, "返回200说明访问成功"

if __name__ == '__main__':
    #1- 框架执行后的结果数据
    pytest.main()