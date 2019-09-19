class Person(object):
    def __init__(self, person_name):
        self.name = person_name

    def say_hello(self):
        print("Hi, everyone! My name is {}! I am 23 years old and happy".format(self.name))


Jibryll = Person("Jibryll")

Jibryll.say_hello()
