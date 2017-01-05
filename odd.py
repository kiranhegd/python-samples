def odd_occur(arr):
    result=0
    for element in arr:
        result= result ^ element

        return(result)

    num1=[4,5,4,5,2,2,2,3,5,6]

    print(odd_occur(num1))