# -*- coding: utf-8 -*-
seg = int(input('Digite o tempo em segundos: '))
minuto = 0
hora = 0

if(seg>=60):
    minuto = seg / 60
    seg = seg % 60
    print("%d:"%hora,"%d:"%minuto,"%d"%seg)
    if(minuto>=60):
        hora = minuto / 60
        minuto = minuto % 60
        print("%d:"%hora,"%d:"%minuto,"%d"%seg)
        if (hora>=24):
            hora = hora % 24
            print("%d:"%hora,"%d:"%minuto,"%d"%seg)
else:
    print("%d:"%hora,"%d:"%minuto,"%d"%seg)
