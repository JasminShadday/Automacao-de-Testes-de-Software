def fizBuzz(valor):
    if valor % 3 == 0  and valor % 5 == 0:
        return 'FizzBuzz'
    elif valor % 3 == 0:
        return 'Fizz'
    elif valor % 5 == 0:
        return 'Buzz'
    return valor 