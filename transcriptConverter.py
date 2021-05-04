file1 = open('/Users/zhuang/Desktop/KatieBauer.txt', 'r')
Lines = file1.readlines()
 
cleaned = []
for i in range(0, len(Lines), 2):
    new = Lines[i].strip('\n') + ' ' + Lines[i + 1]
    cleaned.append(new)
# print(cleaned)
file1.close()

file1 = open('myfile.txt', 'w')
file1.writelines(cleaned)
file1.close()
print('DONE!!!!!!!')
