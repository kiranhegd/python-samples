num=int(input("enter a number"))

if num > 1:

  for i in range(2,num):
    if(num % i)== 0:
        print(num,"it is not a prime number")

        print(i,"times", num//i, "is", num)
        break

    else:
        print("its a prime number")

else:
    print("its not a prime number")