x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
#solution
x[1][0]=15
students[0]['last_name'] = 'Bryant'

sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30
#################################

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


#2
def key_and_value(arr):
    for i in arr:
        print(i)

key_and_value(students)

#3
def iterate_dictionary(arr, key):
    for i in arr:
        print(i[key])

iterate_dictionary(students,'first_name')

#4
def dojo_info(arr):
    print((len(arr['locations'])), "LOCATIONS", (arr['locations']))
    print((len(arr['instructors'])), "INSTRUCTORS", (arr['instructors']))

dojo_info(dojo)