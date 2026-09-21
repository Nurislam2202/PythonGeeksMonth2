# Декораторы, множественное наследование, ветки в гите
# Инкапсуляция

class ABC:
    def __init__(self, a, b, c):
        self.a = a  # public
        self._b = b  # protected
        self.__c = c  # private

    def isB(self, a):
        self._setB(a)
        self._getB()

    def _getB(self):
        print(self._b)

    def _setB(self, b):
        self._b = b

    def __str__(self):
        return self.__c


a = ABC("a", "_b", "__c")
a.isB("великий")
# a._b = "newB"
# print(a._b)
#
# a.setB("новый атрибут")
# print(a.getB())
#
# print(dir(a))
# a.__c = "ложный си"
# a._ABC__c = "настоящий си"
# print(a.__c)
# print(a)
