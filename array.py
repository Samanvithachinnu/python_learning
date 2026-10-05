array = [10, 20, 30,]
print(array)
print(len(array))
print(array[0])
print(array[1])
print(array[2])
print(array[-1])
print(array[-2])
print(array[-3])
array.append(40)
array.insert(3, 35)
print(array)
array.remove(35)
array.pop()
array.pop(2)

#access by value
for x in array:
    print(x)

#access by index
for i in range(len(array)):
    print(array[i])

#reverse access by index
for i in range(len(array)-1, -1, -1):
    print(array[i])

#reverse access by value
for x in reversed(array):
    print(x)
