import requests
import smtplib
from bs4 import BeautifulSoup
user={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
url="https://www.amazon.in/Redmi-Y3-Display-Storage-4000mAH/dp/B07QS42NKG/ref=sr_1_1_sspa?pf_rd_p=3008cff4-fd19-408e-876d-86411b2832ca&pf_rd_r=4DAQPF8P8ERT5Y043S5F&qid=1569996691&refinements=p_36%3A-1500000%2Cp_85%3A10440599031&rnid=1389432031&rps=1&s=electronics&smid=A23AODI1X2CEAE&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExSEMxWlhaMklVN1FXJmVuY3J5cHRlZElkPUEwMjI1NDIxM0FaUjFKRDhMT0ZWNiZlbmNyeXB0ZWRBZElkPUEwMjY1Mzg4MzRJMEtESUNBTFdJRSZ3aWRnZXROYW1lPXNwX2F0Zl9icm93c2UmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"
page=requests.get(url,headers=user)
soup=BeautifulSoup(page.content,'html.parser')
#print(soup.prettify())
search=soup.find(id="productTitle")
name=search.getText().strip()

price=soup.find(class_="a-color-price")
price1=price.getText()
price2=price1.split(",")
p3=''.join(price2)
s=p3[9:13]
print(s)
email=input("enter your email from where you want to send the email")
password=input("enter the password")
def send_mail():
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email,password)
    subject="price fell down"
    body="check the amazon url:"+url
    message="subject:"+subject+"\n\n"+body
    server.sendmail(email,"500063329@stu.upes.ac.in",message)
    print("email has been sent")
if int(s)>=1599:
    send_mail()

