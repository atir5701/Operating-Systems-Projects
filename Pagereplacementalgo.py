import time
from IPython.display import clear_output


def listrindex(lst, val):
    l = lst.copy()
    l.reverse()
    i = l.index(val)
    if i == -1:
        return -1
    return len(l) - i - 1


def FIFO(seq, frame_size):
    frames = []

    empty_frame = []
    for indx in range(frame_size):
        frames.append('-')
        empty_frame.append('-')

    frame_curr_size = 0
    frame_sequence = []
    # print(frame_sequence)
    counter = 0
    page_faults = 0
    for pgno in seq:
        if pgno not in frames:
            page_faults += 1
            if frame_curr_size == frame_size:
                frames[counter] = pgno
                counter += 1
                counter = counter % frame_size
                frame_sequence.append(frames.copy())
            else:
                frames[counter] = pgno
                counter += 1
                counter = counter % frame_size
                frame_curr_size += 1
                frame_sequence.append(frames.copy())
        else:
            frame_sequence.append(empty_frame)

    print("\n\nFinal Seq : ")

    for seq_num in range(len(seq)):
        print("\n" * 2)
        time.sleep(0.1)
        clear_output(wait=True)
        print("\n\n FCFS : ")
        print("{:<20}".format("Sequence : "), end='')
        for seq_item in seq:
            print("{:>3}".format(seq_item), end='')
        print('\n')
        for i in range(len(frames)):
            print("{:<20}".format(""), end='')
            for j in range(len(seq)):

                if (j <= seq_num):
                    print("{:>3}".format(frame_sequence[j][i]), end='')
            print()
    print('\n\n')
    print("Page Faults: ", page_faults)
    waitbuffer = input("Enter anything to go back to menu screen:")


def LRU(seq, frame_size):
    frames = []
    for indx in range(frame_size):
        frames.append('-')

    frame_curr_size = 0
    frame_sequence = []
    counter = 0
    page_faults = 0
    current_check_frame = -1
    for pgno in seq:
        current_check_frame += 1
        if pgno not in frames:
            page_faults += 1
            #             print("current page is : ",pgno)
            if frame_curr_size == frame_size:
                # lru algo
                indx = current_check_frame
                for cur_frame in frames:
                    #                     print("current Frame is : ", cur_frame, " with index : ",
                    #                           listrindex(seq[:current_check_frame], cur_frame))
                    if indx > listrindex(seq[:current_check_frame], cur_frame):
                        indx = listrindex(seq[:current_check_frame], cur_frame)
                ele = seq[indx]
                #                 print("element to be deleted is : ",ele)
                indx = frames.index(ele)
                frames[indx] = pgno
                frame_sequence.append(frames.copy())
            else:
                frames[counter] = pgno
                counter += 1
                counter = counter % frame_size
                frame_curr_size += 1
                frame_sequence.append(frames.copy())

        else:
            frame_sequence.append(frames.copy())

    for seq_num in range(len(seq)):
        print("\n" * 2)
        time.sleep(0.1)
        clear_output(wait=True)
        print("\n\n LRU : ")
        print("{:<20}".format("Sequence : "), end='')
        for seq_item in seq:
            print("{:>3}".format(seq_item), end='')
        print('\n')
        for i in range(len(frames)):
            print("{:<20}".format(""), end='')
            for j in range(len(seq)):

                if (j <= seq_num):
                    print("{:>3}".format(frame_sequence[j][i]), end='')
            print()
    print('\n\n')
    print("Page Faults: ", page_faults)
    waitbuffer = input("Enter anything to go back to menu screen:")


def MRU(seq, frame_size):
    frames = []
    for indx in range(frame_size):
        frames.append('-')

    frame_curr_size = 0
    frame_sequence = []
    counter = 0
    page_faults = 0
    current_check_frame = -1
    for pgno in seq:
        current_check_frame += 1
        if pgno not in frames:
            page_faults += 1
            #             print("current page is : ",pgno)
            if frame_curr_size == frame_size:
                # lru algo
                indx = 0
                for cur_frame in frames:
                    #                     print("current Frame is : ", cur_frame, " with index : ",
                    #                           listrindex(seq[:current_check_frame], cur_frame))
                    if indx < listrindex(seq[:current_check_frame], cur_frame):
                        indx = listrindex(seq[:current_check_frame], cur_frame)
                ele = seq[indx]
                #                 print("element to be deleted is : ",ele)
                indx = frames.index(ele)
                frames[indx] = pgno
                frame_sequence.append(frames.copy())
            else:
                frames[counter] = pgno
                counter += 1
                counter = counter % frame_size
                frame_curr_size += 1
                frame_sequence.append(frames.copy())

        else:
            frame_sequence.append(frames.copy())

    for seq_num in range(len(seq)):
        print("\n" * 2)
        time.sleep(0.1)
        clear_output(wait=True)
        print("\n\n MRU : ")
        print("{:<20}".format("Sequence : "), end='')
        for seq_item in seq:
            print("{:>3}".format(seq_item), end='')
        print('\n')
        for i in range(len(frames)):
            print("{:<20}".format(""), end='')
            for j in range(len(seq)):

                if (j <= seq_num):
                    print("{:>3}".format(frame_sequence[j][i]), end='')
            print()
    print('\n\n')
    print("Page Faults: ", page_faults)
    waitbuffer = input("Enter anything to go back to menu screen:")


def Optimal(seq, frame_size):
    frames = []
    for indx in range(frame_size):
        frames.append('-')

    frame_curr_size = 0
    frame_sequence = []
    counter = 0
    page_faults = 0
    current_check_frame = -1
    for pgno in seq:
        current_check_frame += 1
        #         print("current page is : ",pgno)
        if pgno not in frames:
            page_faults += 1
            if frame_curr_size == frame_size:
                # algo
                indx = current_check_frame
                for cur_frame in frames:
                    #                     print("current Frame is : ", cur_frame)
                    #                     if seq.index(cur_frame,current_check_frame ) == -1:
                    if cur_frame not in seq[current_check_frame:]:
                        # this element will never arive, so can remove this
                        ele = cur_frame
                        break

                    else:
                        #                         print(" with index : ",
                        #                           seq.index(cur_frame,current_check_frame ))
                        if indx < seq.index(cur_frame, current_check_frame):
                            indx = seq.index(cur_frame, current_check_frame)
                        ele = seq[indx]
                #                 print("element to be deleted is : ",ele)
                indx = frames.index(ele)
                frames[indx] = pgno
                frame_sequence.append(frames.copy())
            else:
                frames[counter] = pgno
                counter += 1
                counter = counter % frame_size
                frame_curr_size += 1
                frame_sequence.append(frames.copy())

        else:
            frame_sequence.append(frames.copy())

    for seq_num in range(len(seq)):
        print("\n" * 2)
        time.sleep(0.1)
        clear_output(wait=True)
        print("\n\n Optimal : ")
        print("{:<20}".format("Sequence : "), end='')
        for seq_item in seq:
            print("{:>3}".format(seq_item), end='')
        print('\n')
        for i in range(len(frames)):
            print("{:<20}".format(""), end='')
            for j in range(len(seq)):

                if (j <= seq_num):
                    print("{:>3}".format(frame_sequence[j][i]), end='')
            print()
    print('\n\n')
    print("Page Faults: ", page_faults)
    waitbuffer = input("Enter anything to go back to menu screen:")


def page():
    m=0
    while True:
        print("Enter Sequence (space seperated values) : ")
        seq_raw = input()
        seq = seq_raw.split(' ')

        print("Sequence is :")
        print(seq)
        # error Handling if input is not integers, maybe menu based program

        print("Enter Data Frames : ")
        frame_size = int(input())
        print(frame_size)
        # error handling again , frames only int
        # FCFS(seq,frame_size)

        #          MRU(seq, frame_size)

        while True:
            print(
                "Algorithms:\n1.First In First Out\n2.Least Recently Used\n3.Most Recently Used\n4.Optimal\n5. To exit ")
            choice = input()

            if choice == '1':
                FIFO(seq, frame_size)
            elif choice == '2':
                LRU(seq, frame_size)
            elif choice == '3':
                MRU(seq, frame_size)
            elif choice == '4':
                Optimal(seq, frame_size)
            elif choice == '5':
                m=1
                break
            else:
                print("invalid Choice. Enter Again")
        if m==1:
            break
        else:
            continue
        clear_output(wait=True)

