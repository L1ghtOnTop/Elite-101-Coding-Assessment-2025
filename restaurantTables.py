def get_free_tables(tables):
    # Level 1: Returns a list of table IDs that are free in the current timeslot
    free_tables = []
    for i in range(1, len(tables[0])):  # Start from 1 because 0th index is for table labels
        if tables[1][i] == 'o':  # If the table is free its called 'o'
            free_tables.append(tables[0][i])  # Add the table label to the free tables list
    return free_tables


def find_one_table_for_size(tables, party_size):
    # Level 2: Returns the first table that can seat the party and is free.
    # If no table is found then returns none
    for i in range(1, len(tables[0])):  # Loop through tables
        table_label = tables[0][i]
        capacity = int(table_label.split('(')[1][:-1])  # Get the tables seating capacity
        if tables[1][i] == 'o' and capacity >= party_size:  # Check if its free and can seat the party
            return table_label  # Return the table label
    return None  # Return none if no suitable table is found


def find_all_tables_for_size(tables, party_size):
    # Level 3: Returns a list of all free tables that can seat at least 'party_size'.
    suitable_tables = []
    for i in range(1, len(tables[0])):  # Loops through tables
        table_label = tables[0][i]
        capacity = int(table_label.split('(')[1][:-1])  # Get the table's seating capacity
        if tables[1][i] == 'o' and capacity >= party_size:  # Check if it's free and can seat the party
            suitable_tables.append(table_label)  # Add it to the list of suitable tables
    return suitable_tables


def find_tables_including_combos(tables, party_size):
    # Level 4: Returns a list of single tables or adjacent table combinations that can seat 'party_size'.
    results = []
    for i in range(1, len(tables[0])):  # Loop through tables
        table_label = tables[0][i]
        capacity = int(table_label.split('(')[1][:-1])  # Get the table's seating capacity
        
        # If a single table is free and can seat the party, add it to the results
        if tables[1][i] == 'o' and capacity >= party_size:
            results.append((table_label,))  # Add single table as a tuple
        
        # Check for adjacent tables if a single table can't seat the party
        if i < len(tables[0]) - 1:  # Ensure there is a next table to check
            next_table_label = tables[0][i+1]
            next_capacity = int(next_table_label.split('(')[1][:-1])  # Get the next table's capacity
            if tables[1][i] == 'o' and tables[1][i+1] == 'o' and capacity + next_capacity >= party_size:
                results.append((table_label, next_table_label))  # Add the combo of adjacent tables
    
    return results


# Example data structure
restaurant_tables = [
    [0, 'T1(2)', 'T2(4)', 'T3(2)', 'T4(6)', 'T5(4)', 'T6(2)'],
    [1, 'o', 'o', 'o', 'o', 'o', 'o'],
    [2, 'o', 'o', 'o', 'o', 'o', 'o'],
    [3, 'o', 'o', 'o', 'o', 'o', 'o'],
    [4, 'o', 'o', 'o', 'o', 'o', 'o'],
    [5, 'o', 'o', 'o', 'o', 'o', 'o'],
    [6, 'o', 'o', 'o', 'o', 'o', 'o']
]

restaurant_tables2 = [
    [0, 'T1(2)', 'T2(4)', 'T3(2)', 'T4(6)', 'T5(4)', 'T6(2)'],
    [1, 'x', 'o', 'o', 'o', 'o', 'x'],
    [2, 'o', 'x', 'o', 'o', 'x', 'o'],
    [3, 'x', 'x', 'o', 'x', 'o', 'o'],
    [4, 'o', 'o', 'o', 'x', 'o', 'x'],
    [5, 'o', 'x', 'o', 'x', 'o', 'o'],
    [6, 'o', 'o', 'o', 'o', 'x', 'o']
]

# Test the functions with the restaurant_tables2 data
print("LEVEL 1: Free tables =", get_free_tables(restaurant_tables2))
print("LEVEL 2: One table for party size 2 =", find_one_table_for_size(restaurant_tables2, 2))
print("LEVEL 3: All tables for party size 2 =", find_all_tables_for_size(restaurant_tables2, 2))
print("LEVEL 4: Single or combined tables for party size 4 =", find_tables_including_combos(restaurant_tables2, 4))
