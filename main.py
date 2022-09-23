def fizz_buzz(numbers):
    '''
    Given a lit of integers:
    1. Replace all integers that are evenly divisible by 3 with "fizz"
    2. Replace all integers divisible by 5 with "buzz"
    3. Replace all integers divisible by both 3 and 5 with "fizzbuzz"
    >>> numbers = [45, 22, 14, 65, 97, 72]
    >>> fizz_buzz(numbers)
    >>> numbers
    ['fizzbuzz', 22, 14, 'buzz', 97, 'fizz']
    '''
    # for i in (range(len(numbers))):
    #     num = numbers[i]
    #     if num % 3 == 0:
    #         numbers[i] = "fizz"
    #     if num % 5 == 0:
    #         numbers[i] = "buzz"
    #     if num % 3 == 0 and num % 5 == 0:
    #         numbers[i] = "fizzbuzz"
    # for i, num in (enumerate(numbers)):
    #     if num % 3 == 0:
    #         numbers[i] = "fizz"
    #     if num % 5 == 0:
    #         numbers[i] = "buzz"
    #     if num % 3 == 0 and num % 5 == 0:
    #         numbers[i] = "fizzbuzz"
    for i, num in (enumerate(numbers)):
        if num % 3 == 0 and num % 5 == 0:
            numbers[i] = "fizzbuzz"
        elif num % 3 == 0:
            numbers[i] = "fizz"
        elif num % 5 == 0:
            numbers[i] = "buzz"


numbers = [45, 22, 14, 65, 97, 72]
fizz_buzz(numbers)
print(numbers)
print([tup for tup in enumerate([1, 2, 3], start=10)])

lst = [1, 2, -5, 4]


def square(x):
    return x * x


print(list(map(square, lst)))

result = []
for num in lst:
    result.append(square(num))
print(result)

print([square(num) for num in lst])


def is_odd(x):
    return x % 2 == 1


print(list(filter(is_odd, lst)))
print([num for num in lst if is_odd(num)])

grid = [[0, 0, 0],
         [0, 0, 0]]

num_rows = 2
num_columns = 3
grid = []
for _ in range(num_rows):
    curr_row = []
    for _ in range(num_columns):
        curr_row.append(0)
    grid.append(curr_row)
print(grid)

print([[0 for _ in range(num_columns)] for _ in range(num_rows)])

print(max(lst))
print(max(lst, key=lambda x: x * x))
print([(lambda x: x % 2 == 1)(num) for num in lst])
print(any([(lambda x: x % 2 == 1)(num) for num in lst]))
print(all([(lambda x: x % 2 == 1)(num) for num in lst]))

def max(lst):
    max_num = -float('inf')
    for num in lst:
        # breakpoint()
        if num > max_num:
            max_num = num
    return max_num
print(max([-1, -2, -4]))

age = 10
name = "Bob"
print("My name is %s. I am %s years old." % (name, age))
print("My name is {0}. I am {1} years old.".format(name, age))
print("My name is {name}. I am {age} years old.".format(name=name, age=age))
print(f"My name is {name}. I am {age} years old.")
print(f"My name is {name}. I am {age + 5} years old.")


class A(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return (
            f"My name is {self.name}."
            f"I am {self.age + 5} years old."
        )


print(A(name, age))

animals = ["cat", "dog", "cheetah", "rhino"]
print(sorted(animals))
print(animals)
print(sorted(animals, reverse=True))

animals = [
    {'type': 'cat', 'name': 'Stephanie', 'age': 8},
    {'type': 'dog', 'name': 'Devon', 'age': 3},
    {'type': 'rhino', 'name': 'Moe', 'age': 5}
]
print(sorted(animals, key=lambda animal: animal['age']))
print(sorted(animals, key=lambda animal: animal['age'], reverse=True))
print(sorted(animals, key=lambda animal: animal['age'], reverse=True)[0])  # oldest animal

animals.sort(key=lambda animal: animal['age'])
print(animals)


def func():
    print("I am a function func()!")


func()
another_name = func
another_name()
print("cat", func, 42)
objects = ["cat", func, 42]
print(objects[1])
objects[1]()
d = {"cat": 1, func: 2, 42: 3}
print(d[func])


def inner():
    print("I am function inner()!")


def outer(function):
    function()


outer(inner)

animals = ["ferret", "vole", "dog", "gecko"]
print(sorted(animals))
print(sorted(animals, key=len))
print(sorted(animals, key=len, reverse=True))


def reverse_len(s):
    return -len(s)


print(sorted(animals, key=reverse_len))


def outer():
    def inner():
        print("I am function inner()!")
    return inner


function = outer()
print(function)
function()
outer()()

print((lambda s: s[::-1])("I am a string"))
print(sorted(animals, key=lambda s: -len(s)))

forty_two_producer = lambda: 42
print(forty_two_producer())


def func(x):
    return x, x ** 2, x ** 3


print(func(3))
print(f"--- {(lambda s: s[::-1])('I am a string')} ---")


def reverse(s):
    return s[::-1]


iterator = map(reverse, animals)
for i in iterator:
    print(i)
iterator = map(reverse, animals)
print(list(iterator))
iterator = map(lambda s: s[::-1], animals)
print(list(iterator))
print(list(map(lambda s: s[::-1], animals)))

print("+".join(["cat", "dog", "hedgehog", "gecko"]))
strings = []
for i in [1, 2, 3, 4, 5]:
    strings.append(str(i))
print(strings)
print("+".join(strings))
print("+".join(map(str, [1, 2, 3, 4, 5])))


def f(a, b, c):
    return a + b + c


print(list(map(f, [1, 2, 3], [10, 20, 30], [100, 200, 300])))

print(
    list(
        map(
            (lambda a, b, c: a + b + c),
            [1, 2, 3],
            [10, 20, 30],
            [100, 200, 300]
        )
    )
)


def greater_then_100(x):
    return x > 100


print(list(filter(greater_then_100, [1, 111, 2, 222, 3, 333])))
print(list(filter(lambda x: x > 100, [1, 111, 2, 222, 3, 333])))


def is_even(x):
    return x % 2 == 0


print(list(filter(is_even, range(10))))
print(list(filter(lambda x: x % 2 == 0, range(10))))

animals = ["cat", "Cat", "CAT", "dog", "Dog", "DOG", "emu", "Emu", "EMU"]


def all_caps(s):
    return s.isupper()


print(list(filter(all_caps, animals)))
print(list(filter(lambda s: s.isupper(), animals)))

# from functools import reduce


def f(x, y):
    return x + y


# print(reduce(f, [1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5]))
# print(reduce(f, ["cat", "dog", "hedgehog", "gecko"]))
print("".join(["cat", "dog", "hedgehog", "gecko"]))


def multiply(x, y):
    return x * y


def factorial(n):
    from functools import reduce
    return reduce(multiply, range(1, n + 1))


print(factorial(4))
print(factorial(6))

from math import factorial

print(factorial(4))
print(factorial(6))

print(max([23, 49, 6, 32]))


def greater(x, y):
    return x if x > y else y


from functools import reduce

print(reduce(greater, [23, 49, 6, 32]))
print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
print(reduce(lambda x, y: x + y, ["foo", "bar", "baz", "quz"]))


def factorial(n):
    from functools import reduce
    return reduce(lambda x, y: x * y, range(1, n + 1))


print(factorial(4))
print(factorial(6))
print(reduce(lambda x, y: x if x > y else y, [23, 49, 6, 32]))


def f(x,y):
    return x + y


from functools import reduce

print(reduce(f, [1, 2, 3, 4, 5], 100))
print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], 100))
print(100 + sum([1, 2, 3, 4, 5]))

numbers = [1, 2, 3, 4, 5]
print(list(map(str, numbers)))


def custom_map(function, iterable):
    from functools import reduce

    return reduce(
        lambda items, value: items + [function(value)],
        iterable,
        []
    )


print(custom_map(str, numbers))

numbers = list(range(10))
print(numbers)


def is_even(x):
    return x % 2 == 0


print(list(filter(is_even, numbers)))


def custom_filter(function, iterable):
    from functools import reduce

    return reduce(
        lambda items, value: items + [value] if function(value) else items,
        iterable,
        []
    )


print(custom_filter(is_even, numbers))
