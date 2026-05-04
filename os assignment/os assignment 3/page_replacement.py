from collections import deque

# -------------------------------
# FIFO
# -------------------------------
def fifo(pages, capacity):
    memory = []
    faults = 0
    queue = deque()

    for page in pages:
        if page not in memory:
            faults += 1
            if len(memory) < capacity:
                memory.append(page)
                queue.append(page)
            else:
                old = queue.popleft()
                memory.remove(old)
                memory.append(page)
                queue.append(page)
    return faults


# -------------------------------
# LRU
# -------------------------------
def lru(pages, capacity):
    memory = []
    faults = 0

    for page in pages:
        if page not in memory:
            faults += 1
            if len(memory) < capacity:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
        else:
            memory.remove(page)
            memory.append(page)
    return faults


# -------------------------------
# OPTIMAL
# -------------------------------
def optimal(pages, capacity):
    memory = []
    faults = 0

    for i in range(len(pages)):
        if pages[i] not in memory:
            faults += 1
            if len(memory) < capacity:
                memory.append(pages[i])
            else:
                future = []
                for m in memory:
                    if m in pages[i+1:]:
                        future.append(pages[i+1:].index(m))
                    else:
                        future.append(float('inf'))
                memory[future.index(max(future))] = pages[i]
    return faults


# -------------------------------
# MRU
# -------------------------------
def mru(pages, capacity):
    memory = []
    faults = 0

    for page in pages:
        if page not in memory:
            faults += 1
            if len(memory) < capacity:
                memory.append(page)
            else:
                memory.pop()  # remove most recent
                memory.append(page)
        else:
            memory.remove(page)
            memory.append(page)
    return faults


# -------------------------------
# SECOND CHANCE
# -------------------------------
def second_chance(pages, capacity):
    memory = []
    ref = []
    pointer = 0
    faults = 0

    for page in pages:
        if page not in memory:
            faults += 1
            if len(memory) < capacity:
                memory.append(page)
                ref.append(1)
            else:
                while ref[pointer] == 1:
                    ref[pointer] = 0
                    pointer = (pointer + 1) % capacity
                memory[pointer] = page
                ref[pointer] = 1
                pointer = (pointer + 1) % capacity
        else:
            ref[memory.index(page)] = 1
    return faults


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    capacity = 3

    print("Page Reference String:", pages)
    print("Number of Frames:", capacity)

    print("\nFIFO Faults:", fifo(pages, capacity))
    print("LRU Faults:", lru(pages, capacity))
    print("Optimal Faults:", optimal(pages, capacity))
    print("MRU Faults:", mru(pages, capacity))
    print("Second Chance Faults:", second_chance(pages, capacity))
