def create_schedule_from_input(input):
    """
    Creates a schedule of instructions from user input
    :param input: user inputted set of instructions, space-separated
    :return: a set of instructions (schedule) of the form (R/W, num, data_item)
    """

    instructions_text = input.split()
    schedule = set()
    for instruction_text in instructions_text:
        sides = instruction_text.split('(')
        read_or_write = sides[0][0]
        number = sides[0][1:]
        length_data_item_text = len(sides[1]) - 1
        data_item = sides[1][:length_data_item_text]
        instruction = (read_or_write, number, data_item)
        schedule.add(instruction)

    return schedule


def is_conflict_serializable(schedule):
    return False


def create_serial_equiv_schedule():
    return set()


def create_at_least_one_cycle():
    pass


def print_schedule(schedule):
    schedule_reformatted = set()
    for instruction in schedule:
        instruction_reformatted = instruction[0] + instruction[1] + '(' + instruction[2] + ')'
        schedule_reformatted.add(instruction_reformatted)
    print(schedule_reformatted)


if __name__ == '__main__':
    prompt = 'Pass in a set of instructions on one line, separated by a space. Examples of instructions are R1(A) and W2(B).\n'
    schedule = create_schedule_from_input(input(prompt))

    if (is_conflict_serializable(schedule)):
        print_schedule(create_serial_equiv_schedule())
    else:
        print(create_at_least_one_cycle())
