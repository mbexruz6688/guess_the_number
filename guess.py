import random
def give_a_num():
    return random.randrange(50, 100)
def get_num():
    return int(input("Sonni taxmin qilib ko'ring: "))
def num_is_biger():
    print(f"Random number{son}is bigger")
def num_is_smaller():
    print(f"Random number{son}is smaller")
def num_is_detected():
    print("You win!")
a = give_a_num()
while True:
    son = get_num()
    if son < a:
        num_is_bigger()
    elif son > a:
        num_is_smaller()
    else:
        num_is_detected()
        break
