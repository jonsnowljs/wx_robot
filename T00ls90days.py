from wxpy import *
import time

#休眠时间
def sleeptime(hour,min,sec):
    return hour*3600+min*60+sec

def searchinmps(name):
    return robot.mps().search(name)[0]

#寻找公众号名称
robot  = Robot()
my_mp =searchinmps('T00ls')

#设置时间间隔
interval = sleeptime(23,50,0)

#给公众号T00ls每天发3,4
while 1==1:
    time.sleep(interval)
    my_mp.send('3')
    my_mp.send('4')

