from typing import Optional
from io import StringIO

__all__ = ("Brainfuck",)


class Brainfuck:
    def __init__(self, code: str, memory_size: int = 30000):
        self.code = [i for i in code if i in "+-<>[].,"]
        self.memory_size = memory_size
        self.brace_map = {}
        self.build_brace_map()

    def build_brace_map(self):
        stack = []
        for i, c in enumerate(self.code):
            if c == "[":
                stack.append(i)
            elif c == "]":
                pair = stack.pop()
                self.brace_map[i] = pair
                self.brace_map[pair] = i

    def evaluate(self, stdin: str = "", limit: Optional[int] = None) -> str:
        memory = [0 for _ in range(self.memory_size)]
        code_pointer = 0
        data_pointer = 0
        stdout = ""
        stdin = StringIO(stdin)
        step = 0

        while (limit is None or step < limit) and code_pointer < len(self.code):
            current = self.code[code_pointer]
            if current == ".":
                stdout += chr(memory[data_pointer])
            elif current == ",":
                c = stdin.read(1)
                memory[data_pointer] = ord(c) if c else 0
            elif current == "+":
                memory[data_pointer] += 1
            elif current == "-":
                memory[data_pointer] -= 1
            elif current == ">":
                data_pointer = min(self.memory_size - 1, data_pointer + 1)
            elif current == "<":
                data_pointer = max(0, data_pointer - 1)
            elif current == "[" and not memory[data_pointer]:
                code_pointer = self.brace_map[code_pointer]
            elif current == "]" and memory[data_pointer]:
                code_pointer = self.brace_map[code_pointer]
            code_pointer += 1
            step += 1

        return stdout
