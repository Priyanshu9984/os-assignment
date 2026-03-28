def calculate_need(max_matrix, allocation):
    n = len(max_matrix)
    m = len(max_matrix[0])

    need = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            need[i][j] = max_matrix[i][j] - allocation[i][j]

    return need


def bankers_algorithm(n, m, allocation, max_matrix, available):
    need = calculate_need(max_matrix, allocation)

    print("\nNeed Matrix:")
    for row in need:
        print(row)

    finish = [False] * n
    safe_sequence = []
    work = available[:]

    while len(safe_sequence) < n:
        found = False

        for i in range(n):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(m)):
                    for j in range(m):
                        work[j] += allocation[i][j]

                    safe_sequence.append(f"P{i}")
                    finish[i] = True
                    found = True

        if not found:
            break

    if len(safe_sequence) == n:
        print("\nSystem is in SAFE state")
        print("Safe Sequence:", " -> ".join(safe_sequence))
    else:
        print("\nSystem is NOT in safe state")


# ================= MAIN =================

n = int(input("Enter number of processes: "))
m = int(input("Enter number of resource types: "))

print("\nEnter Allocation Matrix:")
allocation = []
for i in range(n):
    row = list(map(int, input(f"P{i}: ").split()))
    allocation.append(row)

print("\nEnter Maximum Matrix:")
max_matrix = []
for i in range(n):
    row = list(map(int, input(f"P{i}: ").split()))
    max_matrix.append(row)

print("\nEnter Available Resources:")
available = list(map(int, input().split()))

bankers_algorithm(n, m, allocation, max_matrix, available)