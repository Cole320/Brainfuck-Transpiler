# Declaring Constants

brainfuck_file = open(input("Please enter file path of your Brainfuck program: "), 'r')
output_file = open(input("Please enter the output path: "), 'w')

python_code = ""
indentation = 0
indent = "        "

# External Helper Code


formatted_code = []

for line in brainfuck_file:
    for char in line:
        if char == ">" or char == "<" or char == "+" or char == "-" or char == "." or char == "," or char == "[" or char == "]":
            formatted_code.append(char)
            

# Initialize Code

python_code += "memory = []\n"
python_code += "for i in range(0, 30000):\n"
python_code += "    memory.append(0)\n\n"

python_code += "pointer = 0\n\n"

# Parse Brainfuck

for char in formatted_code:
        if char == '>':
            python_code += indent * indentation + "pointer += 1\n"
            
        if char == '<':
            python_code += indent * indentation + "pointer -= 1\n"
            
        if char == '+':
            python_code += indent * indentation + "memory[pointer] += 1\n"
            
        if char == '-':
            python_code += indent * indentation + "memory[pointer] -= 1\n"
            
        if char == '.':
            python_code += indent * indentation + "print(chr(memory[pointer]), end='')\n"
            
        if char == ',':
            python_code += indent * indentation + "memory[pointer] = input()\n"
            
        if char == '[':
            python_code += indent * indentation + "while memory[pointer] != 0:\n"
            indentation += 1
        
        if char == ']':
            indentation = indentation - 1
            
output_file.write(python_code)
output_file.close()
brainfuck_file.close()