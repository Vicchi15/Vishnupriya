#Imagine an parking lot with 20 parking spaces, where each parking space has an ID which is a natural number, starting with 1, 2, 3, ….upto 20. Parking space '1' is the one closest to the entrance.
#The parking space can be in three sizes: small(10 parking spaces), medium(7 parking spaces) and large slots(3 parking spaces).
#Three types of vehicles are allowed to be parked in a parking space: motorcycle(small), car(medium) and bus(large)
#A motorcycle can be parked in any small, medium or large parking spaces.
#A car can be parked in either a medium slot or a large parking spaces.
#A bus can be parked only in a large parking space.
#When a user enters the parking lot, vehicle type and vehicle ID are noted and fed as input to our system
#Our system should assign the vehicle to the nearest parking space available(if any parking space is available)
#User should be given a printed ticket with the assigned parking spot ID and his vehicle ID
class parking:
  def __init__(self,t,id):
    self.t=t
    self.id=id
  def print(self,sid):
    self.sid=sid
    
class bike(parking):
  def __init__(self,t,id):
    print("The id of vehicle is {}".format(id))
  def print(self,sid):
    print("The slot id is {}".format(sid))
  
class car(parking):
  def __init__(self,t,id):
    print("The id of vehicle is {}".format(id))
  def print(self,sid):
    print("The slot id is {}".format(sid))
  
  
class bus(parking):
  def __init__(self,t,id):
    print("The id of vehicle is {}".format(id))
  def print(self,sid):
    print("The slot id is {}".format(sid))
  
    
def main():
  allocated=0
  sizes=[]
  small=1
  medium=2
  large=3
  for i in range(1,11):
    sizes.append(small)
  for i in range(11,18):
    sizes.append(medium)
  for i in range(18,21):
    sizes.append(large)
  itr=0
  while(itr<20):
    itr=itr+1
    print("Parking lot allocation....Enter option as 1 for bike,2 for car and 3 for bus:")
    x=input()
    if(x=='1'):
      print("Input Vehicle Type and Vehicle Id:")
      vt=input()
      vi=input()
      for j in range(1,20):
        if((sizes[j-1]==small) or (sizes[j-1]==medium) or (sizes[j-1]==large)):
          sizes[j-1]=allocated
          slot_id_bike=j
          break
      b=bike(vt,vi)
      b.print(slot_id_bike)
    if(x=='2'):
      print("Input Vehicle Type and Vehicle Id:")
      vt1=input()
      vi1=input()
      for j in range(11,18):
        if((sizes[j-1]==medium) or (sizes[j-1]==large)):
          sizes[j-1]=allocated
          slot_id_car=j
          break
      d=car(vt1,vi1)
      d.print(slot_id_car)
    if(x=='3'):
      print("Input Vehicle Type and Vehicle Id:")
      vt2=input()
      vi2=input()
      for j in range(18,21):
        if(sizes[j-1]==large):
          sizes[j-1]=allocated
          slot_id_bus=j
          break
      bu=bus(vt2,vi2)
      bu.print(slot_id_bus)
    print("Input 1 to continue and 0 to exit:")
    choice=input()
    if(choice=='1'):
      continue
    else:
      break
main()
  
