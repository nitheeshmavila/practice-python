'''Exercise 8.3.
-------------------
 Given that fruit is a string, what does fruit[:] mean?'''

fruit = 'apple'
a = fruit[:]
print(id(a))
print(id(fruit))

# fruit[:] just copy the string in fruit
