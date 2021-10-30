"""
* 테스트용 데코레이터 만들어두기
* 멮지지 갱신필요 추가 필요
* @CallFuncTest
* @TryFuncTest : 실행 후 에러 발생시 에러 메시지 출력
"""
import sys, traceback


"""
class CallFuncTest:   
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('{} 함수가 호출되기전 입니다.'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)
"""

"""
* @TryFuncTest
* 
"""
class TryFuncTest:   
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        try:
            return self.func(*args, **kwargs)
        except Exception:
            traceback.print_exc()
