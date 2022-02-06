# brainfuck
Brainfuck transpiler and compiler written in Python 

## Contents

Project contains five Python and several Brainfuck files.

### Python files

+ **brainlib.py** contains definitions of functions used by other files: bfcompile() and bfgenerate().

+ **compile.py** translates Brainfuck code given in input into Python code and executes it.

+ **compilefile.py** translates Brainfuck code given in file specified in input and executes it.

+ **generate.py** generates Brainfuck code, which prints out string given in input, and prints the code.

+ **generatefile.py** generates Brainfuck code, which prints out string given in input, and writes it into specified file.
