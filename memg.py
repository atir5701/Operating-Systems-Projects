from IPython.display import clear_output
def diagram(holes, processes, ind):
    i = 0
    while i < len(holes):
        if i < len(holes) - 1:
            if i == 0:
                print('''                        ------
                        |  %d |
                        -------''' % holes[i], end=" ")
            elif i != 0:
                print('''                      
                        |  %d |
                        -------  ''' % holes[i], end=" ")

            for x in processes:
                if ind[processes.index(x)] == i:
                    print('''            
                            | P %d|
                            -------''' % processes.index(x), end="")
                else:
                    pass

        else:

            for x in processes:
                if ind[processes.index(x)] == i:
                    print('''             
                            | P %d|
                            -------''' % processes.index(x), end="")
                else:
                    pass

            print('''                      
                         |  %d |
                         ------  ''' % holes[i], end=" ")
        i = i + 1


def First_fit(holes, processes, ind):
    for z in processes:
        i = 0
        while i < holes.__len__():
            if z <= holes[i]:
                holes[i] = holes[i] - z

                ind[processes.index(z)] = i

                print("Process ", processes.index(z), " is Alloted to hole no.:", i)
                break
            else:
                i = i + 1
        else:
            print("Process ", z, " Can't be accomodated in any holes.")
    print("holes left::", holes)
    return holes, ind


def Next_fit(holes, processes, ind):
    i = 0
    for z in processes:

        while i < holes.__len__():
            if z <= holes[i]:
                holes[i] = holes[i] - z
                print(holes)
                ind[processes.index(z)] = i
                print(ind)
                print(processes)
                print("Process ", processes.index(z), " is Alloted to hole no.:", i)
                break
            else:
                i = (i + 1) % (len(holes))
        else:
            print("Process ", z, " Can't be accomodated in any holes.")
    print("holes left::", holes)
    return holes, ind


def Best_fit(holes, processes, ind):
    for z in processes:
        j = 0
        i = 0
        while i < holes.__len__():
            if z <= holes[i]:

                while j < holes.__len__():

                    if holes[j] >= z and holes[j] < holes[i]:
                        i = j
                    else:
                        j = j + 1

                holes[i] = holes[i] - z

                print("Process ", processes.index(z), " is Alloted to hole no.:", i, )
                ind[processes.index(z)] = i
                break
            else:
                i = i + 1
        else:
            print("Process ", z, " Can't be accomodated in any holes.")
    print("holes left::", holes)
    return holes, ind


def Worst_fit(holes, processes, ind):
    for z in processes:
        if max(holes) >= z:
            holes[holes.index(max(holes))] = holes[holes.index(max(holes))] - z
            ind[processes.index(z)] = holes.index(max(holes))
            print("Process ", processes.index(z), " is Alloted to hole no.:", holes.index(max(holes)))
        else:
            print("Process ", processes.index(z), " of size ", z, " Can't be accomodated in any holes.")

    print("holes left::", holes)
    return holes, ind


def memorymanagement():

    holes = input("Enter your holes(Enter in single line and seperate them with spaces):")
    list_holes = holes.split(" ")
    # print(list_holes)

    ind = []
    temp_holes = []  # temporary list of holes
    for x in list_holes:
        temp_holes.append(int(x))

    # print(temp_holes)

    processes = input("Enter your processes(Enter in single line and seperate them with spaces):")
    list_processes = processes.split(" ")

    # print(list_processes)

    temp_processes = []  # temporary list of processes
    for x in list_processes:
        temp_processes.append(int(x))
        ind.append(-1)

    # print(temp_processes)
    while(True):
        print("::::::::::::::::::::DIAGRAM OF AVAILABLE HOLES::::::::::::::::::::")
        diagram(temp_holes, temp_processes, ind)
        print('''
    
    
                        Choose Your Memory Allocation Algorithm
                        Menu::
                        1.First Fit
                        2.Next Fit
                        3.Best Fit
                        4.Worst Fit
                        5.Exit
    
    
        ''')

        choice = int(input("Enter your Choice::"))

        if choice == 1:
            # i=0
            temp_holes, ind = First_fit(temp_holes, temp_processes, ind)
            # print(ind)

            print("::::::::::::::::::::DIAGRAM OF AVAILABLE HOLES and Processes After Allocation::::::::::::::::::::")

            diagram(temp_holes, temp_processes, ind)

        elif choice == 2:
            # i=0
            temp_holes, ind = Next_fit(temp_holes, temp_processes, ind)
            # print(ind)

            print("::::::::::::::::::::DIAGRAM OF AVAILABLE HOLES and Processes After Allocation::::::::::::::::::::")

            diagram(temp_holes, temp_processes, ind)

        elif choice == 3:
            # i=0
            temp_holes, ind = Best_fit(temp_holes, temp_processes, ind)
            # print(ind)

            print("::::::::::::::::::::DIAGRAM OF AVAILABLE HOLES and Processes After Allocation::::::::::::::::::::")

            diagram(temp_holes, temp_processes, ind)

        elif choice == 4:
            # i=0
            temp_holes, ind = Worst_fit(temp_holes, temp_processes, ind)
            # print(ind)

            print("::::::::::::::::::::DIAGRAM OF AVAILABLE HOLES and Processes After Allocation::::::::::::::::::::")

            diagram(temp_holes, temp_processes, ind)
        elif choice==5:
            clear_output(wait=True)
            break
        else:
            print("Wrong choice!!")

        print("\n\n\n\n\n\nMinimum Hole remaining:", min(temp_holes))
        print("Maximum Hole remaining:", max(temp_holes))

