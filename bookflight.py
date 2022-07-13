class flight :
  price = 5000
  tickets = 50
  id = 1
#  passenger_id = []
 # passengerperseats = []
  #passcost = []
  #passenger_details = []
  #pas_detail = []
  def __init__(self,passenger_id,passengerperseats,passcost,passenger_details,pas_detail) :
    self.id = flight.id
    flight.id = flight.id + 1
    self.tickets = flight.tickets
    self.price =flight.price
    self.passenger_detail = pas_detail
    self.pass_id = passenger_id
    self.pas_detail = passenger_details
    self.passperseats = passengerperseats
    self.passcost = passcost

  def book(self,pass_id,pass_details,seats,price) :
   self.passcost.append(price)
   self.passenger_detail.append(pass_details)
   self.passperseats.append(seats)
   self.pass_id.append(pass_id)
#   print(self.pass_id)
 #  print(self.passenger_detail)
   self.tickets = self.tickets - seats
   self.price =  self.price + 200 * seats

  def flight_detail(self) :
    print('flight ID : {} '.format(self.id) ,end='--')
    print('no of tickets : {} '.format(self.tickets),end='--')
    print('current Price : {} '.format(self.price))
    print('-------------------------------------------')
    print()
  def passenger_details(self,id) :
   print('flight ID' + ' -- '+str(id))
   for i in self.passenger_detail :
     if i == '' :
      continue
     if self.id == id:
      print(i)
   print()
   print('-------------------------------------')
   print()

  def cancel(self,passid) :
    if passid in self.pass_id :
       index = self.pass_id.index(passid)
    else :
     return -1
    seat  =   self.passperseats[index]
    self.tickets += seat
    self.price = self.price - 200*seat
    self.pass_id[index] = 0
    self.passenger_detail[index] = ''
    self.passperseats[index] = 0
   #refund 
    amount = self.passcost[index]
    print('refunded successfully -- > {}'.format(amount))

