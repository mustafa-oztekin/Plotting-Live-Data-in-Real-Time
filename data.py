import csv
import time
import serial

arduino = serial.Serial("COM3", 9600)

sira = 0
deger = 0

fieldnames = ["sira", "deger"]

with open("data.csv", "w") as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    with open("data.csv", "a") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "sira" : sira,
            "deger" : deger
            }
        csv_writer.writerow(info)
        print(sira, deger)

        data = arduino.readline()
        data = data.decode("utf").rstrip("\n")
        data = float(data)

        sira += 1
        deger = data

    time.sleep(1)
    
        
