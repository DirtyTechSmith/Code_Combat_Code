import math
pi = 3.14159265359
e = 2.718281828459045

def sin(x):
    e = 2.718281828459045
    result = (e ** (x * 1j)).imag
    return result

def cos(x):
    e = 2.718281828459045
    result = (e ** (x * 1j)).real
    return result



if __name__ == "__main__":
    test_num = 5

    test_1 = sin(test_num)
    print(f'fake sin: {test_1}')

    test_2 = math.sin(test_num)
    print(f'sin: {test_2}')


    test_3= cos(test_num)
    print(f'fake cos: {test_3}')

    test_4 = math.cos(test_num)
    print(f'cos: {test_4}')

    print(1j)