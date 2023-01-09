print ("Round Robin Scheduling Algorithm By: \n Omar Madbouly & Muhammad Ashraf \n Please Give us bonus! :'( we need it \n\n")

def roundRobin():
    
    #Take the number of processes from the user 
    n = int(input("What is the number of processes:"))
    
    #Define processes,  
    processes = []
    # Initializing values, Total Time, and Total Time Cnted 
    TT = 0
    TTC = 0
    # Variables for storing values, Waiting Time, and Turnaround Time
    WT = []
    TAT = []
    
    for i in range(n):
        print("\n\nProcess #" + str(i+1))
        
        # Reading input from user (Arrival Time and Burst Time and Remaining Time)
        AT = int(input("What is the process arrivalTime: "))
        BT = int(input("What is the process burstTime: "))
        RT = BT
        # Assigning as a list
        processes.append([AT, BT, RT, 0])
        # Updating total time
        TT = TT + BT
    
    # Reading time quantum
    timeQuantum = int(input("\n\nEnter time quantum: "))
    
    
    # Implementing Round Robin

    while TT != 0:
        # Iterating over processes
        for i in range(len(processes)):
            # checking remaining time
            if processes[i][2] <= timeQuantum and processes[i][2] >= 0:
                TTC = TTC + processes[i][2]
                TT = TT - processes[i][2]
                # Process completed its execution
                processes[i][2] = 0
            elif processes[i][2] > 0:
                # Updating remaining time
                processes[i][2] = processes[i][2] - timeQuantum
                TT = TT - timeQuantum
                TTC = TTC + timeQuantum
            if processes[i][2] == 0 and processes[i][3] != 1:
                # Calculating statistics
                waitTime.append(TTC - processes[i][0] - processes[i][1])
                TAT.append(TTC - processes[i][0])
                # Time Calculation completed
                processes[i][3] = 1
    
    # Printing header
    print("\n%-15s %-15s %-10s\n\n"%("Process ID", "Waiting Time", "Turnaround Time"))
    for i in range(len(processes)):
        print("\t%-10d %-15.2f \t %-10.2f"%(i, WT[i], TAT[i]))
    # Printing Result
    print("\nAverage Waiting Time is ", (sum(WT)/n))
    print("\nAverage Turnaround Time is ", (sum(WT)/n))

# Calling function
roundRobin()