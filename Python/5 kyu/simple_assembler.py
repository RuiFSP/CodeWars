def execute_mov(registers, x, y):
    if y in registers:
        registers[x] = registers[y]
    else:
        registers[x] = int(y)


def execute_inc(registers, x):
    registers[x] += 1


def execute_dec(registers, x):
    registers[x] -= 1


def execute_jnz(registers, x, y, pc):
    if (x in registers and registers[x] != 0) or (x not in registers and int(x) != 0):
        return pc + int(y)
    return pc + 1


def simple_assembler(program):
    registers = {}
    pc = 0  # Program Counter

    while pc < len(program):
        instruction = program[pc].split()
        opcode = instruction[0]

        if opcode == 'mov':
            x, y = instruction[1], instruction[2]
            execute_mov(registers, x, y)

        elif opcode == 'inc':
            x = instruction[1]
            execute_inc(registers, x)

        elif opcode == 'dec':
            x = instruction[1]
            execute_dec(registers, x)

        elif opcode == 'jnz':
            x, y = instruction[1], instruction[2]
            pc = execute_jnz(registers, x, y, pc)
            continue

        pc += 1

    return registers


if __name__ == '__main__':
    assert simple_assembler(['mov a 5', 'inc a', 'dec a', 'jnz a -1', 'inc a']) == {'a': 1}
    assert simple_assembler(['mov a -10', 'mov b a', 'inc a', 'dec b', 'jnz a -2']) == {'a': 0, 'b': -20}
    print('Tests passed!')
