#### Q1
##class Circle:
##    def setRadius(self, r):
##        self.radius = r
##
##    def getRadius(self):
##        return self.radius
##
##    def setColor(self, c):
##        self.color = c
##
##    def getColor(self):
##        return self.color
##
##    def getCircumference(self):
##        return 2 * (22 / 7) * self.radius
##
##    def getArea(self):
##        return (22 / 7) * (self.radius ** 2)
##
##a = Circle()
##a.setRadius(32)
##print(f"Radius of a: {a.getRadius()}")
##a.setColor("Blue")
##print(f"Area and circumference of a: {a.getArea()}, {a.getCircumference()}")
##print(f"Color of a: {a.getColor()}")
##a.setRadius(2)
##print(f"New radius of a: {a.getRadius()}")


#### Q2
##class BankAccount:
##    current_balance = 0
##    
##    def withdraw(self):
##        amount = float(input("Enter amount to be withdrawn: "))
##        if amount <= self.current_balance:
##            self.current_balance -= amount
##        else:
##            print("Not enough balance.")
##
##    def deposit(self):
##        amount = float(input("Enter amount to be deposited: "))
##        self.current_balance += amount
##
##    def balance(self):
##        return self.current_balance
##
##Ahmed_account = BankAccount()
##Ahmed_account.deposit()
##Ahmed_account.withdraw()
##print(Ahmed_account.balance())
##Ahmed_account.current_balance += 800
##print(Ahmed_account.current_balance)
##Ahmed_account.withdraw()
##print(Ahmed_account.balance())

#### Q3
##class BankAccount:
##    __current_balance = 0
##    
##    def withdraw(self):
##        amount = float(input("Enter amount to be withdrawn: "))
##        if amount <= self.__current_balance:
##            self.__current_balance -= amount
##        else:
##            print("Not enough balance.")
##
##    def deposit(self):
##        amount = float(input("Enter amount to be deposited: "))
##        self.__current_balance += amount
##
##    def balance(self):
##        return self.__current_balance
##
##Ahmed_account = BankAccount()
##Ahmed_account.deposit()
##Ahmed_account.withdraw()
##print(Ahmed_account.balance())
##Ahmed_account._BankAccount__current_balance += 800
##print(Ahmed_account._BankAccount__current_balance)
##Ahmed_account.withdraw()
##print(Ahmed_account.balance())    


#### Q4
##class Worker:
##    def setHoursWorked(self, h):
##        self.__hoursWorked = h
##
##    def changeRate(self, r):
##        self.__wageRate = r
##
##    def pay(self):
##        return self.__hoursWorked * self.__wageRate
##
##Ahmed = Worker()
##Ahmed.setHoursWorked(2)
##Ahmed.changeRate(10)
##print(Ahmed.pay())
##Ahmed.setHoursWorked(4)
##print(Ahmed.pay())
##Ahmed.changeRate(20)
##print(Ahmed.pay())


#### Q5
##class Worker:
##    def __init__(self, h=0, r=0):
##        self.__hoursWorked = h
##        self.__wageRate = r
##        
##    def setHoursWorked(self, h):
##        self.__hoursWorked = h
##
##    def changeRate(self, r):
##        self.__wageRate = r
##
##    def pay(self):
##        return self.__hoursWorked * self.__wageRate
##
##Ahmed = Worker(r = 10)
##print(Ahmed.pay())
##Ahmed.setHoursWorked(3)
##print(Ahmed.pay())
##Ali = Worker(3)
##print(Ali.pay())
##Kamran = Worker(3, 5)
##print(Kamran.pay())

#### Q6
##class Vehicle:
##    def __init__(self, w = 4, c = "white", m = 0):
##        self.__noOfWheels = w
##        self.__color = c
##        self.__modelNo = m
##
##    def getNumWheels(self):
##        return self.__noOfWheels
##    
##    def getColor(self):
##        return self.__color
##    
##    def getModelNum(self):
##        return self.__modelNo
##
##    def setColor(self, c):
##        self.__color = c
##
##a = Vehicle(8, 'black', 2007)
##print(f"a: wheels = {a.getNumWheels()}, color = {a.getColor()}, Model Number = {a.getModelNum()}")
##a.setColor("green")
##print(f"a: wheels = {a.getNumWheels()}, color = {a.getColor()}, Model Number = {a.getModelNum()}")
##b = Vehicle(m = 2019)
##print(f"b: wheels = {b.getNumWheels()}, color = {b.getColor()}, Model Number = {b.getModelNum()}")

#### Q7
##class Engine:
##    def __init__(self, e = 0, d = 1900):
##        self.__engineNo = e
##        self.__dateOfManufacture = d
##
##    def getEngineNo(self):
##        return self.__engineNo
##
##    def getDateOfManufacture(self):
##        return self.__dateOfManufacture
##
##a = Engine(d = 2012, e = 492)
##b = Engine(625)
##print(f"a: Engine Number = {a.getEngineNo()}, Date of manufacture = {a.getDateOfManufacture()}")
##print(f"b: Engine Number = {b.getEngineNo()}, Date of manufacture = {b.getDateOfManufacture()}")


#### Q8
##class Int:
##    def __init__(self, i = 0):
##        try:
##            self.__i = int(i)
##        except ValueError:
##            print("Invalid value for integer.")
##            del self
##            
##    def setValue(self, i=0):
##        self.__init__(i)
##
##    def getValue(self):
##        return self.__i
##
##    def displayValue(self):
##        print(self.__i)
##
##    def add(self, a):
##        return Int(self.__i + a.getValue())
##
##x = Int()
##y = Int("32")
##z = Int(-5)
##
##x = y.add(z)
##x.displayValue()


#### Q9
##class TollBooth:
##    def __init__(self):
##        self.__numCars = 0
##        self.__moneyCollected = 0
##
##    def payingCar(self):
##        self.__numCars += 1
##        self.__moneyCollected += 50
##
##    def nopaycar(self):
##        self.__numCars += 1
##
##    def display(self):
##        print(f"Cars passed: {self.__numCars}, Cash collected: {self.__moneyCollected}")
##
##TollBooth_x = TollBooth()
##import keyboard
##while 1:
##    inp = input("Press 1 to count paying car, 2 to count nonpaying car, 0 to exit: ")
##    if inp == "1":
##        TollBooth_x.payingCar()
##    elif inp == "2":
##        TollBooth_x.nopaycar()
##    elif inp == "0":
##        TollBooth_x.display()
##        print()
##        break
##    else:
##        print("Invalid input")
##    print()     
    
        
#### Q10
##class Time:
##    def __init__(self, hours=0, minutes=0, seconds=0):
##        if any((type(seconds) != int, type(minutes) != int, type(hours) != int)):
##            raise ValueError("Time values can only be ints")
##        else:
##            self.__seconds = int(seconds) % 60
##            self.__minutes = ((seconds // 60) + int(minutes)) % 60
##            self.__hours = ((minutes // 60) + int(hours)) % 24
##            
##
##    def displayTime(self):
##        print(f"{self.__hours:02}:{self.__minutes:02}:{self.__seconds:02}")
##
##    def addTime(self, t):
##        if not isinstance(t, Time):
##            raise ValueError("Can not add non-Time type object to Time type object")
##        self.__seconds += t._Time__seconds
##        self.__minutes += (self._Time__seconds // 60) + t._Time__minutes
##        self.__hours += (self._Time__minutes // 60) + t._Time__hours
##        self.__seconds %= 60
##        self.__minutes %= 60
##        self.__hours %= 24
##        
##t1 = Time(23, 59,25)
##t1.displayTime()
##
##t2 = Time(61,5,45)
##t2.displayTime()
##
##t1.addTime(t2)
##t1.displayTime()


## Q11
##In ocean navigation, locations are measured in degrees and minutes of latitude and longitude.
##Thus if you’re lying off the mouth of Papeete Harbor in Tahiti, your location is 149 degrees 34.8
##minutes west longitude, and 17 degrees 31.5 minutes south latitude. This is written as 149°34.8’ W,
##17°31.5’ S. There are 60 minutes in a degree (an older system also divided a minute into 60 seconds,
##                                              but the modern approach is to use decimal minutes instead).
##Longitude is measured from 0 to 180 degrees, east or west from Greenwich, England, to the international
##dateline in the Pacific. Latitude is measured from 0 to 90 degrees, north or south from the equator to
##the poles. Write code to create a class Angle that includes three member variables: int for degrees, a
##float for minutes, and a char for the direction letter (N, S, E, or W). This class can hold either a latitude
##variable or a longitude variable. Write one method to obtain an angle value (in degrees and minutes) and a direction
##from the user, and a second to display the angle value in 179°59.9’ E format. Also write a three-argument constructor.
##Write a main program that displays an angle initialized with the constructor, and then, within a loop, allows the user
##to input any angle value, and then displays the value. You can use the hex character constant ‘\xF8’, which usually
##prints a degree (°) symbol.


#### Q12
##class Tracker:
##    count = 0
##    def __init__(self):
##        Tracker.count += 1
##        self.__serialNo = Tracker.count
##        
##    def tellSerialNo(self):
##        print(f"I am object number {self.__serialNo}")
##
##a = Tracker()
##b = Tracker()
##c = Tracker()
##a.tellSerialNo()
##b.tellSerialNo()
##c.tellSerialNo()


## Q13
