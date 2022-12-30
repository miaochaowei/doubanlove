import time
import pandas   as pd
import datetime
import  json
import requests
import os.path as Path
from bs4 import BeautifulSoup





cookie1 = "__yadk_uid=5TNtHQvyp1qL0GRCaXM9qaTRmb9mjDvm; __utmv=30149280.25722; __gpi=UID=00000610ef0c4d1e:T=1655912585:RT=1663771205:S=ALNI_MYN5am8NIGUA0Min4qlAvklEZhBzQ; _ga=GA1.2.768202420.1638024587; ll=\"108288\"; bid=YfNLjses1s4; __utmc=30149280; push_noty_num=0; push_doumail_num=0; __utmz=30149280.1672239718.97.15.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap_v=0,6.0; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1672326612%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DOosC4PFSlNyuVTDPjJtFk9gGHyqm_7jWWFWHT3cMT-SybRvGU2i-cmhvrhK2s2X0%26wd%3D%26eqid%3Db13263af0012d1b70000000363ac5a7c%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.768202420.1638024587.1672239718.1672326612.98; __utmt=1; dbcl2=\"257220224:sWQl98MlbWg\"; ck=JIAp; _pk_id.100001.8cb4=b6abc13b15efde79.1638024585.93.1672327744.1672244310.; __utmb=30149280.26.5.1672327744047"

# print(cookie)
# cookie="ll=\"108288\"; bid=dDMMFxNh_y0; _pk_ses.100001.8cb4=*; __utma=30149280.1639651790.1672302648.1672302648.1672302648.1; __utmc=30149280; __utmz=30149280.1672302648.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; dbcl2=\"140005612:U1zhcJlWzW0\"; ck=T_pG; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; __utmv=30149280.14000; __yadk_uid=ItOMXOTiKjjFV7B4kMqJPzQUy5bGSMLu; douban-fav-remind=1; _pk_id.100001.8cb4=48c32bce946dc4e1.1672302648.1.1672302950.1672302648.; __utmb=30149280.12.7.1672302949913"
# cookie="douban-fav-remind=1; __yadk_uid=ItOMXOTiKjjFV7B4kMqJPzQUy5bGSMLu; __utmv=30149280.14000; push_doumail_num=0; push_noty_num=0; ap_v=0,6.0; __utmb=30149280.3.10.1672302648; __utmz=30149280.1672302648.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _pk_id.100001.8cb4=48c32bce946dc4e1.1672302648.1.1672302655.1672302648.; ck=T_pG; __utmt=1; dbcl2=\"140005612:U1zhcJlWzW0\"; __utmc=30149280; __utma=30149280.1639651790.1672302648.1672302648.1672302648.1; _pk_ses.100001.8cb4=*; bid=dDMMFxNh_y0; ll=\"108288\""
# cokie="douban-fav-remind=1; ll=\"108288\"; bid=5Z-fX5U2XPI; __utmc=30149280; __yadk_uid=7TPnyXnAad8IRoiCHFh9ZDw3Xc2GRQ4L; __utmz=30149280.1672288398.13.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; frodotk_db=\"129554e3858a230037bffeaa909e6900\"; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1672296772%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_ses.100001.8cb4=*; ap_v=0,6.0; __utma=30149280.1662088207.1634110102.1672293900.1672296772.15; __utmt=1; dbcl2=\"257220224:sWQl98MlbWg\"; ck=JIAp; push_noty_num=0; push_doumail_num=0; __utmv=30149280.25722; _pk_id.100001.8cb4=47136e70f8f6a6f7.1634110101.15.1672297067.1672294595.; __utmb=30149280.19.4.1672297067098"
#

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
     "Cookie":cookie1}


urls=["https://www.douban.com/group/topic/271400586/add_comment"
    ,"https://www.douban.com/group/topic/272016212/add_comment"
    ,"https://www.douban.com/group/topic/198250668/add_comment"
    ,"https://www.douban.com/group/topic/260384350/add_comment"]
d={d.split("=")[0].replace(" ",""):d.split("=")[1].replace(" ","")  for d in cookie1.split(";")}
print(d)
params = {
"ck": d["ck"],
"rv_comment": "--"
}
print(params)
for u in urls:
    r= requests.post(u,headers=headers,data=params)
    print(u,r.status_code)