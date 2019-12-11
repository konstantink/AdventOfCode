#!/usr/bin/python3

import time

test_input = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,32,43,225,101,68,192,224,1001,224,-160,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1001,118,77,224,1001,224,-87,224,4,224,102,8,223,223,1001,224,6,224,1,223,224,223,1102,5,19,225,1102,74,50,224,101,-3700,224,224,4,224,1002,223,8,223,1001,224,1,224,1,223,224,223,1102,89,18,225,1002,14,72,224,1001,224,-3096,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,1101,34,53,225,1102,54,10,225,1,113,61,224,101,-39,224,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1101,31,61,224,101,-92,224,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1102,75,18,225,102,48,87,224,101,-4272,224,224,4,224,102,8,223,223,1001,224,7,224,1,224,223,223,1101,23,92,225,2,165,218,224,101,-3675,224,224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,1102,8,49,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1107,226,226,224,1002,223,2,223,1005,224,329,1001,223,1,223,1007,677,226,224,1002,223,2,223,1006,224,344,1001,223,1,223,108,677,226,224,102,2,223,223,1006,224,359,1001,223,1,223,7,226,226,224,1002,223,2,223,1005,224,374,101,1,223,223,107,677,677,224,1002,223,2,223,1006,224,389,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,404,1001,223,1,223,1107,677,226,224,1002,223,2,223,1005,224,419,1001,223,1,223,108,226,226,224,102,2,223,223,1006,224,434,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,449,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,464,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,479,1001,223,1,223,1008,226,226,224,102,2,223,223,1005,224,494,101,1,223,223,7,677,226,224,1002,223,2,223,1005,224,509,101,1,223,223,8,226,677,224,1002,223,2,223,1006,224,524,1001,223,1,223,1007,226,226,224,1002,223,2,223,1006,224,539,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,554,101,1,223,223,1108,677,677,224,102,2,223,223,1006,224,569,101,1,223,223,1107,226,677,224,102,2,223,223,1005,224,584,1001,223,1,223,8,677,226,224,1002,223,2,223,1006,224,599,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,614,1001,223,1,223,7,226,677,224,1002,223,2,223,1005,224,629,101,1,223,223,107,226,677,224,102,2,223,223,1005,224,644,101,1,223,223,8,677,677,224,102,2,223,223,1005,224,659,1001,223,1,223,108,677,677,224,1002,223,2,223,1005,224,674,101,1,223,223,4,223,99,226]
# test_input = [1002,4,3,4,33]
# test_input = [1,9,10,3,2,3,11,0,99,30,40,50]
# test_input = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,5,19,23,2,9,23,27,1,6,27,31,1,31,9,35,2,35,10,39,1,5,39,43,2,43,9,47,1,5,47,51,1,51,5,55,1,55,9,59,2,59,13,63,1,63,9,67,1,9,67,71,2,71,10,75,1,75,6,79,2,10,79,83,1,5,83,87,2,87,10,91,1,91,5,95,1,6,95,99,2,99,13,103,1,103,6,107,1,107,5,111,2,6,111,115,1,115,13,119,1,119,2,123,1,5,123,0,99,2,0,14,0]


class State:
    ''' Base state class that basically specifies the interface
        for the derived state classes
    '''
    _name = '__State__'

    def __hash__(self):
        return hash(self._name)

    def get_name(self):
        raise NotImplementedError('Must be implemented in derived class')

    def get_params(self, fsm):
        raise NotImplementedError('Must be implemented in derived class')

    def get_modes(self, fsm):
        raise NotImplementedError('Must be implemented in derived class')

    def process(self, inp, fsm):
        raise NotImplementedError('Must be implemented in derived class')


class ArithmeticCheckState(State):
    def __init__(self):
        self._modes = (0, 0, 0)
        self._params = (0, 0, 0)

    def get_name(self):
        return self._name

    def get_modes(self, op_code):
        without_op_code = op_code // 100
        left_operand_mode = without_op_code % 10
        right_operand_mode = (without_op_code // 10) % 10
        store_at_mode = ((without_op_code // 10) //10) % 10
        # print('[{}] MODES: left {}; right {}; store {}'.format(
        #     self._name, left_operand_mode, right_operand_mode, store_at_mode))
        return (left_operand_mode, right_operand_mode, store_at_mode)

    def get_params(self, fsm):
        left_operand = fsm.read_next() if self._modes[0] else fsm.read_at(fsm.read_next())
        right_operand = fsm.read_next() if self._modes[1] else fsm.read_at(fsm.read_next())
        store_at = fsm.read_next()  #if self._modes[2] else fsm.read_at(fsm.read_next())
        # print('[{}] VALUES: left {}; right {}; store {}'.format(
        #     self._name, left_operand, right_operand, store_at))
        return (left_operand, right_operand, store_at)

    def process(self, op_code, fsm):
        self._modes = self.get_modes(op_code)
        self._params = self.get_params(fsm)
        value = self._action(*self._params[:2])
        fsm.put_at(self._params[2], value)


class AddState(ArithmeticCheckState):
    _name = '__AddState__'

    def __init__(self):
        super().__init__()
        self._action = lambda x, y: x + y


class MultiplyState(ArithmeticCheckState):
    _name = '__MultiplyState__'

    def __init__(self):
        super().__init__()
        self._action = lambda x, y: x * y


class ReadInputState(State):
    _name = '__ReadInputState__'

    def __init__(self):
        pass

    def _action(self):
        value = int(input('>>> Please enter systemID: '))
        return value

    def get_name(self):
        return self._name

    def get_modes(self, op_code):
        without_op_code = op_code // 100
        mode = without_op_code % 10
        print('[{}] MODES: mode {}'.format(self._name, mode))
        return mode
    
    def get_params(self, fsm):
        param = fsm.read_next()
        print('[{}] VALUE: param {}'.format(self._name, param))
        return param

    def process(self, op_code, fsm):
        self._mode = self.get_modes(op_code)
        self._param = self.get_params(fsm)
        value = self._action()
        print('[{}] PUTTING value {} to {}'.format(self._name, value, self._param))
        fsm.put_at(self._param, value)


class WriteOutputState(State):
    _name = '__WriteOutputState__'

    def __init__(self):
        self._mode = 0
        self._param = 0

    def get_name(self):
        return self._name

    def get_modes(self, op_code):
        without_op_code = op_code // 100
        mode = without_op_code % 10
        print('[{}] MODES: mode {}'.format(self._name, mode))
        return mode
    
    def get_params(self, fsm):
        param = fsm.read_next()  # if self._mode else fsm.read_at(fsm.read_next())
        print('[{}] VALUE: param {}'.format(self._name, param))
        return param

    def process(self, op_code, fsm):
        self._mode = self.get_modes(op_code)
        self._param = self.get_params(fsm)
        print('>>> OUTPUT: {}'.format(fsm.read_at(self._param)))


class IfState(State):
    def __init__(self):
        self._modes = 0
        self._params = (0, 0)

    def get_name(self):
        return self._name

    def get_modes(self, op_code):
        without_op_code = op_code // 100
        test_value_mode = without_op_code % 10
        next_position_mode = (without_op_code // 10) % 10
        print('[{}] MODES: test {}; next {}'.format(self._name, test_value_mode, next_position_mode))
        return (test_value_mode, next_position_mode)

    def get_params(self, fsm):
        test_value = fsm.read_next() if self._modes[0] else fsm.read_at(fsm.read_next())
        next_position = fsm.read_next() if self._modes[1] else fsm.read_at(fsm.read_next())
        print('[{}] VALUES: test {}; next {}'.format(
            self._name, test_value, next_position))
        return (test_value, next_position)

    def process(self, op_code, fsm):
        self._modes = self.get_modes(op_code)
        self._params = self.get_params(fsm)
        if self._action(self._params[0]):
            fsm.move_pointer_to(self._params[1])


class JumpIfTrueState(IfState):
    _name = '__JumpIfTrueState__'

    def __init__(self):
        super().__init__()
        self._action = lambda x: x != 0


class JumpIfFalseState(IfState):
    _name = '__JumpIfFalseState__'

    def __init__(self):
        super().__init__()
        self._action = lambda x: x == 0


class ComparisonState(State):
    def __init__(self):
        self._modes = (0, 0, 0)
        self._params = (0, 0, 0)

    def get_name(self):
        return self._name

    def get_modes(self, op_code):
        without_op_code = op_code // 100
        left_operand_mode = without_op_code % 10
        right_operand_mode = (without_op_code // 10) % 10
        store_at_mode = (without_op_code // 100) %10
        return (left_operand_mode, right_operand_mode, store_at_mode)

    def get_params(self, fsm):
        left_operand = fsm.read_next() if self._modes[0] else fsm.read_at(fsm.read_next())
        right_operand = fsm.read_next() if self._modes[1] else fsm.read_at(fsm.read_next())
        store_at = fsm.read_next()
        return (left_operand, right_operand, store_at)

    def process(self, op_code, fsm):
        self._modes = self.get_modes(op_code)
        self._params = self.get_params(fsm)
        self._action(*self._params[:2])
        fsm.put_at(self._params[2], 1 if self._action(*self._params[:2]) else 0)


class LessThanState(ComparisonState):
    _name = '__LessThanState__'

    def __init__(self):
        super().__init__()
        self._action = lambda x, y: x < y


class EqualsState(ComparisonState):
    _name = '__EqualsState__'

    def __init__(self):
        super().__init__()
        self._action = lambda x, y: x == y


class ExitState(State):
    _name = '__ExitState__'

    def get_name(self):
        return self._name

    def process(self, current, fsm):
        print('Work has finished')


class IntCode:
    def __init__(self, initial_state=None, rules=None):
        self._initial_state = initial_state
        self._rules = rules
        self.reset()

    def reset(self):
        self._state = self._initial_state
        self._instructions = None
        self._pointer = None
        self._last_output = None
        self._outputs = []

    def get_state(self):
        return self._state

    def change_state(self, instruction):
        print('Changing state: {}'.format(instruction))
        for state, rule in self._rules.items():
            if rule(instruction):
                print("NEXT STATE: {}".format(state.get_name()))
                self.next_state(state)
                break
        else:
            print("NEXT STATE: {}".format(state.get_name()))

    def next_state(self, state):
        self._state = state

    def read_next(self):
        self._pointer += 1
        return self._instructions[self._pointer]
        # return next(self._iter)

    def move_pointer_to(self, idx):
        self._pointer = idx-1

    def read_at(self, idx):
        return self._instructions[idx]

    def put_at(self, idx, value):
        self._instructions[idx] = value

    def load(self, instructions):
        self._instructions = instructions
        self._pointer = -1
        # self._iter = iter(self._instructions)

    def process(self, inp):
        self._state.process(inp, self)

    def run(self):
        print("Let's start!")
        while not isinstance(self.get_state(), ExitState):
            current = self.read_next()
            self.change_state(current)
            self.process(current)

def main():
    rules = {
        AddState(): lambda inp: inp % 100 == 1,
        MultiplyState(): lambda inp: inp % 100 == 2,
        ReadInputState(): lambda inp: inp % 100 == 3,
        WriteOutputState(): lambda inp: inp % 100 == 4,
        JumpIfTrueState(): lambda inp: inp % 100 == 5,
        JumpIfFalseState(): lambda inp: inp % 100 == 6,
        LessThanState(): lambda inp: inp % 100 == 7,
        EqualsState(): lambda inp: inp % 100 == 8,
        ExitState(): lambda inp: inp % 100 == 99,
    }

    int_code = IntCode(State(), rules)
    int_code.load(test_input)
    int_code.run()
    print(int_code.read_at(0))

main()
