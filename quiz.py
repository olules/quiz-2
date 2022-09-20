import numpy as np
class Sensor():
    def __init__(self, name, location, record_date):
        self.name = name
        self.location = location
        self.record_date = record_date
        self.data = {}

    def add_data(self, t, data):
        self.data['time'] = t
        self.data['data'] = data
        print(f'We have {len(data)} points saved')

    def clear_data(self):
        self.data = {}
        print('Data cleared!')


sensor1 = Sensor('sensor1', 'Berkeley', '2019-01-01')
data = np.random.randint(-10, 10, 10)
sensor1.add_data(np.arange(10), data)
sensor1.data


class Accelerometer(Sensor):

    def show_type(self):
        print('I am an accelerometer!')


acc = Accelerometer('acc1', 'Oakland', '2019-02-01')
acc.show_type()
data = np.random.randint(-10, 10, 10)
acc.add_data(np.arange(10), data)
acc.data

#encpsulation: Encapsulation is one of the fundamental concepts in OOP. 
# It describes the idea of restricting access to methods and attributes in a class. 
# This will hide the complex details from the users, and prevent data being modified by accident. 
# In Python, this is achieved by using private methods or attributes using underscore as prefix, 
# i.e. single “_” or double “__”. Let us see the following example.



class Sensor():
    def __init__(self, name, location):
        self.name = name
        self._location = location
        self.__version = '1.0'

    # a getter function
    def get_version(self):
        print(f'The sensor version is {self.__version}')

    # a setter function
    def set_version(self, version):
        self.__version = version
