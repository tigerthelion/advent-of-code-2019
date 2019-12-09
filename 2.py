program = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,6,19,23,2,23,6,27,1,5,27,31,1,10,31,35,2,6,35,39,1,39,13,43,1,43,9,47,2,47,10,51,1,5,51,55,1,55,10,59,2,59,6,63,2,6,63,67,1,5,67,71,2,9,71,75,1,75,6,79,1,6,79,83,2,83,9,87,2,87,13,91,1,10,91,95,1,95,13,99,2,13,99,103,1,103,10,107,2,107,10,111,1,111,9,115,1,115,2,119,1,9,119,0,99,2,0,14,0]
program[1] = 12
program[2] = 2

class IntCode():

    def __init__(self, instructions: list) -> None:
        self.seek_position = 0
        self._instructions: list = instructions

        self._register: list = self.load_register()
        self.value = None
        print(self.register)
        while True:
            self.value = self.operate()
            if self.value:
                break
            self.seek()
            self.load_register()




    def read(self, location: int) -> int:
        return self._instructions[location]

    def write(self, location: int, value: int) -> None:

        self._instructions[location] = value

    def load_register(self) -> None:
        self.register = self._instructions[self.seek_position : self.seek_position + 4]

    def seek(self) -> None:       
        self.seek_position += 4

    def operate(self) -> None:
        op_code = self.register[0]
        ops = {
            1: self.one,
            2: self.two,
            99: self.ninetynine
        }
        if op_code in list(ops.keys()):
            return ops[op_code]()
        else:
            raise AttributeError(f'Unknown Op Code. {op_code}')
        
    def one(self):
        self.write(self.register[3], self.read(self.register[1]) + self.read(self.register[2]))
        return None
    
    def two(self):
        self.write(self.register[3], self.read(self.register[1]) * self.read(self.register[2]))
        return None
    
    def ninetynine(self):
        return self._instructions[0]




# prog = IntCode(program)
# print(prog.value)

num_range = [i for i in range(0, 100)]
perms = []
for i in num_range:
    for j in num_range:
        perms.append((i, j))



num_to_find = 19690720      
for perm in perms:
    program[1], program[2] = perm
    prog = IntCode(program[:])
    if prog.value == num_to_find:
        print(perm)
        print(100 *perm[0] + perm[1])
        break