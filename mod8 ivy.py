def greater_than (x, y):
    if x > y:
        return True
    else:
        return False

a = 2
b = 3

outcome = greater_than(a, b)
print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(outcome))
