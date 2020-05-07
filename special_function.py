'''
All the classes by default inherit - Object class

And object class has special methods inside it

__methodname__ ----> methodname(object) ---->  object.__methodname__

__init__   special/magic/dunder functions

'''
def appendInFile(filename,line):
    file_1 = open(filename, 'a')
    file_1.write(line)
    file_1.close()


class Account:
    def __init__(self,name,amount):
        self.name = name
        self.amount = amount
        self.__transactions = []

    def __str__(self):
        return "Account holder name is {0}. {0} has {1} in his account \n".format(self.name,self.amount)

    def __repr__(self):
        return "{}({!r},{!r})".format(self.__class__.__name__,self.name,self.amount)

    def __len__(self):
        print("The no of transaction for ",self.__repr__()," :")
        return len(self.__transactions)

    # def __iter__(self):
    #     return iter(self.__transactions)
    #
    # def __next__(self):
    #     return self.__iter__()

    def __add__(self, other):
        return self.name +" and " + other.name + " has joint amount " +str(self.amount+other.amount)

    def doTransaction(self,amt):
        self.__transactions.append(amt)

    def transactionHistory(self):
        for i in self.__transactions:
            yield i




acc_1 = Account("Suman",4000)
acc_2 = Account("Raman",50000)


#appendInFile("log.txt",str(acc_1))
#appendInFile("log.txt",str(acc_2))

print(str(acc_1))
print(repr(acc_1))


acc_1.doTransaction(4000)
acc_1.doTransaction(6000)
acc_1.doTransaction(-3000)
acc_1.doTransaction(-2000)
acc_1.doTransaction(-2000)
print(len(acc_1))
print(len(acc_2))

# for trans in acc_1:
#     print(trans)
#
# print("---------------------")

# iterated = iter(acc_1)  #iterator - iterable object
#
# while True:
#     try:
#         print(next(iterated))
#     except StopIteration:
#         break;
# print("---------------------")

a = acc_1.transactionHistory()

print(next(a))

print(acc_1+acc_2)
print("---------------------")
for i in acc_1.transactionHistory():
    print(i)

print("---------------------")


while True:
    try:
        print(next(a))
    except StopIteration:
        break;
print("---------------------")

for i in range(10):
    print(i)

print(i)







