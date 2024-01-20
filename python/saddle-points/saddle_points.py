def saddle_points(matrix):
    if len(matrix) <= 0:
        return []
    
    validate_matrix(matrix)
    
    candidates = []
    tallest_trees_in_rows = []
    shortest_trees_in_columns = []
    
    # Walk rows finding tallest trees
    for i, row in enumerate(matrix):
        tallest_in_row = max(row)
        tallest_trees_in_rows.append({"row": i+1, "column": row.index(tallest_in_row)+1})

    # Walk columns based on length of first row, finding shortest in each column
    for i in range(0, len(matrix)):
        column = [row[i] for row in matrix]
        
        shortest_in_column = min(column)
        shortest_trees_in_columns.append({"row": column.index(shortest_in_column)+1, "column": i+1})
            
        # column = []
    
    # Do a set intersection on tallest_trees_in_rows and shortest_trees_in_columns?
    print("Tallest trees in rows: ", tallest_trees_in_rows)
    print("Shortest trees in columns: ", shortest_trees_in_columns)
    
    for tree in tallest_trees_in_rows:
        if tree in shortest_trees_in_columns:
            candidates.append(tree)
    
    return candidates

def validate_matrix(matrix):
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise ValueError("irregular matrix")
    
    return True


[8, 7, 9],
[6, 7, 6],
[3, 2, 5]