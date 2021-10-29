"""
* 데이터 가져오는거 : get
* 클래스/함수 내부적 사용 : _
* 
"""def GetEvent() :
    eventData = []
    eventDate = []
    eventUrl = []
    _bs = BeautifulSoup(requests.get("https://maplestory.nexon.com/News/Event").text, 'html.parser')
    _tags = _bs.find_all('div',{'class':'event_list_wrap'})
    for _tag in _tags :
        _dds = _tag.find_all('dd')
        for _dd in _dds:
            if _dd.find('a'):
                eventData.append(_dd.text.strip('\n'))
                eventUrl.append("https://maplestory.nexon.com/"+_dd.find('a')["href"])
            if _dd.find('dd', {'class':'date'}):    
                eventDate.append(_dd.text.strip('\n'))
    return eventData, eventDate, eventUrl