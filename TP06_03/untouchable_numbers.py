def somme_div(y: int) -> int:
    sum = 0
    for i in range(y-1, 0, -1):
        if y % i == 0:
            sum += i

    return sum

def intouchable(x:int) -> bool:
    for y in range(2, x*x):
        if x == somme_div(y):
            return False

    return True

user_input = -1
while user_input < 0 or user_input > 125:
    user_input = int(input("Entrez un nombre entre 0 et 125 : "))

print("{} est intouchable".format(user_input) if intouchable(user_input) else "{} n'est pas intouchable".format(user_input))