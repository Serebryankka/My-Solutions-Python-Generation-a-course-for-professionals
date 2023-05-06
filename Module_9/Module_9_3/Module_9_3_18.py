def print_operation_table(operation, rows, cols):
    mat = [[str(operation(j, i)).ljust(3) for i in range(1, cols + 1)] for j in range(1, rows + 1)]
    for i in mat:
        print(*i)
        
