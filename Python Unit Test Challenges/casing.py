import unittest
# write a function that convernts a word into different casings
# assume no spacing
# snake_case example fire_truck OR Fire_Truck  (capitalization does not matter)
# camelCase example fireTruck
# PascalCase example FireTruck
# kebab-case example fire-truck

# casing('registeredUser','camelCase','kebab-case') -> registered-user
def casing(word, initial, target):
    word2=""
    count=0
    if initial=='camelCase' and target=='PascalCase':
        word = word[0:1].upper()+word[1:]
        return word
    elif initial=='camelCase' and target=='kebab-case':
        for x in word:
            if x.isupper():
                word2+="-"+x.lower()
            else:
                word2+=str(x)
        return word2
    elif initial=='camelCase' and target=='snake_case':
        for x in word:
            if x.isupper():
                word2+="_"+x
            else:
                word2+=x
        return word2
    elif initial=='PascalCase' and target=='snake_case':
        for x in word:
            if x.isupper() and count !=0:
                word2+="_"+x
            else:
                word2+=x
            count+=1
        return word2
    elif initial=='PascalCase' and target=='kebab-case':
        count=0
        for x in word:
            if x.isupper() and count==0:
                word2+=x.lower()
            elif x.isupper() and count!=0:
                word2+="-"+x.lower()
            else:
                word2+=x
            count+=1
        return word2
    elif initial=='PascalCase' and target=='camelCase':
        count=0
        for x in word:
            if x.isupper() and count==0:
                word2+=x.lower()
            else:
                word2+=x
            count+=1
        return word2
    elif initial=='kebab-case' and target=='camelCase':#initial==green-apple ;;solution==greenApple
        count=0
        for x in word:
            if x=='-':
                count=1
            elif count==1:
                word2+=x.upper()
                count=0
            else:
                word2+=x
        return word2
    elif initial=='kebab-case' and target=='PascalCase':#initial==green-apple ;;solution==GreenApple
        count=0
        for x in word:
            if x=='-':
                count=0
            elif count==0:
                word2+=x.upper()
                count=1
            else:
                word2+=x
            # count+=1
        return word2
    elif initial=='kebab-case' and target=='snake_case':#initial==green-apple ;;solution==green_Apple
        count=1
        for x in word:
            if x=='-':
                word2+='_'
                count=0
            elif count==0:
                word2+=x.upper()
                count=1
            else:
                word2+=x
        return word2
    elif initial=='snake_case' and target=='camelCase':#initial==green_apple ;;solution==greenApple
        count=0
        for x in word:
            if x=='_':
                count=1
            elif count==1:
                word2+=x.upper()
                count=0
            else:
                word2+=x
        return word2
    elif initial=='snake_case' and target=='PascalCase':#initial==green_apple ;;solution==GreenApple
        count=1
        for x in word:
            if x=='_':
                count=1
            elif count==1:
                word2+=x.upper()
                count=0
            else:
                word2+=x
        return word2
    elif initial=='snake_case' and target=='kebab-case':#initial==green_apple ;;solution==green-apple
        for x in word:
            if x=='_':
                word2+='-'
            else:
                word2+=x
        return word2
    else:
        return "issues happened"

########################### TESTS ##############################################################
class TestMethods(unittest.TestCase):

    def test_camel_to_Pascal(self):
        result = casing(word='redSphere',initial='camelCase',target='PascalCase')
        self.assertEquals(result,'RedSphere')

    def test_camel_to_kebab(self):
        result = casing('redSphere','camelCase','kebab-case')
        self.assertEquals(result,'red-sphere')

    def test_camel_to_snake(self):
        result = casing('redSphere','camelCase','snake_case')
        self.assertEquals(result,'red_Sphere')

    def test_Pascal_to_snake(self):
        result = casing('GreenApple','PascalCase','snake_case')
        self.assertEquals(result,'Green_Apple')

    def test_Pascal_to_kebab(self):
        result = casing('GreenApple','PascalCase','kebab-case')
        self.assertEquals(result,'green-apple')

    def test_Pascal_to_camel(self):
        result = casing('GreenApple','PascalCase','camelCase')
        self.assertEquals(result,'greenApple')

    def test_kebab_to_camel(self):
        result = casing('green-apple','kebab-case','camelCase')
        self.assertEquals(result,'greenApple')

    def test_kebab_to_Pascal(self):
        result = casing('green-apple','kebab-case','PascalCase')
        self.assertEquals(result,'GreenApple')

    def test_kebab_to_snake(self):
        result = casing('green-apple','kebab-case','snake_case')
        self.assertEquals(result,'green_Apple')


    def test_snake_to_camel(self):
        result = casing('green_apple','snake_case','camelCase')
        self.assertEquals(result,'greenApple')

    def test_snake_to_Pascal(self):
        result = casing('green_apple','snake_case','PascalCase')
        self.assertEquals(result,'GreenApple')

    def test_snake_to_kebab(self):
        result = casing('green_apple','snake_case','kebab-case')
        self.assertEquals(result,'green-apple')

if __name__ == '__main__':
    unittest.main()