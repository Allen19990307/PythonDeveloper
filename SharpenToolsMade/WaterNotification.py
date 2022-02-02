import time
import webbrowser
total_breaks = 7
break_count = 0
#上班的时候给自己自制bgm提醒休息的时间
while(break_count < total_breaks):
    webbrowser.open("https://www.youtube.com/watch?v=oNPVZKQB3Kg")
    webbrowser.open("https://pixabay.com/zh/photos/stanford-university-church-3861259/")
    time.sleep(60 * 30)
    break_count = break_count + 1