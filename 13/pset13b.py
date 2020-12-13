# TAKEN FROM REDDIT, BECAUSE I KNOW NOTHING ABOUT THE CHINESE REMAINDER THEOREM

from functools import reduce

def main():
    with open("input.txt", "r") as f:
        rawinput = f.read().splitlines()
        
    rawinputlist = rawinput[1].split(',')
    input = []
    for i in rawinputlist:
        if i == 'x':
            input.append(0)
        else:
            input.append(int(i))

    buses = []
    a = []
    for i, bus in enumerate(input):
        if bus == 0:
            continue
        buses.append(bus)
        a.append((- i) % bus)
    
    print(chinese_remainder(buses, a))

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod



def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
 
 
 
if __name__ == '__main__':
    main()