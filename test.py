#!/usr/bin/env python3
#ls  l s  l s  l s  l s  l s  l s  l o g o u t root@u3:/usr/local/webssh# 
with  open("new",'r') as f:
    msg = f.read()
f = open('aa','a+')
s=''
for i in msg:
    i = i.replace('\n',' ')
    s+=i
s_list=s.split('  ')
print(s_list)
for  str in s_list:
    str=str.replace(' ','')
    str=str+'\n'
    f.write(str)
f.close() 
