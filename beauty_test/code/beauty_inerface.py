import base64
import json
import requests

def test_face(img):
    ak = '****'
    sk = '****'
    headers =  {"Content-Type": "application/json; charset=UTF-8"}
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' +ak + '&client_secret=' + sk
    #添加自己的百度aipid和secretkey
    resp = requests.get(url=host,headers=headers)
    json_resp = json.loads(resp.text)
    access_token = json_resp['access_token']
    #响应获得access token
    with open(img,'rb') as f:
        new_img = base64.b64encode(f.read())
    resp_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"+"?access_token=" + access_token
    post_data = {
        "image":new_img,
        "image_type":"BASE64",
        "face_field":"age,beauty",
        "face_type":"LIVE"
    }
    #设置你想要的数据
    response = requests.post(url=resp_url, data=post_data, headers=headers)
    #根据resp-url进行访问获得想要检测的数据
    json_result = json.loads(response.text)
    return json_result['result']['face_list'][0]['beauty']

