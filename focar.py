#lisätään micropythonin tarvitsemat moduulit
from machine import Pin, PWM
from time import sleep

#luodaan led olio
led = Pin("LED", Pin.OUT)


# Moottori A
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

# Moottori B
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

# Aseta PWM-taajuus 1000 Hz
e1.freq(1000)
e2.freq(1000)

#vilkuta lediä
def vilkuta_ledvaloa(kerrat, aika):
    for _ in range (kerrat):
        led.on()
        sleep(aika)
        led.off()
        sleep(aika)


#Liikuta FoCaria eteenpäin
def eteenpain (nopeus = 32767, aika =6):
    m1.value(1)
    m2.value(1)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)

#Liikuta FoCaria taaksepäin
def taaksepain(nopeus =32767, aika =6):
    m1.value(0)
    m2.value(0)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)

#Käännä FoCaria
def kaanny(suunta, maara, nopeus =32767):
    if(suunta== "vasen"):
        m1.value(1)
        m2.value(0)
        e1.duty_u16(nopeus)
        e2.duty_u16(nopeus)
        sleep(maara)
    else: #mennään oikealle
        m1.value(0)
        m2.value(1)
        e2.duty_u16(nopeus)
        e1.duty_u16(nopeus)
        sleep(maara)

#Pysäytä FoCar
def pysayta():
    m1.value(0)
    m2.value(0)
    e1.duty_u16(0)
    e2.duty_u16(0)