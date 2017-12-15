# -*- coding: utf-8 -*-
from datetime import datetime
import sys
sys.path.append('..')
from methods import *

def preview_invitation_from_yonghuyaoqingliebiao(driver):
    '''
    营销管理-》用户邀请列表-》预览
    :param driver:
    :return:
    '''
    try:
        print_log(u'【case】：test_suit_电商平台_10营销管理_用户邀请列表_预览邀请情况',',')
        original_window=driver.current_window_handle
        enter_module(driver,'营销管理')
        enter_index(driver,'用户邀请列表')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        select_first(driver)
        #获取第一条的用户名称
        name=driver.find_elements_by_css_selector('td[field="name"]')[1].find_element_by_tag_name('div').text
        #获取第一条的邀请码
        invitation_code=driver.find_elements_by_css_selector('td[field="inviteCode"]')[1].find_element_by_tag_name('div').text
        #获取第一条的成功邀请数
        total=driver.find_elements_by_css_selector('td[field="total"]')[1].find_element_by_tag_name('div').text
        #获取第一条的邀请码创建时间
        create_time=driver.find_elements_by_css_selector('td[field="createTime"]')[1].find_element_by_tag_name('div').text
        #点击预览
        driver.find_element_by_id('previewBtn').click(), wait(driver)
        #获取预览的用户名称
        name_preview=driver.find_element_by_id('preview_userName').text
        #获取预览的邀请码
        invitation_code_preview=driver.find_element_by_id('preview_inviteCode').text
        #获取预览的成功邀请数
        total_preview=driver.find_element_by_id('preview_total').text
        #获取预览的创建时间
        create_time_preview=driver.find_element_by_id('preview_createTime').text
        # print(name==name_preview)
        # print(invitation_code==invitation_code_preview)
        # print(total==total_preview)
        # print(create_time==create_time_preview[0:19])
        #暂不对比时间
        if name==name_preview and invitation_code==invitation_code_preview and total==total_preview:
                #and create_time==create_time_preview[0:19]:
            print(u'测试成功')
            print_log(u'     【result】：ok')
            result_insert_sql('预览邀请情况','success')
        else:
            print(u'测试失败')
            print_log(u'     【result】：fail')
            result_insert_sql('预览邀请情况','fail')
        driver.switch_to_window(original_window)
    except Exception,e:
        print_log(u'     【result】：fail')
        result_insert_sql('预览邀请情况','fail')
