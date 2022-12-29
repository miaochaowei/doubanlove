from selenium import webdriver
import time
import urllib.request
from chaojiying import Chaojiying_Client
chrome_driver="/home/mi/PycharmProjects/doubanlove/ke/chromedriver"
driver=webdriver.Chrome(executable_path=chrome_driver)
url = 'https://www.douban.com/'
driver.get(url)

def get_cookies():
    # option = webdriver.ChromeOptions()
    # option.set_headless()
    # driver = webdriver.Chrome(options=option)
    driver.find_element_by_id('form_email').clear()
    driver.find_element_by_id('form_email').send_keys('18518056212')
    driver.find_element_by_id('form_password').clear()
    driver.find_element_by_id('form_password').send_keys('mcw19910212')
    driver.implicitly_wait(5)
    driver.find_element_by_class_name('bn-submit').click()

    time.sleep(10)  # 这里再想办法处理验证码的事情，现在手动输入
    cookies_list = driver.get_cookies()
    driver.quit()
    use_cookies(cookies_list)

def get_cookies2():
    driver.find_element_by_id('form_email').clear()
    driver.find_element_by_id('form_email').send_keys('18518056212')
    driver.find_element_by_id('form_password').clear()
    driver.find_element_by_id('form_password').send_keys('mcw19910212')

    img = driver.find_element_by_id('captcha_image')
    img_url = img.get_attribute('src')
    urllib.request.urlretrieve(img_url, '/home/mi/PycharmProjects/doubanlove/data/douban.jpg')
    time.sleep(3)
    yanzhengma = Chaojiying_Client.result222()
    driver.find_element_by_id('captcha_field').send_keys(yanzhengma)  # 验证码输入搞定了，非常好用
    driver.implicitly_wait(5)
    driver.find_element_by_class_name('bn-submit').click()

    time.sleep(5)
    cookies_list = driver.get_cookies()
    driver.quit()

def use_cookies(cookies_list):
    driver=webdriver.Chrome(executable_path=chrome_driver)
    driver.get(url)
    driver.delete_all_cookies()
    time.sleep(3)
    for cookie in cookies_list:
        cookie_dict={
        "domain":".douban.com",
        'name': cookie.get('name'),
        'value': cookie.get('value'),
        "expires": "",
        'path': '/',
        'httpOnly': False,
        'HostOnly': False,
        'Secure': False
        }
        driver.add_cookie(cookie_dict)
    driver.refresh()
    if(driver.find_element_by_xpath('//*[@id="db-nav-sns"]/div/div/div[3]/ul/li[2]/a').text=='我的豆瓣'):
        print('恭喜你已经使用cookies登录成功。')
    driver.quit()

try:
    driver.find_element_by_id('captcha_field')
    a=True
except:
    a=False

    if a==True:
        print("验证码元素存在，保存验证码图片，并将图片上传给超级鹰识别，取的回传的验证码进行登录")
        get_cookies2()
    elif a==False:
        print("验证码元素不存在")
        get_cookies()