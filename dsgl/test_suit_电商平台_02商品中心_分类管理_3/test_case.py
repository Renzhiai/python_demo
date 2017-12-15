# -*- coding: utf-8 -*-
from datetime import datetime
import sys
sys.path.append('..')
from methods import *

def add_category_from_fenleiguanli(driver,category_name=u'测试分类',category_desc=u'这是一个测试分类的描述',serial_num='1'):
    '''
    从商品中心-》分类管理里面添加一个分类
    :param driver:
    :param category_name:要添加分类的名字
    :param category_desc:分类的描述
    :param category_serial_num:分类的序号
    :return:
    '''
    try:
        print_log(u'【case】：test_suit_电商平台_02商品中心_分类管理_添加分类',',')
        original_window=driver.current_window_handle
        enter_module(driver,'商品中心')
        enter_index(driver,'分类管理')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #点击添加分类
        click_add_btn(driver)
        #设置分类名称     //要填写的数据必须是unicode编码
        send_keys_by_name(driver,'categoryName',category_name)
        #设置分类描述
        send_keys_by_name(driver,'categoryDesc',category_name)
        #设置序列号
        send_keys_by_name(driver,'serialNum',serial_num)
        #点击确定
        click_add_ok_btn(driver)
        '''
        #切换窗口
        driver.switch_to_window(right_window)
        driver.switch_to_frame(0)
        #获得分类名称     //从网页获取的数据，全部是Unicode编码
        category_name_new=driver.find_elements_by_css_selector('td[field="categoryName"]')[1].\
                                 find_element_by_tag_name('div').\
                                 find_elements_by_tag_name('span')[2].text
        # category_name_new=driver.find_element_by_xpath(".//*[@id='datagrid-row-r2-2-1114']/td[1]/div/span[3]").text
        #获得修改时间
        category_time_new=driver.find_elements_by_css_selector('td[field="updateTime"]')[1].\
                                 find_element_by_tag_name('div').text
        #获得分类排序号
        category_serial_num_new=driver.find_elements_by_css_selector('td[field="serialNum"]')[1].\
                                 find_element_by_tag_name('div').text
        #时间对比，只对比到分钟，不对比秒钟
        now_time=get_current_time_nozero()
        print(type(category_time_new[0:-3]))
        log('实际时间为：'+now_time)
        log('网页上显示的时间为：'+str(category_time_new[0:-3]))
        if category_name==category_name_new and now_time==category_time_new[0:-3]\
                and category_serial_num==category_serial_num_new:
            print(u'测试成功')
        else:
            print(u'测试失败')
            return False
        '''
        driver.switch_to_window(original_window)
        print_log(u'     【result】：ok')
        result_insert_sql('添加分类','success')
    except Exception,e:
        print_log(u'     【result】：fail')
        result_insert_sql('添加分类','fail')

def edit_category_from_fenleiguanli(driver,category_name=u'这是编辑测试分类'):
    '''
    从商品中心-》分类管理里面编辑分类
    :param driver:
    :param category_name: 分类名字
    :return:
    '''
    try:
        print_log(u'【case】：test_suit_电商平台_02商品中心_分类管理_编辑分类',',')
        original_window=driver.current_window_handle
        enter_module(driver,'商品中心')
        enter_index(driver,'分类管理')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #点击第一个分类
        select_first(driver)
        #点击编辑
        click_edit_btn(driver)
        #设置分类名称
        send_keys_by_name(driver,'categoryName',category_name)
        #点击确定
        click_edit_ok_btn(driver)
        '''
        #切换窗口
        driver.switch_to_window(right_window)
        driver.switch_to_frame(0)
        #获得分类名称
        category_name_new=driver.find_elements_by_css_selector('td[field="categoryName"]')[1].\
                                 find_element_by_tag_name('div').\
                                 find_elements_by_tag_name('span')[2].text
        print(category_name_new)
        if category_name==category_name_new:
            print(u'测试成功')
        else:
            print(u'测试失败')
            return False
        '''
        driver.switch_to_window(original_window)
        print_log(u'     【result】：ok')
        result_insert_sql('编辑分类','success')
    except Exception,e:
        print_log(u'     【result】：fail')
        result_insert_sql('编辑分类','fail')

def delete_category_from_fenleiguanli(driver):
    '''
    从商品中心-》分类管理里面删除一个分类
    :param driver:
    :return:
    '''
    try:
        print_log(u'【case】：test_suit_电商平台_02商品中心_分类管理_删除分类',',')
        original_window=driver.current_window_handle
        enter_module(driver,'商品中心')
        enter_index(driver,'分类管理')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #点击第一个分类
        select_first(driver)
        # 获得分类名称
        # category_name=driver.find_elements_by_css_selector('td[field="categoryName"]')[1].\
        #                          find_element_by_tag_name('div').\
        #                          find_elements_by_tag_name('span')[2].text
        #点击删除
        click_delete_btn(driver)
        #点击确定
        click_delete_ok_btn(driver)
        '''
        #切换窗口
        driver.switch_to_window(right_window)
        driver.switch_to_frame(0)
        #获得分类名称
        category_name_new=driver.find_elements_by_css_selector('td[field="categoryName"]')[1].\
                                 find_element_by_tag_name('div').\
                                 find_elements_by_tag_name('span')[2].text
        print(category_name_new)
        if category_name!=category_name_new:
            print(u'测试成功')
        else:
            print(u'测试失败')
            return False
        '''
        driver.switch_to_window(original_window)
        print_log(u'     【result】：ok')
        result_insert_sql('删除分类','success')
    except Exception,e:
        print_log(u'     【result】：fail')
        result_insert_sql('删除分类','fail')