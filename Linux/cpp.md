# C++

## PRVI PROGRAM

V datoteko `main.cpp` napišemo program:

```cpp
#include <stdio.h>
char s[] = "GeeksforGeeks";

int main()
{
	int a = 2000, b =17;
	printf("%s %d \n", s, a+b);
}
```

## Compiling & running

da program skompajliramo zaženemo ukaz:

		gcc main.cpp -o main

zaženemo program `main`

		./main

## Cpp to assembly

		gcc -S main.cpp

in dobimo strojno kodo:

´´´asm
	.file	"main.cpp"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movl	$0, -4(%rbp)
.L2:
	addl	$1, -4(%rbp)
	jmp	.L2
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (GNU) 11.1.0"
	.section	.note.GNU-stack,"",@progbits
´´´

## BOOKS

- An Introduction to GCC (Brain Gough)
-
