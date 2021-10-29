# -*- coding:utf-8 -*- 

class EfficiencyCalc:
    def __init__(self, _atc, _def, _boss):
        list(map(lambda x, y, z: 100*(((100+x)/100)*((100+y)/100))*(z/100*300-300+100), _atc, _def, _boss))
    