import re,urllib
import urllib.request
f=open("phone.txt","w")
u=urllib.request.urlopen("http://www.okcaller.com/74177012")
t=u.read()
for a in t:
     b=re.findall("[7][0-9]{9}",str(t))
     for number in b:
          f.write(number+"\n")
f.close()
