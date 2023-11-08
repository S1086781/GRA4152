#In the Appointment class different kinds of appointments can be created. Onetime, Daily and Monthly appointments are the subclasses of the appointment class. The user can check for a certain day which appointments are scheduled. Furthermore, all scheduled appointments can be saved to a csv file and loaded from a csv file.

#datetime library is necessary to manage the date of appointments
from datetime import date

#creating the superclass appointment
class Appointment:
    #the class variable appointments is created to store all appointments and helps to write out the appointments to a csv file.
    appointments=[]

    #In the constructor 2 instance variables are created: description and date. And the objects are appended to the classs variable.
    #@params: -description: short description of the appointment, -year: year of the appointment, -month: month of the appointment, day: - day of the appointment
    def __init__(self, description, year, month, day):
        self._description = description
        self._date = date(year, month, day)
        Appointment.appointments.append(self)

    
    #The occursOn method takes in a date and decides whether a certain appointment is scheduled on that date. This method returns a boolean variable. Later in the subclasses of Appointment class this method is overridden.
    #@params: -year: the year that the user wants to check appointments, -month: the month that the user wants to check appointments, -day: The day that the user wants to check appointments
    def occursOn(self, year, month, day):
        return self._date == date(year, month, day)
    
    #This method is created to support the saving of the objects of the class. Implementation are different for the subclasses.
    def __repr__(self):
        raise NotImplementedError
    
    #This method supports printing the parameters of a given appointment
    def __str__(self):
        return f"Appointment: {self._description}"

    #This class method prints the appointments on a given date
    #@params: -year: the year that the user wants to check appointments, -month: the month that the user wants to check appointments, -day: The day that the user wants to check appointments
    @classmethod
    def getAppointments(cls, year, month, day):
        print(f"Appointments on {date(year, month, day)}:")
        for appointment in Appointment.appointments:
            if appointment.occursOn(year, month, day):
                print(appointment)

    #This class method saves all created appointments to a csv file with the help of repr method.
    #@params: -filename: the name of the file the user wants to save. default name: appointment.csv
    @classmethod
    def save(cls, filename='appointment.csv'):
        with open(filename, 'w') as file:
            for i in Appointment.appointments:
                file.write(repr(i))

    #This class method loads and creates instances from a csv file.
    #@params: -filename: the name of the csv file that the user wants to load.
    @classmethod
    def load(cls, filename):
        with open(filename) as file:
            lines=file.readlines()
            #string operations to get class type, description and date parameters
            for line in lines:
                splittedline=line.split(',')
                CLASS=splittedline[0]
                description=splittedline[1]
                datelist=splittedline[2].split('-')
                year=int(datelist[0])
                month=int(datelist[1])
                day=int(datelist[2])
            
                #creates an instance with the loaded parameters
                if CLASS in globals():
                    class_ = globals()[CLASS]
                    instance = class_(description, year, month, day)

#Class Onetime is a subclass of Appointment. This class inherits from Appointment and some methods are overridden
class Onetime(Appointment):

    #Inheritence form the superclass
    def __init__(self, description, year, month, day):
        super().__init__(description, year, month, day)

    #Not neccessary to override occursOn method

    #Repr method is overridden to save the class name.
    def __repr__(self):
        return f"Onetime, {str(self._description)+', '+str(self._date)}"+'\n'

class Daily(Appointment):
    #Inheritence form the superclass
    def __init__(self, description, year, month, day):
        super().__init__(description, year, month, day)

    #occursOn method is overridden. The output is true for all days after the starting day of the appointment.
    def occursOn(self, year, month, day):
        if date(year, month,day)>= self._date:
            return True
        else:
            return False
        
    #repr method is overridden to save the class name.
    def __repr__(self):
        return f"Daily, {str(self._description)+', '+str(self._date)}"+'\n'

class Monthly(Appointment):
    #Inheritence form the superclass
    def __init__(self, description, year, month, day):
        super().__init__(description, year, month, day)

    #occursOn method is overridden. Checks only for the day parameter in the case of monthly appointment
    def occursOn(self, year, month, day):
        return self._date.day == day
    
    #repr method is overridden to save the class name.
    def __repr__(self):
        return f"Monthly, {str(self._description)+', '+str(self._date)}"+'\n'

