# -*- coding: utf-8 -*-
"""백준 2292

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yBmThSijUWamLvw629xq7X2sn0_1rktb
"""

#2292

#n=1이면 room=0
#n=2~7이면 room=1
#n=8~13이면 room=2
#n=14~19이면 room=3


n=int(input())      #방의 숫자
room=0     #최소 방 개수
honey=1     #시작 꿀 숫자
d=6

while n>honey:
    room+=1
    honey+=d
    d+=6
    

print(room+1)