# -*- coding: utf-8 -*-
from datetime import datetime
import sys
sys.path.append('..')
from methods import *

def add_product_from_chanpinzuguanli(driver,product_name=u'美味草莓',product_desc=u'这个草莓很好吃，很大，很红润',product_status=u'生效'):
    '''
    从商品中心-》产品组管理(SPU)里面增加一个商品
    :param driver:
    :param product_name: 产品名字
    :param product_desc: 产品描述
    :param product_status: 生效或者失效
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_03商品中心_产品组管理(SPU)_新增产品',',')
        original_window=driver.current_window_handle
        enter_module(driver,'商品中心')
        enter_index(driver,'产品组管理(SPU)')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #点击新增
        click_add_btn(driver)
        #点击后台分类
        driver.find_element_by_css_selector('div[class="fl"]').click(), wait(driver)
        #点击优选水果 //id变动可能性大
        driver.find_element_by_id('_easyui_tree_3').click() ,wait(driver)
        #设置产品名字
        send_keys_by_id(driver,'spuName',product_name)
        #设置产品描述
        send_keys_by_id(driver,'spuDesc',product_desc)
        #设置失效状态
        if product_status==u'生效':
            product_status=0
        else:
            product_status=1
        set_status(driver,product_status)
        #点击上传图片
        driver.find_element_by_id('bgImgBtn').click() ,wait(driver)
        #输入图片的名字 test.png   桌面放置一张以test.png命名的图片
        upload_pic(driver)
        #有的电脑慢，等待5秒加载
        time.sleep(5)
        #点击保存
        click_add_ok_btn(driver)

        '''
        #切换到窗口
        driver.switch_to_window(right_window)
        driver.switch_to_frame(0)
        current_time=get_current_time_nozero()
        #获取产品所属分类
        product_category_new=driver.find_elements_by_css_selector('td[field="classifyName"]')[1].\
               find_element_by_tag_name('div').text
        print(product_category_new)
        #获取产品名称
        product_name_new=driver.find_elements_by_css_selector('td[field="spuName"]')[1].\
               find_element_by_tag_name('div').text
        print(product_name_new)
        #获取产品描述
        product_desc_new=driver.find_elements_by_css_selector('td[field="spuDesc"]')[1].\
               find_element_by_tag_name('div').text
        print(product_desc_new)
        #获取产品状态
        product_status_new=driver.find_elements_by_css_selector('td[field="status"]')[1].\
               find_element_by_tag_name('div').text
        print(product_status_new)
        #获取产品更新时间
        product_time=driver.find_elements_by_css_selector('td[field="updateTime"]')[1].\
               find_element_by_tag_name('div').text
        print(product_time[0:-3])
        print(current_time)
        #从网页获取的数据都是Unicode编码
        if product_category_new==u'产地特卖-优选水果' and product_name_new==u'美味草莓' and \
            product_desc_new==product_desc and product_status_new==u'生效' and \
            product_time[0:-3]==current_time:
            print(u'测试成功')

        else:
            print(u'测试失败')
            return False
        '''
        driver.switch_to_window(original_window)
        print_log('     【result】：ok')
        result_insert_sql('添加商品','success')
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('添加商品','fail')

def edit_product_from_chanpinzuguanli(driver,product_name=u'好吃的草莓',product_desc=u'来自美丽的东北大草原',product_status=u'失效'):
    '''
    商品中心-》产品组管理(SPU)-》编辑产品，修改产品名字，产品描述，产品状态置为失效
    :param driver:
    :param product_name:产品名字
    :param product_desc:产品描述
    :param product_status:产品状态，生效或者失效
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_03商品中心_产品组管理(SPU)_编辑产品',',')
        original_window=driver.current_window_handle
        enter_module(driver,'商品中心')
        enter_index(driver,'产品组管理(SPU)')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #选中第一条产品
        select_first(driver)
        #点击编辑
        click_edit_btn(driver)
        #设置产品名字
        send_keys_by_id(driver,'spuName',product_name)
        #设置产品描述
        send_keys_by_id(driver,'spuDesc',product_desc)
        #设置状态   失效
        if product_status==u'生效':
            product_status=0
        else:
            product_status=1
        set_status(driver,product_status)
        #点击保存
        click_edit_ok_btn(driver)

        '''
        #切换到窗口
        driver.switch_to_window(right_window)
        driver.switch_to_frame(0)
        current_time=get_current_time_nozero()
        #获取产品名称
        product_name_new=driver.find_elements_by_css_selector('td[field="spuName"]')[1].\
               find_element_by_tag_name('div').text
        print(product_name_new)
        #获取产品描述
        product_desc_new=driver.find_elements_by_css_selector('td[field="spuDesc"]')[1].\
               find_element_by_tag_name('div').text
        print(product_desc_new)
        #获取产品状态
        product_status_new=driver.find_elements_by_css_selector('td[field="status"]')[1].\
               find_element_by_tag_name('div').text
        print(product_status_new)
        #获取产品更新时间
        product_time=driver.find_elements_by_css_selector('td[field="updateTime"]')[1].\
               find_element_by_tag_name('div').text

        if product_name_new==product_name and \
            product_desc_new==product_desc and product_status_new==u'失效' and \
            product_time[0:-3]==current_time:
            print(u'测试成功')
        else:
            print(u'测试失败')
            return False
        '''
        driver.switch_to_window(original_window)
        print_log('     【result】：ok')
        result_insert_sql('编辑产品','success')
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('编辑产品','fail')

def modify_category_from_chanpinzuguanli(driver):
    '''
    商品中心-》产品组管理(SPU)-》修改产品分类，前提是产品是失效状态
    :param driver:
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_03商品中心_产品组管理(SPU)_修改分类',',')
        original_window=driver.current_window_handle
        enter_module(driver,'商品中心')
        enter_index(driver,'产品组管理(SPU)')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #选中第一条产品
        select_first(driver)
        #点击批量修改分类
        driver.find_element_by_id('classify').click()   ,wait(driver)
        #点击后台分类
        print(len(driver.find_elements_by_css_selector('div[class="fl"]')))
        driver.find_elements_by_css_selector('div[class="fl"]')[1].click(), wait(driver)
        #点击坚果熟食 //id变动可能性很大
        driver.find_element_by_id('_easyui_tree_66').click()    ,wait(driver)
        #点击保存
        driver.find_element_by_id('editCapOkBtn').click()   ,wait(driver)
        #点击确定
        driver.find_element_by_xpath('html/body/div[14]/div[2]/div[4]/a/span/span').click(), wait(driver)

        '''
        #切换到窗口
        driver.switch_to_window(right_window)
        driver.switch_to_frame(0)
        current_time=get_current_time_nozero()
        #获取产品所属分类
        product_category_new=driver.find_elements_by_css_selector('td[field="classifyName"]')[1].\
               find_element_by_tag_name('div').text
        print(product_category_new)
        #获取产品更新时间
        product_time=driver.find_elements_by_css_selector('td[field="updateTime"]')[1].\
               find_element_by_tag_name('div').text
        if product_category_new==u'产地特卖-坚果熟食' and product_time[0:-3]==current_time:
            print(u'测试成功')
        else:
            print(u'测试失败')
            return False
        '''
        driver.switch_to_window(original_window)
        print_log('     【result】：ok')
        result_insert_sql('修改产品分类','success')
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('修改产品分类','fail')