# Banker's safety algorithm implementation

def bankers_algorithm(processes, resources, allocation, maximum, available):
    need = []
    for i in range(processes):
        row = [] 
        for j in range(resources):
            row.append(maximum[i][j] - allocation[i][j])
        need.append(row)

    work = available[:]
    finish = [False] * processes
    safe_sequence = []

    while len(safe_sequence) < processes:
        found = False
        for i in range(processes):
            if not finish[i]:
                can_execute = True
                for j in range(resources):
                    if need[i][j] > work[j]:
                        can_execute = False
                        break

                if can_execute:
                    for j in range(resources):
                        work[j] += allocation[i][j]
                    finish[i] = True
                    safe_sequence.append(f"P{i}")
                    found = True

        if not found:
            break

    if len(safe_sequence) == processes:
        return True, safe_sequence, need
    else:
        return False, [], need


def read_matrix(rows, cols, name):
    matrix = []
    print(f"\nEnter {name} matrix:")
    for i in range(rows):
        while True:
            row = list(map(int, input(f"P{i}: ").split()))
            if len(row) == cols:
                matrix.append(row)
                break
            else:
                print(f"Enter exactly {cols} values.")
    return matrix


def main():
    processes = int(input("Enter number of processes: "))
    resources = int(input("Enter number of resources: "))

    allocation = read_matrix(processes, resources, "Allocation")
    maximum = read_matrix(processes, resources, "Maximum")

    while True:
        available = list(map(int, input("\nEnter Available Resources: ").split()))
        if len(available) == resources:
            break
        else:
            print(f"Enter exactly {resources} values.")

    safe, sequence, need = bankers_algorithm(
        processes, resources, allocation, maximum, available
    )

    print("\nNeed Matrix:")
    for i in range(processes):
        print(f"P{i}: {need[i]}")

    if safe:
        print("\nSystem is in SAFE state.")
        print("Safe Sequence:", " -> ".join(sequence))
    else:
        print("\nSystem is in DEADLOCK (UNSAFE) state.")


if __name__ == "__main__":
    main()
