import sys

# f = open("input1.txt", "r")
f = open("input2.txt", "r")

array = f.readlines()
# print(array) # it stores all the lines of a file in an array

space = ' '

a = [[[0 for k in range(100)] for j in range(100)] for i in range(100)]
x = [0 for k in range(100)]
b = [[0 for k in range(100)] for j in range(100)]
r = 0
c = 0
n = 0

for i in range(len(array)):
    eqn = array[i]
    word = eqn.split()

    for j in range(len(word)):
        if word[j] == '=':
            b[0][i] = float(word[j + 1])
            break
        elif word[j][len(word[j]) - 2] == 'x':
            num = word[j][0:len(word[j]) - 2]
            if len(num) == 0:
                a[0][i][j] = 1.0
            elif (len(num) == 1):
                if num == '+':
                    a[0][i][j] = 1.0
                elif num == '-':
                    a[0][i][j] = -1.0
                else:
                    a[0][i][j] = float(num)
            else:
                if num[0] == '+':
                    a[0][i][j] = float(num[1:len(num)])
                elif num[0] == '-':
                    a[0][i][j] = -1 * float(num[1:len(num)])
                else:
                    a[0][i][j] = float(num[1:len(num)])
            r = i + 1
            c = j + 1
        elif word[j][len(word[j]) - 1] >= 'A' and word[j][len(word[j]) - 1] <= 'Z':
            num = word[j][0:len(word[j]) - 1]
            if len(num) == 0:
                a[0][i][j] = 1.0
            elif (len(num) == 1):
                if num == '+':
                    a[0][i][j] = 1.0
                elif num == '-':
                    a[0][i][j] = -1.0
                else:
                    a[0][i][j] = float(num)
            else:
                if num[0] == '+':
                    a[0][i][j] = float(num[1:len(num)])
                elif num[0] == '-':
                    a[0][i][j] = -1 * float(num[1:len(num)])
                else:
                    a[0][i][j] = float(num[1:len(num)])
            r = i + 1
            c = j + 1
        else:
            print("Wrong input format")
            sys.exit(1)

f.close()


print('ITERATION=0')

for i in range(r):
    for j in range(c):
        print('(0,' + str(i) + ',' + str(j) + ')=' + str(a[0][i][j]), end=" ")
    print('b=' + str(b[0][i]))

for k in range(r):
    a[k] = a[0]

for k in range(r - 1):
    ind = k
    mx = abs(a[k][k][k])
    for i in range(k + 1, r):
        if (abs(a[k][i][k]) > mx):
            mx = abs(a[k][i][k])
            ind = i

    temp = a[k][ind]
    a[k][ind] = a[k][k]
    a[k][k] = temp

    temp = b[k][ind]
    b[k][ind] = b[k][k]
    b[k][k] = temp
    print('-------------------------------------------------------------------------------')

    print('ITERATION='+str(k+1))
    for i in range(k + 1, r):
        p = a[k][i][k]
        for j in range(k, c):
            if a[k][k][k] == 0:
                print('found 0')
            else:
                a[k + 1][i][j] = a[k][i][j] - a[k][k][j] * p / a[k][k][k]

        b[k + 1][i] = b[k][i] - b[k][k] * p / a[k][k][k]
        print('-------------------------------------------------------------------------------')



    for i in range(r):
        for j in range(c):
            print("("+str(k+1)+" "+str(i)+" "+str(j)+")="+str(a[k + 1][i][j]), end=" ")
        print(b[k+1][i],end=" ")
        print()

print("BACK SUBSTITUTION:...............................")

x[r-1] = b[r-2][r-1]/a[r-2][r-1][r-1]

for k in range(r-2,-1,-1):
    sum=0.0
    for i in range(k+1, r):
        sum+= a[r-1][k][i]*x[i]
    x[k] = (b[r-1][k]-sum)/a[r-1][k][k]




ff = open("result.txt","w")
for i in range(r):
    print("x["+str(i+1)+"]="+str(x[i]))
    ff.write("x["+str(i+1)+"]="+str(x[i])+'\n')
ff.close()
