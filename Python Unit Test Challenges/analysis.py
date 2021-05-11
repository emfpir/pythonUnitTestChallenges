import unittest

# the analyze function takes in an var argument of numbers
# it should return a dictionary of {'mean':0,'median':0,'mode':0,'largest':0,'smallest':0}
def mean(list):
    temp_number = 0
    for x in list:
        temp_number+=x
    return {"mean":int(temp_number/len(list))}

def median(list):
    list.sort()
    # print(list)
    median_number=0
    if len(list)%2==0:
        length_half = int(len(list)/2)
        number1= list[(length_half-1)]
        number2= list[(length_half)]
        median_number=(number1+number2)/2.0
    else:
        median_number=list[int((len(list)+1)/2.0)-1]
    return {'median':median_number}

def mode(list):
    highest_count=0
    mode_number = None
    mode_list = []
    for x in list:
        if list.count(x)>highest_count:
            mode_number=x
            highest_count=list.count(x)
    mode_list.append(mode_number)
    for x in list:
        if list.count(x)==highest_count and not mode_number==x:
            mode_list.append(x)
    if(len(mode_list)>1):
        return {'mode':mode_list}
    else:
        return {'mode':mode_number}

def largest(list):
    list.reverse()
    return {'largest':list[0]}

def smallest(list):
    list.sort()
    return {'smallest': list[0]}

#return type must be dictionary
def analyze(*num):
    list = []
    for x in num:
        #check every position is equal to int before adding to the list
        if type(x)==type(1):
            list.append(x)
    #call each function for dictionary math formulas
    dictionary_data = mean(list)
    dictionary_data.update(median(list))
    dictionary_data.update(mode(list))
    dictionary_data.update(largest(list))
    dictionary_data.update(smallest(list))
    return dictionary_data
########################### TESTS ##############################################################
class TestMethods(unittest.TestCase):

    def test_analyze_1(self):
        data = analyze(1,2,2,2,3)
        self.assertDictEqual(data, {'mean':2,'median':2,'mode':2, 'largest':3,'smallest':1})

    def test_analyze_2(self):
        data = analyze(10,5,10,200,-65)
        self.assertDictEqual(data, {'mean':32,'median':10,'mode':10, 'largest':200,'smallest':-65})

if __name__ == '__main__':
    unittest.main()
