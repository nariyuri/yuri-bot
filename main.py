# -*- coding:utf-8 -*- 
import os
import requests
import re
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from urllib import parse
from zeep import Client
import json

class get_InspectionInfo:
    def __init__(self):
        wsdl = 'http://api.maplestory.nexon.com/soap/maplestory.asmx?wsdl'
        client = Client(wsdl=wsdl)
        soapDate = client.service.GetInspectionInfo()['_value_1']['_value_1'][0]['InspectionInfo']
        self.startDateTime = soapDate['startDateTime']
        self.endDateTime = soapDate['endDateTime']
        self.strObstacleContents = soapDate['strObstacleContents']

InspectionInfo = get_InspectionInfo()



print(InspectionInfo.endDateTime)