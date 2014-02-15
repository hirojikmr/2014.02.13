#!/usr/bin/python
# coding: UTF-8
 
str = """It is meaningless only to think my long further aims idly.
It is important to set my aims but at the same time I should confirm my present condition.
Unless I set the standard where I am in any level, I'll be puzzled about what I should do from now on."""
strs = str.split('n') # 一行が一要素(文字列)のリスト
 
#f.writelines(strs) # シーケンスが引数。
#f.close()

f = open('text.txt', 'w') # 書き込みモードで開く

for i in range(10):
	f.write("he%d\n" % i)

f.close()
