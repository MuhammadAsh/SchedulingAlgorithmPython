print ("FCFS Scheduling Algorithm By: \n Omar Madbouly & Muhammad Ashraf \n Please Give us bonus! :'( we need it \n\n")

def FCFS():
    
    #Take the number of processes from the user 
    n= int(input('What is  the Number of processes: '))

    #create empty list of waiting time,turnaround time and brust time
    wt=[]
    tat=[]
    bt=[]

    wt.insert(0,0)

    totwt=0
    tottat=0

    #input from user
    for i in range(0,n):
        btime=int(input('Enter Burst time for process: '))
        bt.insert(i,btime)

    #find waiting time of each process
    for i in range(1,n):
        w=bt[i-1]+wt[i-1]
        wt.insert(i,w)

    #find turnaround time by adding bt[i] + wt[i]
    # find total waiting and turnaround time
    for i in range(0,n):
        turn_time=bt[i]+wt[i]
        tat.insert(i,turn_time)
        totwt=totwt+wt[i]
        tottat=tottat+tat[i]


    avgwt=float(totwt)/n
    avgtat=float(tottat)/n

    print("\n")
    print("Process\t Burst Time\t Waiting Time\t Turn Around Time")
    for i in range(0,n):
        print(str(i+1)+"\t\t"+str(bt[i])+"\t\t"+str(wt[i])+"\t\t"+str(tat[i]))
        print("\n")

    print("Average Waiting time is: "+str(round(avgwt,2)))
    print("Average Turn Arount Time is: "+str(round(avgtat,2)))
# Calling function
FCFS()