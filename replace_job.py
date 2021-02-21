#/usr/bin/python3
# _*_ coding=utf-8 _*_


import sys
import os
import re
import errno
import pathlib
import fileinput

print ("İşlemci iş parçacığı sayısını ayarlamak için lütfen pisi.conf dosyasını yolunu yazın...")
pconf = input()

with open(pconf) as f:
  for line in f.readlines():
     j=re.match("jobs = -j.",line)
     if j:
       print(j.group())
print ("Değiştirmek istediğiniz değeri giriniz.Örnek '5'.")
oldJ = input(int())

print ("Yeni değeri giriniz. Örnek '8'.")
newJ = input(int())


try:
  for line in fileinput.input(pconf, inplace=True):
    line = line.replace("-j"+oldJ, "-j"+newJ)
    print (line, end='')
  print ("İsteğiniz üserine " + oldJ + " olan iş parçacık sayısı " + newJ + " olarak değiştirilmiştir.")
except IOError as e:
  print (pconf + " dosyası belirttiğiz dizinde yok")
