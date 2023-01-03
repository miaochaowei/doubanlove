from selenium import webdriver
import time
import pandas   as pd
import datetime
import  json
import requests
import os.path as Path
from bs4 import BeautifulSoup



chrome_driver="/home/mi/PycharmProjects/doubanlove/ke/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get('https://www.douban.com/')
# # 点击 密码登录  按钮 。但是找不到该element，不存在网页中
# 找到登陆的iframe
login_iframe = driver.find_element_by_xpath('//div[@class="login"]/iframe')
# 切换到iframe
driver.switch_to.frame(login_iframe)
# 点击密码登陆account-tab-account
driver.find_element_by_class_name('account-tab-account').click()
# 填写账号
driver.find_element_by_id('username').clear()
driver.find_element_by_id('username').send_keys('18518056212')
time.sleep(2)
# 填写密码
driver.find_element_by_id('password').clear()
driver.find_element_by_id('password').send_keys('mcw19910212')
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[5]/a').click()


