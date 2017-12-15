# -*- coding: utf-8 -*-
from datetime import datetime
import sys
sys.path.append('..')
from methods import *

def select_verifycode_from_duanxinyanzhengmachaxun(driver,phone=u'17722402544'):
    '''
    基础管理-》短信验证码查询-》查询验证码
    :param driver:
    :param phone:要查询的手机号
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_18基础管理_短信验证码查询_查询验证码',',')
        original_window=driver.current_window_handle
        enter_module(driver,'基础管理')
        enter_index(driver,'短信验证码查询')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #设置移动电话
        send_keys_by_name(driver,'phone',phone)
        #点击搜索
        driver.find_element_by_id('btn-search').click(), wait(driver)
        #切换原来的窗口
        driver.switch_to_window(right_window)
        print_log('     【result】：ok')
        result_insert_sql('查询验证码','success')
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('查询验证码','fail')
