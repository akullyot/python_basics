#First: give an indication youre inside the file
print('hello from inside setup')

#function that prints hello
def hello():
    print('Hi, User!')

#function that takes any number of arguments and returns them as a list. I know it said 3 but generalizing seemed like a fun idea
def pack(*args):
    list = []
    for arg in args:
        list.append(arg)
    return list

#function that accepts a list of foods and prints out what one ate in the order of the list
def eat_lunch(food_list):
    if len(food_list) == 0:
        print('My lunchbox is empty!')
    else:
        for index in range(len(food_list)):
            if index == 0:
                print(f"First I eat {food_list[index]}")
            else:
                print(f"Next I eat {food_list[index]}")


#Tests
hello()

print(pack(1,"a string",3,4,5,None, {'key': 'value'},7))
print(pack('one', 'two', 'three'))

print(eat_lunch([]))
print(eat_lunch(['haggis']))
print(eat_lunch(['apple', 'banana', 'mango']))

        

