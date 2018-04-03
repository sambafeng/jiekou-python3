from suds.client import Client
from suds.xsd.doctor import ImportDoctor,Import
# page='http://ws.webxml.com.cn/WebServices/TrainTimeWebService.asmx?wsdl'
# imp= Import('http://www.w3.org/2001/XMLSchema',
#  location='http://www.w3.org/2001/XMLSchema.xsd')
# imp.filter.add("http://WebXml.com.cn/")
# d= ImportDoctor(imp)
# client=Client(page,autoblend = True,doctor=d)
# result=client.service.getStationAndTimeByStationName(StartStation='北京',ArriveStation='上海',UserID='')
# print((result['diffgram']['getStationAndTime']['TimeTable']))
def web_interfa(url,interface):
    imp= Import('http://www.w3.org/2001/XMLSchema',
     location='http://www.w3.org/2001/XMLSchema.xsd')
    imp.filter.add("http://WebXml.com.cn/")
    d= ImportDoctor(imp)
    page1 = Client("%s?wsdl"%url,autoblend = True,doctor=d)
    resul=page1.service.getAreaDataSet()
    return resul