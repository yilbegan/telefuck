from typing import Optional
from io import StringIO

__all__ = ("Brainfuck",)


def preprocess_brainfuck(code: str) -> list[tuple[str, Optional[int]]]:
    preprocessed = []
    pointer = 0
    difference = 0

    for i in code:
        if i not in "+-<>[].,":
            continue
        if i == "+":
            difference += 1
        elif i == "-":
            difference -= 1
        elif difference:
            preprocessed.append(("add", difference))
            difference = 0
        if i == ">":
            pointer += 1
        elif i == "<":
            pointer -= 1
        elif pointer:
            preprocessed.append(("move", pointer))
            pointer = 0
        if i in "[].,":
            preprocessed.append((i, None))

    return preprocessed


class Brainfuck:
    def __init__(self, code: str, memory_size: int = 30000):
        self.code = preprocess_brainfuck(code)
        self.memory_size = memory_size
        self.brace_map = {}
        self.build_brace_map()

    def build_brace_map(self) -> None:
        stack = []
        for i, (c, _) in enumerate(self.code):
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

        while code_pointer < len(self.code):
            if limit is not None and step > limit:
                raise TimeoutError()
            current, value = self.code[code_pointer]
            if current == ".":
                stdout += chr(memory[data_pointer])
            elif current == ",":
                c = stdin.read(1)
                memory[data_pointer] = min(ord(c), 254) if c else 0
            elif current == "add":
                memory[data_pointer] = (memory[data_pointer] + value) % 256
            elif current == "move":
                data_pointer = (data_pointer + value) % self.memory_size
            elif current == "[" and not memory[data_pointer]:
                code_pointer = self.brace_map[code_pointer]
            elif current == "]" and memory[data_pointer]:
                code_pointer = self.brace_map[code_pointer]
            code_pointer += 1
            step += 1

        return stdout
