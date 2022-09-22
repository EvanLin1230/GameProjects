from dataclasses import asdict


class TestPrivateMethod:
    def _PublicMethod(self):
        print("Outside can call this method")
    def __PrivateMethod(self):
        print("Outside can't call this method")

class TestCallMethod(TestPrivateMethod):
    def __init__(self) -> None:
        pass
    def Call_Private(self):
        self.__PrivateMethod()
    def Call_(self):
        self._PublicMethod()

# 以下為 private method 的測試
TCM = TestCallMethod()
TCM.Call_()

for i in range(0,4):
    print(i+1)