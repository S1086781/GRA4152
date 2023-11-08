#Due to the complexity of the class instead of documenting with argparse, I created a txt file - appointment_docstring.txt - to document the details of the class.

def appointment_test():

    from appointment import Appointment, Monthly, Onetime, Daily

    Onetime("See the dentist", 2023, 11, 7)
    Daily("Stand-up meeting", 2023, 1, 1)
    Monthly("Pay the rent", 2023, 1, 5)
    Monthly("Yoga class", 2023, 1, 15)
    Daily("Playing chess", 2023, 9, 13)

    Appointment.getAppointments(2023,10,5)

    print('Expected:\nAppointments on 2023-10-05:\nAppointment: Stand-up meeting\nAppointment: Pay the rent\nAppointment: Playing chess')

appointment_test()
