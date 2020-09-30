import requests
import io
from bs4 import BeautifulSoup

url="https://economictimes.indiatimes.com/archivelist/year-2015,month-"
mnth=1
day=42005
var1=",starttime-"
var2=".cms"
cnt=1
final=[]
for i in range(1,366):
    turl=url+str(mnth)+var1+str(day)+var2
    r1=requests.get(turl)
    coverpage=r1.content
    #mnth+=1
    print(mnth,cnt)
    if(mnth==2):
        if(cnt==28):
            mnth+=1
            cnt=0
    elif(mnth<8):
        if(mnth%2==0 and cnt==30):
            mnth+=1
            cnt=0
        elif(mnth%2==1 and cnt==31):
            mnth+=1
            cnt=0
    else:
        if(mnth%2==0 and cnt==31):
            mnth+=1
            cnt=0
        elif(mnth%2==1 and cnt==30):
            mnth+=1
            cnt=0
    day+=1
    cnt+=1

    soup1=BeautifulSoup(coverpage,"html5lib")
    year_news=soup1.find_all("ul",class_="content")

    st=year_news[0].get_text("\n")
    st2=year_news[1].get_text("\n")
    fst=st+"\n"+st2


    with io.open("mk2.txt", "a", encoding="utf-8") as f:
        f.write(fst)


#print(final)
#year_news=soup1.find_all("h2",class_="newstit")

#print(year_news[0].get_text())
