# Brainfuck-Transpiler
A really bad transpiler, with absolutely zero compiler optimizations.

## What is Brainfuck?

Brainfuck is an esoteric programming language in which there is an array of ascii
characters (with a size of at least 30,000 cells), and a pointer which can move
from cell to cell one at a time. The pointer can also increment or decrement the values in each cell
one at a time. The language consists of only 8 commands as follows:

Command | Action
-------:|---
``>``   | move to next cell
``<``   | move to previous cell
``+``   | increment the value of the current cell by 1
``-``   | decrement the value of the current cell by 1
``.``   | print the ascii character of the current cell to stdout
``,``   | get a character from stdin and store it in the current cell
``[``   | if the current cell is 0, jump to the matching ``]``
``]``   | if the current cell is **not** 0, jump to the matching ``[``

If you would like to try to master the language, feel free to build my interpreter on
your system (instructions below)
or try out this [nifty brainfuck visualizer.](http://fatiherikli.github.io/brainfuck-visualizer/)

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
