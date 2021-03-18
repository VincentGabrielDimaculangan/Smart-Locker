#Do it Smart
#A cura di Fornasiero, Dimaculangan, Giacometti, Serra, Sedda

from maxim.max7219 import max7219
# import fonts file where matrix numbers are defined
import fonts
# Setup Led Matrix (8x8 Click on slot C)
display = max7219.MAX7219(SPI0, D30)
display.shutdown(False)
intensity = 1
display.set_intensity(intensity)

#---------WIFI-----------------
from wireless import wifi
# this example is based on Particle Photon
# change the following line to use a different wifi driver
from stm.spwf01sa import spwf01sa as wifi_driver
import streams
from zerynthapp import zerynthapp
streams.serial()

print("STARTING...")

try:
    # Device UID and TOKEN can be created in the ADM panel
    zapp = zerynthapp.ZerynthApp("lNuw0JxdSB6q1VlAuf5xrA","bq9Dcq5QRt2NUk2AblWgjg", log=True)

    # connect to the wifi network (Set your SSID and password below)
    wifi_driver.init(SERIAL1,D16,baud=9600) #wifi nello slot A
    for i in range(0,5):
        try:
            wifi.link("TIM-30033547",wifi.WIFI_WPA2,"dDumVmiQGJ8REiM6")
            break
        except Exception as e:
            print("Can't link",e)
    else:
        print("Impossible to link!")
        while True:
            sleep(1000)
except Exception as e:
    print(e)

    zapp.run()

#--------------------------------

sleep(1000)
num=0
row=0
col=0
print("---------Do it Smart----------")

def system_setup():

    onPinFall(D24, btn_press_a)  #touchkey nello slot B
    onPinFall(A1, btn_press_b)
    onPinFall(D7, btn_press_c)
    onPinFall(D26, btn_press_d)
    

while True:
    passw=[1,2,3,4]       #array password già popolato   ABCD
    inserisci= [] #array che verrà popolato dal touchkey
    conta = 0

    def btn_press_a():
        print("Button A Pressed")
        inserisci.insert(1,1)
    def btn_press_b():
        print("Button B Pressed")
        inserisci.insert(2,2)
    def btn_press_c():
        print("Button C Pressed")
        inserisci.insert(3,3)
    def btn_press_d():
        print("Button D Pressed")
        inserisci.insert(4,4)
    #quindi inserisci diventa --> inserisci[1,2,3,4]
    
    if passw == inserisci:
            print("giusta")
            conta=0
            while True:
                for num in range(2):
                    intensity += 1
                if intensity > 15:
                    intensity = 0
                display.set_intensity(intensity)
                for row in range(8):
                    for col in range(8):
                        if fonts.numbers[num][row][col]:
                            display.set_led(row, col, 0)
                sleep(2000)
            
            zapp.notify("ATTENZIONE!","La scatola e' aperta!")
            #apri motore
    else:
            print("sbagliata")
            conta=0
            while True:
                for num in range(2):
                    intensity += 1
                if intensity > 15:
                    intensity = 0
                display.set_intensity(intensity)
                for row in range(8):
                    for col in range(8):
                        if fonts.numbers[num][row][col]:
                            display.set_led(row, col, 1)
                sleep(2000)
        
        #inserisci = inserisci[:4]    operatore per ridurre il numero degli elementi
       # print(inserisci)
       
    # Setup the system
    system_setup()

#se uso inserisci.insert() l'array viene incrementato ogni volta, quindi devo fissare la lunghezza dell'array
#l'ultimo tasto dà sempre print non so pk
