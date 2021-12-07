filename = input('Please enter the filename  ')

content = input("Please enter the content ")
print(filename)
print(content)

# Alway Open the file
fo = open(filename, 'a')
fo.write('\n'+content)
# Alway Close the file
fo.close()