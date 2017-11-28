def create_schedule_from_input(input):
    """
    Creates a schedule of instructions from user input
    :param input: user inputted set of instructions, space-separated
    :return: a set of instructions (schedule) of the form (R/W, num, data_item)
    """

    instructions_text = input.split()
    schedule = []
    for instruction_text in instructions_text:
        sides = instruction_text.split('(')
        read_or_write = sides[0][0]
        number = sides[0][1:]
        length_data_item_text = len(sides[1]) - 1
        data_item = sides[1][:length_data_item_text]
        instruction = (read_or_write, number, data_item)
        schedule.append(instruction)

    return schedule

graph_dict = {}

def cycle(t, visited):
    global graph_dict
    if t in visited:
        return visited + [t]
    newlist = visited + [t]
    for j in graph_dict[t]:
        return cycle(j, newlist)
    return None

def is_conflict_serializable(schedule):
    global graph_dict
    for i in range(len(schedule)):
        graph_dict[schedule[i][1]] = set()
    for i in range(len(schedule)):
        curr = schedule[i]
        if curr[0].upper() == "W":
            for j in range(i+1, len(schedule)):
                inst = schedule[j]
                # if different transactions
                if curr[1] != inst[1] and curr[2] == inst[2]:
                    graph_dict[curr[1]].add(inst[1])
        if curr[0].upper() == "R":
            for j in range(i+1, len(schedule)):
                inst = schedule[j]
                if curr[1] != inst[1] and curr[2]==inst[2] and inst[0].upper() == "W":
                    graph_dict[curr[1]].add(inst[1])
    for i in graph_dict:
        print(i, ":", graph_dict[i])
    for i in graph_dict:
        if cycle(i, []):
            return False
    return True

def create_serial_equiv_schedule():
    return set()


def create_at_least_one_cycle():
    for i in graph_dict:
        if cycle(i, []):
            return cycle(i, [])


def print_schedule(schedule):
    schedule_reformatted = set()
    for instruction in schedule:
        instruction_reformatted = instruction[0] + instruction[1] + '(' + instruction[2] + ')'
        schedule_reformatted.add(instruction_reformatted)
    print(schedule_reformatted)


if __name__ == '__main__':
    prompt = 'Pass in a list of instructions on one line, separated by a space. Examples of instructions are R1(A) and W2(B).\n'
    schedule = create_schedule_from_input(input(prompt))
    print(schedule)
    cs = is_conflict_serializable(schedule)
    print("Conflict Serializable:", cs)
    if cs:
        create_serial_equiv_schedule()
    else:
        print("A cycle:", create_at_least_one_cycle())