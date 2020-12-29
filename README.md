# Brainfuck-Transpiler
A really bad transpiler, with absolutely zero compiler optimizations.

# Examples:
```bf
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.
```

To:

```python
memory = []
for i in range(0, 30000):
    memory.append(0)

pointer = 0

memory[pointer] += 1
memory[pointer] += 1
memory[pointer] += 1
memory[pointer] += 1
memory[pointer] += 1
memory[pointer] += 1
memory[pointer] += 1
memory[pointer] += 1
while memory[pointer] != 0:
        pointer += 1
        memory[pointer] += 1
        memory[pointer] += 1
        memory[pointer] += 1
        memory[pointer] += 1
        while memory[pointer] != 0:
                pointer += 1
                memory[pointer] += 1
                memory[pointer] += 1
                pointer += 1
                memory[pointer] += 1
                memory[pointer] += 1
                memory[pointer] += 1
                pointer += 1
                memory[pointer] += 1
                memory[pointer] += 1
                memory[pointer] += 1
                pointer += 1
                memory[pointer] += 1
                pointer -= 1
                pointer -= 1
                pointer -= 1
                pointer -= 1
                memory[pointer] -= 1
        pointer += 1
        memory[pointer] += 1
        pointer += 1
        memory[pointer] += 1
        pointer += 1
        memory[pointer] -= 1
        pointer += 1
        pointer += 1
        memory[pointer] += 1
        while memory[pointer] != 0:
                pointer -= 1
        pointer -= 1
        memory[pointer] -= 1
pointer += 1
pointer += 1
print(chr(memory[pointer]), end='')
pointer += 1
memory[pointer] -= 1
memory[pointer] -= 1
memory[pointer] -= 1
print(chr(memory[pointer]), end='')
memory[pointer] += 1
memory[pointer] += 1
memory[pointer] += 1
memory[pointer] += 1
memory[pointer] += 1
memory[pointer] += 1
memory[pointer] += 1
print(chr(memory[pointer]), end='')
print(chr(memory[pointer]), end='')
memory[pointer] += 1
memory[pointer] += 1
memory[pointer] += 1
print(chr(memory[pointer]), end='')
pointer += 1
pointer += 1
print(chr(memory[pointer]), end='')
pointer -= 1
memory[pointer] -= 1
print(chr(memory[pointer]), end='')
pointer -= 1
print(chr(memory[pointer]), end='')
memory[pointer] += 1
memory[pointer] += 1
memory[pointer] += 1
print(chr(memory[pointer]), end='')
memory[pointer] -= 1
memory[pointer] -= 1
memory[pointer] -= 1
memory[pointer] -= 1
memory[pointer] -= 1
memory[pointer] -= 1
print(chr(memory[pointer]), end='')
memory[pointer] -= 1
memory[pointer] -= 1
memory[pointer] -= 1
memory[pointer] -= 1
memory[pointer] -= 1
memory[pointer] -= 1
memory[pointer] -= 1
memory[pointer] -= 1
print(chr(memory[pointer]), end='')
pointer += 1
pointer += 1
memory[pointer] += 1
print(chr(memory[pointer]), end='')
pointer += 1
memory[pointer] += 1
memory[pointer] += 1
print(chr(memory[pointer]), end='')
```
