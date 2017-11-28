
def create_schedule_from_input(input):
    """
    Creates a schedule of instructions from user input
    :param input: user inputted set of instructions, space-separated
    :return: a set of instructions (schedule) of the form (R/W, num, data_item)
    """
    instructions_text = input.split()
    instructions = set()
    for instruction_text in instructions_text:
        instruction = ()
        instructions.add(instruction)

def is_conflict_serializable(schedule):
    pass

def create_serial_equiv_schedule():
    pass

def create_at_least_one_cycle():
    pass


if __name__ == '__main__':
    prompt = 'Pass in a set of instructions on one line, separated by a space. Examples of instructions are R1(A) and W2(B).'
    schedule = create_schedule_from_input(input('prompt'))
    is_conflict_serializable(schedule)
    create_serial_equiv_schedule()
    create_at_least_one_cycle()