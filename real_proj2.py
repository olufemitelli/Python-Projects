# Global variables
ram = []  # list to hold the random access memory
program_memory = []  # list to hold the program memory
instruction_pointer = 0  # register to hold the current instruction location
equal_flag = False  # flag to indicate if the last CMP was equal
less_flag = False  # flag to indicate if the last CMP was less than

# Function to initialize RAM
def initialize_ram(size):
    global ram  
    ram = [0] * size

# Function to load the program into memory
def load_program(file_name):
    global program_memory
    with open(file_name) as f:
        program_memory = f.readlines()

# Function to execute instructions
def execute_instruction(instruction):
    global instruction_pointer, equal_flag, less_flag
    # TODO: Implement instruction execution logic here
    pass

def int(interrupt_code, memory, input_buffer):
    if interrupt_code == "PRINT":
        # get the memory address or value to print
        print_arg = memory[memory[0]]
        if isinstance(print_arg, str):
            print(print_arg)
        else:
            print(print_arg)

    elif interrupt_code == "INPUT":
        # get the memory address to store the input
        input_location = memory[memory[0]]
        user_input = input(">> ")
        # store the input in the specified memory location
        memory[input_location] = int(user_input)
        # add the input to the input buffer
        input_buffer.append(int(user_input))

    else:
        print("Invalid interrupt code")

    # increment the instruction pointer to move past the interrupt instruction
    memory[0] += 1

def nop(program_counter, ram):
    # NOP does nothing, so we just increment the program counter
    program_counter += 1
    return program_counter, ram

def hlt(cpu, ram, flags, args):
    """
    Halts the program and ends the simulation.

    Arguments:
    cpu: dict, the CPU state.
    ram: list, the memory.
    flags: dict, the flags state.
    args: list, the arguments.

    Returns:
    True, indicating the end of the program.
    """
    print("HLT: Halting the program.")
    return True

def mov(args, ram):
    destin = int(args[0].strip('[]'))
    src = args[1]
    if src.startswith('['):
        # move from one ram location to another
        src_addr = int(src.strip('[]'))
        ram[destin] = ram[src_addr]
    else:
        # move a value into a ram location
        ram[destin] = int(src)

def jmp(instruction, registers, ram):
    """
    Jump to program memory address.
    """
    # Get the jump location from the instruction.
    jump_location = instruction[1]

    # If the jump location is enclosed in square brackets,
    # get the actual location from RAM.
    if jump_location.startswith('[') and jump_location.endswith(']'):
        address = int(jump_location[1:-1])
        jump_location = ram[address]

    # Set the instruction register to the jump location.
    registers['IR'] = jump_location


# Main program
if __name__ == '__main__':
    # Get input file name and RAM size
    file_name, ram_size = input("What file should we assemble, and what size of ram should we use? ").split()
    ram_size = int(ram_size)

    # Initialize RAM
    initialize_ram(ram_size)

    # Load program
    load_program(file_name)

    # Execute instructions
    while instruction_pointer < len(program_memory):
        instruction = program_memory[instruction_pointer].strip()
        execute_instruction(instruction)
        if instruction.split()[0].upper() != 'JMP':
            instruction_pointer += 1
        if instruction_pointer == "MOV":
            destination, source = arguments.split(' ')
            MOV(destination, source)
        elif instruction_pointer == "ADD":
            destination, source = arguments.split(' ')
            ADD(destination, source)
        elif instruction_pointer == "JMP":
            location = arguments
            JMP(location)
        elif instruction_pointer == "NOP":
            NOP()
        elif instruction_pointer == "HLT":
            HLT()