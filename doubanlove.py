import pandas as pd
import time
from mail import sendmail_douban
import threadpool
from bs4 import BeautifulSoup
import datetime
import os
import re



path="data/douban2/"
# 返回path下所有文件构成的一个list列表
filelist=os.listdir(path)

tiltle="douban_xiaohei_test"
mailfiles=[path+file for file in filelist]
comment_firstpra=["你好.看到你得帖子觉得很舒服,很想要认识一下，上班时间发的，不能尽善尽美的写邮件，希望可以得到你得回复\n"]


contents=["  基本情况 人工智能炼丹工程师,91年 山西人，月入40k 外地有一套房，还有三四十万得贷款,没有负担，想还随时可以\n"
,"  兴趣爱好 不喝酒 不抽烟，不打游戏，喜欢健身，有胸肌 有腹肌，比较壮。\n"
,"  未来规划 因为行业原因，北京得行业前景最好，但是没有户口，未来的话，我觉得可以两个人共同决定\n"
,"  个人经历 硕士毕业之后，负责风控算法项目，后带领一个4-5 人的团队在公司对公司的贷前贷后做算法服务赋能，之后跳槽到小米现在负责组件商店的搜索推荐算法。总的来讲 职业前景很好，现在小米又接触到很多优质的资源。\n"
,"  我的希望 努力的找到合适的另一半，可以建立健康的稳定的亲密关系，可以有共同的生活人生目标，就算两个人有些地方有分歧可以求同存异，为了这个目标团结一致。\n","附件是我得照片，请你检阅。非常感谢你看了我的介绍阿，我也非常期待你的回信和对我的看法"]
all_df_path="ke/douban/all.csv"
new_df_path="ke/douban/20220118.csv"
allsend_df=pd.DataFrame(columns=["id","title","link",'mail','pageindex','content','fedback','date'])
if os.path.exists(all_df_path):
    allsend_df = pd.read_csv(all_df_path)
# doubanSpider=doubanSpider(DOUBAN_SPIDER)
# doubanSpider.collect_area_ershou_data()
new_send=pd.read_csv(new_df_path)
# new_send.columns=["id","title","link",'mail','pageindex']
new_send=new_send[~new_send["link"].isin(allsend_df["link"].unique().tolist())]
new_success=[]
for index,row in new_send.iterrows():
   id=row["id"]
   title = row["title"]
   print(title)
   link = row["link"]
   mail = row["mail"]
   pageindex = row["pageindex"]
   if int(pageindex) > 8:
      comment_firstpra = ["小姐姐 真的翻了好久才看到你的贴子，觉得很想要认识一下，上班时间发的，不能尽善尽美的写邮件，希望可以得到你得回复\n"]
   if int(pageindex)==-1:
      comment_firstpra=["你好 ,之前发的没有回复，但是还是很喜欢，所以再试一下\n"]
   content=comment_firstpra+contents
   content_str = id+"".join(comment_firstpra)
   issuc=sendmail_douban(id=id,title="豆瓣相亲贴",contents=content,files=mailfiles,mail=mail)

   if issuc:
      new_success.append([id,title,link,mail,pageindex,content_str,0,datetime.datetime.today()])
rc=["id","title","link",'mail','pageindex','content','fedback','date']
newsudf=pd.DataFrame(data=new_success,columns=rc)

df=allsend_df[rc].append(newsudf[rc])
df.reset_index(inplace=True)
df.to_csv(all_df_path)