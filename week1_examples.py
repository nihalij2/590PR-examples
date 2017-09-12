# week1 simple examples of Python syntax and peculiarities.

# looping and counting in Python.
# Each of these next 3 loops will output integers from 0 to 9:

# the "traditional" way you'll see in many languages:
i = 0
while i < 10:
    print(i)
    i += 1


# variation as an infinite loop with a conditional "break" in the middle
i = 0
while True:
    print(i)
    if i >= 9:
        break
    i += 1


# the most common "Pythonic" way to loop with an integer counter:
for i in range(10):
    print(i)


# But range() has up to 3 parameters, START, STOP, and STEP.
# Remember the range doesn't include the STOP value but quits iterating
# just BEFORE it reaches it.


# count forward by even numbers 2 - 10:
for i in range(2, 11, 2):
    print(i)

# count backward by tens:
for i in range(100,0,-10):
    print(i)

# range() actually returns a special "range" data type (object), which is
# a type of iterator.  So if you print it directly, you don't get what you
# expect.  You can uncover the whole range of values it will produce by
# converting it to a list first:

print(list(range(10)))


# Fortunately, range() parameters work like the indexing and slicing operations
# with square brackets on a sequence data type (strings, lists, tuples, and more)

s = 'the quick brown fox'
print(s)

# we can extract part of a string (like the last 3 characters, 'fox')
# by using negative index as the start, and a colon to indicate continuing
# to the end:
print(s[-3:])


# but we CAN'T assign a value to just a part of an IMMUTABLE data type.  So
# to replace 'fox' with 'dog' we have to create a brand new string and then
# assign that to the same variable.  It will disconnect variable s from the
# previous value.


# this way uses one of the built-in string methods:
s = s.replace('fox','dog')
print(s)

# this way uses string concatenation to construct a new string without 'fox', plus 'dog'
if s[-3:] == 'fox':
    s = s[0:-3] + 'dog'
print(s)


# Python has no "case" or "switch" keywords like you would find in
#  C, Java, or many other languages.  To do something similar, just
#  create a series of if ... elif ... elif ... else like this:

w = input('give me a word')
if 'x' in w:
    print('x!')
elif 'y' in w:
    print('y!')
elif 'a' in w:
    print('a!')
elif 'p' in w:
    print('p!')
elif 'r' in w:
    print('r!')
else:
    print("I didn't find any of my expected letters.")

