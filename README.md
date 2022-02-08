# brainfuck
Brainfuck transpiler and compiler written in Python.

## Contents

Project contains five Python and several Brainfuck files.

### Python files

+ **brainlib.py** contains definitions of functions used by other files: bfcompile() and bfgenerate().

+ **compile.py** translates Brainfuck code given in input into Python code and executes it.

+ **compilefile.py** translates Brainfuck code given in file specified in input and executes it.

+ **generate.py** generates Brainfuck code, which prints out string given in input, and prints the code.

+ **generatefile.py** generates Brainfuck code, which prints out string given in input, and writes it into specified file.

### Brainfuck files

Brainfuck files are intended for testing compilers, some of them are taken from the internet.

+ **add2.bf** adds two digits.
+ **caesar.bf** applies Ceasar cipher to a string.
+ **[helloworld.bf](https://codegolf.stackexchange.com/a/68494)** prints "Hello, World!"
+ **[random.bf](https://github.com/cagataycali/awesome-brainfuck/blob/master/examples/random.bf)** print random characters.
+ **[reverse.bf](https://gist.github.com/anilsathyan7/2d5214e7ab711fbe9b3113711b637916)** reverses a string.
+ **[sierpinski.bf](http://www.brainfuck.org/sierpinski.b)** prints Sierpinski triangle.
