from timeit import default_timer as timer
import random
import matplotlib.pyplot as plt


matrix = [[1,0,1]]

first = [0,0,0]
second = [1,0,0]
third = [0,1,0]
fourth = [0,0,1]


all = []
all.append(first)
all.append(second)
all.append(third)
all.append(fourth)


#numWays(l,c) = min(numWays(l-1,c), numWays(l-1,c-1) + 1, numWays(l-1,c+1) + 1)
import sys

sys.setrecursionlimit(100000)

"""def min(a,b,c):
    if(a <= b and a<=c):
        return a
    elif(b<= a and b<= c):
        return b
    else:
        return c"""



def findLane(matrix,l,c): # naive recursion

    if(matrix[l][c] != 1):
        if(l == 0 and c == 1):
            return 0
        if(c == 1):
            return min(findLane(matrix,l-1,c),findLane(matrix,l-1,c-1)+1,findLane(matrix,l-1,c+1)+1)
        elif(c == 0):
            return min(findLane(matrix,l-1,c),findLane(matrix,l-1,c+1) + 1,sys.maxsize)
        elif(c == 2):
            return min(findLane(matrix,l-1,c),findLane(matrix,l-1,c-1)+ 1,sys.maxsize)
    else:
        return sys.maxsize


def findMemo(matrix,l,c,memo): # recursion with memoization

    if(matrix[l][c] != 1):
        if(memo[l][c] == sys.maxsize):
            if (c == 1):
                memo[l][c] = min(findMemo(matrix,l-1,c,memo),findMemo(matrix,l-1,c-1,memo)+1,findMemo(matrix,l-1,c+1,memo)+1)
                return memo[l][c]
            elif (c == 0):
                memo[l][c] = min(findMemo(matrix,l-1,c,memo),findMemo(matrix,l-1,c+1,memo)+1,sys.maxsize)
                return memo[l][c]
            elif (c == 2):
                memo[l][c] =  min(findMemo(matrix,l-1,c,memo),findMemo(matrix,l-1,c-1,memo)+1,sys.maxsize)
                return memo[l][c]
        else:
            return memo[l][c]
    else:
        return memo[l][c]
    #return memo[l][c]

naive_list = []
def bottomUp(matrix,l,c,memo):

   for i in range(1,len(matrix)):
       for x in range(3):
           if(matrix[i][x] != 1):
               if(x == 0):
                   memo[i][x] = min(memo[i-1][x],memo[i-1][x+1]+1)
               elif(x == 1):
                    memo[i][x] = min(memo[i-1][x],memo[i-1][x-1]+1,memo[i-1][x+1]+1)
               else:
                   memo[i][x] = min(memo[i-1][x],memo[i-1][x-1]+1)
   return memo[l][c]



#matrix = [[1,0,1],[0,1,0],[0,0,1]]
memo = []

for i in range(len(matrix)):
    memo.append([0,0,0])
    for x in range(3):
        memo[i][x] = sys.maxsize
memo[0][1] = 0

naive_time = []
naive_size = []


for i in range(5):
    matrix = [[1,0,1]]
    size = int(input("Enter the number of row for the naive version: "))
    naive_size.append(size)
    for x in range(size - 1):
        matrix.append(all[random.randint(0, 3)])
    start = timer()
    print("Minimum cost for naive recursive algorithm:",min(findLane(matrix,len(matrix)-1,0),findLane(matrix,len(matrix)-1,1),findLane(matrix,len(matrix)-1,2)))
    end = timer()
    naive_time.append(end-start)
    print(end - start)
    print("********************")

plt.xlabel("Input size")
plt.ylabel("Running time(seconds)")
plt.plot(naive_size,naive_time)
plt.show()

memo = []
dynamic_time = []
dynamic_size = []
for i in range(5):
    matrix = [[1, 0, 1]]
    size = int(input("Enter the number of row for the dynamic recursive version: "))
    dynamic_size.append(size)
    for x in range(size - 1):
        matrix.append(all[random.randint(0, 3)])
    memo = []
    for i in range(len(matrix)):
        memo.append([0, 0, 0])
        for x in range(3):
            memo[i][x] = sys.maxsize
    memo[0][1] = 0

    for i in range(len(matrix)):
        memo.append([0, 0, 0])
        for x in range(3):
            memo[i][x] = sys.maxsize
    memo[0][1] = 0
    first_start = timer()
    a = findMemo(matrix, len(matrix) - 1, 0, memo)
    first_end = timer()

    for i in range(len(matrix)):
        memo.append([0, 0, 0])
        for x in range(3):
            memo[i][x] = sys.maxsize
    memo[0][1] = 0
    second_start = timer()
    b = findMemo(matrix, len(matrix) - 1, 1, memo)
    second_end = timer()
    for i in range(len(matrix)):
        memo.append([0, 0, 0])
        for x in range(3):
            memo[i][x] = sys.maxsize
    memo[0][1] = 0
    third_start = timer()
    c = findMemo(matrix, len(matrix) - 1, 2, memo)
    third_end = timer()
    print("Minimum cost for memoization:",min(a,b,c))
    dynamic_time.append(first_end-first_start + second_end-second_start + third_end-third_start)
    print(first_end-first_start + second_end-second_start + third_end-third_start)
    print("********************")

plt.xlabel("Input size")
plt.ylabel("Running time(seconds)")
plt.plot(dynamic_size,dynamic_time)
plt.show()


iterative_size = []
iterative_time = []
for i in range(5):
    matrix = [[1, 0, 1]]
    size = int(input("Enter the number of row for the iterative recursive version: "))
    iterative_size.append(size)
    for x in range(size - 1):
        matrix.append(all[random.randint(0, 3)])
    memo = []
    for i in range(len(matrix)):
        memo.append([0, 0, 0])
        for x in range(3):
            memo[i][x] = sys.maxsize
    memo[0][1] = 0
    start_first = timer()
    a = bottomUp(matrix, len(matrix) - 1, 0, memo)
    end_first = timer()
    for i in range(len(matrix)):
        memo.append([0, 0, 0])
        for x in range(3):
            memo[i][x] = sys.maxsize
    memo[0][1] = 0
    start_second = timer()
    b = bottomUp(matrix, len(matrix) - 1, 1, memo)
    end_second = timer()
    for i in range(len(matrix)):
        memo.append([0, 0, 0])
        for x in range(3):
            memo[i][x] = sys.maxsize
    memo[0][1] = 0
    start_third = timer()
    c = bottomUp(matrix, len(matrix) - 1, 2, memo)
    end_third = timer()
    print("Minimum cost for iterative algorithm:",min(a,b,c))
    iterative_time.append(end_first-start_first + end_second-start_second + end_third-start_third)
    print(end_first-start_first + end_second-start_second + end_third-start_third)

plt.xlabel("Input size")
plt.ylabel("Running time(seconds)")
plt.plot(iterative_size,iterative_time)
plt.show()


# Black Box Testing
print("Black Box Testing.......")
 # matrix with a single row
for j in range(5):
    matrix = [[1, 0, 1]]
    size = int(input("Enter the number of row: "))
    for x in range(size - 1):
        matrix.append(all[random.randint(0, 3)])
    for i in range(len(matrix)):
        memo.append([0, 0, 0])
        for x in range(3):
            memo[i][x] = sys.maxsize
    memo[0][1] = 0
    print("Minimum cost for naive recursive algorithm:",min(findLane(matrix,len(matrix)-1,0),findLane(matrix,len(matrix)-1,1),findLane(matrix,len(matrix)-1,2)))
    print("Minimum cost for memoization:",min(findMemo(matrix,len(matrix)-1,0,memo),findMemo(matrix,len(matrix)-1,1,memo),findMemo(matrix,len(matrix)-1,2,memo)))
    print("Minimum cost for iterative algorithm:",min(bottomUp(matrix,len(matrix)-1,0,memo),bottomUp(matrix,len(matrix)-1,1,memo),bottomUp(matrix,len(matrix)-1,2,memo)))
    for i in matrix:
        print(i)

matrix = [[1,0,1],[0,0,1],[1,0,0],[0,0,0],[1,0,0]]

for i in range(len(matrix)):
    memo.append([0, 0, 0])
    for x in range(3):
        memo[i][x] = sys.maxsize
memo[0][1] = 0
print("Minimum cost for naive recursive algorithm:",min(findLane(matrix,len(matrix)-1,0),findLane(matrix,len(matrix)-1,1),findLane(matrix,len(matrix)-1,2)))
print("Minimum cost for iterative algorithm:",min(bottomUp(matrix,len(matrix)-1,0,memo),bottomUp(matrix,len(matrix)-1,1,memo),bottomUp(matrix,len(matrix)-1,2,memo)))
print("Minimum cost for memoization:",min(findMemo(matrix,len(matrix)-1,0,memo),findMemo(matrix,len(matrix)-1,1,memo),findMemo(matrix,len(matrix)-1,2,memo)))
