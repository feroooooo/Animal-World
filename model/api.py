import requests
import base64
import json

# 动物识别
def predict(url):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/animal"
    # 二进制方式打开图片所属的[本地文件]
    f = open(url, 'rb')
    img = base64.b64encode(f.read())

    # params = {"image":img, 'baike_num':1}
    params = {"image":img}
    access_token = '24.4b0a8ec9a214ed6e8d0621fc3a614566.2592000.1712219879.282335-55261071'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        ret = {}
        response_dict = response.json()
        # print(response_dict)
        ret['prediction'] = response_dict['result'][0]['name']
        if ret['prediction'] == '非动物':
            ret['is_animal'] = False
        else:
            ret['is_animal'] = True
            if ret['prediction'] == '金钱豹':
                ret['prediction'] = '花豹'
        ret['genus'] = crawl_wiki_data(ret['prediction'])
        # try:
        #     ret['image_url'] = response_dict['result'][0]['baike_info']['image_url']
        #     ret['baike_url'] = response_dict['result'][0]['baike_info']['baike_url']
        #     ret['description'] = response_dict['result'][0]['baike_info']['description']

        #     # 删除空格
        #     no_spaces_string = ret['description'].replace(" ", "")
        #     # 查找'属'字符的位置
        #     pos_shu = no_spaces_string.find('属')
        #     # 在'属'字符之前查找'科'或'、'字符的位置
        #     pos_ke = no_spaces_string.rfind('科', 0, pos_shu)
        #     pos_dou = no_spaces_string.rfind('、', 0, pos_shu)
        #     # 使用两个位置中较大的那一个作为起始位置
        #     start_pos = max(pos_ke, pos_dou) + 1
        #     # 提取子字符串
        #     ret['genus'] = no_spaces_string[start_pos:pos_shu]
        
        # except:
        #     ret['image_url'] = ''
        #     ret['baike_url'] = ''
        #     ret['description'] = ''
        #     ret['genus'] = ''
        return ret
    else:
        return {}


# 获取token
def get_access_token():
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=lLBFhgAQlV6KpgNYf0NCX3oR&client_secret=J5STHfbFdPiw9X8JgCO2ClfbFCcTAuAf"
    
    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    

# 爬取属
def crawl_wiki_data(animal):
    headers = { 
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    url='https://baike.baidu.com/item/' + animal      
    try:
        response = requests.get(url,headers=headers)
        
        pos = response.text.find(r'属</dt>')
        
        if pos == -1:
            pos = response.text.find(r'/item/' + animal)
            url = 'https://baike.baidu.com' + response.text[pos:pos+30][:response.text[pos:pos+30].find('?')]
            response = requests.get(url,headers=headers)
            pos = response.text.find(r'属</dt>')
        
        sub_string = response.text[pos+1:pos+300]
        ret = sub_string[sub_string.find('/item/') + 6:sub_string.find('属')]
        if len(ret) > 3:
            ret = ''
        return ret
    except Exception as e:
        print(e)
        return ''

if __name__=="__main__":
    # get_access_token()
    # prediction = predict(r'C:\Custom\DataSet\WildLife\fox\00000035_224resized.jpg')
    # print(prediction)
    print(crawl_wiki_data('棕熊'))