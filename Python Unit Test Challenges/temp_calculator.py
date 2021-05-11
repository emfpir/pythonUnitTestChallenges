import unittest
# write a method that allows you to convert the temperature using key word arguments
# example calculate_temp(temp =100, original='C', to="F") -> 212
def calculate_temp(**kwargs):
    if(kwargs["original"]=='C'):
        temp_number = kwargs["temp"]
        temp_number = (temp_number*(9/5))+32
        return temp_number
    else:
        temp_number = kwargs["temp"]
        temp_number = (temp_number-32)*(5/9)
        return temp_number

########################### TESTS ##############################################################
class TestMethods(unittest.TestCase):

    def test_add_1(self):
        result = calculate_temp(temp=100, original='C', to='F')
        self.assertEquals(result,212)

    def test_add_2(self):
        result = calculate_temp(temp=212, original='F', to='C')
        self.assertEquals(result,100)

if __name__ == '__main__':
    unittest.main()