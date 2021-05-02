A=int(input("请选择纪年方式:"))
if (A==1):
  a=int(input("请输入西元年份:"))
  b=2019
  c=1989
  d=1926
  e=1912
  f=1868
  if a > b:
   print(('令和'),(a-b+1))
  if(a==2019):
   print('令和元年 平成31年')
  if c < a < b:
   print(('平成'),(a-c+1))  
  if(a==1989):
   print('平成元年 昭和64年')
  if d < a < c:
   print(('昭和'),(a-d+1))
  if(a==1926):
   print('昭和元年 大正15年') 
  if e < a < d:
   print(('大正'),(a-e+1))
  if(a==1912):
   print('大正元年 明治45年')  
  if f < a < e:
   print(('明治'),(a-f+1))
  if(a==1868):
   print('明治元年')
if (A==2):
  h=int(input("请输入皇纪年份:"))
  g=660
  print(h-g)   




  
  
     
