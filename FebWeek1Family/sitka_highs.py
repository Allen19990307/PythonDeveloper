import csv
import matplotlib.pyplot as plt
from datetime import datetime
filename = "sitka_weather_07-2018_simple.csv"
filename1 = "sitka_weather_2018_simple.csv"
with open(filename1) as f:
    """读取文件头,按照下标的方式去读取相应的数据"""
    reader = csv.reader(f)
    next1 = next(reader)

    # for index,column_head in enumerate(next1):
    #     print(index,column_head)
    dates,highs,lows =[],[],[]
    for row in reader:
        MaxTemp = int(row[5])
        LowTemp = int(row[6])
        date = datetime.strptime(row[2],'%Y-%m-%d')
        dates.append(date)
        highs.append(MaxTemp)
        lows.append(LowTemp)
    print(highs)
    print(dates)
    """根据最高的温度实现图像的绘制"""
    plt.style.use('seaborn')
    fig,ax = plt.subplots()
    """设置最低的温度折线图，alpha制定其中的透明程度"""
    ax.plot(dates,highs,c= 'red',alpha = 0.5)
    ax.plot(dates,lows, c='blue',alpha = 0.5)
    ax.fill_between(dates,highs,lows,facecolor = 'green',alpha = 0.1)
    """设置图形的格式"""
    ax.set_title("2018  Max&Low Temp",fontsize = 24)
    ax.set_xlabel('',fontsize = 16)
    fig.autofmt_xdate()
    ax.set_ylabel("Teamperature:F",fontsize = 18)
    ax.tick_params(axis = 'both',which = 'major',labelsize =18)
    plt.show()
