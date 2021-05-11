import unittest
# write a method that takes in a sales tax as the first argument
# then takes in varargs of tuples with the name of the item and its base cost
# it should return a list of dictionaries ordered by cost descending
# purchases(10,('shoes',15),('apple',1),('stapler',11))
# -> [{'item':'shoes','base':15,'taxed':16.50},
# {'item':'stapler','base':11,'taxed':12.10},
# {'item':'apple','base':1,'taxed':1.10}]



def purchases(tax,*items):
    temp_list = []
    list_holder = []
    expected = []
    if(len(str(tax))==1):
        new_tax = float("0.0"+str(tax))
    else:
        new_tax = float("0."+str(tax))
    for x in items:
        temp_list.append(x[1])
    temp_list.sort(reverse=True)
    for y in temp_list:
        for x in items:
            if(x[1]==y):
                dictionary_holder = {}
                dictionary_holder.update({x[0]:x[1]})
                list_holder.append(dictionary_holder)
    for x in list_holder:
        for y in items:
            dict_temp = {y[0]:y[1]}
            if(x==dict_temp):
                final_tax = y[1] * new_tax + y[1]
                expected.append({'item': y[0], 'base': y[1], 'taxed': final_tax})
    return expected


########################### TESTS ##############################################################
class TestMethods(unittest.TestCase):

    def test_add_1(self):
        result = purchases(5,('soda',12),('pop rocks',2),('steak',35))
        expected = [
        {'item':'steak','base':35,'taxed':36.75},
        {'item':'soda','base':12,'taxed':12.6}, 
        {'item':'pop rocks','base':2,'taxed':2.1}
        ]
        self.assertListEqual(result,expected)

    def test_add_2(self):
        result = purchases(15,('ginger ale',12),('ice cream',9),('pork chops',21))
        expected = [
        {'item':'pork chops','base':21,'taxed':24.15},
        {'item':'ginger ale','base':12,'taxed':13.8}, 
        {'item':'ice cream','base':9,'taxed':10.35}
        ]
        self.assertListEqual(result,expected)


if __name__ == '__main__':
    unittest.main()