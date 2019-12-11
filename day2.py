input = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,5,19,23,2,9,23,27,1,6,27,31,1,31,9,35,2,35,10,39,1,5,39,43,2,43,9,47,1,5,47,51,1,51,5,55,1,55,9,59,2,59,13,63,1,63,9,67,1,9,67,71,2,71,10,75,1,75,6,79,2,10,79,83,1,5,83,87,2,87,10,91,1,91,5,95,1,6,95,99,2,99,13,103,1,103,6,107,1,107,5,111,2,6,111,115,1,115,13,119,1,119,2,123,1,5,123,0,99,2,0,14,0]
# test_input = [1,9,10,3,2,3,11,0,99,30,40,50]

# input = test_input

def calc1(inp, noun, verb):
    current_pos = 0
    current_op = input[current_pos]
    arr = inp[:]
    arr[1], arr[2] = noun, verb

    while (current_op == 1 or current_op == 2):
        n1 = arr[arr[current_pos + 1]]
        n2 = arr[arr[current_pos + 2]]
        res_pos = arr[current_pos + 3]
        if (current_op == 1):
            arr[res_pos] = n1 + n2
        elif (current_op == 2):
            arr[res_pos] = n1 * n2

        current_pos += 4
        current_op = arr[current_pos]

    return arr[0]

operations = {
    1: lambda x, y: x + y,
    2: lambda x, y: x * y,
}

def calc2(inp, noun=0, verb=0):
    READ_OPERATION_CODE, READ_LEFT_OPERAND, READ_RIGHT_OPERAND, STORE_RESULT = range(4)
    action = READ_OPERATION_CODE
    arr = inp[:]
    arr[1], arr[2] = noun, verb
    for code in inp:
        # print("idx: {}; code: {}; action: {}".format(idx, code, action))
        if action == READ_OPERATION_CODE:
            operation = operations.get(code)
            if operation is None:
                break
            action = READ_LEFT_OPERAND
        elif action == READ_LEFT_OPERAND:
            left_operand = arr[code]
            action = READ_RIGHT_OPERAND
        elif action == READ_RIGHT_OPERAND:
            right_operand = arr[code]
            action = STORE_RESULT
        elif action == STORE_RESULT:
            arr[code] = operation(left_operand, right_operand)
            action = READ_OPERATION_CODE
    return arr[0]


# calc1(input)
for noun in range(100):
    for verb in range(100):
        result = calc1(input, noun, verb)
        if result == 19690720:
            print(100*noun + verb)