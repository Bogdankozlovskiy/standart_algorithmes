***
$$\text{Matrix multiply}$$
---
***
$$
A=
\left|\begin{matrix}
a_{1,1} & a_{1,2}\\
a_{2,1} & a_{2,2}
\end{matrix}\right|\\
B=
\left|\begin{matrix}
b_{1,1} & b_{1,2}\\
b_{2,1} & b_{2,2}
\end{matrix}\right| \\
A \times B =
\left|\begin{matrix}
a_{1,1}\cdot b_{1,1} + a_{1,2}\cdot b_{2,1} & a_{1,1}\cdot b_{1,2} + a_{1,2}\cdot b_{2,2}\\
a_{2,1}\cdot b_{1,1} + a_{2,2}\cdot b_{2,1} & a_{2,1}\cdot b_{1,2} + a_{2,2}\cdot b_{2,2}
\end{matrix}\right|\\
$$
***
$$\text{with recursion}$$
---
***
$$
A=
\left|\begin{matrix}
a_{1,1} & a_{1,2} & a_{1,3} & a_{1,4}\\
a_{2,1} & a_{2,2} & a_{2,3} & a_{2,4}\\
a_{3,1} & a_{3,2} & a_{3,3} & a_{3,4}\\
a_{4,1} & a_{4,2} & a_{4,3} & a_{4,4}
\end{matrix}\right|\\
atl=
\left|\begin{matrix}
a_{1,1} & a_{1,2}\\
a_{2,1} & a_{2,2}
\end{matrix}\right|
atr=
\left|\begin{matrix}
a_{1,3} & a_{1,4}\\
a_{2,3} & a_{2,4}
\end{matrix}\right|
abl=
\left|\begin{matrix}
a_{3,1} & a_{3,2}\\
a_{4,1} & a_{4,2}
\end{matrix}\right|
abr=
\left|\begin{matrix}
a_{3,3} & a_{3,4}\\
a_{4,3} & a_{4,4}
\end{matrix}\right|\\
A=
\left|\begin{matrix}
atl & atr\\
abl & abr
\end{matrix}\right|\\
B=
\left|\begin{matrix}
b_{1,1} & b_{1,2} & b_{1,3} & b_{1,4}\\
b_{2,1} & b_{2,2} & b_{2,3} & b_{2,4}\\
b_{3,1} & b_{3,2} & b_{3,3} & b_{3,4}\\
b_{4,1} & b_{4,2} & b_{4,3} & b_{4,4}
\end{matrix}\right|\\
btl=
\left|\begin{matrix}
b_{1,1} & b_{1,2}\\
b_{2,1} & b_{2,2}
\end{matrix}\right|
btr=
\left|\begin{matrix}
b_{1,3} & b_{1,4}\\
b_{2,3} & b_{2,4}
\end{matrix}\right|
bbl=
\left|\begin{matrix}
b_{3,1} & b_{3,2}\\
b_{4,1} & b_{4,2}
\end{matrix}\right|
bbr=
\left|\begin{matrix}
b_{3,3} & b_{3,4}\\
b_{4,3} & b_{4,4}
\end{matrix}\right|\\
B=
\left|\begin{matrix}
btl & btr\\
bbl & bbr
\end{matrix}\right|\\
$$
***
$$\text{simple multiply algorithm}$$
---
***
$$
A \times B =
\left|\begin{matrix}
atl & atr\\
abl & abr
\end{matrix}\right|\times
\left|\begin{matrix}
btl & btr\\
bbl & bbr
\end{matrix}\right|=
\left|\begin{matrix}
atl\cdot btl + atr\cdot bbl & atl\cdot btr + atr\cdot bbr\\
abl\cdot btl + abr\cdot bbl & abl\cdot btr + abl\cdot bbr
\end{matrix}\right|\\
P_1 = atl\cdot btl \\
P_2 = atr\cdot bbl \\ 
P_3 = atl\cdot btr \\
P_4 = atr\cdot bbr \\
P_5 = abl\cdot btl \\
P_6 = abr\cdot bbl \\
P_7 = abl\cdot btr \\
P_8 = abl\cdot bbr \\
A \times B = 
\left|\begin{matrix}
P_1 + P_2 & P_3 + P_4\\
P_5 + P_6 & P_7 + P_8
\end{matrix}\right|
$$
***
$$\text{Strassen multiply algorithm}$$
---
***
$$
P_1 = (atl + abr)\times(btl + bbr) \\
P_2 = (abl + abr)\times btl \\
P_3 = atl\times(btr - bbr) \\
P_4 = abr\times(bbl - btl) \\
P_5 = (atl + atr)\times bbr \\
P_6 = (abl - atl)\times(btl + btr) \\
P_7 = (atr - abr)\times(bbl + bbr) \\
A\times B=
\left|\begin{matrix}
P_1 + P_4 - P_5 + P_7 & P_3 + P_5\\
P_2 + P_4 & P_1 - P_2 + P_3 + P_6
\end{matrix}\right|
$$
***