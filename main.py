from memg import memorymanagement
from BankersAlgo_ import inputBanker
from Pagereplacementalgo import page
from processschedulling import process
while (True):
    print("Choose Among the following options :\nEnter 1 for Using Bankers Algorithm"
          "\nEnter 2 for Using Memory Management Algorithm\nEnter 3 for Using Page Replacement Algorithm\n"
          "Enter 4 for Using Page Scheduling Algorithm"
          "Enter 5 for Exiting the Program\n")
    n=int(input("Enter the Option : "))

    if n==1:
        inputBanker()
    elif n==2:
        memorymanagement()
    elif n==3:
        page()
    elif n==4:
        process()
    elif n==5:
        break
    else:
        print("\nIncorrect Option Selected.Please Re-enter the Options\n")

