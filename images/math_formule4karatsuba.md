### Karatsuba multiply
$$
\overline{ab} \cdot \overline{cd}=\\
(a\cdot 10 + b)\cdot(c\cdot 10 + d)=\\
a\cdot c \cdot 100 + a\cdot d \cdot 10 + b\cdot c\cdot 10 + b\cdot d=\\
a\cdot c \cdot 100 + (a\cdot d + b\cdot c)\cdot 10 + b\cdot d=\\
a\cdot c \cdot 100 + ((a + b)\cdot(c + d) - a\cdot c - b\cdot d)\cdot 10 + b\cdot d
$$