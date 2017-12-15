# -*- coding: utf-8 -*-
from datetime import datetime
import sys
sys.path.append('..')
from methods import *

def add_information_from_xitonggonggaoliebiao(driver,title=u'物价上涨，以后电费10元/度',content=u'我不是和你开玩笑，我说真的'):
    '''
    内容管理-》系统公告列表-》新增公告
    :param driver:
    :param title: 主题
    :param content: 内容
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_21内容管理_系统公告列表_新增公告',',')
        original_window=driver.current_window_handle
        enter_module(driver,'内容管理')
        enter_index(driver,'系统公告列表')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #点击新增
        click_add_btn(driver)
        #设置标题
        send_keys_by_id(driver,'title',title)
        #设置内容
        send_keys_by_id(driver,'content',content)
        #设置开始时间
        set_period(driver,False)
        #点击保存
        click_add_ok_btn(driver)
        #切换原来的窗口
        driver.switch_to_window(right_window)
        print_log('     【result】：ok')
        result_insert_sql('新增公告','success')
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('新增公告','fail')

def edit_information_from_xitonggonggaoliebiao(driver,title=u'物价上涨，以后电费10元/度',content=u'不好意思，开玩笑的，哈哈'):
    '''
    内容管理-》系统公告列表-》编辑公告
    :param driver:
    :param title: 主题
    :param content: 内容
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_21内容管理_系统公告列表_编辑公告',',')
        original_window=driver.current_window_handle
        enter_module(driver,'内容管理')
        enter_index(driver,'系统公告列表')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        select_first(driver)
        #点击新增
        click_edit_btn(driver)
        #设置标题
        send_keys_by_id(driver,'title',title)
        #设置内容
        send_keys_by_id(driver,'content',content)
        #设置开始时间
        set_period(driver,False)
        #点击保存
        driver.find_element_by_id('addOkBtn2').click(), wait(driver)
        #切换原来的窗口
        driver.switch_to_window(right_window)
        print_log('     【result】：ok')
        result_insert_sql('编辑公告','success')
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('编辑公告','fail')

def delete_information_from_xitonggonggaoliebiao(driver):
    '''
    内容管理-》系统公告列表-》删除公告
    :param driver:
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_21内容管理_系统公告列表_删除公告',',')
        original_window=driver.current_window_handle
        enter_module(driver,'内容管理')
        enter_index(driver,'系统公告列表')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #选中第一条
        select_first(driver)
        #点击删除
        click_delete_btn(driver)
        #点击确定
        driver.find_element_by_xpath('html/body/div[10]/div[2]/div[4]/a[1]/span/span').click(), wait(driver)
        #切换原来的窗口
        driver.switch_to_window(right_window)
        print_log('     【result】：ok')
        result_insert_sql('删除公告','success')
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('删除公告','fail')

def publish_information_from_xitonggonggaoliebiao(driver):
    '''
    内容管理-》系统公告列表-》发布公告
    :param driver:
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_21内容管理_系统公告列表_发布公告',',')
        original_window=driver.current_window_handle
        enter_module(driver,'内容管理')
        enter_index(driver,'系统公告列表')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #选中第一条
        select_first(driver)
        #点击发布
        driver.find_element_by_id('publishBtn').click(), wait(driver)
        #点击确定
        driver.find_element_by_xpath('html/body/div[10]/div[2]/div[4]/a[1]/span/span').click(), wait(driver)
        #切换原来的窗口
        driver.switch_to_window(right_window)
        print_log('     【result】：ok')
        result_insert_sql('发布公告','success')
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('发布公告','fail')

def unpublish_information_from_xitonggonggaoliebiao(driver):
    '''
    内容管理-》系统公告列表-》取消发布公告
    :param driver:
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_21内容管理_系统公告列表_取消发布公告',',')
        original_window=driver.current_window_handle
        enter_module(driver,'内容管理')
        enter_index(driver,'系统公告列表')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #选中第一条
        select_first(driver)
        #点击取消发布
        driver.find_element_by_id('unPublishBtn').click(), wait(driver)
        #点击确定
        driver.find_element_by_xpath('html/body/div[10]/div[2]/div[4]/a[1]/span/span').click(), wait(driver)
        #切换原来的窗口
        driver.switch_to_window(right_window)
        print_log('     【result】：ok')
        result_insert_sql('取消发布公告','success')
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('取消发布公告','fail')