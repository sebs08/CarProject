import lcd_i2c as lcd
from time import sleep

lcd.lcd_init()

for i in range(3):
    lcd.lcd_string("RPiSpy         <", lcd.LCD_LINE_1)
    lcd.lcd_string("I2C LCD        <", lcd.LCD_LINE_2)
    print("Run: " + str(i))
    sleep(2)


