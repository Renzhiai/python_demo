# coding:utf-8
import requests
import time
import re
from bs4 import BeautifulSoup

cookie106 = ''
cookie28 = 'plf=/manage/systemAction!centerInfoShow.do; JSESSIONID=378D71082871D483B51DC4FC6F9F5080; eid01=wKgAyFqxsvsYJktrPLSnAg==; UM_distinctid=1644a29cbe6279-0143d8149ef771-3e3d5f01-1fa400-1644a29cbe75aa'
host106 = 'https://testone.0easy.com'
host28 = 'https://01.0easy.com'
host = host28
cookie = cookie28
unitId = '971379'
roomCode = '01010101'

def getTotalPage():
    '''获取总页数'''
    totalPage = ''  # 数据所显示的页数
    urlFind = host + '/yihao01-ecommunity-cloud/manage/doorAction!nfcList.do'
    result = requests.get(urlFind, headers={'Cookie': cookie}, verify=False)
    for line in result.content.decode('utf-8').split('\n'):
        kw = re.findall(re.compile('条(.*?)页'),line)
        if kw:
            #得到的kw是一个list
            for s in kw[0]:
                if s.isdigit():
                    totalPage = totalPage + s
    if not totalPage.isdigit():
        print('没有获取到总页数')
        return 0
    print('发卡页数为：' + totalPage)
    return totalPage

def getAllCardId():
    cardIds = []  # 用于保存获取到的卡号
    totalPage = getTotalPage()
    for i in range(int(totalPage)):
        #页码规律是
        page = (int(i) - 1) * 10
        urlFindByPage = host + '/yihao01-ecommunity-cloud/manage/doorAction!nfcList.do?pager.offset=' + str(page)
        
        result = requests.get(urlFindByPage, headers={'Cookie': cookie},verify=False)
        bsObj = BeautifulSoup(result.content.decode('utf-8'))
        for line in result.content.decode('utf-8').split('\n'):
            if "detail('" in line:
                startIndex = line.find("detail('")
                endIndex = line.find("')\" value")
                cardIds.append(line[startIndex+8:endIndex])
        time.sleep(0.1)
    return cardIds


def deleteCardById():
    cardIds = getAllCardId()
    for cardId in cardIds:
        # 注销卡
        url = host + '/yihao01-ecommunity-cloud/manage/nfcCardAction!delNfcRecord.do'
        dict_all = {
            'unitId': '971379',
            'roomCode': '01010101',
            'cardId': cardId,
            'cardType': '2'
        }
        result = requests.post(url, params=dict_all, headers={'Cookie': cookie}, verify=False)
        print(result.status_code)
        # print(result.content.decode('utf-8'))
        time.sleep(0.1)

if __name__ == '__main__':
    getAllCardId()
    # deleteCardById()