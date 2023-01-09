print ("Priority Scheduling Algorithm By: \n Omar Madbouly & Muhammad Ashraf \n Please Give us bonus! :'( we need it \n\n")
def Priority():
    
    #Take the number of processes from the user 
    n = int(input("What is the number of processes:"))
    
    #Define processes, Waiting Time, and BurstTime 
    processes = []
    WT = []
    TAT = []

    for i in range (n):
        
        # Reading values of burst time and priority 

        print ("\n\nProcesses No." + str(i+1))

        BT = int(input("Enter Process Busrt Time:"))
        P = int(input("Enter Process Priority: "))
        
        #Assign to a list 
        processes.append([BT, P])
        
    # Sorting processes based on Priority
    for i in range(n):
    # Initially store 0
        WT.append(0)
    for j in range(n):
        # comparing priority
        if(processes[i][1] < processes[j][1]):
            # Swapping processes
            temp = processes[i]
            processes[i] = processes[j]
            processes[j] = temp
            
    # Iterating over processes
    for i in range(1, n):
        WT[i] = 0
    for j in range(i):
    # Accumulating waiting time
        WT[i] = WT[i] + processes[j][0]
    
    # Calculating turnaround time
    for i in range(n):
        TAT.append(processes[i][0] + WT[i])
    
    # Printing header (because we deserve bonus)
    print("\n%-15s %-15s %-15s %-10s\n"%("Process ID", "Burst Time", "Waiting Time", "Turnaround Time"))
    for i in range(len(processes)):
        print("\t%-10d %-15d %-15d \t %-10d"%(i, processes[i][0], WT[i], TAT[i]))
    
    # Printing Result
    print("\nAverage Waiting Time is ", (sum(WT)/n))
    print("\nAverage Turnaround Time is ", (sum(WT)/n))

# Calling function
Priority()
