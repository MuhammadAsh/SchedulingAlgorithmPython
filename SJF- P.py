print ("SJF-P Scheduling Algorithm By: \n Omar Madbouly & Muhammad Ashraf \n Please Give us bonus! :'( we need it \n\n")

def getOrder(tasks):
    import heapq
    wat = [0]*len(tasks)
    for i, p in (enumerate(tasks)):
        p.append(i)
        wat[i] = p[1]
    
    tasks.sort(key = lambda x: x[0])
    i, time = 0, tasks[0][0]
    minHeap, res = [], []
    todo = len(tasks)
    tat = [0]*len(tasks)
   

    while todo:
        while i < len(tasks) and time >= tasks[i][0]:
            heapq.heappush(minHeap, [tasks[i][1], tasks[i][0], tasks[i][2]])
            i += 1
        
        if not minHeap:
            time = tasks[i][0]
        else:
            procTime, arrTime, ind = heapq.heappop(minHeap)
            time += 1 
            procTime -= 1 
            if procTime == 0:
                todo -= 1 
                tat[ind] = time - arrTime
                wat[ind] = tat[ind] - wat[ind]
                res.append(ind)
            else:
                heapq.heappush(minHeap, [procTime, arrTime, ind])
    
    print("Avg. Turnaround Time: ", sum(tat)/len(tat))       
    print("Avg. Waiting Time: ", sum(wat)/len(wat))       
    return res

n = int(input("Enter no. of processes to be executed: "))
tasks = []
for i in range(n):
    tasks.append(list(map(int, input("Enter arrival and burst time: ").split())))
print("Completion Order: ", getOrder(tasks))