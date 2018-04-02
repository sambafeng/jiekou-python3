import urllib.request
import xmltodict,json
from urllib.parse import urlencode
from urllib import request,parse
# page = urllib.request.urlopen("http://ws.webxml.com.cn/webservices/ChinaTVprogramWebService.asmx/getAreaDataSet")
# lines = page.readlines()
# page.close()
# document = ""
# for line in lines :
#     document = document + line.decode('utf-8')
# hmo=xmltodict.parse(document)
# h=hmo['DataSet']['diffgr:diffgram']['Area']['AreaList']
# m=0
# for m in range(len(h)):
#     print(h[m]['Zone'])
#     m+=1
from suds.client import Client
page='http://ws.webxml.com.cn/webservices/DomesticAirline.asmx?op=getDomesticAirlinesTime'
headers={
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
data1={'startCity':'北京','lastCity':'上海','theDate':'','userID':''}

encode_arg = urllib.parse.urlencode(data1)

req = request.Request(url=page,data=encode_arg)
print(req)
reponse=urllib.request.urlopen(req)
m=reponse.readlines()
print(m)
