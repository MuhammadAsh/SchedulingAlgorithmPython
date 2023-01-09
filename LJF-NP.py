print ("LJF-NP Scheduling Algorithm By: \n Omar Madbouly & Muhammad Ashraf \n Please Give us bonus! :'( we need it \n\n")

def findWaitingTime(processes, n,
                    bt, wt):
 
    # waiting time for
    # first process is 0
    wt[0] = 0
 
    # calculating waiting time
    for i in range(1, n ):
        wt[i] = bt[i - 1] + wt[i - 1]
 
# Function to calculate turn
# around time
def findTurnAroundTime(processes, n,
                       bt, wt, tat):
 
    # calculating turnaround
    # time by adding bt[i] + wt[i]
    for i in range(n):
        tat[i] = bt[i] + wt[i]
 
# Function to calculate
# average time
def findavgTime( processes, n, bt):
 
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0
 
    # Function to find waiting
    # time of all processes
    findWaitingTime(processes, n, bt, wt)
 
    # Function to find turn around
    # time for all processes
    findTurnAroundTime(processes, n,
                       bt, wt, tat)
 
    # Display processes along
    # with all details
    print( "Processes Burst time " +
                  " Waiting time " +
                " Turn around time")
 
    # Calculate total waiting time
    # and total turn around time
    for i in range(n):
     
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" " + str(i + 1) + "\t\t" +
                    str(bt[i]) + "\t " +
                    str(wt[i]) + "\t\t " +
                    str(tat[i]))
 
    print( "Average waiting time = "+
                   str(total_wt / n))
    print("Average turn around time = "+
                     str(total_tat / n))
 
# Driver code
if __name__ =="__main__":
     
    # process id's
    #processes = [ 0, 1, 2, 3]
    n = int(input("What is the number of processes:"))
    processes = []
    burst_time = []
    

    for i in range (n):
        
        # Reading values of burst time and priority 

        print ("\n\nProcesses No." + str(i+1))

        BT = int(input("Enter Process Busrt Time:"))

        #Assign to a list 
        processes.append(i)
 
        # Burst time of all processes
        burst_time.append(BT)
    print (burst_time)
 
    findavgTime(processes, n, burst_time)