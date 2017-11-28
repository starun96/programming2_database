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
    pass


def create_serial_equiv_schedule():
    pass


def create_at_least_one_cycle():
    pass


if __name__ == '__main__':
    prompt = 'Pass in a set of instructions on one line, separated by a space. Examples of instructions are R1(A) and W2(B).\n'
    schedule = create_schedule_from_input(input(prompt))
    print(schedule)
    is_conflict_serializable(schedule)
    create_serial_equiv_schedule()
    create_at_least_one_cycle()
