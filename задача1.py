import csv
import math
res=0
c=1

with open ("data.csv", "r")as f:
    #fields = ("ID", "Parkingname", "global_id", "ParkingZonenNumber", "AdmArea", "District", "Address", "WorkingHours", "Price", "CarCapacity", "Longitude_WGS84", "latitude_WGS84", "Coordinates", "geoData")
    fields = ('ID','Name','INN','global_id','KPP','OGRN','Sum','ExtraInfo')

    reader = csv.DictReader (f, fields, delimiter = ";")
    for i in reader:
        #print (i.get ('ID'))
        s= i['Sum']
        s=s.split('E')
        s=float(s[0])*(10**float(s[1]))
        res=res+s
        c+=1
        res=res/c
    print (res)
