#Due to the complexity of the class instead of documenting with argparse, I created a txt file - appointment_docstring.txt - to document the details of the class.
def appointment_load_save_test():
    from appointment import Appointment, Monthly, Onetime, Daily
    Appointment.load('appointment.csv')
    Appointment.save('appointment_save_load_test.csv')


appointment_load_save_test()