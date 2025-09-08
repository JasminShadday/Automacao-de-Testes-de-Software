#primeiro teste

def fizzbuzz(n):
    return "1"

#segundo teste
def fizzbuzz(n):
    if n == 2:
        return "2"
    return 1

#terceiro teste
def fizzbuzz(n):
    if n == 3:
        return "Fizz"
    if n == 2:
        return "2"
    return 1

#quarto teste
def fizzbuzz(n):
    if n == 4:
        return "4"
    if n == 3:
        return "Fizz"
    if n == 2:
        return "2"
    return 1

# primeira refatoração para o teste 4
def fizzbuzz(n):
    if n == 3:
        return "Fizz"
    return str(n)

# quinto teste
def fizzbuzz(n):
    if n == 5:
        return "Buzz"
    if n == 3:
        return "Fizz"
    return str(n)

# sexto sétimo oitavo nono teste 
    if n == 5:
        return "Buzz"
    if n % 3 == 0:
        return "Fizz"
    return str(n)

# décimo teste
    if n % 5 == 0:
        return "Buzz"
    if n % 3 == 0:
        return "Fizz"
    return str(n)

# décimo quinto teste
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 5 == 0:
        return "Buzz"
    if n % 3 == 0:
        return "Fizz"
    return str(n)

