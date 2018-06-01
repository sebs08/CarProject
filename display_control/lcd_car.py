import lcd_i2c as lcd
from time import sleep



lcd.lcd_init()

def display_info(text):
    if isinstance(text, str):
        text_len = len(text)
        if text_len > 16:
            for i in range(text_len):
                if i < text_len:
                    lcd.lcd_string(text[i:i+16], 1)
                    sleep(0.3)
        else:
            lcd.lcd_string(text,1)

    if isinstance(text, list):
        #TODO: add writing on both lines
        pass





if __name__ == "__main__":
    for i in range(3):
        display_info("abcdefghijklmnopqrstuvwxyz")