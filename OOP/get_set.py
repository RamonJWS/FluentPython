"""
__setitem__ can be used to allow the user to set instance attributes with the following notation:
object['item'] = 'apple', this will change the self.item = 'apple'
__getitem__ allows for instance attributes to be accessed with the same notation:
object['somelist'][2:4] -> [2,3]
"""

class Person:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_hist = []

    def __setitem__(self, idx, value):
        self.__dict__[idx] = value
        if idx == 'balance':
            if self.transaction_hist:
                trans_diff = self.balance - self.transaction_hist[-1]
            else:
                trans_diff = self.balance
            self.transaction_hist.append(trans_diff)

    def __getitem__(self, item):
        return self.__dict__[item]


a = Person('ray', 100)
print(a.__dict__)

# set items
a['name'] = 'amy'
a['balance'] = 200
a['balance'] = 300
print(a.__dict__)
a['balance'] = -50
print(a.__dict__)


# get items
print(a['balance'])
print(a['transaction_hist'][1:3])

"""
output:
{'name': 'ray', 'balance': 100, 'transaction_hist': []}
{'name': 'amy', 'balance': 300, 'transaction_hist': [200, 100]}
{'name': 'amy', 'balance': -50, 'transaction_hist': [200, 100, -150]}
-50
[100, -150]
"""
