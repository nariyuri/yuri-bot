"""
* ConvertWorld: 입력된 월드를 멮지지 주소에 맞게 변환
"""

def ConvertWorld(world) :
        worldName = None
        if world == "루나" :
            return("luna")
        elif world == "스카니아" :
            return("scania")
        elif world == "엘리시움" :
            return("elysium")
        elif world == "리부트" :
            return("reboot")
        elif world == "크로아" :
            return("croa")
        elif world == "오로라" :
            return("aurora")
        elif world == "베라" :
            return("bera")
        elif world == "레드" :
            return("red")
        elif world == "유니온" :
            return("union")
        elif world == "제니스" :
            return("zenith")
        elif world == "이노시스" :
            return("enosis")
        elif world == "리부트2" :
            return("reboot2")
        elif world == "아케인" :
            return("arcane")
        elif world == "노바" :
            return("nova")
        else :
            return("None")