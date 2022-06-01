import numpy as np
from pip._vendor.distlib.compat import raw_input


def Condition_Number(A):
    A_inv = np.linalg.inv(A)
    mu = abs(np.linalg.norm(A)) * abs(np.linalg.norm(A_inv))
    print(mu)


def Gauss_Seidel(A, B, x, iter):
    for i in range(iter):
        val = x.copy()
        for j in range(len(B)):
            x[j] = (B[j] - np.sum(A[j][:j] * x[:j]) - np.sum(A[j][j+1:] * x[j+1:])) / A[j][j]
        #x[0] = (B[0] - A[0][1] * x[1] - A[0][2] * x[2] - A[0][3] * x[3]) / A[0][0]
        #x[1] = (B[1] - A[1][0] * x[0] - A[1][2] * x[2] - A[1][3] * x[3]) / A[1][1]
        #x[2] = (B[2] - A[2][0] * x[0] - A[2][1] * x[1] - A[2][3] * x[3]) / A[2][2]
        #x[3] = (B[3] - A[3][0] * x[0] - A[3][1] * x[1] - A[3][2] * x[2]) / A[3][3]
        error = np.linalg.norm(x - val)
        print(i, x, error)


if __name__ == "__main__":  #Programm launch
    #A = np.array([[12, 2, 4, 2], [2, 16, 2, 4], [4, 2, 12, 2], [2, 4, 2, 16]])
    A = np.array([[12, 52, 4, 2], [2, 16, 122, 4], [4, 2, 12, 2], [2, 4, 2, 16]])
    B = np.array([36, 56, 52, 80])
    x = np.array([0, 0, 0, 0])

    print("We will work with the matrix A: ")
    print(A)
    print("and the matrix B: ")
    print(B)
    print("The condition number is: ")
    Condition_Number(A)
    iter = int(raw_input("Please enter the maximum of iteration: "))
    print(x)
    Gauss_Seidel(A, B, x, iter)