# This is a sample Python script.
import json
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(int("234"))
    cookies = [{'domain': '.douban.com', 'expiry': 1735373184, 'httpOnly': False, 'name': '__utmv', 'path': '/',
                'secure': False, 'value': '30149280.14000'},
               {'domain': '.douban.com', 'expiry': 1674893183, 'httpOnly': False, 'name': 'push_doumail_num',
                'path': '/', 'secure': False, 'value': '0'},
               {'domain': '.douban.com', 'expiry': 1674893183, 'httpOnly': False, 'name': 'push_noty_num', 'path': '/',
                'secure': False, 'value': '0'},
               {'domain': '.douban.com', 'expiry': 1672308380, 'httpOnly': False, 'name': 'ap_v', 'path': '/',
                'secure': False, 'value': '0,6.0'},
               {'domain': '.douban.com', 'expiry': 1672302984, 'httpOnly': False, 'name': '__utmb', 'path': '/',
                'secure': False, 'value': '30149280.3.10.1672301171'},
               {'domain': '.douban.com', 'expiry': 1688069184, 'httpOnly': False, 'name': '__utmz', 'path': '/',
                'secure': False, 'value': '30149280.1672301171.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'},
               {'domain': 'www.douban.com', 'expiry': 1735373183, 'httpOnly': False, 'name': '_pk_id.100001.8cb4',
                'path': '/', 'secure': False, 'value': '0dcc9e58630e27ea.1672301169.1.1672301184.1672301169.'},
               {'domain': '.douban.com', 'httpOnly': False, 'name': 'ck', 'path': '/', 'secure': False,
                'value': 'T_pG'},
               {'domain': '.douban.com', 'expiry': 1672301771, 'httpOnly': False, 'name': '__utmt', 'path': '/',
                'secure': False, 'value': '1'},
               {'domain': '.douban.com', 'expiry': 1674893182, 'httpOnly': True, 'name': 'dbcl2', 'path': '/',
                'secure': False, 'value': '"140005612:U1zhcJlWzW0"'},
               {'domain': '.douban.com', 'httpOnly': False, 'name': '__utmc', 'path': '/', 'secure': False,
                'value': '30149280'},
               {'domain': '.douban.com', 'expiry': 1735373184, 'httpOnly': False, 'name': '__utma', 'path': '/',
                'secure': False, 'value': '30149280.1227971892.1672301171.1672301171.1672301171.1'},
               {'domain': 'www.douban.com', 'expiry': 1672302983, 'httpOnly': False, 'name': '_pk_ses.100001.8cb4',
                'path': '/', 'secure': False, 'value': '*'},
               {'domain': '.douban.com', 'expiry': 1703837167, 'httpOnly': False, 'name': 'bid', 'path': '/',
                'secure': False, 'value': '38qC2NZwOHE'},
               {'domain': '.douban.com', 'expiry': 1703837166, 'httpOnly': False, 'name': 'll', 'path': '/',
                'secure': False, 'value': '"108288"'}]

    # for j in cookies:
    #     print(j)
    #     # dc = json.load(j)
    #     print(j["name"] + "  " + j["value"])


    def getcookiedict(s):
        s=s.replace(" ","")
        dict_s={}
        ss=s.split(";")
        for s in ss:
            a=s.split("=")
            if len(a)==2:
                dict_s[a[0]]=a[1]

        return dict_s
    cookie1 = "ll=\"108288\"; bid=mBsf4AURe7o; _pk_ses.100001.8cb4=*; __utma=30149280.239647387.1672306801.1672306801.1672306801.1; __utmc=30149280; __utmz=30149280.1672306801.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); dbcl2=\"140005612:U1zhcJlWzW0\"; ck=T_pG; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; __utmv=30149280.14000; __yadk_uid=occP7eJRR4k7xevj42DAlAzFuG2eQsIk; __utmt=1; douban-fav-remind=1; _pk_id.100001.8cb4=3b95490bcb233ad3.1672306798.1.1672307444.1672306798.; __utmb=30149280.12.7.1672307443938"
    cookie2 = "b__yadk_uid=occP7eJRR4k7xevj42DAlAzFuG2eQsIk;__utmv=30149280.14000;push_doumail_num=0;push_noty_num=0;ap_v=0,6.0;__utmb=30149280.3.10.1672306801;__utmz=30149280.1672306801.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none);_pk_id.100001.8cb4=3b95490bcb233ad3.1672306798.1.1672306808.1672306798.;ck=T_pG;__utmt=1;dbcl2=\"140005612:U1zhcJlWzW0\";__utmc=30149280;__utma=30149280.239647387.1672306801.1672306801.1672306801.1;_pk_ses.100001.8cb4=*;bid=mBsf4AURe7o;ll=\"108288\""
    d1=getcookiedict(cookie1)
    d2=getcookiedict(cookie2)

    for key in d1.keys():
        if d2.__contains__(key)==False:
             print(key)
        else:
            if d2[key]!=d1[key]:
                print("not equal:"+key)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
