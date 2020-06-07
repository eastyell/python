import requests, json

weatherUrl = "http://wthrcdn.etouch.cn/WeatherApi?city="        #返回xml数据
weatherUrl = "http://wthrcdn.etouch.cn/weather_mini?city="      #返回json数据

cityName = input("请输入你要查询的城市：")

weatherResp = requests.get(weatherUrl + cityName)
print(weatherResp)
d = weatherResp.json()
print(d)
if(d['status'] >= 1000):
    print("城市：", d["data"]["city"])
    print("时间：", d["data"]["forecast"][0]["date"])
    print("温度：", d["data"]["forecast"][0]["high"], d["data"]["forecast"][0]["low"])
    print("天气：", d["data"]["forecast"][0]["type"])
    print("风向：", d["data"]["forecast"][0]["fengxiang"])
    print("风力：", d["data"]["forecast"][0]["fengli"])
    print("感冒指数：", d["data"]["ganmao"])
  
