import requests
from bs4 import BeautifulSoup
import csv

def ExtractData(url):
    response = requests.get(url=url).content
    soup = BeautifulSoup(response, 'lxml')

    newsbody = soup.find("div",{"class":"QG_2t"})

    newsdata = newsbody.find("div",{"class":"undefined"}).find("div",{"class":"_3sL7K undefined"})

    newsurl = newsdata.find("a",{"class":"_3HExI"})

    newsposted = newsdata.find("span",{"class":"_3brJw"})



    print(newsurl)

    print(newsposted)

    

    with open("report.csv","w",newline="") as csv_file:
        csv_write = csv.writer(csv_file)
        csv_write.writerow(newsurl)
        csv_write.writerow(newsposted)


ExtractData(url="https://timesofindia.indiatimes.com/videos?from=mdr#_ga=2.135146417.1486211953.1616041818-amp-nGGGc9pnM-cmw7Tkv3GejPTeBzV0DH7wluFUS3V4fKzxYIGy1VBx8dWDTT403H36")