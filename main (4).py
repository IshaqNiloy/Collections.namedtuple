# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
def print_average(my_list):
    total = 0
    for i in range(len(my_list)):
        #Getting the value which is stored in the 'MARKS' field and adding them up
        total += int(my_list[i].MARKS)
    #Printing the average(Keeping two digits after the decimal point) 
    print("{:.2f}".format(total/len(my_list)))
    
if __name__ == '__main__':
    #Defining a list to store all the named tuples
    my_list = []
    number_of_students = int(input())
    #Stores the names of the fields
    fields = input()
    for _ in range(number_of_students):
        #Defining the named tuple
        student = namedtuple('Student',fields)
        #Values for the fields of the named tuple
        field1, field2, field3, field4 = input().split()
        #Putting the values in the named tuple
        st = student(field1, field2, field3, field4)
        #Putting the named tuple in a list
        my_list.append(st)
    #Calling the function to print the average
    print_average(my_list)
