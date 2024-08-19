from bs4 import BeautifulSoup
import requests
import schedule
import time

link = "https://data.bmkg.go.id/gempaterkini.xml"
i=0

def getInfo(link):
    global i
    i+=1
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "html.parser")
    if page.status_code == 200:
        infogempa = soup.find_all("gempa")
        for a in infogempa:
            print("""
            Tanggal     : {tanggal},
            Jam         : {jam},  
            Koordinat   : {koordinat},
            Lintang     : {lintang}, 
            Bujur       : {bujur},
            Magnitude   : {magnitude}, 
            Kedalaman   : {kedalaman},
            Wilayah     : {wilayah}

            Waiting{num}


            """.format(
                tanggal=a.find("tanggal").text,
                jam=a.find("jam").text,
                koordinat=a.find("coordinates").text,
                lintang=a.find("lintang").text, 
                bujur=a.find("bujur").text,
                magnitude=a.find("magnitude").text,
                kedalaman=a.find("kedalaman").text,
                wilayah=a.find("wilayah").text,
                num=i)
                        )
            
def job():
    getInfo(link)
schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)