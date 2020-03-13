'''
amount = int(input("enter your amount: " ))
def get_icecream(amount):
    icecream = "vanilla"
    print("your balance is:" , amount - 100)
    return icecream

print(get_icecream(amount))

'''
'''
class Rectangle:
    def __init__(self,length,width):
        print("i am inside constructor")
        self.length = length
        self.width = width
    
    def area(self):
        square_feet = self.length * self.width
        return square_feet
    
    def perimeter(self):
        perimeter_total = (2 * self.length) + (2 * self.width)
        return perimeter_total
        
a = Rectangle(4,4)
print(a.area())
print(a.perimeter())

'''  
'''  
        
class Square:
    def __init__(self,side):
        print("I am inside the constructor")
        self.side = side
    
    def area(self):
        square_feet = self.side * self.side
        return square_feet
    
    def perimeter(self):
        peri = 4 * self.side
        return peri
    
ab = Square(5)
print(ab.area())
print(ab.perimeter())

'''


class Coffee:
      
    def __init__(self, brand_list):
         self.Brand = brand_list
                
    def search(self, brand_to_find):
        if brand_to_find in self.Brand.keys():
            print("got the brand")
            return True
        else:
            print("the brand is not available")
            return False
    
    coffee_brand = input("Enter a brand name:  ")
    def coffee_1(self):
        if self.search(self.coffee_brand) :
            print('This is an', self.coffee_brand)
            print(self.Brand.get(self.coffee_brand))
        else:
            print("No coffee")


# a = Coffee(["Nescafe", "Bru", "Sunrise", "xyz"])
a = Coffee({'Bru':100})
a.coffee_1()
#print(a.Brand)


# # def convert_to_days(month):
# #     x = month * 30
# #     return x

# # print(convert_to_days())


# # convert_to_days = str(input("enter the month"))
# # if convert_to_days == "January":
# #     print("31 days")
# # elif convert_to_days == "February":
# #     print("28 days")
# # elif convert_to_days == "March":
# #     print("31 days")
# # elif convert_to_days == "April":
# #     print("30 days")
# # elif convert_to_days == "May":
# #     print("31 days")
# # elif convert_to_days == "June":
# #     print("30 days")
# # elif convert_to_days == "July":
# #     print("31 days")
# # elif convert_to_days == "August":
# #     print("31 days")
# # elif convert_to_days == "September":
# #     print("30 days")
# # elif convert_to_days == "October":
# #     print("31 days")
# # elif convert_to_days == "November":
# #     print("30 days")
# # elif convert_to_days == "December":
# #     print("31 days")
    

# class marks:
#     def __init__(self, a, b, c, d, e):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#         self.e = e
        
        
#     def marks_obtained(self):
#         total_marks = self.a + self.b + self.c + self.d + self.e
#         return total_marks
    
#     def percentage(self):
#         percentage_of_marks = (self.marks_obtained()/500) * 100
#         return percentage_of_marks

# grade = marks(10, 20, 30, 40, 50)

# print(grade.percentage())


