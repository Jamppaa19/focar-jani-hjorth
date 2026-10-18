import focar
from time import sleep

#Tehdään FoCarilla kolmen pisteen käännös

#odotetaan 10 sekunttia ennen lähtöä
sleep(10)

#Ajetaan FoCaria  eteenpäin noin metri
focar.eteenpain(aika=5)

#Käännetään FoCaria
focar.kaanny(suunta="vasen", maara=4)

#Peruutetaan FoCaria
focar.taaksepain(aika=2)

#Käännetään FoCaria
focar.kaanny(suunta="vasen", maara=4)

#Ajetaan FoCaria eteenpäin noin metri
focar.eteenpain(aika=5)

#Pysäytetään FoCar
focar.pysayta()

