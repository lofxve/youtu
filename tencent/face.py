import base64, hashlib, json, random, string, time
from urllib import parse, request
from urllib.parse import quote
import hmac, hashlib
import requests
import binascii
def app_sign(appid,secret_id,expired,secret_key,puserid):
    now = int(time.time())
    rdm = random.randint(0, 999999999)
    plain_text = 'a=' + appid + '&k=' + secret_id + '&e=' + str(expired) + '&t=' + str(now) + '&r=' + str(
        rdm) + '&u=' + puserid + '&f='
    bin = hmac.new(secret_key.encode(), plain_text.encode(), hashlib.sha1)
    s = bin.hexdigest()
    s = binascii.unhexlify(s)
    s = s + plain_text.encode('ascii')
    signature = base64.b64encode(s).rstrip()  # 生成签名
    return signature
def get_headers(appid,secret_id,secret_key,puserid):
    expired = int(time.time()) + 2592000
    sign = app_sign(appid,secret_id,expired,secret_key,puserid)
    headers = {
        'Authorization': sign,
        'Content-Type': 'text/json'
    }
    return headers
def youtu(img_path):
    appid = '10151047'
    secret_id = 'AKID59AA4pi1Sis5GIS2tdCe1b7W2T2asTjr'
    secret_key = 'N5mMxsiO6zjIk7Kj3DIPPLG4mOvOjvpk'
    userid = '924271966'

    url = 'http://api.youtu.qq.com/youtu/api/detectface'
    image = base64.b64encode(open(img_path, 'rb').read()).rstrip().decode('utf-8')

    data = {
        "app_id": appid,
        "mode": 0,
        "image":image,
    }
    headers = get_headers(appid=appid,secret_id=secret_id,secret_key=secret_key,puserid=userid)
    r = requests.post(url,headers=headers,data=json.dumps(data))
    print(r)
    if r.status_code == 200:
        ret = r.json()
        print(ret)
    return ret