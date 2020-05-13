time_sek = int(input('Введите время в секундах '))
time_hour = time_sek // 3600
time_minut = (time_sek / 60) % 60
time_sek = time_sek % 60

print('%02d:%02d:%02d'%(time_hour,time_minut,time_sek))
