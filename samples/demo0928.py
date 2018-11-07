import hashlib
import json
import requests
import time


def md5(s):
    m = hashlib.md5(s)
    return m.hexdigest()


appkey = '5bab4260f1f556843f000013'
app_master_secret = '3hd5e3ektibgkngqq1oxq8xuxsfutr5g'
timestamp = '1538120328000'
method = 'POST'
url = 'http://msg.umeng.com/api/send'
params = {"policy":{"expire_time":"2018-09-30 17:00:00"},"description":"测试","production_mode":True,"appkey":"5bab4260f1f556843f000013","payload":{"body":{"title":"这是个测试标题","ticker":"这是个测试","text":"这是个测试这是个测试这是个测试这是个测试","after_open":"go_custom","custom":{"type":"gjyg","aid":66666},"play_vibrate":"false","play_lights":"false","play_sound":"true"},"display_type":"notification","extra":{}},"mipush":True,"mi_activity":"com.ailk.xhs.ui.MipushTestActivity","filter":{"where":{"and":[{"or":[{"tag":"gonggao"},{"tag":"xinhua"}]}]}},"type":"groupcast","timestamp":"1538120328000"}
post_body = json.dumps(params)
print(post_body)
sign = md5(('%s%s%s%s' % (method, url, post_body, app_master_secret)).encode())
print(sign)

headers = {'Content-Type': 'application/json'}
with requests.post(url + "?sign=" + sign, headers=headers, data=post_body) as f:
    print("------")
    print(f.text)
