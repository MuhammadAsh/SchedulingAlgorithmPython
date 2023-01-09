# SchedulingAlgorithmPython
Implement Scheduling Algorithms Using Python


CPU Scheduling Algorithms
CPU scheduling is a process to determine which process a CPU will have to complete while another process is suspended. The main task of CPU scheduling is to ensure that whenever the CPU is idle, the operating system selects one of the available processes in the queue ready to run. The selection process will be performed by the CPU programmer. Select one of the processes in memory that is ready to complete.

 
Section 1: First come first serve (FCFS) – Non-Preemptive 
Definition
First Come First Served is the complete FCFS form. It is the easiest and simplest CPU scheduling algorithm. In this type of algorithm, the process that requests the CPU first gets the CPU allocation. This scheduling method can be managed with a FIFO queue.
As the process enters the queue smoothly, its PCB (Process Control Block) is connected to the queue of the queue. So when a CPU is free, it must be allocated to the process at the beginning of the queue.
Characteristics of the FCFS method:
•	It offers a preemptive and non-preemptive scheduling algorithm.
•	Jobs are always done in order of arrival.
•	It is easy to implement and use.
•	However, this method has weak performance, and the overall wait time is quite high.
Code Logic: 
•	At first, we take the input from the user 
•	Then, we calculate the waiting time and turn-around time for each process based on the arrival time 
•	Then, we calculate the average waiting time and average turn-around time for all processes
Code Snippet: 
 
Results Snippet: 
  
Section 2: Shortest Job First (SJF) – Preemptive/ Non-Preemptive 
Definition
SJF is a full form of scheduling algorithm (shortest job first) in which the process with the shortest running time should be selected for subsequent execution. This programming method can be preemptive or non-preemptive. Greatly reduces the average wait time for other processes waiting for completion.
Characteristics of the SJF method:
•	It relates to each job as a unit of time to complete.
•	In this mode, when the CPU is available, the next process or job with the shortest completion time will be executed first.
•	It is implemented with a non-preemptive policy.
•	This algorithm method is useful for batch processing, when waiting for jobs to finish is not critical.
•	Improve job throughput by offering shorter, first-to-complete jobs, most of which have a shorter turnaround time.
Code Logic: 
•	At first, we take the input from the user 
•	Then, we sort which process will be processes first:
o	In case of Preemptive scheduling, we prioritize the processes with shorter burst time over current process in progress 
o	In case of Non-Preemptive scheduling, we prioritize the current process in progress 
•	Then, we calculate the waiting time and turn-around time for each process based on the arrival time 
•	Then, we calculate the average waiting time and average turn-around time for all processes
SJF- NP Code Snippet: 
 
SJF- NP Results Snippet: 
 
SJF- P Code Snippet: 
 
SJF- P Results Snippet: 
 
Section 3: Longest Job First (LJF) – Non-Preemptive 
Definition
Longest Job First (LJF) is a non-preemptive scheduling algorithm. This algorithm is based on the burst time of the processes. Processes are queued based on their burst times, that is, in descending order of burst times. As the name suggests, this algorithm is because the process with the highest burst time is processed first. The burst time is considered only for those processes that have reached the system up to that moment. Its preemptive version is called the Longest Remaining Time First (LRTF) algorithm. 
Characteristics of the LJF method:
•	Among all the processes waiting in a queue, the CPU is always allocated to the process that has the highest burst time.
•	If two processes have the same burst time, the tie is broken using FCFS , that is, the process that arrived first is processed first. 
•	LJF CPU Scheduling can be both preemptive and non-preemptive.
 
 
 
Section 4: Priority Scheduling Algorithm – Non-Preemptive 
Definition
Priority scheduling is a method of scheduling processes based on priority. In this mode, the scheduler selects the tasks to be executed based on priority.
Characteristics of the Priority method:
Priority scheduling helps the operating system to include priority tasks. Higher priority processes must complete first, but jobs with equal priorities are performed on a precise robin or FCFS basis. Priority can be determined based on memory requirements, timing requirements, etc.
Code Logic: 
•	At first, we take the input from the user 
•	Then, we sort the processes based on priority 
•	Then, we calculate the waiting time and turn-around time for each process based on the arrival time 
•	Then, we calculate the average waiting time and average turn-around time for all processes
Priority Scheduling Code Snippet: 
 
Priority Scheduling Results Snippet: 
 
 
Section 5: Round Robin Scheduling Algorithm – Preemptive 
Definition
The exact robin is the oldest and simplest programming algorithm. The name of this algorithm comes from the round robin principle, where everyone, in turn, gets an equal share of something. It is mainly used to program multitasking algorithms. This algorithm method helps to complete processes without starvation.
Characteristics of the Round-Robin method:
•	The clock-driven round robin is a hybrid model
•	There must be at least a slice of time allocated to process a specific task. However, it may vary for different processes.
•	It is a real-time system that responds to the event within a specific time limit.
Round-Robin Code Snippet: 
 
Round-Robin Results Snippet: 
