# -*- coding:utf-8 -*- 
import importBasedPackage

class EfficiencyCalc:
    def __init__(self):
        None
    def AtkBoss(self):
        self.atkboss = self.AtkBossCalc()
    
    class AtkBossCalc:
        def AtkBoss(_atk: list, _boss: list, _def: list):
            """
            * >brief: 방무 300% 기준
                      데미지 계산식에서 방무 보뎀 공퍼 제외 모든항목 고려 X 
                      두 Test Case에 대한 비교를 위한 근사치
            * >param: _atk: 총공퍼 <list>, _boss: 보공 <list>, _def: 방무 <list>
            * >return: 데미지 추정치 <list>
            """
            return(list(map(lambda x, y, z: 100*(((100+x)/100)*\
            ((100+y)/100))*\
            (z/100*300-300+100),\
             _atk, _boss, _def)))
            """
            * 계산식 {(100+공퍼)/100}*{(100+보뎀)/100}*방무
            * 방무: (방무/100*보스방어력-보스방어력+100)
            """
class Test:
    @classmethod
    def TestAll(cls):
        cls.TestEfficiencyCalc()
    @classmethod
    def TestEfficiencyCalc(cls):
        print(EfficiencyCalc.AtkBossCalc.AtkBoss([10,10],[100,100],[90,93]))
if __name__=="__main__":
    Test.TestAll()
