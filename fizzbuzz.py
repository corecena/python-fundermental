X = int(input("enter a number to test"))
def fizz_buzz(input):
    if(input%3==0 & input %5==0 ):
        return "fizz_buzz"
    elif(input%3==0):
        return "fizz"
    elif(input%5==0):
        return "buzz"
    else:
        return input
print(fizz_buzz(X))
def cal_Tax():
    print("from the core oblect")