import re
import requests

def get_xsrf(session):
    index_url = "https://www.zhihu.com"
    index_page = session.get(index_url,headers = headers)
    html = index_page.text
    pattern = r'name="_xsrf" value="(.*?)"'
    _xsrf = re.findall(pattern,html)
    return _xsrf[0]
agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
headers = {
    'User-Agent':agent
}
session = requests.session()
_xsrf = get_xsrf(session)
post_url = 'https://www.zhihu.com/signin'
postdata = {
    '_xsrf':_xsrf,
    'password':'',
    'remember':'true',
    'phone_num':'',
}
login_page = session.post(post_url,data=postdata,headers=headers)
login_code = login_page.text
print(login_page.status_code)
print(login_code)


