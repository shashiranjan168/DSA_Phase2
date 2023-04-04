#selection sort
A = [64, 25, 12, 22, 11]
for i in range(len(A)):
    min_index = i
    for j in range(i+1, len(A)):
        if A[min_index] > A[j]:
            min_index = j       
    A[i], A[min_index] = A[min_index], A[i]
print ("Sorted array")
for i in range(len(A)):
    print(A[i],end=" ")

#question fruits
 #   
'''Write a python program to implement the class diagram given below.

RULES TO FOLLOW
=================
Class Description:
Fruit Info class:
fruit_name_list: Static list which contains the list of fruits available
fruit_price_list: Static list which contains the price/kg of fruits
The above two lists have one-to-one correspondence, initialize it with the data given in the table
get_fruit_price(fruit_name): Accept a fruit name and return its price/kg. If fruit is not available, return -1

Fruit Name	Apple	Guava	Orange	Grape	Sweet Lime
Price per Kg	200	80	70	110	60Purchase class:
Initialize static variable counter to 101
calculate_price(): Calculate and return total fruit price based on rules given below
For valid fruit name (hint: invoke get_fruit_price(fruit_name)),
Calculate price based on price/kg and quantity of the fruit purchased by the customer
If price/kg of the fruit is maximum among the fruits in fruit lists and quantity purchased is more than 1kg, apply 2% discount on calculated price
If price/kg of the fruit is minimum among the fruits in fruit lists and quantity purchased is 5kg or more, apply 5% discount on calculated price
If the customer is a "wholesale" customer, provide an additional 10% discount. Apply this discount on already discounted price, 
if any one of the above two points are applicable. Else apply it on calculated price
Auto-generate purchase id starting from 101 prefixed by “P”. Example – P101,P102 P103 etc.
Return final fruit price
Else, return -1.
Note:
Perform case sensitive string comparison 
There will be only one fruit with maximum price and one with minimum price

For testing:
Create objects of Customer and Purchase class
Invoke calculate_price() on Purchase object
Display the details'''



#Bake house
'''The owner of a BakeHouse wants to keep track of the tables 
that are occupied in his cafe. Assume that there are 10 tables in his cafe numbered from 1 to 10. As and when a table is occupied, it must be added to the occupied_table_list and when a customer leaves, the corresponding table must be removed from the list.

BakeHouse
- occupied_table_list
_init_()
+ get_occupied_table_list()
+ allocate_table()
+ deallocate_table(table_number)
Write a python program to implement BakeHouse class. 
Represent occupied_table_list using an appropriate data 
structure.


Note: Table numbers should be maintained in ascending order in the occupied_table_list.


Tables should be allocated and de-allocated as mentioned in the example below:

Example: Suppose tables 1, 2, 3 and 4 are initially allocated. Now if a new customer arrives, he should be allocated table 5 and the table list should be accordingly updated. If now customer at table 2 leaves, table list should be accordingly updated and the next new customer should be allocated table 2 as it is the first free table.


Implement the allocation logic in allocate_table() method and de-allocation logic in deallocate_table() method.
-------------------------------------------------------
10.Write a python program to reverse a linked list containing 
integer data.
Use the LinkedList class and methods in it to implement the
 above program.'''
#solution
class Bakehouse:
    def __init__(self,occupied_table,allocate_table,deallocate_table):
        self.occupied_table= occupied_table
        self.allocate_table=allocate_table
        self.delocate_table=delocate_table

    def occupied_table_list(self,data):
        
    

# employee
"""Softsytems Ltd is a private firm that provides software solutions to its customers.40 min
The management wants to calculate salary for the employees. There are two types of employees namely graduates 
who are in probation period and laterals who are experienced joiners in the company. 
Write a python program based on the class diagram given below.

RULES TO FOLLOW
===================
Class Description:
Employee class:
validate_basic_salary(): Basic salary of an employee is always more than 3000
If basic salary is valid, return true. Else return false
validate_qualification(): Employee should posses either a "Bachelors" or "Masters" degree
If qualification is valid, return true. Else return false
Graduate class:
validate_job_band(): Graduates can be in "A", "B" or "C" job band
If job band is valid, return true. Else return false
calculate_gross_salary(): Calculate gross salary
Validate basic salary, qualification and job band
If valid,
Compute gross salary as basic salary + PF+ TPI amount + incentive
    PF is 12% of basic salary
    Identify TPI amount based on cgpa
    Identify incentive based on job band. Incentive should be applied on basic
    salary (Refer tables given)
Return gross salary
Else return -1
Job Band	A	B	C	D	E	F
Incentive %	4	6	10	13	16	20

CGPA	4 to 4.25	4.26 to 4.5	4.51 to 4.75	4.76 to 5
TPI Amount	1000	1700	3200	5000
Lateral class:
validate_job_band(): Laterals can be in "D", "E" or "F" job band
If job band is valid, return true. Else return false
calculate_gross_salary(): Calculate gross salary
Validate basic salary, qualification and job band
If valid,
Compute gross salary as basic salary + PF + SME bonus + incentive
    PF is 12% of basic salary
    Identify SME bonus based on skill set
    Identify incentive based on job band. Incentive should be applied on basic salary (Refer
    tables given)
Return gross salary
Skill Set	SME Bonus
AGP	        6500
AGPT	        8200
AGDEV	        11500
Else return -1
Perform case sensitive string comparison.
For testing:
Create objects of Graduate and Lateral classes
Invoke calculate_gross_salary() on Graduate and Lateral objects
Display the details"""
#solution
class Employee:
    def __init__(self, basic_salary, qualification):
        self.basic_salary = basic_salary
        self.qualification = qualification
        
    def validate_basic_salary(self):
        if self.basic_salary > 3000:
            return True
        else:
            return False
        
    def validate_qualification(self):
        if self.qualification == "Bachelors" or self.qualification == "Masters":
            return True
        else:
            return False


class Graduate(Employee):
    def __init__(self, basic_salary, qualification, job_band, cgpa):
        super().__init__(basic_salary, qualification)
        self.job_band = job_band
        self.cgpa = cgpa
        
    def validate_job_band(self):
        if self.job_band == "A" or self.job_band == "B" or self.job_band == "C":
            return True
        else:
            return False
        
    def calculate_gross_salary(self):
        if self.validate_basic_salary() and self.validate_qualification() and self.validate_job_band():
            pf = 0.12 * self.basic_salary
            
            if 4 <= self.cgpa <= 4.25:
                tpi = 1000
            elif 4.26 <= self.cgpa <= 4.5:
                tpi = 1700
            elif 4.51 <= self.cgpa <= 4.75:
                tpi = 3200
            elif 4.76 <= self.cgpa <= 5:
                tpi = 5000
            
            if self.job_band == "A":
                incentive = 0.04 * self.basic_salary
            elif self.job_band == "B":
                incentive = 0.06 * self.basic_salary
            elif self.job_band == "C":
                incentive = 0.1 * self.basic_salary
                
            gross_salary = self.basic_salary + pf + tpi + incentive
            return gross_salary
        else:
            return -1


class Lateral(Employee):
    def __init__(self, basic_salary, qualification, job_band, skill_set):
        super().__init__(basic_salary, qualification)
        self.job_band = job_band
        self.skill_set = skill_set
        
    def validate_job_band(self):
        if self.job_band == "D" or self.job_band == "E" or self.job_band == "F":
            return True
        else:
            return False
        
    def calculate_gross_salary(self):
        if self.validate_basic_salary() and self.validate_qualification() and self.validate_job_band():
            pf = 0.12 * self.basic_salary
            
            if self.skill_set == "AGP":
                sme_bonus = 6500
            elif self.skill_set == "AGPT":
                sme_bonus = 8200
            elif self.skill_set == "AGDEV":
                sme_bonus = 11500
                
            if self.job_band == "D":
                incentive = 0.13 * self.basic_salary
            elif self.job_band == "E":
                incentive = 0.16 * self.basic_salary
            elif self.job_band == "F":
                incentive = 0.2 * self.basic_salary
                
            gross_salary = self.basic_salary + pf + sme_bonus + incentive
            return gross_salary
        else:
            return -1



