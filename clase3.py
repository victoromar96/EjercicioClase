import time
import os
print (time.localtime())

t = time.localtime()
year = t[0]
month = t[1]
print (year)
print (month)

#dia con el mes
month = t[1]
day = t[2]
print(month)
print(day)
print (t[4])
print(t[2])
hora = t[3]
min = t[4]
seg = t[5]
#primero hacer string para concatenar cadenas
#print(t[3]+":"+t[4]+":"+t[5])
#print("la hora es: ")
#print(hora,':',min,':',seg)


#print("")
#for x in range(1,61):
#    print(x)


#for x in range(1,61):
#    print(x)
#    time.sleep(1)


# que cambie la hora



#ejercicio resuelto

while True:
    t = time.localtime()
    print(str(t[3])+":"+str(t[4])+":"+str(t[5]))
    time.sleep(1)
    os.system("cls") #en windows


#temporizador de (cuenta regresiva) // deber



