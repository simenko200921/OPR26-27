#Integer - whole number
#Operations
x, y = 4, 2
print(
    x+y,
    x-y,
    x/y,
    x*y,
    x//y,
    x**y,
    x%y
)
#parse
x = "12"
x = int(x)

#String - sequence of signs
#Operations
a = "a"
b = "b"
c = "c"
d = "d"

print(
    a+b,
    (a+b)[0],
    (a+b+c+d)[1:3],
    "abc"[::-1]
)

name = "Anja"
print(f"Hello {name}!")