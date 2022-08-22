import requests #pip install requests
import os
clear = lambda : os.system('clear')


print('Open Weather App.....')
print('                    Developed by SHAN...')

print()
print('1.by city name.... ') 
print('2.by latitude and longitude') #This Method is not yet ready
choice = int(input('enter your choice '))
   
def weather_check(url) :

   
   
        clear() 
        url = url
    #this is my api key if you want api key login into openweather website and get the apikeys
        try :
            response = requests.get(url,timeout=5)
        except :
            print('server down try again later....')
            return
        if response.ok :
            print('*------------------------------------------------*')
            print('|                     {0} {1}                        '.format(response.json()['name'].upper(),response.json()['sys']['country'].upper()))
            lon = response.json()['coord']['lon']
            lat = response.json()['coord']['lat']
            print('| '+'city coordinates..........                     |')
            print('| ' + f'longitude : {lon}   ',end = '    ')
            print( f'lattitude : {lat}  ')
            print('|                                                |')
            print('| '+'weather : {}                     '.format(response.json()['weather'][0]['description']))
            print('|                                                |')
            print('| '+'temperature condtions......                    |')
            value = response.json()['main']
            cnt = 0
            for i,j in value.items() :
                if cnt%2 == 0:
                    print('| '+ str(i) + ' : ' + str(j),end = '    ')
                    cnt += 1
                else :
                    print( str(i) + ' : ' + str(j))
                    print('|                                                |')
                    cnt += 1
            
            print('| ' + 'wind conditions....                            |')
            print('| ' + 'wind speed : {} '.format(response.json()['wind']['speed']),end= '    ')
            print( 'wind degree : {}        |'.format(response.json()['wind']['deg']))
            print('|                                                |')
            print('*------------------------------------------------*')
            print()
            
            
                 
        else :
            print('city not found....')
            print()

if choice == 1 :
  while(True) :
    city = input('enter your city ')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7716c5e05f8561c1893c02ae19c63e24&units=metric'
    weather_check(url)
  
elif choice == 2 :
    while(True) :
     lon,lat = map(float,(input('enter your longitude and lattitude ').strip().split()))
     url = 'http://api.openweathermap.org/data/2.5/weather?lon={0}&lat={1}&appid=7716c5e05f8561c1893c02ae19c63e24'.format(lon,lat)
     weather_check(url)
else :
    raise KeyError('Invalid Input.....')


print('This is Developed by SHAN.......')
