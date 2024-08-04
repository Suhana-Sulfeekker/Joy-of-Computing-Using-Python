def FizzBuzz(r):
    for i in range(1,r+1):
        if i%3==0 and i%5==0:
            print(str(i)+" Fizzbuzz")
        else:
            if (i%3==0):
                print(str(i)+" Fizz")
            else:
                if (i%5==0):
                    print(str(i)+" Buzz")
                else:
                    print(str(i))

r=int(input("Enter the limit:"))
FizzBuzz(r)
