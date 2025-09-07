
# # print(f.read())
# print(f.readline(), end='')
# print(f.readline(),end='')
# print(f.readline())


# f1=open('abc','w')
# f1.write('')
f=open('myData','r')
f1=open('abc','a')
# f1.write('this is append')

# for data in f:
#     f1.write(data)

f2=open('abc','r')

for data1 in f2:
    print(data1)


f_image=open('test.jpg','rb')
f_new=open('copy_test.jpg','wb')

for i in f_image:
    f_new.write(i)