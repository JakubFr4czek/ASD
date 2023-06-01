class employee:
    
    def __init__(self, fun, emp):
        self.emp = emp
        self.fun = fun
        self.f = -1
        self.g = -1

#Przyklad z wykladu 11/2023
A = []
A.append(employee(50, [1,2,3])) #0
A.append(employee(10, [4,5,6])) #1
A.append(employee(20, [7,8]))   #2
A.append(employee(1, [9,10]))   #3
A.append(employee(18, [11,12,13])) #4
A.append(employee(5, []))       #5
A.append(employee(23, []))      #6
A.append(employee(21, [14,15,16])) #7
A.append(employee(17, []))      #8
A.append(employee(1, [17,18]))  #9
A.append(employee(2, [19]))     #10
A.append(employee(24, []))      #11
A.append(employee(36, []))      #12
A.append(employee(7, [20, 21, 22])) #13
A.append(employee(18, []))      #14
A.append(employee(1, []))       #15
A.append(employee(5, []))       #16
A.append(employee(1, []))       #17
A.append(employee(1, []))       #18
A.append(employee(1, []))       #19
A.append(employee(100, []))     #20
A.append(employee(100, []))     #21
A.append(employee(100, []))     #22

def g(v, A):

    if v.g >= 0: return v.g

    x = 0
    for i in range(len(v.emp)):
        x += f(A[v.emp[i]], A)
    
    v.g = x
    return v.g

def f(v, A):
    if v.f >= 0: return v.f

    
    x = v.fun
    for i in range(len(v.emp)):
        x += g(A[v.emp[i]], A)

    y = g(v, A)
    v.f = max(x,y)
    return v.f

f(A[0], A)

for x in A:
    print(x.fun, x.f, x.g)



