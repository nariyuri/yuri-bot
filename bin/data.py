# -*- coding:utf-8 -*- 
import requests
import time
from datetime import datetime
import json
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from zeep import Client
import importBasedPackage

class GetInspectionInfo:
    """
    * @brief: get inspection info.
    * @param: None
    * @instance variable: .inspectionInfo <json>
    * {
    *   "inspectionContents": inspection info,
    *   "startDateTime": "inspection start time" <Y-%m-%d %H:%M:%S+09:00>,
    *   "endDateTime": "inspection end time" <%Y-%m-%d %H:%M:%S+09:00>
    * }                     
    """
    def __init__(self):
        _inspectionInfo = {}
        _wsdl = 'http://api.maplestory.nexon.com/soap/maplestory.asmx?wsdl'
        _client = Client(wsdl=_wsdl)
        _soapData = _client.service.GetInspectionInfo()['_value_1']['_value_1'][0]['InspectionInfo']
        _inspectionInfo['inspectionContents'] = _soapData['strObstacleContents']
        _inspectionInfo['startDateTime'] = str(_soapData['startDateTime'])
        _inspectionInfo['endDateTime'] = str(_soapData['endDateTime'])
        self.inspectionInfo = json.dumps(_inspectionInfo, ensure_ascii=False, indent=4)
        print(self.inspectionInfo)

        

class GetEvent:
    """
    * @brief: get event data.
    * @param: None
    * @instance function: _GetEvent: get event data from maplestory ofiicial site and return json
    *
    """
    def __init__(self):
        self._GetEvent()

    def _GetEvent(self) :
        """
        * @brief: 공홈에서 이벤트 정보 크롤링
        * @param: None
        * @variable: .eventData <json> 
        * {
        *   "eventName": {
        *       "url": "eventUrl"
        *       "imgUrl": "eventImgUrl"
        *       "startDateTime": "event start Date <%Y-%m-%D>"
        *       "endDateTime": "event end Date <%Y-%m-%D>"
        *       }   
        * }                               
        *  
        """
        _eventData = {}
        _bs = BeautifulSoup(requests.get("https://maplestory.nexon.com/News/Event").text, 'html.parser')
        _tags = _bs.find_all('div',{'class':'event_list_wrap'})
        for _tag in _tags :
            temp = {}
            if _tag.find('dd', {'class':'data'}):
                _eventName = _tag.find('dd', {'class':'data'}).text.strip('\n')
                _eventUrl = "https://maplestory.nexon.com/"+_tag.find('a')['href']
                temp['url'] = _eventUrl
                if _eventUrl.find('/News/Event/') == -1:
                    pass
                else:
                    __bs = BeautifulSoup(requests.get(_eventUrl).text, 'html.parser')
                    __tag = __bs.find('div',{'class':'new_board_con'})
                    temp['imgUrl'] = __tag.find("img")["src"]
            if _tag.find('dd', {'class':'date'}):
                temp['startDateTime'], temp['endDateTime'] = GetEvent._StrToDatetime(_tag.find('dd', {'class':'date'}).text.strip('\n'))
                _eventData[_eventName] = temp
            else:
                _eventData[_eventName] = temp
        self.eventData = json.dumps(_eventData, ensure_ascii=False, indent=4)
    @staticmethod
    def _StrToDatetime(string):
        dates = string.replace(" ", "").split('~')
        startDateTime, endDateTime = datetime.strptime(dates[0], '%Y.%m.%d').strftime('%Y-%m-%d'), datetime.strptime(dates[1], '%Y.%m.%d').strftime('%Y-%m-%d')
        return startDateTime, endDateTime

class GetGuildInfo:
    def __init__(self, guildName, guildWorld):
        self.guildName = guildName
        self.guildWorld = guildWorld

    def GetGuildData(self):
        _bs = BeautifulSoup(requests.get("www.maple.gg/guild/"+self.guildWorld+"/"+self.guildName+"/members?sort=level").text, 'html.parser')
        """
        * 데코레이터로 바꾸기 위해 시도할 예정
        * why? user Data불러올때도 동일한 상황 발생
        """
        if _bs.find('i', {'class':'fa fa-info-circle'}): #갱신이 필요할경우
            done = False
            while done == True: #완료될때까지
                _json = json.loads(requests.get("www.maple.gg/guild/"+self.guildWorld+"/"+self.guildName+"/sync").text) #sync request후 json Data 받아오기
                if 'error' in _json: #{"error": True}
                    return "길드를 찾을 수 없습니다."
                else:
                    if _json['done'] == True: #{"done": True}
                        done == True     
                        _bs = BeautifulSoup(requests.get("www.maple.gg/guild/"+self.guildWorld+"/"+self.guildName+"/members?sort=level").text, 'html.parser')       
                    else: #{"done":False}시 2초 후 재 요청
                        time.sleep(2)
        self.guildInfoData = _bs    
    """
    * 여기서 받아와야 할 정보
    * 최근접속일, 레벨, 닉네임 etc
    * 무릉 층수및 상세정보는 GetUserInro에서 처리할 예정
    """
    def GetGuildUserInfo(self):
        None
        

class GetUserInfo:
    """
    * @brief: get user's info.
    * @param: userNames <str or list>
    * @instance function: _GetEvent: get event data from maplestory ofiicial site
    *                     GetDetailEvent: get image data about event                     
    * @instance variable: _GetEvent
    *                     >.eventData: name of ongoing events <list>
    *                     >.eventDate: duration of events <list>
    *                     >.eventUrl: url of events <list>
    *                     >.sundayMaple
    * 
    *                     .GetDetailEvent
    *                     >.imgUrl: url of event images <list>
    * TODO: list > json change 
    * HACK: GetDetailEvent 
    *
    """
    def __init__(self, userNames):
        self.userNames = userNames
        self.fetchedData = []
        self.GetUserData()

    def GetUserData(self):
        for userName in self.userNames:
            self.fetchedData.append(requests.get("www.maple.gg/u"+userName).text)
        
    def ParseUserMurung(self):
        for _fetchedData in self.fetchedData:
            _bs = BeautifulSoup(_fetchedData, 'html.parser')
            _tags = _bs.find('div',{'class':'user-summary-box-content text-center position-relative'})
            if _tags:
                for _tag in _tags:
                    floor = (" ".join(_tag.h1.text.split()))
                    userFloor.append(floor)
            else :
                userFloor.append('x')


"""
* For Test Func
* If I add something, MUST be add here
* 
"""     

class Test:
    """
    * Test all funcs
    """
    @classmethod
    def TestAll(cls):
        cls.TestInspectionInfo()
        cls.TestEvent()

    @classmethod
    @importBasedPackage.decorators.TryFuncTest #Complate
    def TestInspectionInfo(cls):
        _InspectionInfo = GetInspectionInfo()
        print("패치정보:", _InspectionInfo.startDateTime, _InspectionInfo.endDateTime, _InspectionInfo.strObstacleContents)
        """
        * 시작시간, 끝나는시간, 패치정보
        """

    @classmethod
    @importBasedPackage.decorators.TryFuncTest
    def TestEvent(cls):
        _Event = GetEvent()
        print(_Event.eventData) #추가
        
    @importBasedPackage.decorators.TryFuncTest
    def TestGuildInfo():
        None

if __name__ == '__main__':
    Test.TestAll()

    
