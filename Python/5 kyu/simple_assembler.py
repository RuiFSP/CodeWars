def execute_mov(registers, x, y):
    if y in registers:
        # If y is a register, copy its value to register x
        registers[x] = registers[y]
    else:
        # If y is a constant, convert it to an integer and store in register x
        registers[x] = int(y)


def execute_inc(registers, x):
    # Increment the value of register x by 1
    registers[x] += 1


def execute_dec(registers, x):
    # Decrement the value of register x by 1
    registers[x] -= 1


def execute_jnz(registers, x, y, pc):
    if (x in registers and registers[x] != 0) or (x not in registers and int(x) != 0):
        # If x is not zero, jump to the instruction y steps away
        return pc + int(y)
    else:
        # If x is zero, continue to the next instruction
        return pc + 1


def simple_assembler(program):
    registers = {}  # Dictionary to store register values
    pc = 0  # Program Counter

    while pc < len(program):
        instruction = program[pc].split()  # Split the instruction into opcode and operands
        opcode = instruction[0]  # Get the opcode

        if opcode == 'mov':
            x, y = instruction[1], instruction[2]  # Get the operands
            execute_mov(registers, x, y)  # Execute mov instruction

        elif opcode == 'inc':
            x = instruction[1]  # Get the operand
            execute_inc(registers, x)  # Execute inc instruction

        elif opcode == 'dec':
            x = instruction[1]  # Get the operand
            execute_dec(registers, x)  # Execute dec instruction

        elif opcode == 'jnz':
            x, y = instruction[1], instruction[2]  # Get the operands
            pc = execute_jnz(registers, x, y, pc)  # Execute jnz instruction and update pc
            continue  # Skip incrementing pc at the end of the loop

        pc += 1  # Increment the Program Counter to move to the next instruction

    return registers  # Return the final register values


if __name__ == '__main__':
    assert simple_assembler(['mov a 5', 'inc a', 'dec a', 'jnz a -1', 'inc a']) == {'a': 1}
    assert simple_assembler(['mov a -10', 'mov b a', 'inc a', 'dec b', 'jnz a -2']) == {'a': 0, 'b': -20}
    print('Tests passed!')
