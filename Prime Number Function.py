def prime(num):
    if num>1:
        for i in range(2,num):
            if num%i == 0:
                print("Not a Prime Number")
                break
        else:
            print("Prime Number")


n = int(input("Enter a NUmber "))
prime(n)
