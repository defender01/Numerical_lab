import numpy as np
import matplotlib.pyplot as plt

f = open('inputData.txt','r')
n = int(f.readline())
X = np.zeros(n)
Y = np.zeros(n)
for i in range(n):
    st = f.readline()
    string = st.split()
    X[i] = float(string[0])
    Y[i] = float(string[1])


# X = np.array([-7., -9., 0., 9., 8., 3., -3.])
#
# Y = np.array([2., 8., 1., 9., 5., -3., -7.])


n= int(X.shape[0])


flag = np.zeros((n+1,n+1))
A = np.zeros((n+5,n+5))


print(X,Y)

def lagrange_InterPolation(X, x, Y, n):
    result = 0.0
    for i in range(n):
        s = 1.0
        t = 1.0
        for j in range(n):
            if (i != j):
                s = s * (x - X[j])
                t = t * (X[i] - X[j])
        result = result + (s / t) * Y[i]
    return result


def divided_diff(i,j,X,Y):
    if flag[i][j]==1:
        return A[i][j]
    if i==j:
        flag[i][j] = 1
        A[i][j] = Y[i]
        return A[i][j]
    A[i][j] = (divided_diff(i+1,j,X,Y)-divided_diff(i,j-1,X,Y))/(X[j]-X[i])
    flag[i][j] = 1
    return A[i][j]
def newton(X,Y,n,inputx):
    outputy = 0
    for i in range(n):
        temp=divided_diff(0,i,X,Y)
        mul=1
        for j in range(i):
            mul *= (inputx-X[j])
        temp *= mul
        outputy += temp
    return outputy

X_in= np.linspace(-30,30,1000)
Y_out_newton= np.zeros((len(X_in),1))
Y_out_lagrance= np.zeros((len(X_in),1))


for i in range(len(X_in)):
    Y_out_newton[i] = newton(X,Y,n,X_in[i])

Y_out_lagrance= lagrange_InterPolation(X,X_in,Y,len(X))

plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(min(X_in),max(X_in))
plt.ylim(-10,10)
plt.grid()
plt.plot(X_in,Y_out_newton,'r')
plt.plot(X_in,Y_out_lagrance,'g')
plt.scatter(X,Y)
plt.show()