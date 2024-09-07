import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import winsound  # 仅限 Windows 系统

headers = {
    # 手动粘贴你的 cookie 值
    'cookie': 'JSESSIONID=6D3F0E4541F895CCBDECA7939C51FFB4; nmstat=5dd7beba-ff83-e784-8182-40e60d1e4049; _fbp=fb.2.1704168180141.207476065; _hjSessionUser_1947642=eyJpZCI6ImRiMTk2M2IwLTU2NDMtNWFjNy1hYmMzLWIyMjgwZWI2MmRhZCIsImNyZWF0ZWQiOjE3MDQxNjgxODAyMzMsImV4aXN0aW5nIjp0cnVlfQ==; _tt_enable_cookie=1; _ttp=lDodFcTOxNgnqFpL5LK2oeSPNQn; gtm_stage=BRAND_AWARE; _ga_53SJ2ZHQGG=GS1.3.1704881236.3.1.1704881252.0.0.0; __gsas=ID=607f9d3e1ae7eba4:T=1704882546:RT=1704882546:S=ALNI_MZNjxONbadL6x6-Sk-k9xzeKFpDbA; gtm_source=my.unsw.edu.au; _ga_LH31YLLQQ3=deleted; _ga_VJWZRWYE2C=GS1.1.1708243921.44.1.1708244942.0.0.0; _ga_LH31YLLQQ3=deleted; _ga=GA1.4.1956998889.1704168004; _ga_HYNPT9QJK3=GS1.1.1710933916.1.1.1710933919.0.0.1548226153; _ga_DJQRKLRFDQ=GS1.1.1712722037.1.0.1712723033.0.0.0; _cs_c=0; _ga_6YR60TCKL0=GS1.1.1713832943.3.0.1713832943.0.0.0; _hjSessionUser_1718158=eyJpZCI6IjA5Y2ZhMDMwLTU4YmQtNThiYy05ZDBhLWExMjk0NDM3OWIxNyIsImNyZWF0ZWQiOjE3MTQ1NzMwNTA2NjMsImV4aXN0aW5nIjpmYWxzZX0=; _ga_JN7NPPFBWJ=GS1.1.1714573050.1.0.1714573053.57.0.0; _ga_Z7EXLLG4FW=GS1.1.1714573050.1.0.1714573053.0.0.0; _ga_LY5KE5RC47=GS1.1.1716151997.10.0.1716152780.0.0.0; _gcl_au=1.1.429249714.1721010326; gtm_counter=9; _cs_id=dd69ee71-4d49-ae20-9d68-0a57ea19c49f.1709594614.8.1721493482.1721493482.1712544458.1743758614814.1; _ga_LGV1CPB4JE=GS1.1.1721493483.2.1.1721493778.0.0.0; _ga_0QVB0WWDN1=GS1.1.1721493483.2.1.1721493778.0.0.0; _ga_N0VNR66LS1=GS1.1.1721713028.53.1.1721713601.60.0.0; _ga_9NN9GZCN8D=GS1.1.1721713028.52.1.1721713601.0.0.0; _ga_5NGSBFF2BC=GS1.1.1724507074.222.1.1724507292.60.0.0; _gid=GA1.3.2007377606.1725619408; __utmc=116357658; __utmz=116357658.1725662986.4.2.utmcsr=sso.unsw.edu.au|utmccn=(referral)|utmcmd=referral|utmcct=/; _ga_34N1K2P6PZ=GS1.1.1725662982.59.1.1725662989.0.0.0; at_check=true; s_plt=0.53; s_pltp=undefined; mbox=PC#13baebd9c41747e88c03c9b162403788.36_0#1788907795|session#8d9dc9944f1b4fca8eb01473c78958fc#1725664855; s_nr30=1725662994407-New; AMCVS_8A5564D65437E5950A4C98A2%40AdobeOrg=1; s_cc=true; __utma=116357658.1956998889.1704168004.1725676152.1725680692.7; __utmt=1; __utmb=116357658.2.10.1725680692; AMCV_8A5564D65437E5950A4C98A2%40AdobeOrg=179643557%7CMCIDTS%7C19973%7CMCMID%7C52233145265997427194349359326408844223%7CMCAAMLH-1726285502%7C8%7CMCAAMB-1726285502%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1725687902s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-19980%7CvVersion%7C5.5.0; s_dslv=1725680704750; _ga_MJPVLKET54=GS1.1.1725680704.71.0.1725680705.0.0.1906740686; _gat=1; _ga=GA1.1.1956998889.1704168004; AWSALB=1hNhhfL1n6sb/+zbRuv9veqI25WghwJNTAzi2xkFyE6V88kKk8WshgPKn5FRp/0UTkSN97RBEzdEP50HjwmVJfz8Js6KvBUy5pRBXAsjPAWc2cchyjLCABNsLF+TNn2se56AFVtCici/pQPWCgOHZVEIEeKoYYp0CFR37jSqxBK/zaU6oJvcEMZ+CymyjPNtYgYHM7MZtc+lMGwfAMM/FizUx1Zw3VzIzs85khq6KyfP477PWx3Rph2b8FMlOP8=; AWSALBCORS=1hNhhfL1n6sb/+zbRuv9veqI25WghwJNTAzi2xkFyE6V88kKk8WshgPKn5FRp/0UTkSN97RBEzdEP50HjwmVJfz8Js6KvBUy5pRBXAsjPAWc2cchyjLCABNsLF+TNn2se56AFVtCici/pQPWCgOHZVEIEeKoYYp0CFR37jSqxBK/zaU6oJvcEMZ+CymyjPNtYgYHM7MZtc+lMGwfAMM/FizUx1Zw3VzIzs85khq6KyfP477PWx3Rph2b8FMlOP8=; _ga_LH31YLLQQ3=GS1.1.1725680597.93.1.1725680898.39.0.0',
}

url = "https://my.unsw.edu.au/active/studentClassEnrol/classInfo.xml"


def fetch_enrolment_info():
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            dt_tags = soup.find_all('dt')
            for dt in dt_tags:
                if 'Enrols / Capacity' in dt.text:
                    enrolment_info = dt.find_next('dd').text.strip()
                    enrols, capacity = map(int, enrolment_info.split("/"))
                    current_time = datetime.now().strftime("%m/%d/%H:%M:%S")
                    print(f"监控时间: {current_time} - 当前注册人数: {enrols} / {capacity}")

                    if enrols < capacity:
                        print("有空位！提醒你！")
                        # 播放声音提醒 (Windows 上使用 'winsound.Beep')
                        winsound.Beep(1000, 1000)
                    else:
                        print("暂无空位。")
                    break
            else:
                print("无法找到注册信息。")
        else:
            print(f"请求失败，状态码: {response.status_code}")

    except Exception as e:
        print(f"发生错误: {e}")


while True:
    fetch_enrolment_info()
    time.sleep(5)  # 每隔5秒请求一次
