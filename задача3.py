import csv
import math
res=0
c=1

with open ("data-4905-2017-01-27.csv", "r")as f:
    fields = ('ID','ParkingName','global_id','ParkingZoneNumber','AdmArea','District','Address','WorkingHours','Price','CarCapacity','Longitude_WGS84','Latitude_WGS84','Coordinates','geoData')

    #fields = ('ID','Name','INN','global_id','KPP','OGRN','Sum','ExtraInfo')

    reader = csv.DictReader (f, fields, delimiter = ";")
    for i in reader:
        #print (i.get ('Price'))
        s= float(i['Price'])
        #s=s.split('E')
        #s=float(s[0])*(10**float(s[1]))
        res=res+s
    print (res)
