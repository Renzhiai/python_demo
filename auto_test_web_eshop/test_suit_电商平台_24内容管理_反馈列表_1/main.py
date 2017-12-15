# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from test_case import *
import sys

sys.path.append('..')

print_log('开始测试：test_suit_电商平台_24内容管理_反馈列表')

#获取driver,登录系统
driver = get_driver('http://192.168.0.96','/yihao01-eshop-web/loginPage')
log_in_eshop(driver,"super","123456")

#==========case==========
#查看回复
select_reply_from_fankuiliebiao(driver)

wait(driver,3)
driver.quit()

print_log('【测试结果】：test_suit_电商平台_24内容管理_反馈列表 ok！\n')