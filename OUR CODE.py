from machine import Pin, I2C ,ADC
from utime import sleep
from ssd1306 import SSD1306_I2C

WIDTH =128
HEIGHT= 64
i2c=I2C(0,scl=Pin(17),sda=Pin(16),freq=200000)

oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)
#sensor = Pin(26, Pin.OUT)
soil=ADC(Pin(26))
min_moisture=0
max_moisture=65535
moisture_percentage= (max_moisture- soil.read_u16())*100/(max_moisture-min_moisture)
relay_sensor= Pin(2, Pin.OUT)
relay_sensor.value(0)
def pump_on():
    #relay_sensor.toggle() # relay will turn on the pump
    relay_sensor.value(1)
    sleep(10)  # Hold , it show new moisture level
    relay_sensor.value(0)
    sleep(10)
    moisture_percentage= (max_moisture- soil.read_u16())*100/(max_moisture-min_moisture)
    print("Now Moisture level:",moisture_percentage)
    oled.text("Now moisture level:", 0, 0)
    oled.text(str(moisture_percentage),0,8)
    oled.fill(0)
    oled.show()
    
 
 
#sleep(5)
while True:
    if(moisture_percentage<20.0):
      print("Current Moisture level:",moisture_percentage)
      oled.text("Sufficient :", 0, 0)
      oled.text("Moisture", 0,8)
      oled.text("level:", 0, 16)
      oled.text(str(moisture_percentage),0,24)
      oled.show()
      sleep(10)
      oled.fill(0)
      oled.show()
      sleep(2)
      
    else :
      print("Moisture level is Low:",moisture_percentage)
      print('Pump is turning on!!!')
      oled.fill(0)
      oled.show()
      sleep(5)
      oled.text("Moisture level: LOW ",0,0)
      oled.text("Pump is turning ON", 0, 8)
      oled.fill(0)
      oled.show()
      sleep(2)
      pump_on()
      
      sleep(1087)
    
    
      
      
    
   