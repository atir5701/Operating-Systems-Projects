import math
import numpy as np
import sys
from IPython.display import clear_output
class Exp(Exception):
    def __init__(self,value):
        self.value=value

    def __str__(self):
        return self.value

def Print2(allocation,need,max,Process,Resource):
    if len(allocation)==0 or len(need)==0 or len(max)==0:
        return
    print("So now State of System : \n")
    print("Process Id\t\tAllocated\t\t Maximum\t\t  Need")

    x =Resource[0]+" "+Resource[1]+" "+Resource[2]
    x=x.center(9)
    print("           \t\t" + x + "\t\t" + x + "\t\t" + x)
    for i in range(len(need)):
        p = Process[i]
        av = ' '.join([str(a) for a in allocation[i]]).center(9)
        ma = ' '.join([str(a) for a in max[i]]).center(9)
        ne = ' '.join([str(a) for a in need[i]]).center(9)
        print(p.center(10) + "\t\t" + av + "\t\t" + ma + "\t\t" + ne)

def safety(A,N,M,P,AV,n,Resource):
    arr1 = np.array(AV)
    safety = []
    i=0
    while (i != n):
        for j in range(len(N)):
            arr2 = np.array(N[j])
            if (np.all(arr2 <= arr1)):
                print("Presently Available : "+str(arr1))
                arr1 = arr1 + np.array(A[j])
                Print2(A, N, M, P,Resource)
                A.pop(j)
                N.pop(j)
                M.pop(j)
                print()
                print("Process " + P[j] + " need is less then the available so hence we give available resource to " + P[j])
                print("So now Available : " + str(arr1))
                safety.append(P[j])
                P.pop(j)
                print()

                break;
        else:
            if len(N) != 0:
                print("DeadLock Occured")
                SystemExit(0)

        i += 1

        print()

    print("As all process get the resources they need without system going into deadlock hence,  System is in safe state and the safe sequence is : ")
    print(safety)
    return 0

def request(A1,N1,M1,P1,AV1,n,Resource):
    print("\nEnter the process which makes the request : ")
    y = input()
    Req = []
    print()
    for i in Resource:
        t = "Enter the request for resource of type " + i + " : "
        j = int(input(t))
        Req.append(j)

    t = P1.index(y)
    ar = np.array(Req)
    ar1 = np.array(N1[t])
    ar2 = np.array(AV1)
    ar3 = np.array(A1[t])

    try:
        if np.all(ar <= ar1) and np.all(ar <= ar2):
            print(
                "\nAs the request made by " + y + " is less then its need and available so we temporarily grant the resources")
            print("\nNew Available is : ")
            # Availble = Avialble - Request
            ar2 = ar2 - ar
            ar2 = ar2.tolist()
            print(ar2)
            # Allocation = Allocation + Request
            ar3 = ar3 + ar
            ar3 = ar3.tolist()
            # Need= Need - Request
            ar1 = ar1 - ar
            ar1 = ar1.tolist()
            N1.pop(t)
            A1.pop(t)
            A1.insert(t, ar3)
            N1.insert(t, ar1)

            Print2(A1, N1, M1, P1)
            print("Now checking if resources can be given to " + y + " or not : ")
            print()
            Y = safety(A1, N1, M1, P1, ar2)
            print("\n")
            if Y == 0:
                print(
                    "As system is not in Unsafe state so " + y + " can be allocated the resource which it had request for.\n")
        else:
            raise Exception("Invalid Request made by the Process")
    except Exception as e:
        print(e)

def inputBanker():
    allocation=[]
    max=[]
    Maxsystem=[]
    available=[]
    Resource=[]
    need=[]
    Process=[]

    n=int(input("Enter total number of Resource Type : "))
    print()
    for i in range(n):
        t="Enter the Name of Resource "+str(i+1)+" : "
        x=input(t)
        Resource.append(x)

    # Allocated Resources
    print()
    Max=[]
    for i in Resource:
        st="Enter the Max instances of resource type "+i+" in system : "
        t=int(input(st))
        Max.append(t)

    M=np.array(Max)
    print()
    n=int(input("Enter the total number of Process : "))
    print()
    for j in range(n):
        temp = []
        p="P"+str(j)
        Process.append(p)
        for i in Resource:
            st="Enter the allocated instances of resource type "+i+" for "+Process[j]+" : "
            t=int(input(st))
            temp.append(t)
        print()
        M=M-np.array(temp)
        allocation.append(temp)

    P=Process.copy()
    P1=Process.copy()

    A=allocation.copy()
    A1=allocation.copy()

    available=list(M)

    AV=available.copy()
    AV1=available.copy()

    print()

    # Maximum Resources
    for j in range(n):
        temp = []
        for i in Resource:
            st="Enter the maximum instances of resource type "+i+" required by "+Process[j]+" : "
            t=int(input(st))
            temp.append(t)
        print()
        max.append(temp)
    M=max.copy()
    M1=max.copy()

    # Available Number of Resource

    # Calculating Need

    for i in range(n):
        a1=np.array(allocation[i])
        a2=np.array(max[i])
        t=a2-a1
        t=t.tolist()

        y=[]
        for i in t:
            try:
                if i >= 0:
                    y.append(i)
                else:
                    raise Exp("Invalid values of max and allocation enter")
                    print("Re-start the execution")
            except Exp as e:
                print(e.__str__())
        need.append(y)
    N=need.copy()
    N1=need.copy()

    print()
    print("Current Status of System : \n")
    print("Process Id\t\tAllocated\t\t Maximum\t\t  Need")
    for i in range(n):
        av = ' '.join([str(a) for a in allocation[i]]).center(9)
        ma=' '.join([str(a) for a in max[i]]).center(9)
        ne=' '.join([str(a) for a in need[i]]).center(9)
        print(Process[i].center(9)+"\t\t"+av+"\t\t"+ma+"\t\t"+ne)
    print()
    print("Initially Available Resources : "+str(AV))
    # Determining Safe Sequence
    print()
    print()
    # Safety Algorithm
    safety(A, N, M, P, AV,n,Resource)
    clear_output(wait=True)
    # Resource request algorithm
    request(A1,N1,M1,P1,AV1,n,Resource)
    clear_output(wait=True)

