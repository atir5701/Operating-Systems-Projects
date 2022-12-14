from IPython.display import clear_output

def FCFS():
    print("FIRST COME FIRST SERVE SCHEDULLING")
    n = int(input("Enter number of processes : "))
    d = dict()

    for i in range(n):
        key = "P" + str(i + 1)
        a = int(input("Enter arrival time of process " + str(i + 1) + ": "))
        b = int(input("Enter burst time of process " + str(i + 1) + ": "))
        l = []
        l.append(a)
        l.append(b)
        d[key] = l

    d = sorted(d.items(), key=lambda item: item[1][0])

    ET = []
    for i in range(len(d)):
        if (i == 0):
            ET.append(d[i][1][1])
        else:
            ET.append(ET[i - 1] + d[i][1][1])

    TAT = []
    for i in range(len(d)):
        TAT.append(ET[i] - d[i][1][0])

    WT = []
    for i in range(len(d)):
        WT.append(TAT[i] - d[i][1][1])

    avg_WT = 0
    for i in WT:
        avg_WT += i
    avg_WT = (avg_WT / n)

    print("Process | Arrival | Burst | Exit    | Turn Around | Wait |")
    for i in range(n):
        print("   ", d[i][0], "   |   ", d[i][1][0], " |    ", d[i][1][1], " |    ", ET[i], "  |    ", TAT[i], "  |   ",
              WT[i], "   |  ")
    print("Average Waiting Time: ", avg_WT)

def processData(no_of_processes):
        process_data = []
        for i in range(no_of_processes):
            temporary = []
            process_id = int(input("Enter Process ID: "))

            arrival_time = int(input(f"Enter Arrival Time for Process {process_id}: "))

            burst_time = int(input(f"Enter Burst Time for Process {process_id}: "))

            temporary.extend([process_id, arrival_time, burst_time, 0, burst_time])
            '''
            '0' is the state of the process. 0 means not executed and 1 means execution complete

            '''
            process_data.append(temporary)

        time_slice = int(input("Enter Time Slice: "))

        schedulingProcess(process_data, time_slice)


def schedulingProcess(process_data, time_slice):
    start_time = []
    exit_time = []
    executed_process = []
    ready_queue = []
    s_time = 0
    process_data.sort(key=lambda x: x[1])
    '''
    Sort processes according to the Arrival Time
    '''
    while 1:
        normal_queue = []
        temp = []
        for i in range(len(process_data)):
            if process_data[i][1] <= s_time and process_data[i][3] == 0:
                present = 0
                if len(ready_queue) != 0:
                    for k in range(len(ready_queue)):
                        if process_data[i][0] == ready_queue[k][0]:
                            present = 1
                '''
                The above if loop checks that the next process is not a part of ready_queue
                '''
                if present == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                    ready_queue.append(temp)
                    temp = []
                '''
                The above if loop adds a process to the ready_queue only if it is not already present in it
                '''
                if len(ready_queue) != 0 and len(executed_process) != 0:
                    for k in range(len(ready_queue)):
                        if ready_queue[k][0] == executed_process[len(executed_process) - 1]:
                            ready_queue.insert((len(ready_queue) - 1), ready_queue.pop(k))
                '''
                The above if loop makes sure that the recently executed process is appended at the end of ready_queue
                '''
            elif process_data[i][3] == 0:
                temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                normal_queue.append(temp)
                temp = []
        if len(ready_queue) == 0 and len(normal_queue) == 0:
            break
        if len(ready_queue) != 0:
            if ready_queue[0][2] > time_slice:
                '''
                If process has remaining burst time greater than the time slice, it will execute for a time period equal to time slice and then switch
                '''
                start_time.append(s_time)
                s_time = s_time + time_slice
                e_time = s_time
                exit_time.append(e_time)
                executed_process.append(ready_queue[0][0])
                for j in range(len(process_data)):
                    if process_data[j][0] == ready_queue[0][0]:
                        break
                process_data[j][2] = process_data[j][2] - time_slice
                ready_queue.pop(0)
            elif ready_queue[0][2] <= time_slice:
                '''
                If a process has a remaining burst time less than or equal to time slice, it will complete its execution
                '''
                start_time.append(s_time)
                s_time = s_time + ready_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                executed_process.append(ready_queue[0][0])
                for j in range(len(process_data)):
                    if process_data[j][0] == ready_queue[0][0]:
                        break
                process_data[j][2] = 0
                process_data[j][3] = 1
                process_data[j].append(e_time)
                ready_queue.pop(0)
        elif len(ready_queue) == 0:
            if s_time < normal_queue[0][1]:
                s_time = normal_queue[0][1]
            if normal_queue[0][2] > time_slice:
                '''
                If process has remaining burst time greater than the time slice, it will execute for a time period equal to time slice and then switch
                '''
                start_time.append(s_time)
                s_time = s_time + time_slice
                e_time = s_time
                exit_time.append(e_time)
                executed_process.append(normal_queue[0][0])
                for j in range(len(process_data)):
                    if process_data[j][0] == normal_queue[0][0]:
                        break
                process_data[j][2] = process_data[j][2] - time_slice
            elif normal_queue[0][2] <= time_slice:
                '''
                If a process has a remaining burst time less than or equal to time slice, it will complete its execution
                '''
                start_time.append(s_time)
                s_time = s_time + normal_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                executed_process.append(normal_queue[0][0])
                for j in range(len(process_data)):
                    if process_data[j][0] == normal_queue[0][0]:
                        break
                process_data[j][2] = 0
                process_data[j][3] = 1
                process_data[j].append(e_time)
    t_time = calculateTurnaroundTime(process_data)
    w_time = calculateWaitingTime(process_data)
    printData(process_data, t_time, w_time, executed_process)


def calculateTurnaroundTime(process_data):
    total_turnaround_time = 0
    for i in range(len(process_data)):
        turnaround_time = process_data[i][5] - process_data[i][1]
        '''
        turnaround_time = completion_time - arrival_time
        '''
        total_turnaround_time = total_turnaround_time + turnaround_time
        process_data[i].append(turnaround_time)
    average_turnaround_time = total_turnaround_time / len(process_data)
    '''
    average_turnaround_time = total_turnaround_time / no_of_processes
    '''
    return average_turnaround_time


def calculateWaitingTime(process_data):
    total_waiting_time = 0
    for i in range(len(process_data)):
        waiting_time = process_data[i][6] - process_data[i][4]
        '''
        waiting_time = turnaround_time - burst_time
        '''
        total_waiting_time = total_waiting_time + waiting_time
        process_data[i].append(waiting_time)
    average_waiting_time = total_waiting_time / len(process_data)
    '''
    average_waiting_time = total_waiting_time / no_of_processes
    '''
    return average_waiting_time


def printData(process_data, average_turnaround_time, average_waiting_time, executed_process):
    process_data.sort(key=lambda x: x[0])
    '''
    Sort processes according to the Process ID
    '''
    print(
        "Process_ID  Arrival_Time  Rem_Burst_Time   Completed  Original_Burst_Time  Completion_Time  Turnaround_Time  Waiting_Time")
    for i in range(len(process_data)):
        for j in range(len(process_data[i])):
            print(process_data[i][j], end="				")
        print()

    print(f'Average Turnaround Time: {average_turnaround_time}')

    print(f'Average Waiting Time: {average_waiting_time}')

    print(f'Sequence of Processes: {executed_process}')


def RR():
    no_of_processes = int(input("Enter number of processes: "))
    processData(no_of_processes)

def process():
    while(True):
        print("Enter 1 for using First Come First Serve Schedulling\nEnter 2 for using Round Robing Schedulling\nEnter 3 for exiting\n")
        n=int(input("Enter the choice : "))
        print()
        if n==1:
            FCFS()
        elif n==2:
            RR()
        elif n==3:
            clear_output(wait=True)
            break
        else:
            print("Incorrect Choice entered - please re-enter the choice")



