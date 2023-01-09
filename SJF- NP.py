print ("SJF-NP Scheduling Algorithm By: \n Omar Madbouly & Muhammad Ashraf \n Please Give us bonus! :'( we need it \n\n")

def getOrder(tasks):
    import heapq
    for i, p in (enumerate(tasks)):
        p.append(i)
    
    tasks.sort(key = lambda x: x[0])
    i, time = 0, tasks[0][0]
    minHeap, res = [], []
    tat = [0]*len(tasks)
    wat = [0]*len(tasks)
    
    while minHeap or i < len(tasks):
        while i < len(tasks) and time >= tasks[i][0]:
            heapq.heappush(minHeap, [tasks[i][1], tasks[i][0], tasks[i][2]]) #tasks[i][1]-burst time, tasks[i][0]-arr time, tasks[i][2]]-index
            i += 1
        
        if not minHeap:
            time = tasks[i][0]
        else:
            procTime, arrTime, ind = heapq.heappop(minHeap)
            time += procTime
            tat[ind] = time - arrTime
            wat[ind] = tat[ind] - procTime
            res.append(ind)
    
    print("Avg. Turn around time: ", sum(tat)/len(tat))
    print("Avg. Waiting time: ", sum(wat)/len(wat))
    return res

n = int(input("Enter no. of processes to be executed: "))
tasks = []
for i in range(n):
    tasks.append(list(map(int, input("Enter arrival and burst time: ").split())))
print("Completion Order: ", getOrder(tasks))