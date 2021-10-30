"""
* 테스트용 데코레이터 만들어두기
*
* @CallFuncTest
* @Wraps
"""
class TestDecorator:
    def __init__(self):
        exit()

class CallFuncTest:   
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('{} 함수가 호출되기전 입니다.'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

class TryFuncTest:   
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            return self.func(*args, **kwargs)
        except:
            print("error on")
