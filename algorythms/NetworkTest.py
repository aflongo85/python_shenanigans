
# import urllib.request
# contents = urllib.request.urlopen("https://swapi.co/api/people/1").read()
# print(contents)

set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5, 77, 9, 12}

print(set1.intersection(set2))

my_tuple = (20)
print(my_tuple)


mystring = "Andrea, Drew, Tom, Ben"
peoples = mystring.split(",")
people_no_spaces = []
print(peoples)

for person in peoples:
    people_no_spaces.append(person.strip())

print(people_no_spaces)