#coding:UTF-8

a = (2,5,8)  #タプル


print len(a) #3
print a * 3  # (2, 5, 8, 2, 5, 8, 2, 5, 8)

# a[2] = 10  # ng

#タプル　リストの変換

b =  list(a)
print b
b[2] = 100
print b
