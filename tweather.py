from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
from tkinter import Tk,Button,Text,END

class Weather(object):
    def __init__(self):
        pass
    def crawl(word,self):
        resp = urlopen('http://www.weather.com.cn/weather/101270116.shtml') #标签国内有效
        #http://www.weather.com.cn/weather/101270102.shtml（龙泉驿）
        soup = BeautifulSoup(resp, 'html.parser')
        tagALL = soup.find('ul', class_="t clearfix")  # 天气标签的所有信息

        AtagALL = tagALL.find_all('p', class_="tem")  # 总的温度
        HtagALL = AtagALL[1].span.string  # 第二天的高温
        LtagALL = AtagALL[1].i.string  # 第二天的低温
        now_temperatureHigh = HtagALL.strip('℃')
        now_temperatureLow = LtagALL.strip('℃')

        weather = tagALL.find_all('p', class_="wea")  # 总的天气
        Aweather = weather[1].string  # 第二天天气

        if float(now_temperatureLow) < 10 and  float(now_temperatureHigh) < 15 :
            result = ("明天成都市锦江区最低温度:" + now_temperatureLow + "℃。",   "最高温度:"+ now_temperatureHigh + "℃。",  "天气:"+ Aweather + "。",  "明天简直是天寒地冻啊，李老师提醒你：衣服要加够哦！" + '  ' + time.strftime("%Y/%m/%d %H:%M"))
        elif float(now_temperatureLow) < 10 :
            result = ("明天成都市锦江区最低温度:" + now_temperatureLow + "℃。",   "最高温度:"+ now_temperatureHigh + "℃。",  "天气:"+ Aweather + "。",  "明天有点冷，但是中午温度还会回升，不过还是不能减少衣服哦！" + '  ' + time.strftime("%Y/%m/%d %H:%M")  )
        elif 10 <= float(now_temperatureLow) < 18:
            result = ("明天成都市锦江区最低温度:" + now_temperatureLow + "℃。",   "最高温度:"+ now_temperatureHigh + "℃。",  "天气:"+ Aweather + "。",  "明天天气有点凉，要记得加衣服哦！" + '  ' + time.strftime("%Y/%m/%d %H:%M")  )
        elif 25 > float(now_temperatureLow) >= 18 and float(now_temperatureHigh) <= 28:
            result = ("明天成都市锦江区最低温度:" + now_temperatureLow + "℃。", "最高温度:" + now_temperatureHigh + "℃。", "天气:" + Aweather + "。", "明天我与风为伴，给你带来很温和的一天！" + '  ' + time.strftime("%Y/%m/%d %H:%M")  )
        elif 25 >= float(now_temperatureLow) >= 18 and float(now_temperatureHigh) > 28:
            result = ("明天成都市锦江区最低温度:" + now_temperatureLow + "℃。", "最高温度:" + now_temperatureHigh + "℃。", "天气:" + Aweather + "。", "明天气温差度大，穿衣要适量，别弄感冒了哦！"+ '  ' + time.strftime("%Y/%m/%d %H:%M") )
        else:
            result = ("明天成都市锦江区最低温度:" + now_temperatureLow + "℃。", "最高温度:" + now_temperatureHigh + "℃。", "天气:" + Aweather + "。", "明天有点热哦，不要穿太多啦！" + '  ' + time.strftime("%Y/%m/%d %H:%M") )
        return result

class Application(object):
    def __init__(self):
        self.window = Tk()
        self.weather = Weather()
        self.window.title(u'李老师气象台')
        #设置窗口大小和位置
        self.window.geometry('310x190+500+300')
        self.window.minsize(310,190)
        self.window.maxsize(310,190)
        self.window["bg"] = "SkyBlue"
        self.window.attributes("-alpha", 0.9)
        #创建一个文本框
        self.result_text1 = Text(self.window,background = '#87CEEB')
        self.result_text1.place(x = 10,y = 5,width = 285,height = 155)
        self.result_text1.bind("<Key-Return>",self.submit)
        #创建一个按钮
        #为按钮添加事件
        self.submit_btn = Button(self.window,text=u'查询一下',command=self.submit,background = '#ADD8E6')
        self.submit_btn.place(x=170,y=162,width=55,height=25)
        self.submit_btn2 = Button(self.window,text=u'知道啦',command = self.clean,background = '#ADD8E6')
        self.submit_btn2.place(x=240,y=162,width=55,height=25)

    def submit(self):
        result = self.weather.crawl(None)
        # #将结果显示在窗口中的文本框中
        self.result_text1.insert(END,result)
        print(result)
    #清空文本域中的内容
    def clean(self):
        self.result_text1.delete(0.0,END)
    def run(self):
        self.window.mainloop()

if __name__=="__main__":
    app = Application()
    app.run()