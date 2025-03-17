from abc import ABC, abstractmethod

def sum_squares(numbers):
    if not numbers:
        return 0
    else:
        return numbers[0]*numbers[0] + sum_squares(numbers[1:])

def main ():
    n = [3,2,1,5,6,1,8,9]
    suma = sum_squares(n)
    suma2 = 0
    print(suma)

    for  i in n:
        suma2 += i*i

    print(suma2)

if __name__=="__main__":
    main()

