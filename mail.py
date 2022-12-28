import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

#设置登录及服务器信息

mail_host = 'smtp.126.com'
#smtp.163.com mmmcwei@163.com  QHQBZZHYPASVPRDB

mail_user = 'love940712@126.com'
mail_pass = 'LDJUHDHQEAGYMYKG'
sender = 'love940712@126.com'
receivers = ['18734913406@163.com']

#设置eamil信息
#添加一个MIMEmultipart类，处理正文及附件


#推荐使用html格式的正文内容，这样比较灵活，可以附加图片地址，调整格式等
# with open('abc.html','r') as f:
#     content = f.read()
#设置html格式参数
def sendmail(ds,contents,files,htmls=None):
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receivers[0]
    dates="-".join(ds)
    message['Subject'] = dates+'北京住房供应关系分析'
    content="".join(contents)
    part1 = MIMEText(content,'plain','utf-8')
    message.attach(part1)
    #添加一个txt文本附件
    for file in files:
        att_annex1 = MIMEText(open(file, 'rb').read(), 'base64', 'utf-8')
        att_annex1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att_annex1["Content-Disposition"] = 'attachment; filename='+file
        message.attach(att_annex1)
    # for h in htmls:
    #     msg_alternative = MIMEMultipart('alternative')
    #     message.attach(msg_alternative)
    #     try:
    #         with open(h, 'r', encoding='utf8') as html_file:
    #             html_text_content = html_file.read()
    #     except Exception as eh:
    #         print('未找到html文件', eh)
    #     msg_alternative.attach(MIMEText(html_text_content, 'html', 'utf8'))
    #     #添加照片附件
    #     # with open(file,'rb')as fp:
    #     #     picture = MIMEImage(fp.read())
    #     #     #与txt文件设置相似
    #     #     picture['Content-Type'] = 'application/octet-stream'
    #     #     picture['Content-Disposition'] = 'attachment;filename='+file
    #     #     message.attach(picture)

    # mm123ab,【For男】不要以耍流氓为目的的恋爱 ,https://www.douban.com/group/topic/275254796/?_i=41833708rVVZ6R,xiaoxiaozzz123@qq.com,1
    # Angelina,【For男】｜95女｜期待一个真诚待人，热爱生活的你 ,https://www.douban.com/group/topic/275589925/?_i=41839478rVVZ6R,angelina202209@163.com,1
    # 小栗子,浪漫鹊桥【for 男】 暂时写到这，后续有想法再补充 ,https://www.douban.com/group/topic/275292891/?_i=41841888rVVZ6R,linqiao12@foxmail.com,1
    # 十又,【for 男】【96科普编辑】【趁夏风还未吹落花香】 ,https://www.douban.com/group/topic/227845580/?_i=41851028rVVZ6R,binruzhi@163.com,1
    # 猫咪不会喵,【for男】【93年处女座】【找到男朋友一起去涠洲岛】 ,https://www.douban.com/group/topic/264068592/?_i=41873498rVVZ6R,chengsiyuan1993@126.com,1
    # yuko,【for男】【燕郊】【93天秤】【是不是，甜甜的笑总能给人带来温暖】 ,lizhigunihttps://www.douban.com/group/topic/172301662/?_i=41875958rVVZ6R,ang@sina.com,1
    # (｡ì _ í｡),浪漫鹊桥|【For男】【87 来这里希望能遇到灵魂共鸣的你】 ,https://www.douban.com/group/topic/207373696/?_i=41876838rVVZ6R,ninayang1208@qq.com,1
    # 小樱桃,浪漫鹊桥｜「for男」「北京」90年 真诚寻找人生伴侣 ,https://www.douban.com/group/topic/270517607/?_i=41884868rVVZ6R,1710022965@qq.com,1

    #将内容附加到邮件主体中
    #登录并发送   http://bj.ke.com/ershoufang/liuliqiao1/sf1y3p1p2p3/pg1
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host,25)
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(
            sender,receivers,message.as_string())
        print('success')
        smtpObj.quit()
    except smtplib.SMTPException as e:
        print('error',e)
def sendmail_douban(id,title,contents,files,mail):
    message = MIMEMultipart()
    message['From'] = sender
    receive = []
    receive.append(mail)
    message['To'] = mail
    message['Subject'] = title
    content=id+"".join(contents)
    part1 = MIMEText(content,'plain','utf-8')
    message.attach(part1)
    #添加一个txt文本附件
    for file in files:
        att_annex1 = MIMEText(open(file, 'rb').read(), 'base64', 'utf-8')
        att_annex1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att_annex1["Content-Disposition"] = 'attachment; filename='+file
        message.attach(att_annex1)
    # for h in htmls:
    #     msg_alternative = MIMEMultipart('alternative')
    #     message.attach(msg_alternative)
    #     try:
    #         with open(h, 'r', encoding='utf8') as html_file:
    #             html_text_content = html_file.read()
    #     except Exception as eh:
    #         print('未找到html文件', eh)
    #     msg_alternative.attach(MIMEText(html_text_content, 'html', 'utf8'))
    #     #添加照片附件
    #     # with open(file,'rb')as fp:
    #     #     picture = MIMEImage(fp.read())
    #     #     #与txt文件设置相似
    #     #     picture['Content-Type'] = 'application/octet-stream'
    #     #     picture['Content-Disposition'] = 'attachment;filename='+file
    #     #     message.attach(picture)
    #将内容附加到邮件主体中
    #登录并发送   http://bj.ke.com/ershoufang/liuliqiao1/sf1y3p1p2p3/pg1
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host,25)
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(
            sender,receive,message.as_string())
        print('success')
        return True

        smtpObj.quit()
    except smtplib.SMTPException as e:
        print('error', e)
        return False

# spider = ErShouSpider(SPIDER_NAME)
# spider.settoday_path()
# files=[ spider.today_path + "/" + spider.date_string + "-all.csv",spider.today_path + "/" + spider.date_string + "sta-all.csv"]
#
# contents=["今天是"+spider.date_string+"  房屋分析统计 如两张表\n",""]
# htmls=["page_layout.html"]
# #
# sendmail(contents,files,htmls)