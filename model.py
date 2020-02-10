

def is_prime(param):
    a_prime = "prime"
    not_a_prime = "not prime!"
    if param < 2:
        return not_a_prime
    if param == 2:
        return a_prime
    if param % 2 == 0:
        return "Come on dude, you know even numbers are not prime!"
    i = 3
    while i * i < param:
        if param % i == 0:
            return not_a_prime
        i += 3

    return a_prime


def is_factorial(param):
    a_factorial = "factorial"
    not_a_factorial = "not factorial!"
    if param < 1:
        return not_a_factorial
    i = 2
    while param > 1:
        if param % i != 0:
            return not_a_factorial
        param /= i
        i += 1

    return a_factorial


def is_palindrome(param: int):
    a_palindrome = "palindrome"
    not_a_palindrome = "not palindrome!"
    if param < 0:
        return not_a_palindrome
    if param / 10 == 0:
        return a_palindrome

    reversed_param: int = 0

    while reversed_param < param:
        reversed_param *= 10
        reversed_param += param % 10
        if param == reversed_param:
            return a_palindrome

        param //= 10

    print(param, reversed_param)

    return a_palindrome if reversed_param == param else not_a_palindrome


def is_sqrt(param: int):
    a_int_sqrt = "int sqrt"
    not_a_int_sqrt = "not int sqrt!"
    i = 1
    while i*i < param:
        i += 1

    return a_int_sqrt if i*i == param else not_a_int_sqrt


command_to_function = {
    '/check': is_prime,
    '/factorial': is_factorial,
    '/palindrome': is_palindrome,
    '/sqrt': is_sqrt
}
