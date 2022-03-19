
import json
import sys,os
from imp import reload

from FebWeek3WebCrawler.Financial import file

reload(sys)
sys.setdefaultencoding('utf-8')
def getFileCon(filename):
    if not os.path.isfile(filename):
        return

    try:
        f = open(filename, "r")
        con = f.read()
        f.close()
        return con
    except Exception as e:
        pass

# 向文件写内容
def writeFile(filepath,con):
    if con:
        f = file(filepath, "w")
        f.write(con)
        f.close()
    else:
        print (filepath, "filepath FAIL")

if __name__ == "__main__":
    fl = os.listdir("data")
    for f in fl:
        g = f
        try:
            con = json.loads(getFileCon(f))
            # print con
            writeFile(f,json.dumps(con,indent=4,ensure_ascii=False).decode('utf8'))
            print (g,'OK')
        except Exception as e:
            print (g,e)