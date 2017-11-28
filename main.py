def create_schedule_from_input(input):
    """Creates a schedule of instructions from user input
    
    Args:
        input (str): user inputted set of instructions, space-separated

    Returns:
        list: a list of instructions (schedule) of the form (R/W, num, data_item)
    """
    # normalize commas to spaces, works with both
    instructions_text = input.replace(",", " ")
    instructions_text = instructions_text.split()
    schedule = []
    for instruction_text in instructions_text:
        instruction_text = instruction_text.replace("(", " ")
        instruction_text = instruction_text.replace(")", " ")
        sides = instruction_text.split()
        read_or_write = sides[0][0]
        number = sides[0][1:]
        data_item = sides[1]
        instruction = (read_or_write, number, data_item)
        schedule.append(instruction)
    return schedule

graph_dict = {}

def cycle(t, visited):
    """Recursively searches for a cycle in the graph
    
    Args:
        t(int): a node to start at
        visited(list): a list of previously visited nodes
    
    Returns:
        list OR None: a list of visited nodes, ending in a cycle OR None
    """
    global graph_dict
    if t in visited:
        return visited + [t]
    newlist = visited + [t]
    for j in graph_dict[t]:
        return cycle(j, newlist)
    return None

def is_conflict_serializable(schedule):
    """Tests if a given schedule is conflict serializable

    Args:
        schedule(list): a list of instructions (schedule) of the form (R/W, num, data_item)

    Returns:
        bool: True if the schedule is conflict serializable, False otherwise
    """
    global graph_dict
    for i in range(len(schedule)):
        graph_dict[schedule[i][1]] = set()
    for i in range(len(schedule)):
        curr = schedule[i]
        if curr[0].upper() == "W":
            for j in range(i+1, len(schedule)):
                inst = schedule[j]
                # if different transactions on same data item
                if curr[1] != inst[1] and curr[2] == inst[2]:
                    graph_dict[curr[1]].add(inst[1])
        if curr[0].upper() == "R":
            for j in range(i+1, len(schedule)):
                inst = schedule[j]
                # if different transactions on same data item AND write's
                if curr[1] != inst[1] and curr[2]==inst[2] and inst[0].upper() == "W":
                    graph_dict[curr[1]].add(inst[1])
    # prints out nodes and edges
    #for i in graph_dict:
        #print(i, ":", graph_dict[i])
    for i in graph_dict:
        if cycle(i, []):
            return False
    return True

def create_serial_equiv_schedule(schedule):
    """Generates a serial equivalent schedule

    Args:
        schedule(list): a list of instructions (schedule) of the form (R/W, num, data_item)

    Returns:
        list: a list of instructions (schedule) of the form (R/W, num, data_item)
    """
    global graph_dict
    graph = graph_dict
    equiv_schedule = []
    # find nodes with no incoming edges
    no_inc_edge = set(graph.keys())
    for i in graph:
        for j in graph[i]:
            if j in no_inc_edge:
                no_inc_edge.remove(j)
    while len(no_inc_edge) > 0:
        n = no_inc_edge.pop()
        equiv_schedule.append(n)
        graph[n] = set()
        new_no_inc_edge = set(graph.keys())
        for i in graph:
          for j in graph[i]:
                if j in new_no_inc_edge:
                    new_no_inc_edge.remove(j)
        for i in equiv_schedule:
            if i in new_no_inc_edge:
                new_no_inc_edge.remove(i)
        no_inc_edge = new_no_inc_edge
    final_schedule = []
    for t in equiv_schedule:
        for inst in schedule:
            if inst[1] == t:
                final_schedule.append(inst)
    return final_schedule
    
        

def create_at_least_one_cycle():
    """Recursively searches for a cycle in the graph, returning the first one found
    
    Returns:
        list OR None: a list of visited nodes, ending in a cycle OR None
    """
    global graph_dict
    for i in graph_dict:
        if cycle(i, []):
            return cycle(i, [])


def print_schedule(schedule):
    """Prints out a given schedule in human-readable form

    Args:
        schedule(list): a list of instructions (schedule) of the form (R/W, num, data_item)
    """
    cell_width = 9 + max([len(inst[2]) for inst in schedule])
    transactions = sorted(list(set([inst[1] for inst in schedule])))
    total_width = len(transactions) * cell_width + len(transactions) + 1
    # if total_width is small, create table. Otherwise, output string
    if total_width < 80:
        seperator = "+" 
        seperator += "".join(["-"*cell_width + "+" for i in range(len(transactions))])
        header = "|"
        header += "".join([" t"+t+" "*(cell_width-len(t)-2) + "|" for t in transactions])
        print()
        print(seperator)
        print(header)
        print(seperator)
        for i in schedule:
            t_pos = transactions.index(i[1])
            row = "|"
            row += "".join([" "*cell_width + "|" for i in range(t_pos)])
            if i[0].upper() == "W":
                row += " Write(" + i[2] + ")" + " "*(cell_width-8-len(i[2])) + "|"
            else:
                row += " Read(" + i[2] + ")" + " "*(cell_width-7-len(i[2])) + "|"
            rem = len(transactions)-1-t_pos
            row += "".join([" "*cell_width + "|" for i in range(rem)])
            print(row)
            print(seperator)
    else:
        schedule_reformatted = []
        for inst in schedule:
            inst_reformatted = "{}{}({})".format(inst[0],inst[1],inst[2])
            schedule_reformatted.append(inst_reformatted)
        for i in schedule_reformatted:
            print(i, end=" ")
    print()

def print_cycle(cycle):
    """Prints out a given cycle in human-readable form

    Args:
        cycle(list): a list of ordered, cylic transactions
    """
    while [cycle.count(i) for i in cycle][0] == 1:
        cycle = cycle[1:]
    while [cycle.count(i) for i in cycle][-1] == 1:
        cycle = cycle[:-1]
    for t in cycle[:-1]:
        print("t"+t, end=" -> ")
    print("t"+cycle[-1])

if __name__ == '__main__':
    prompt = 'Pass in a list of instructions on one line, separated by a space. Examples of instructions are R1(A) and W2(B).\n'
    schedule = create_schedule_from_input(input(prompt))
    #print(schedule)
    cs = is_conflict_serializable(schedule)
    print("Conflict Serializable:", cs)
    if cs:
        print("Serializable Equivalent Schedule", end=": ")
        print_schedule(create_serial_equiv_schedule(schedule))
    else:
        print("A cycle", end=": ")
        print_cycle(create_at_least_one_cycle())
