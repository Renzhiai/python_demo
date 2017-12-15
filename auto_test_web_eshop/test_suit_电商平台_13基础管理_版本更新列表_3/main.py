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

print_log('开始测试：test_suit_电商平台_13基础管理_版本更新列表')

#获取driver,登录系统
driver = get_driver('http://192.168.0.96','/yihao01-eshop-web/loginPage')
log_in_eshop(driver,"super","123456")

#==========case==========
#新增版本更新
add_version_update_from_banbengengxinliebiao(driver)
#修改版本更新
modify_version_update_from_banbengengxinliebiao(driver)
#删除版本更新
delete_version_update_from_banbengengxinliebiao(driver)

wait(driver,3)
driver.quit()

print_log('【测试结果】：test_suit_电商平台_13营销管理_版本更新列表 ok！\n')