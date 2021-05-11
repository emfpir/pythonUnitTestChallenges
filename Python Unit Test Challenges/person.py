import unittest
# write a person class that has the instance variables of name and age
# implement __init__ with the default argument for age as -1
# implement __str__ to give name and age in the following format 'Bill, 40 years old'
# additionally make a class variable that keeps track of the amount of people created

class Person:
    amount=2
    # __str__ = "{self.name}, {self.age} years old".format(self=self)

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return "{self.name}, {self.age} years old".format(self=self)




########################### TESTS ##############################################################
class TestMethods(unittest.TestCase):

    def test_adam(self):
        adam = Person('Adam',19)
        self.assertEquals(adam.__str__(), 'Adam, 19 years old')

    def test_richard(self):
        richard = Person('Richard',22)
        # richard.__str__()
        self.assertEquals(richard.__str__(), 'Richard, 22 years old')

    def test_amount(self):
        self.assertEquals(Person.amount, 2)


if __name__ == '__main__':
    unittest.main()