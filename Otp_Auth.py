import os
import math
import random
import smtplib

def get_otp():
    digits = '0123456789'
    OTP = ''

    for i in range(6):

        print(i)

        OTP += digits[math.floor(random.random()*10)]

    otp = OTP + ' is your current OTP'
    msg = otp

    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()
    s.login('Paynedestinne@gmail.com', 'Ruweidah1')

    emailid = input('Please key in your email: ')
    s.sendmail('&&&&&&&&&&&', emailid, msg)

    a = input('Enter your OTP: ')

    if a == OTP:

        print('OTP has been verified!')

    else:

        print('Oops Incorrect OTP!')

class Pet:

    def __init__(self, age, height, appearance):

        self.names = []
        self.age = age
        self.height = height
        self.appearance = appearance

    def name(self) -> list:

        list1 = self.names

        list1.append('Destinne')

        return list1


class cat(Pet): # inheritance at its best!
    
    def jina(self, jina):

        self.jina = jina

    def currently_named(self) -> str:

        if self.jina in self.names:

            pass

        else:

            print(self.names.append(self.jina))

        return  self.names



    def illness(self):

        if self.age >= 20:

            print(f'{self.age} is above the limit for sickness!')

        else:

            print(f'{self.age} is not above the limit for the sickness!')
    
    def sound(self) -> str:

        return 'meow'


class dog(Pet):

    def jina(self, jina):

        self.jina = jina

    def currently_named(self) -> str:

        if self.jina in self.names:

            pass
        
        else:

            print(self.names.append(self.jina))

        return self.name

    def illness(self):

        if self.appearance == 'Light':

            print(f'{self.age} is good age. The pet cant be sick!')
        
        else:

            print(f'the pet is super sick!')




a = Pet(10, 20, 'light')
c = cat(10, 30, 'Light')
g = dog(10, 30, 'Dark')
d = c.illness()
e = c.sound()
f = c.currently_named()
h = g.jina('destinne')
print(h)
print(e)
b = a.name()
print(b)
print() # the print function here skipps a line