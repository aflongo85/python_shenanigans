
from Room import Room


room_one = Room("ONE", 3, 50)
room_two = Room("TWO", 4, 70)
room_three = Room("THREE", 3, 50, False, False)


room_one.info()
room_one.book(30)
room_one.pay(400)

room_three.info()
room_three.book(9)
room_three.info()

room_one.customer = "Andrea"

print(room_one.customer)
#room_three.charge(500)



