class Process:
    def __init__(self, pid, at, bt):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.ct = 0
        self.tat = 0
        self.wt = 0


def print_table(processes):
    print("\nPID\tAT\tBT\tCT\tTAT\tWT")
    for p in processes:
        print(f"{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")


# ================= FCFS =================
def fcfs(processes):
    processes.sort(key=lambda x: x.at)
    time = 0
    gantt = []

    for p in processes:
        if time < p.at:
            gantt.append(("Idle", time, p.at))
            time = p.at

        start = time
        time += p.bt
        p.ct = time
        p.tat = p.ct - p.at
        p.wt = p.tat - p.bt

        gantt.append((p.pid, start, time))

    print("\n--- FCFS ---")
    print_table(processes)

    avg_wt = sum(p.wt for p in processes) / len(processes)
    avg_tat = sum(p.tat for p in processes) / len(processes)

    print(f"\nAverage WT = {avg_wt:.2f}")
    print(f"Average TAT = {avg_tat:.2f}")

    print("\nGantt Chart:")
    for g in gantt:
        print(f"| {g[0]} ", end="")
    print("|")

    for g in gantt:
        print(f"{g[1]}\t", end="")
    print(f"{gantt[-1][2]}")


# ================= SJF =================
def sjf(processes):
    processes = sorted(processes, key=lambda x: (x.at, x.bt))
    completed = []
    time = 0
    ready = []
    gantt = []

    processes_copy = processes[:]

    while processes_copy or ready:
        while processes_copy and processes_copy[0].at <= time:
            ready.append(processes_copy.pop(0))

        if not ready:
            time += 1
            continue

        ready.sort(key=lambda x: x.bt)
        p = ready.pop(0)

        start = time
        time += p.bt

        p.ct = time
        p.tat = p.ct - p.at
        p.wt = p.tat - p.bt

        gantt.append((p.pid, start, time))
        completed.append(p)

    print("\n--- SJF (Non-Preemptive) ---")
    print_table(completed)

    avg_wt = sum(p.wt for p in completed) / len(completed)
    avg_tat = sum(p.tat for p in completed) / len(completed)

    print(f"\nAverage WT = {avg_wt:.2f}")
    print(f"Average TAT = {avg_tat:.2f}")

    print("\nGantt Chart:")
    for g in gantt:
        print(f"| {g[0]} ", end="")
    print("|")

    for g in gantt:
        print(f"{g[1]}\t", end="")
    print(f"{gantt[-1][2]}")


# ================= MAIN =================
n = int(input("Enter number of processes: "))
processes = []

for i in range(n):
    at = int(input(f"Enter Arrival Time for P{i+1}: "))
    bt = int(input(f"Enter Burst Time for P{i+1}: "))
    processes.append(Process(f"P{i+1}", at, bt))

# Copy list for separate execution
import copy
fcfs(copy.deepcopy(processes))
sjf(copy.deepcopy(processes))