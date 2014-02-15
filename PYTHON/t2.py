#!/usr/bin/python
# coding: UTF-8
 
import datetime # datetimeモジュールのインポート
import locale   # import文はどこに書いてもOK(可読性などの為、慣例でコードの始めの方)
 
 
d = datetime.datetime.today()
 
print 'd == %s : %s\n' % (d, type(d)) # Microsecond(10^-6sec)まで取得
 
print '%s年%s月%s日\n' % (d.year, d.month, d.day)
 
print '%s時%s分%s.%s秒\n' % (d.hour, d.minute, d.second, d.microsecond)
 
# strftime()メソッドで日付時刻の書式を指定して出力
print d.strftime("%Y-%m-%d %H:%M:%S"), '\n'
 
