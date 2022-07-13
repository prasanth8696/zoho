
upper = 2
lower = 2
middle = 2
waiting_list = 2
rac = 2
patient_id = 0
patient_dict = {}
booked_upper = 0
booked_lower = 0
booked_middle = 0
booked_waiting = 0
booked_rac = 0
wait_list = []
rac_list = []
while(True) :

 print('1. book tickets')
 print('2. Available tickets')
 print('3. Cancel tickets')
 print('4. booked tickets')
 print('5. exit')

 no = int(input())
 if no >5 and no < -1 :
  continue

 if no ==1 :
   patient_id += 1
   patient_list = []
   name = input('enter your name : ')
   age = int(input('enter your age : '))
   preference = input('preference : ')
   patient_list.append('id-' + str(patient_id))
   patient_list.append(name)
   patient_list.append(age)
   patient_list.append(preference)
   if waiting_list == 0 :
    print('no tickets available')
    continue
#prefernce lower
   if preference == 'lower' :
     if lower > 0 :
       lower -= 1
       print('Lower birth is given')
       booked_lower += 1
       patient_list.append(str(booked_lower) + 'L')
     elif middle > 0 :
       middle -= 1
       print('middle birth is given')
       booked_middle += 1
       patient_list.append(str(booked_middle) + 'M')

     elif upper > 0 :
       upper -= 1
       print('Upper birth is given')
       booked_upper += 1
       patient_list.append(str(booked_upper) + 'U')

     elif rac > 0 :
       rac -= 1
       print('Rac is given')
       booked_rac += 1
       patient_list.append(str(booked_rac) + 'R')
       rac_list.append(patient_list)

     elif waiting_list > 0 :
       waiting_list -= 1
       print('waiting list is given')
       booked_waiting += 1
       patient_list.append(str(booked_waiting) + 'WL')
       wait_list.append(patient_list)
     else :
       print('no tickets available')
     patient_dict[patient_id] = patient_list
# preference middle
   if preference  == 'middle' :
     if middle > 0 :
       middle -= 1
       print('middle birth is given')
       booked_middle += 1
       patient_list.append(str(booked_middle) + 'M' )

     elif lower > 0 :
       lower -= 1
       print('Lower birth is given')
       booked_lower += 1
       patient_list.append(str(booked_lower) + 'L')

     elif upper > 0 :
       upper -= 1
       print('Upper birth is given')
       booked_upper += 1
       patient_list.append(str(booked_upper) + 'U')

     elif rac > 0 :
       rac -= 1
       print('Rac is given')
       booked_rac += 1
       patient_list.append(str(booked_rac) + 'R')
       rac_list.append(patient_list)

     elif waiting_list > 0 :
       waiting_list -= 1
       print('waiting list is given')
       booked_waiting += 1
       patient_list.append(str(booked_waiting) + 'WL')
       wait_list.append(patient_list)
     else :
       print('no tickets available')
     patient_dict[patient_id] = patient_list 

#preference  upper 

   if preference == 'upper' :
     if upper > 0 :
       upper -= 1
       print('Upper birth is given')
       booked_upper += 1
       patient_list.append(str(booked_upper) + 'U')

     elif middle > 0 :
       middle -= 1
       print('middle birth is given')
       booked_middle += 1
       patient_list.append(str(booked_middle) + 'M')

     elif lower > 0 :
       lower -= 1
       print('Lower birth is given')
       booked_lower += 1
       patient_list.append(str(booked_lower) + 'L')


     elif rac > 0 :
       rac -= 1
       print('Rac is given')
       booked_rac += 1
       patient_list.append(str(booked_rac) + 'R')
       rac_list.append(patient_list)
     elif waiting_list > 0 :
       waiting_list -= 1
       print('waiting list is given')
       booked_waiting += 1
       patient_list.append(str(booked_waiting) + 'WL')
       wait_list.append(patient_list)

     else :
       print('no tickets available')
     patient_dict[patient_id] = patient_list
   print('---------------------booking successfully ')
   print('passenger details ',end='')
   for i in patient_list:
     print(i,end=',')
   print()

# no == 2 for available tickets
 if no == 2 :
  print('Available lower birth : {}'.format(lower))

  print('Available middle births: {}'.format(middle))

  print('Available upper birth : {}'.format(upper))

  print('Available rac  birth : {}'.format(rac))

  print('Available waiting_list birth : {}'.format(waiting_list))


#cancel tickets

 if no == 3 :
  print('enter your passenger id')
  idd = int(input())
  if idd not in patient_dict :
    print('invalid passenger details ')
    continue
  else :
   p_detail = patient_dict[idd]
   del patient_detail
   if p_detail[2] == 'lower' :
     lower += 1
     booked_lower -= 1
   elif p_detail[2] = 'middle':
     middle += 1
     booked_middle -= 1
   elif p_detail[2] == 'upper':
    upper += 1
    booked_upper -= 1

