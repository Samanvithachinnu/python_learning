# Opening a file

f = open('a.txt', 'w')
f.close()

# Closing a file

with open('a.txt', 'w') as f:
    print(f.closed)  

print(f.closed)      
print()

# Write

f = open('a.txt', 'w')
f.write('ab')
f.write('c\n')
f.write('d\ne\nf')
f.close()

# 4. Writelines

f = open('b.txt', 'w')
f.writelines('Guntur\n')
f.writelines(('Hyderabad\n', 'Vizag\n'))
f.writelines(['Guntur\n', 'Hyderabad\n', 'Vizag\n'])
f.close()

# 5. Read

f = open('a.txt', 'r')
print(f.read())
f.close()

f = open('a.txt', 'r')
print(f.read(4))
f.close()

f = open('a.txt', 'r')
print(f.read(5))
print(f.read())
f.close()

# 6. Readline

f = open('c.txt', 'w+')
f.writelines(['abc\n', 'def\n', 'ghi\n'])
f.seek(0)
print(f.readline(), 'end')
f.close()

f = open('c.txt', 'r')
print(f.readline(), 'end')
print(f.readline(2), 'end')
print(f.readline(10), 'end')
print(f.readline(), 'end')
f.close()

# 7. Readlines

f = open('d.txt', 'w+')
f.writelines(['abc\n', 'def\n', 'ghi\n', 'jkl'])
f.close()

f = open('d.txt', 'r')
print(f.read(1))
print(f.readlines(4))
print(f.readlines(2))
print(f.readlines(0))
f.close()

# 8. For loop

f = open('e.txt', 'w')
f.writelines(['abc\n', 'def\n', 'ghi\n', 'jkl'])
f.close()

f = open('e.txt', 'r')
print(next(f))

for x in f:
  print(x, end='')

f.close()