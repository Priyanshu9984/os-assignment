# -------------------------------
# FCFS
# -------------------------------
def fcfs(requests, head):
    seek_time = 0
    sequence = [head]

    for r in requests:
        seek_time += abs(head - r)
        head = r
        sequence.append(head)

    return seek_time, sequence


# -------------------------------
# SSTF
# -------------------------------
def sstf(requests, head):
    seek_time = 0
    sequence = [head]
    req = requests.copy()

    while req:
        nearest = min(req, key=lambda x: abs(x - head))
        seek_time += abs(head - nearest)
        head = nearest
        sequence.append(head)
        req.remove(nearest)

    return seek_time, sequence


# -------------------------------
# SCAN
# -------------------------------
def scan(requests, head, disk_size):
    seek_time = 0
    sequence = [head]

    left = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r >= head])

    # Move right
    for r in right:
        seek_time += abs(head - r)
        head = r
        sequence.append(head)

    # Go to end
    seek_time += abs(head - (disk_size - 1))
    head = disk_size - 1
    sequence.append(head)

    # Move left
    for r in reversed(left):
        seek_time += abs(head - r)
        head = r
        sequence.append(head)

    return seek_time, sequence


# -------------------------------
# C-SCAN
# -------------------------------
def cscan(requests, head, disk_size):
    seek_time = 0
    sequence = [head]

    left = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r >= head])

    # Move right
    for r in right:
        seek_time += abs(head - r)
        head = r
        sequence.append(head)

    # Jump to start
    seek_time += abs(head - (disk_size - 1))
    head = 0
    sequence.append(disk_size - 1)
    sequence.append(head)

    # Move left side
    for r in left:
        seek_time += abs(head - r)
        head = r
        sequence.append(head)

    return seek_time, sequence


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    head = 53
    disk_size = 200

    print("Requests:", requests)
    print("Initial Head:", head)

    fcfs_seek, fcfs_seq = fcfs(requests, head)
    sstf_seek, sstf_seq = sstf(requests, head)
    scan_seek, scan_seq = scan(requests, head, disk_size)
    cscan_seek, cscan_seq = cscan(requests, head, disk_size)

    print("\nFCFS Seek Time:", fcfs_seek)
    print("Sequence:", fcfs_seq)

    print("\nSSTF Seek Time:", sstf_seek)
    print("Sequence:", sstf_seq)

    print("\nSCAN Seek Time:", scan_seek)
    print("Sequence:", scan_seq)

    print("\nC-SCAN Seek Time:", cscan_seek)
    print("Sequence:", cscan_seq)
