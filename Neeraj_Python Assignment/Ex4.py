class Aircraft:
    x=0
    y=0
    acceleration=1
    flight_number = 0
    def move_up(self):
        print"Flight ", self.flight_number ," Moved up . . ."
        self.y +=1 
    def move_down(self):
        print"Flight ",self.flight_number,"Moved down . . ."
        self.y -=1
    def move_right(self):
        print"Flight ",self.flight_number," Moved right . . ."
        self.x +=1
    def move_left(self):
        print"Flight ",self.flight_number," Moved left . . ."
        self.y -=1
    def __init__(self, obj_no, new_x=0, new_y=0):
        print "Aircraft # ",obj_no, " has been istantiated"
        self.flight_number = obj_no
        self.x=new_x
        self.y=new_y



neeraj_airlines = []
for i in range (0,5):
    option=raw_input("Would you like to enter coordinates of new aircraft:(y/n)")
    if(option=='y'):
        x_coord=input("Enter  value of x coordinate for aircraft")
        y_coord=input("Enter  value of y coordinate for aircraft")
        neeraj_airlines.append(Aircraft(i+1,x_coord,y_coord))
    else:
        neeraj_airlines.append(Aircraft(i+1))
    print "Initial X-Coord:",neeraj_airlines[i].x
    print "Initial X-Coord:",neeraj_airlines[i].y
    neeraj_airlines[i].move_up()
    neeraj_airlines[i].move_left()
    neeraj_airlines[i].move_down()
    neeraj_airlines[i].move_up()
    neeraj_airlines[i].move_up()
    neeraj_airlines[i].move_right()
    neeraj_airlines[i].move_down()
    neeraj_airlines[i].move_left()
    neeraj_airlines[i].move_up()
    neeraj_airlines[i].move_down()
    neeraj_airlines[i].move_left()
    neeraj_airlines[i].move_right()

    print "Final X-Coord:",neeraj_airlines[i].x
    print "Final X-Coord:",neeraj_airlines[i].y
