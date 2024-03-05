def predict(url):
    # encoding:utf-8

    import requests
    import base64

    '''
    动物识别
    '''

    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/animal"
    # 二进制方式打开图片所属的[本地文件]
    f = open(url, 'rb')
    img = base64.b64encode(f.read())

    params = {"image":img, 'baike_num':1}
    access_token = '24.4b0a8ec9a214ed6e8d0621fc3a614566.2592000.1712219879.282335-55261071'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        ret = {}
        response_dict = response.json()
        ret['prediction'] = response_dict['result'][0]['name']
        try:
            ret['description'] = response_dict['result'][0]['baike_info']['description']
        except:
            ret['description'] = '暂无'
        return ret
    else:
        return {}

def get_access_token():

    import requests
    import json
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=lLBFhgAQlV6KpgNYf0NCX3oR&client_secret=J5STHfbFdPiw9X8JgCO2ClfbFCcTAuAf"
    
    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)

if __name__=="__main__":
    # get_access_token()
    print(predict(r'C:\Custom\DataSet\WildLife\fox\00000001_224resized.jpg'))   