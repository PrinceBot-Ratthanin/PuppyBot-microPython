from machine import SPI,Pin
from puppybot import puppybot,TFT,sysfont,delay,mapf
from huskylensPythonLibrary import HuskyLensLibrary,husky_read_ID
import time
import math
robot = puppybot()
spi = machine.SPI(0,baudrate=2000000,polarity=1,phase=1,bits=8,firstbit=machine.SPI.MSB,
                  sck=machine.Pin(18),mosi=machine.Pin(19),miso=machine.Pin(16))
tft=TFT(spi,20,21,17)
tft.initr()
tft.rgb(True)

tft.fill(TFT.BLACK)
def wait():
    tft.fill(TFT.BLACK)
    tft.rotation(3)
    while(robot.sw1()==1):
        tft.fill(TFT.WHITE)
        tft.text((0, 0), "ADC 0 = "+str(robot.ADC(0)), TFT.RED, sysfont,2)
        tft.text((0, 16), "ADC 1 = "+str(robot.ADC(1)), TFT.BLUE, sysfont,2)
        tft.text((0, 32), "ADC 2 = "+str(robot.ADC(2)), TFT.GREEN, sysfont,2)
        tft.text((0, 48), "ADC 3 = "+str(robot.ADC(3)), TFT.YELLOW, sysfont,2)
        tft.text((30, 80), "Press SW1", TFT.BLUE, sysfont,2)
        tft.text((40, 110), "To Run", TFT.BLUE, sysfont,2)
    robot.buzzer(1500,300,10)
    robot.buzzer(500,200,1000)


   
#คำสั่งสำหรับการแสดงผลภายในหน้าจอ
# tft.rotation(3)                     
# tft.fill(tft.color(0, 230, 242))
# tft.text((0, 0), "A", TFT.BLUE, sysfont,3)
# tft.text((50, 10), str(mapf(10,0,10,0,5)), TFT.BLUE, sysfont,3)
# delay(100)

#คำสั่งสำหรับหุ่นยนต์วิ่งตามเส้น แบบPD Control
#วิธีการคือให้กำหนด Pin เซ็นเซอร์ให้ตรงเรียงจากซ้ายไปขวา
#แล้วเลือกสีของเส้นให้ตรงกับที่ต้องการ

robot.set_pinSensor([0,1,2,3,4,5,6,7],'Black')
robot.calibrate_sensor(1000)
#set_min_sensor([15,15,15,15,15,15,15,15])
#set_max_sensor([99,99,99,99,99,99,99,99])
wait()
while(1):
    robot.lineFollowing(20,0.3,2)


# while(1):
#     tft.fill(tft.color(0, 230, 242))
#     tft.text((50, 10), str(robot.readLine()), TFT.BLUE, sysfont,3)
#     delay(100)

#คำสั่งสำหรับการใช้งาน มอเตอร์
# wait()
# robot.fd(50,1000)
# robot.ao(500)


#เริ่มเขียนโปรแกรมหลังจากจากนี้

        






