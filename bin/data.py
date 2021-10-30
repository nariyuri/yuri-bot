# -*- coding:utf-8 -*- 
import requests
import time
import json
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from urllib import parse
from zeep import Client

class GetInspectionInfo:
    """
    * get inspection info.
    * 
    * .startDateTime: Inspection start time <datetime>
    * .endDateTime: Inspection start time <datetime>
    * .strObstacleContents: Inspection information <str>
    """
    def __init__(self):
        _wsdl = 'http://api.maplestory.nexon.com/soap/maplestory.asmx?wsdl'
        _client = Client(wsdl=_wsdl)
        _soapData = _client.service.GetInspectionInfo()['_value_1']['_value_1'][0]['InspectionInfo']
        self.startDateTime = _soapData['startDateTime']
        self.endDateTime = _soapData['endDateTime']
        self.strObstacleContents = _soapData['strObstacleContents']

class Event:
    """
    * get event data.
    *
    * .eventData
    * .eventDate
    * .eventUrl
    * .sundayMaple
    *
    * TODO: GetSundayMaple 
    * HACK: GetDetailEvent 
    """
    def __init__(self):
        self._GetEvent()

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
    * 
    """
    def GetSundayMaple(self): 
        self.eventUrl 

class GetGuildInfo:
    def __init__(self, guildName, guildWorld):
        self.guildName = guildName
        self.guildWorld = guildWorld

    def GetGuildData(self):
        _bs = BeautifulSoup(requests.get("www.maple.gg/guild/"+self.guildWorld+"/"+self.guildName+"/members?sort=level").text, 'html.parser')
        if _bs.find('i', {'class':'fa fa-info-circle'}): #갱신이 필요할경우
            done = False
            while done == True:
                _json = json.loads(requests.get("www.maple.gg/guild/"+self.guildWorld+"/"+self.guildName+"/sync").text)
                if 'error' in _json:
                    return "길드를 찾을 수 없습니다."
                else:
                    if _json['done'] == True:
                        done == True     
                        _bs = BeautifulSoup(requests.get("www.maple.gg/guild/"+self.guildWorld+"/"+self.guildName+"/members?sort=level").text, 'html.parser')       
                    else:
                        time.sleep(2)
        self.guildInfoUrl = _bs    
    
    def GetGuildUserInfo(self):
        None
        

class GetUserInfo:
    def __init__(self, userName):
        self.userName = userName
        self.GetUserData()

    def GetUserData(self):
        self.userName
            

if __name__ == '__main__':
    InspectionInfo = GetInspectionInfo()
    print(InspectionInfo.startDateTime, InspectionInfo.endDateTime, InspectionInfo.strObstacleContents)