class IterateNumber:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
       if self.num <= 10:
           value = self.num
           self.num+=1
           return value
       else:
           raise StopIteration

a=IterateNumber()

for i in a:
    print(i)










# from email.policy import default
# num=[]
# for t in range(1,6):
#     # print(t, end=' ')
#     num.append(t)
#
# print(num)
#
# it=iter(num)
#
# print(next(it))
#
# print(it.__next__())
# #
# # for i in it:
# #     print(i)
#
