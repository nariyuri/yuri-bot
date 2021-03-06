# -*- coding:utf-8 -*- 
import importBasedPackage

class EfficiencyCalc:
    def __init__(self):
        None
    def AtkBoss(self):
        self.atkBoss = self.AtkBossCalc()
    def Meso(self):
        #다 갈아엎어
    
    class AtkBossCalc:
        def __init__(self, atk_: list, boss_: list, def_: list):
            self.atk_, self.boss_, self.def_ = atk_, boss_, def_
            self.AtkBoss()
        def AtkBoss(self):
            """
            * >brief: 방무 300% 기준
                      데미지 계산식에서 방무 보뎀 공퍼 제외 모든항목 고려 X 
                      두 Test Case에 대한 비교를 위한 근사치
            * >param: _atk: 총공퍼 <list>, _boss: 보공 <list>, _def: 방무 <list>
            * >return: 데미지 추정치 <list>
            """
            self.damage = (list(map(lambda x, y, z: 100*(((100+x)/100)*\
            ((100+y)/100))*\
            (z/100*300-300+100),\
             self.atk_, self.boss_, self.def_)))
            """
            * 계산식 {(100+공퍼)/100}*{(100+보뎀)/100}*방무
            * 방무: (방무/100*보스방어력-보스방어력+100)
            """
        def CompareAtkBoss(self):
            self.compare = round(self.damage[1]/self.damage[0], 2)
    
    class MesoCalc:
        @staticmethod
        def Meso(_level:int, _per:int, _countMonster:int, _potion:int=1.2):
            return _level*7.5*(100+_per)*_potion*_countMonster

class Test:
    @classmethod
    def TestAll(cls):
        cls.TestEfficiencyCalc()
    @classmethod
    @importBasedPackage.decorators.TryFuncTest
    def TestEfficiencyCalc(cls):
        testatkBossCalc = EfficiencyCalc.AtkBossCalc([10,10],[100,100],[90,93])
        testatkBossCalc.CompareAtkBoss()
        print(testatkBossCalc.compare)
        testMesoCalc = 
        
if __name__=="__main__":
    Test.TestAll()
