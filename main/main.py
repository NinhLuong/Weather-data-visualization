import sys
import requests
import os
from subprocess import call
import playsound
import speech_recognition as sr
import time
import datetime as DateTime
import requests
from gtts import gTTS
import unidecode
import numpy as np
import pandas as pd
from ui_main import*
import seaborn as sns
import matplotlib.pyplot as plt
from PySide2 import QtGui
from PySide2.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtGui import ( QColor, QIcon)
from PySide2.QtCore import (QCoreApplication, QSize)
from splash_screen import *
from threading import *

language = 'vi'
counter = 0
jumper =0
datetime = []
temp = []
humidity = []
windspeed = []
uvindex = []
cloudcover=[]
solarenergy = []
feelslike = []
link = ""   
mode = 0
location = ''
response={}
time_to_get = 8    #Sô kết quả lấy dữ liệu api (3 tiếng cho 1 kết quả)
_translate = QtCore.QCoreApplication.translate
call_url = 'https://api.openweathermap.org/data/2.5/weather?lat=10.850145464871641&lon=106.7716601973813&appid=d80948795e2ec6257f1f62303cf81808&lang=vi'
response = requests.get(call_url)
data = response.json()

class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setWindowTitle("Help")
        self.setMinimumSize(QSize(778, 634))
        self.setMaximumSize(QSize(778, 634))
        self.label = QLabel("")
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.label.setText(QCoreApplication.translate("HelpWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff; background-color:transparent;\">USAGE</span></p><p><span style=\" color:#ffffff; background-color:transparent;\">Mode 0: Input a city name (English) -&gt; Click </span><span style=\" font-weight:600; font-style:italic; color:#ffffff; background-color:transparent;\">Start</span><span style=\" color:#ffffff; background-color:transparent;\"> to run</span></p><p><span style=\" color:#ffffff; background-color:transparent;\">Mode 1: Click </span><span style=\" font-weight:600; font-style:italic; color:#ffffff; background-color:transparent;\">Open file</span><span style=\" color:#ffffff; background-color:transparent;\"> -&gt; Choose csv file download from </span><span style=\" font-style:italic; color:#ffffff; background-color:transparent;\">https://www.visualcrossing.com</span><span style=\" color:#ffffff; background-color:transparent;\"> -&gt; Click </span><span style=\" font-weight:600; font-style:italic; color:#f"
                        "fffff; background-color:transparent;\">Start</span><span style=\" color:#ffffff; background-color:transparent;\"> to run</span></p><p><span style=\" color:#ffffff; background-color:transparent;\">(Mode 1 is always preferred)</span></p><p><span style=\" color:#ffffff; background-color:transparent;\">Click </span><span style=\" font-weight:600; font-style:italic; color:#ffffff; background-color:transparent;\">Exit</span><span style=\" color:#ffffff; background-color:transparent;\"> to close</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff; background-color:transparent;\">REQUERIMENTS</span></p><p><span style=\" color:#ffffff; background-color:transparent;\">*You have to install pip if you use Linux or a similar one to run this project</span></p><p><span style=\" color:#ffffff; background-color:transparent;\">Dowload new version Python -&gt; https://www.python.org</span></p><p><span style=\" color:#ffffff; background-color:transparent;\">pip install numpy</span></p><p><s"
                        "pan style=\" color:#ffffff; background-color:transparent;\">pip install pandas</span></p><p><span style=\" color:#ffffff; background-color:transparent;\">pip install seaborn</span></p><p><span style=\" color:#ffffff; background-color:transparent;\">pip install PySide2</span></p><p><span style=\" color:#ffffff; background-color:transparent;\">pip install requests</span></p><p><span style=\" color:#ffffff; background-color:transparent;\">pip install matplotlib</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff; background-color:transparent;\">ERROR CODE:</span></p><p><span style=\" color:#ffffff;\">Error code 1: Data is not correct</span></p><p><span style=\" color:#ffffff;\">Error code 2: File format must be a csv file</span></p><p><span style=\" color:#ffffff;\">Error code 3: File format or data is not correct</span></p><p><span style=\" color:#ffffff;\">Error code 4: City name is not correct</span></p></body></html>", None))
        self.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255));\n"
"")

class MiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        self.w = None
        self.setWindowTitle("Weather Data Visualization")
        self.setWindowIcon(QtGui.QIcon(":/images/main_icon.png"))
        self.ui.notice_label.setStyleSheet(u"background-color: none;\n""color : red")
        self.ui.notice_label.setText("")
        #Kích thước nút mặc định
        #self.ui.logo_img.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ui.load_button.setFixedWidth(81)
        self.ui.load_button.setFixedHeight(31)
        self.ui.start_button.setFixedWidth(81)
        self.ui.start_button.setFixedHeight(31)
        self.ui.help_button.setFixedWidth(81)
        self.ui.help_button.setFixedHeight(31)
        self.ui.exit_button.setFixedWidth(81)
        self.ui.exit_button.setFixedHeight(31)  
        self.ui.voice.setFixedWidth(30)
        self.ui.voice.setFixedHeight(30)
        self.ui.lineEdit.setFixedHeight(31) 
        
        #Nhận biết kích hoạt button
        self.ui.help_button.clicked.connect(self.show_new_window)
        self.ui.load_button.clicked.connect(self.bt_load)
        self.ui.start_button.clicked.connect(self.bt_start)
        self.ui.exit_button.clicked.connect(QApplication.instance().quit)
        self.ui.voice.clicked.connect(self.bt_voice)
        self.show() 
        self.Timer_Start()

        # cập nhật ngày tháng năm
        self.ui.day.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#000000;\">21/08/2002</span></p></body></html>"))
        tem2="<html><head/><body><p><span style=\" font-size:14pt; color:#000000;\">{VALUE}</span></p></body></html>"
        Date= QtCore.QDate.currentDate()
        text0= Date.toString("dd/MM/yyyy")
        new_date= tem2.replace("{VALUE}",text0)
        self.ui.day.setText(new_date)

        # cập nhật thứ trong tuần 
        self.ui.thu.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Tuesday</span></p></body></html>"))
        tem3= "<html><head/><body><p><span style=\" font-size:12pt; color:##000000;\">{VALUE}</span></p></body></html>"
        Date= QtCore.QDate.currentDate()
        text1=Date.toString("dddd")
        new_day= tem3.replace("{VALUE}",text1)
        self.ui.thu.setText(new_day)

        # cập nhật icon thời tiết
        global data
        if data['weather'][0]['main'] =='Clear':
                self.ui.picture.setStyleSheet("border: none;\n"
                "background: none;\n"
                "image: url(:/img/sum.png);")
        elif data['weather'][0]['main'] =='Rain':
                self.ui.picture.setStyleSheet("border: none;\n"
                "background: none;\n"
                "image: url(:/img/rain.png);")

        elif data['weather'][0]['icon'] =='03n':
                self.ui.picture.setStyleSheet("border: none;\n"
                "background: none;\n"
                "image: url(:/img/night.png);")
        elif data['weather'][0]['main'] =='Clouds':
                self.ui.picture.setStyleSheet("border: none;\n"
                "background: none;\n"
                "image: url(:/img/cloud.png);")    

    def Timer_Start(self):
        self.timer_date = QtCore.QTimer()
        self.timer_date.start(1000)
        self.timer_date.timeout.connect(self.update_date)

        self.timer_tem = QtCore.QTimer()
        self.timer_tem.start(1000)
        self.timer_tem.timeout.connect(self.update_temperature)

        self.timer_tem = QtCore.QTimer()
        self.timer_tem.start(1000)
        self.timer_tem.timeout.connect(self.KK_Gauge_Temp_CallBack(self.update_temperature()))
    
        self.timer_tem = QtCore.QTimer()
        self.timer_tem.start(1000)
        self.timer_tem.timeout.connect(self.update_humi)

        self.timer_humi = QtCore.QTimer()
        self.timer_humi.start(1000)
        self.timer_humi.timeout.connect(self.KK_Gauge_Humi_CallBack(self.update_humi()))

    def update_date(self):
        # câp nhật thời gian
        self.ui.Time.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=40pt\" color:#000000;\">7:10</span></p></body></html>"))
        timer= QtCore.QTime.currentTime()
        text_time= timer.toString("HH:mm")
        self.ui.Time.setText(text_time)

    def update_temperature(self):
        self.current_temperature = int(data["main"]["temp"]-273)
        return self.current_temperature

    def update_humi(self): 
        self.current_humidity = int(data["main"]["humidity"])
        return self.current_humidity
     
    def KK_Gauge_Temp(self, value):
        styleSheet = """border-radius: 75px;
		background-color: qconicalgradient(cx:0.5, cy:0.5, angle:224.5, stop:0 rgba(245, 245, 245, 255), stop:{stop_val1} rgba(245, 245, 245, 255), stop:{stop_val2} rgba(0, 0, 0, 0));"""
        stop2 = str(value * -0.00749 + 1)
        stop1 = str(value * -0.00749 + 1 - 0.01)
        styleSheet = styleSheet.replace("{stop_val1}", stop1).replace("{stop_val2}", stop2)
        self.ui.frame_32.setStyleSheet(styleSheet)

    def KK_Gauge_Temp_CallBack(self, value):
        self.KK_Gauge_Temp(int(value))
        _translate = QtCore.QCoreApplication.translate
        self.ui.pushButton_20.setText(_translate("MainWindow", str(value) + "°C"))
    
    def KK_Gauge_Humi(self, value):
        styleSheet = """border-radius: 75px;
		background-color:qconicalgradient(cx:0.5, cy:0.5, angle:224.5, stop:0 rgba(245, 245, 245, 255), stop:{stop_val1} rgba(245, 245, 245, 255), stop:{stop_val2} rgba(0, 0, 0, 0));"""
        stop2 = str(value * -0.00749 + 1)
        stop1 = str(value * -0.00749 + 1 - 0.01)
        styleSheet = styleSheet.replace("{stop_val1}", stop1).replace("{stop_val2}", stop2)
        self.ui.frame_34.setStyleSheet(styleSheet)

    def KK_Gauge_Humi_CallBack(self, value):
        self.KK_Gauge_Humi(int(value))
        _translate = QtCore.QCoreApplication.translate
        self.ui.pushButton_22.setText(_translate("MainWindow", str(value) + "%"))

    def show_new_window(self, checked):
        if self.w is None:
            self.w = AnotherWindow()
        self.w.show()

    #Hàm vẽ biểu đồ lên màn hình   
    def draw(self):
        self.grafica = Canvas_grafica1()
        self.grafica1 = Canvas_grafica2()
        self.grafica2 = Canvas_grafica3()
        self.grafica3 = Canvas_grafica4()
        self.ui.line_chart.addWidget(self.grafica)
        self.ui.scatter_chart.addWidget(self.grafica1)
        self.ui.bar_chart.addWidget(self.grafica2)
        self.ui.histogram_chart.addWidget(self.grafica3)
        
    
    def remove(self):
        self.ui.line_chart.removeWidget(self.grafica)
        self.ui.scatter_chart.removeWidget(self.grafica1)
        self.ui.bar_chart.removeWidget(self.grafica2)
        self.ui.histogram_chart.removeWidget(self.grafica3)          

    #Thiết lập hoạt động cho load_button
    def bt_load(self):
        global link
        diachi = QFileDialog.getOpenFileNames()
        chuanhoa = str(diachi)[:-20]
        chuanhoa = chuanhoa[3:] 
        link = chuanhoa
        self.ui.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow",link, None))

    #Thiết lập hoạt động cho start_button
    def bt_start(self):
        global link
        global time_to_get
        global datetime
        global temp
        global humidity
        global windspeed
        global uvindex
        global mode
        global response
        #Xóa data cũ, đặt trong try sẽ trừ trường hợp lỗi
        try:
            self.remove()
        except:
           pass
        #Nếu nhấn start_button mà chưa nhập file mà tên thành phố thì sẽ ưu tiên nhập file
        if (link == "") and (self.ui.lineEdit.text() == ""):
            i = 0
            self.bt_load()
            #Đặt trong try để trừ trường hợp bị lỗi phần mềm do data không đúng khi load dữ liệu vẽ
            try:
                pd.read_csv(link)
                self.ui.notice_label.setText("")
                try:
                    self.draw()
                    link = ""
                    self.ui.notice_label.setText("")
                    self.ui.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please input city name", None))
                except:
                    link = ""
                    self.ui.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please input city name", None))
                    self.ui.notice_label.setText("Error code 1")
            except:
                link = ""
                self.ui.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please input city name", None))
                self.ui.notice_label.setText("Error code 2")
        #Nếu đã có link thì sẽ ưu tiên vẽ link
        elif link != "":
            try:
                self.draw()
                link = ""
                self.ui.notice_label.setText("")
                self.ui.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please input city name", None))
            except:
                link = ""
                self.ui.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please input city name", None))
                self.ui.notice_label.setText("Error code 3")
        #Trường hợp còn lại lấy dữ liệu API thời gian thực theo tên thành phố để vẽ
        else:
            api_key = 'TQ39TAZE5EZHHYRGNANAQ5JJB'
            city = self.ui.lineEdit.text()
            url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/' + city + '?key=' + api_key
            try:
                response = requests.get(url).json()
                mode = 1
                self.draw()
                mode = 0
                datetime = []
                temp= []
                humidity = []
                windspeed = []
                self.ui.notice_label.setText("")
                self.ui.lineEdit.clear()
                self.ui.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please input city name", None))
            #Vẽ không thành công sẽ thông báo data lỗi
            except:
                self.ui.lineEdit.clear()
                self.ui.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please input city name", None))
                self.ui.notice_label.setText("Error code 4")
#  hàm chuyển văn bản thành âm thanh
    def speak(self,text):
        print("Bot: {}".format(text))
        self.tts = gTTS(text=text, lang=language, slow=False)    
        self.tts.save("sound.mp3")
        playsound.playsound("sound.mp3", False)
        os.remove("sound.mp3")

        # hàm chuyển anh thanh thành văn bản 
    def get_audio(self):
        self.r = sr.Recognizer()
        with sr.Microphone() as source:
            self.audio = self.r.listen(source, phrase_time_limit=4)
            try:
                self.text = self.r.recognize_google(self.audio, language="vi-VN")
                print("Bot nhận được: ", self.text)
                return self.text
            except:
                print("Bot không nghe được")
                return 0
# hàm xử lý text
    def get_text(self):
        #while True:
        self.text = self.get_audio()
        if self.text:
            return self.text.lower()
        return 0
# hàm lấy thời gian và ngày để đọc
    def get_time(self,text):
        self.now = DateTime.datetime.now()
        if "giờ" in self.text:
            self.speak('Bây giờ là %d giờ %d phút' % (self.now.hour, self.now.minute))
        elif "ngày" in text:
            self.speak("Hôm nay là ngày %d tháng %d năm %d" %
                (self.now.day, self.now.month, self.now.year))
# hàm lấy dữ liệu thời tiết và đọc
    def current_weather(self):
        global data
        if data["cod"] != "404":
            self.city_res = data["main"]
            self.current_temperature = int(self.city_res["temp"]-273)
            self.current_pressure = self.city_res["pressure"]
            self.current_humidity = self.city_res["humidity"]
            self.suntime = data["sys"]
            self.sunrise = DateTime.datetime.fromtimestamp(self.suntime["sunrise"])
            self.sunset = DateTime.datetime.fromtimestamp(self.suntime["sunset"])
            self.now = DateTime.datetime.now()
            self.content = """
            Hôm nay là ngày {day} tháng {month} năm {year}
            Mặt trời mọc vào {hourrise} giờ {minrise} phút
            Mặt trời lặn vào {hourset} giờ {minset} phút
            Nhiệt độ trung bình là {temp} độ C
            Áp suất không khí là {pressure} héc tơ Pascal
            Độ ẩm là {humidity}% """.format(day = self.now.day,month = self.now.month, year= self.now.year, hourrise = self.sunrise.hour, minrise = self.sunrise.minute,
                                                                            hourset = self.sunset.hour, minset = self.sunset.minute, 
                                                                            temp = self.current_temperature, pressure = self.current_pressure, humidity = self.current_humidity)
            self.speak(self.content)
            time.sleep(25)
        else:
            self.speak("Không tìm thấy địa chỉ của bạn")
        # hàm kiểm tra và xuất kết quả
    def LangNghe(self):
        global location
        text = str(self.get_text())
        if "thời tiết"  in text:
            self.current_weather()
                    
        elif "ngày" in text or "giờ" in text or "tháng"  in text or" phút" in text or "năm" in text: 
            self.get_time(text)
        
        elif (text.find('ok google') != -1):
            self.speak("bạn cần gì")
            self.LangNghe()
        else:
            location = unidecode.unidecode(text)


# hàm hỏi
    def GoiTroLiAo(self):
        self.speak("bạn cần gì")
        self.LangNghe()
#  hàm chạy song luồng và lấy văn bản cho khung trực quan hóa dữ liệu
    def bt_voice(self):
        global location
        timer1s = Thread(target=self.GoiTroLiAo())
        timer1s.start()
        self.ui.lineEdit.insert(location)

#Biêu đồ line
class Canvas_grafica1(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(6, 6), 
            sharey=True, facecolor='white') 
        super().__init__(self.fig) 
        global link
        global mode
        global datetime
        global temp
        global uvindex
        global humidity
        global windspeed
        global response
        datetime = []
        temp = []
        humidity = []
        windspeed = []
        uvindex = []
        datetime = []
        


        if mode == 1:
            for i in range(5,18):
                datetime.append(str(response["days"][0]["hours"][i]["datetime"]))
                temp.append(round(float((response["days"][0]["hours"][i]["temp"]-32)/1.8)))
                humidity.append(float(response["days"][0]["hours"][i]['humidity']))
                windspeed.append(float(response["days"][0]["hours"][i]['windspeed']))
                uvindex.append(float(response["days"][0]["hours"][i]['uvindex']))

            self.fig.suptitle('Line Graph: Weather forecast for the next few hours',size=9)
            plt.plot(datetime, humidity, 'b', label='Humidity (%)')
            plt.plot(datetime, temp, 'r', label='Temp (℃)')
            plt.plot(datetime, windspeed, 'g', label='Wind speed (m/s)')
            plt.plot(datetime,uvindex,'y', label="UV index")
            plt.xticks(fontsize = 5, rotation = 20)
            plt.legend(loc='best')
            plt.xlabel("Time")
            plt.ylabel("Index")      
        else:
            try:
                df = pd.read_csv(link)
                self.fig.suptitle('Line Graph: Weather forecast for 14 days',size=9)
                plt.plot(df['datetime'], df['humidity'], 'b', label='Humidity (%)')
                plt.plot(df['datetime'], df['temp'], 'r', label='Temp (℃)')
                plt.plot(df['datetime'], df['windspeed'], 'g', label='Wind speed (kph)')
                plt.plot(df['datetime'], df['uvindex'], 'y', label='UV index')
                plt.xticks(fontsize = 5, rotation = 20)
                plt.legend(loc='best')
                plt.xlabel("Time")
                plt.ylabel("Index")
            except:
                pass


#Biêu đồ box
class Canvas_grafica2(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig , self.ax = plt.subplots(1,dpi=100, figsize=(6, 6), 
            sharey=True, facecolor='white')
        super().__init__(self.fig) 
        global link
        global mode       
        global datetime
        global temp
        global uvindex
        global humidity
        global windspeed    
        global response
        datetime = []
        temp = []
        humidity = []
        windspeed = []
        uvindex = []
        datetime = []
        colum = []
        labels = []
        
        if mode == 1:
            dist={}
            for i in range(10):
                for j in range(23):
                    temp.append(round(float((response["days"][i]["hours"][j]["temp"]-32)/1.8)))        
                dist[str(response["days"][i]["datetime"])] = temp
                temp = []

            data1= pd.DataFrame(dist)
            # print(data1)
            for i in data1.columns:
                labels.append(i)
                colum.append(data1[i])
            k =[]
            for i in range(1,len(labels)+1):
                k.append(i)
            # print(colum)
            self.fig.suptitle('Scatter Plot: Weather forecast for 14 days',size=9)
            
            box= self.ax.boxplot(colum, notch=True, patch_artist=True)
            colors = ['#0000FF', '#00FF00','#aaaa00','#00ffff','#00557f','#aaaaff','#aaff7f',
                        '#ff5500','#FFFF00', '#FF00FF','#ff007f','#55ffff','#ffaa00','#55aaff']

            for patch, color in zip(box['boxes'], colors):
                patch.set_facecolor(color)
            plt.xticks(k,labels,fontsize = 5, rotation = 20)
            plt.xlabel("Day")
            plt.ylabel("Temp") 
        else:
            try:
                df = pd.read_csv(link) 
                self.fig.suptitle('Scatter Plot: Weather forecast for 14 days',size=9)
                plt.scatter(df.datetime, df.humidity, s=50, c='blue', label='Humidity (%)')
                plt.scatter(df.datetime, df.temp, s=50, c='red', label='Temp (℃)')
                plt.scatter(df.datetime, df.windspeed,s=50, c='green', label='Wind speed (kph)')
                plt.scatter(df.datetime, df.uvindex, s=50, c='yellow', label='UV index')
                plt.xticks(fontsize = 5, rotation = 20)
                plt.legend(loc='best')
                plt.xlabel("Time")
                plt.ylabel("Index") 
            except:
                pass


#Biêu đồ headmap
class Canvas_grafica3(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig , self.ax = plt.subplots(1, dpi=100, 
            sharey=True, facecolor='white')
        super().__init__(self.fig) 
        global link
        global mode
        global datetime
        global temp
        global uvindex
        global humidity
        global windspeed
        global response
        datetime = []
        temp = []
        humidity = []
        windspeed = []
        uvindex = []
        datetime = []
        cloudcover=[]
        solarenergy = []
        feelslike = []
        dist ={}

        if mode == 1:

            for j in range(14):
                datetime.append(str(response["days"][j]["datetime"]))
                temp.append(round(float((response["days"][j] ["temp"]-32)/1.8)))
                humidity.append(float(response["days"][j] ['humidity']))
                windspeed.append(float(response["days"][j] ['windspeed']))
                uvindex.append(float(response["days"][j] ['uvindex']))
                cloudcover.append(float(response["days"][j] ['cloudcover']))
                solarenergy.append(float(response["days"][j] ['solarenergy']))
                        
            dist['temp'] = temp
            dist["humidity"] = humidity
            dist["windspeed"] = windspeed
            dist["uvindex"] = uvindex
            dist["cloudcover"] = cloudcover
            dist["solarenergy"] = solarenergy
            df = pd.DataFrame(dist,index =datetime)
            df= round(df.corr(),2)
            data = []
            for row in df.columns:
                data.append(list(df[row]))
            data= np.array(data)

            label1 = ['temp','humidity',"windspeed","uvindex","cloudcover","solarenergy"]
            data = np.array(data)
            im = self.ax.imshow(data)

            # Show all ticks and label them with the respective list entries
            self.ax.set_xticks(np.arange(len(label1)), labels=label1,size=5)
            self.ax.set_yticks(np.arange(len(label1)), labels=label1,size=5)

            # Rotate the tick labels and set their alignment.
            plt.setp(self.ax.get_xticklabels(), rotation=20, ha="right",
                    rotation_mode="anchor")

            # Loop over data dimensions and create text annotations.
            for i in range(len(label1)):
                for j in range(len(label1)):
                    text = self.ax.text(j, i, data[i, j],
                                ha="center", va="center", color="w")

            self.ax.set_title("Harvest of local farmers (in tons/year)", size = 6)
            self.fig.tight_layout()

        else:
            try:
                df2 = pd.read_csv(link)
                plt.bar(df2['datetime'],df2['precip'],width=-0.4,align='edge',label='Precip (mm)')
                plt.bar(df2['datetime'],df2['precipcover'],width=0.4,align='edge',label='Precip-cover (%)')
                plt.plot(df2['datetime'],df2['temp'])
                plt.legend(loc='best')
                plt.xticks(fontsize = 5, rotation = 20)
                self.fig.suptitle("Bar Plot: Raining precipitaion for 14 days",size=9)
                plt.xlabel("Time")
                plt.ylabel("Index")
            except:
                pass


#Biểu đồ histogram
class Canvas_grafica4(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(6, 6), 
            sharey=True, facecolor='white')
        super().__init__(self.fig) 
        global link
        global mode
        global datetime
        global temp
        global uvindex
        global humidity
        global windspeed
        global response
        temp = []
        humidity = []
        windspeed = []
        uvindex = []
        solarenergy = []
        feelslike = []
        dist1 ={}

        if mode == 1:
            for j in range(14):
                for i in range(7,17):
                    temp.append(round(float((response["days"][j]["hours"][i]["temp"]-32)/1.8)))
                    uvindex.append(float(response["days"][j]["hours"][i]['uvindex']))
                    solarenergy.append(float(response["days"][j]["hours"][i]['solarenergy']))
                    
            print('xl xong xl')
            dist1['temp'] = temp
            dist1["solarenergy"] = solarenergy
            dist1["uvindex"] = uvindex
            data = pd.DataFrame(dist1)
            g = pd.plotting.scatter_matrix(data, figsize=(3,3), marker = 'o', hist_kwds = {'bins': 10}, s = 10, alpha = 0.5,ax=self.ax)

            
        else:
            df2 = pd.read_csv(link)
            temp1=df2['temp']
            temp1.plot.hist(align='mid',bins=50)
            avarange=np.median(np.array(df2['temp']))
            plt.axvline(avarange,color='red',label="Avarange temperature") 
            plt.ylabel('Index')
            plt.xticks(fontsize = 5, rotation = 20)
            self.fig.suptitle("Histogram: Temperature for 14 days",size=9)
            plt.legend(loc='best')

class SplashScreen(QMainWindow):
    def __init__(self):
        counter = 0
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## ==> SET INITIAL PROGRESS BAR TO (0) ZERO
        self.progressBarValue(0)

        ## ==> REMOVE STANDARD TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Remove title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # Set background to transparent

        ## ==> APPLY DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(10)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## DEF TO LOANDING
    ########################################################################
    def progress (self):
        global counter
        global jumper
        value = counter

        # HTML TEXT PERCENTAGE
        htmlText = """<p><span style=" font-size:68pt;">{VALUE}</span><span style=" font-size:58pt; vertical-align:super;">%</span></p>"""

        # REPLACE VALUE
        newHtml = htmlText.replace("{VALUE}", str(jumper))

        if(value > jumper):
            # APPLY NEW PERCENTAGE TEXT
            self.ui.labelPercentage.setText(newHtml)
            jumper += 10

        # SET VALUE TO PROGRESS BAR
        # fix max value error if > than 100
        if value >= 100: value = 1.000
        self.progressBarValue(value)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 95:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MiApp()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 0.5

    ## DEF PROGRESS BAR VALUE
    ########################################################################
    def progressBarValue(self, value):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 150px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(85, 170, 255, 255));
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.circularProgress.setStyleSheet(newStylesheet)

#Bắt đấu chương trình chính
if __name__ == "__main__":
     app = QApplication(sys.argv)
     window = SplashScreen()
     sys.exit(app.exec_())  