# 1Q Create an assignment for File handling of JSON files in Python

import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

# Create the JSON file
employees_data = [
    {
        "Name": "neha",
        "DOB": "2001-06-26",
        "Height": 175,
        "City": "vijayawada",
        "State": "andhra pradesh"
    },
    {
        "Name": "yamika",
        "DOB": "1993-05-20",
        "Height": 160,
        "City": "jubilee hills",
        "State": "hyderabad"
    },
    {
        "Name": "ramya",
        "DOB": "2001-03-10",
        "Height": 150,
        "City": "kukatpally",
        "State": "hyderabad"
    },
    {
        "Name": "prahlad",
        "DOB": "1988-11-30",
        "Height": 170,
        "City": "hitech",
        "State": "hyderabad"
    },
    {
        "Name": "vineeth",
        "DOB": "1994-07-05",
        "Height": 178,
        "City": "banjara hills",
        "State": "hyderabad"
    }
]

with open('E:/employee_json.json', 'w') as json_file:
    json.dump(employees_data, json_file)

# Read the JSON file and save information into a list of objects
employees = []

with open('E:/employee_json.json', 'r') as json_file:
    employees_data = json.load(json_file)
    
    for employee_data in employees_data:
        name = employee_data['Name']
        dob = employee_data['DOB']
        height = employee_data['Height']
        city = employee_data['City']
        state = employee_data['State']
        
        employee = Employee(name, dob, height, city, state)
        employees.append(employee)

# Print the list of Employee objects 
for employee in employees:
    print(employee.__dict__)

# 2Q Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.

import json

states = {
    'andhra pradesh': 'hyderabad',
    'gujarat': 'ganhinagar',
    'karnataka': 'bengalore',
    'maharashtra': 'mumbai',
    'rajasthan': 'jaipur',
    'tamil nadu': 'chennai',
    'uttra prades': 'lucknow' 
}    
#write the following dict to a jsno file
with open('E:/indian_states.json','w') as file:
    json.dump(states,file)
print('json file created successfully!')


# 3Q  Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:

class dog:
    def __init__(self,name,age,coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    def description(self):
        print('name:'+self.name)
        print('age:',self.age)
    def get_info(self):
        print('coat_color:'+self.coat_color)

class jackrussellterrier(dog):
    def __init__(self,name,age,coat_color,capacity):
        dog.__init__(self,name,age,coat_color)
        self.capacity = capacity
    def fetch(self):
        print(self.name +" is fetching")
class bulldog(dog):
    def __init__(self,name,age,coat_color,intelligence):
        dog.__init__(self,name,age,coat_color)
        self.intelligence = intelligence
    def snore(self):
        print(self.name +' is snoring')
#create objects
name = input('enter the dog name: ')
age = int(input('enter the age of the dog: '))
coat_color = input('enter the coat color: ' )
name_2 = input('enter the dog name: ')
age_2 = int(input('enter the dog age: '))
coat_color_2 = input('enter the coat color: ')
capacity = input('enter the dog capacity: ')
name_3 = input('enter the dog name: ')
age_3 = int(input('enter the dog age: '))
coat_color_3 = input('enter the coat color: ')
intelligence = input('enter the dogs intelligence level:')
dog_1 = dog(name,age,coat_color) 
jack = jackrussellterrier(name_2,age_2,coat_color_2,capacity)
bulldog_1 = bulldog(name_3,age_3,coat_color_3,intelligence)
#call methods
dog_1.description()
dog_1.get_info()
jack.description()
jack.get_info()
jack.fetch()

bulldog_1.description()
bulldog_1.get_info()
bulldog_1.snore()