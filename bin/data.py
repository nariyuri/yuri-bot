# -*- coding:utf-8 -*- 
import requests
import time
import json
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from zeep import Client
import importBasedPackage
class GetInspectionInfo:
    """
    * get inspection info.
    * 
    * .startDateTime: Inspection start time <datetime>
    * .endDateTime: Inspection start time <datetime>
    * .strObstacleContents: Inspection information <str>
    * Complate
    """
    def __init__(self):
        _wsdl = 'http://api.maplestory.nexon.com/soap/maplestory.asmx?wsdl'
        _client = Client(wsdl=_wsdl)
        _soapData = _client.service.GetInspectionInfo()['_value_1']['_value_1'][0]['InspectionInfo']
        self.startDateTime = _soapData['startDateTime']
        self.endDateTime = _soapData['endDateTime']
        self.strObstacleContents = _soapData['strObstacleContents']

class GetEvent:
    """
    * get event data.
    *
    * .eventData
    * .eventDate
    * .eventUrl
    * .sundayMaple
    * 
    * .GetDetailEvent
    * - .imgUrl
    * 
    * HACK: GetDetailEvent 
    """
    def __init__(self):
        self._GetEvent()

    """
    * _GetEvent()
    * 
    * 
    """
    def _GetEvent(self) :
        self.eventData = []
        self.eventDate = []
        self.eventUrl = []
        _bs = BeautifulSoup(requests.get("https://maplestory.nexon.com/News/Event").text, 'html.parser')
        _tags = _bs.find_all('div',{'class':'event_list_wrap'})
        for _tag in _tags :
            _dds = _tag.find_all('dd')
            for _dd in _dds:
                if _dd.find('a'):
                    _eventData = _dd.text.strip('\n')
                    _eventUrl = "https://maplestory.nexon.com/"+_dd.find('a')['href']
                    self.eventData.append(_eventData)
                    self.eventUrl.append(_eventUrl)
                    if _eventData != -1:
                        self.sundayMaple = _eventUrl
                if _dd.find('dd', {'class':'date'}):    
                    self.eventDate.append(_dd.text.strip('\n'))
    """
    * 코드 재사용을 위해 인자 받는 static 함수로 만들기?
    * 일단 이벤트 이름 : 이벤트url > 이미지까지 가능하게 바꾸는게 나을듯
    * why, 몇개는 /news/event가 아니기에
    """
    def GetDetailEvent(self):
        for _eventUrl in self.eventUrl:
            if _eventUrl.find('/News/Event/') == -1:
                continue
            else:
                _bs = BeautifulSoup(requests.get(_eventUrl).text, 'html.parser')
                _tag = _bs.find('div',{'class':'new_board_con'})
                self.imgUrl = _tag.find("img")["src"]
    """
    * 주기적으로 DB와 비교후? or 금요일 선데이 뜰때 변경점 push
    * 여기서 할게 아님 아마 updatedb.py에서 할 예정
    """

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
    def __init__(self, userName):
        self.userName = userName
        self.GetUserData()

    def GetUserData(self):
        self.userName
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
        print(_Event.eventData, _Event.eventDate, _Event.eventUrl) #추가
        
    @importBasedPackage.decorators.TryFuncTest
    def TestGuildInfo():
        None

if __name__ == '__main__':
    Test.TestAll()

    
