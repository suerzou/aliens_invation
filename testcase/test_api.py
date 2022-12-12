import re

import pytest
import requests


class Test_api:
    access_token = ''

    #@pytest.mark.skip
    @pytest.mark.token
    def test_get_token(self):
        url = 'https://api.weixin.qq.com/cgi-bin/token'
        data = {
            "grant_type":"client_credential",
            "appid":"wxf4c3f50c56a5d499",
            "secret":"ebc4a76e20c9593dea947e40e98de435"
        }
        result = requests.request(method='get',url=url,params=data)
        #Test_api.access_token = result.json()['access_token']
        obj =  re.search('"access_token":"(.*?)"',result.text)
        Test_api.access_token = obj.group(1)

        print(Test_api.access_token)
        assert 1 != 2

    #@pytest.mark.skipif(reason='跳过')
    @pytest.mark.run(order=2)
    @pytest.mark.smoke
    def test_get_label(self):
        url = 'https://api.weixin.qq.com/cgi-bin/tags/get'
        data = {
            "access_token": Test_api.access_token
        }
        res = requests.request(method='get',params=data,url=url)
        print(res.text)


