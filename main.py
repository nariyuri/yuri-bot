# -*- coding:utf-8 -*- 
import os
import requests
import re
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from urllib import parse
from zeep import Client
import json


class GetInspectionInfo:
    """
    * get inspection info.
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
    
    def GetSundayMaple(self):
        self.eventUrl
    
class EfficiencyCalc:
    def __init__(self, _atc, _def, _boss):
        print(list(map(lambda x, y, z: 100*(((100+x)/100)*((100+y)/100))*(z/100*300-300+100), _atc, _def, _boss)))
    
class GetGuildInfo:
    def __init__(self):
        
_atc = [60, 90]
_def = [93, 93]
_boss = [500, 400]
print(92/100*300-300+100)
ho = EfficiencyCalc(_atc, _def, _boss)

print(InspectionInfo.endDateTime)