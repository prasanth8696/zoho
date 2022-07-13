from bookflight import *

passenger_id = []
passengerperseats = []
passcost = []
passenger_details = []
pas_detail = []





flight_list = []
for i in (1,3) :
  flight_list.append(flight(passenger_id,passengerperseats,passcost,passenger_details,pas_detail))

def book(pass_id,seats,currentFlight) :
  price = currentFlight.price * seats
  passenger_detail = 'passenger_id ' + str(pass_id)+ '--' + 'no of seats ' + str(seats) +'--' + 'total cost ' + str(price)
  currentFlight.book(pass_id,passenger_detail,seats,price)
  currentFlight.flight_detail()
  currentFlight.passenger_details(currentFlight.id)

def cancel(currentFlight,passid) :
  n = currentFlight.cancel(passid)
  if n == -1 :
   print('invalid passenger id ')
   return
  print('----------------------cancel successfully')
  currentFlight.flight_detail()
  currentFlight.passenger_details(currentFlight.id)


def show() :
  for i in flight_list :
   i.flight_detail()
   i.passenger_details(i.id)
passenger_id = 1
while(True) :
  print('1 --> book ticket')
  print('2 --> cancel ticket')
  print('3 --> booked tickets')
  print('4 --> Exit ')
  choice = int(input())
  if choice not in [1,2,3,4] :
   print('invalid ')
   continue

  if choice == 1 :
   f = int(input('Flight id '))
   if f > 2 or f<= 0 :
    print('invalid flight details')
    continue
   for i in flight_list :
    if i.id == f :
     currentFlight = i
   currentFlight.flight_detail()
   seats = int(input('no of seats '))
   if seats > currentFlight.tickets :
     print('not enough tickets')
     continue
   print(currentFlight.id)
   book(passenger_id,seats,currentFlight)
   passenger_id += 1
   print('--------------------booked tickets successfully')

  if choice == 2 :
   passId = int(input('enter passengerid '))

   flightId = int(input('enter flight id '))
   for i in flight_list :
     if i.id == flightId :
      currentFlight = i
   cancel(currentFlight,passId)

  if  choice == 3 :
    show()
  if choice == 4 :
   break
