习题 3.1：2, 3, 6, 9, 11

习题 3.2：2, 3, 7, 12, 14（只需写是否独立，不用写计算过程）

补充：完成书上“例 3.3.7（正态分布的可加性）”中“不难得到”那一步被省略的计算。

3.1-2 盒子里装有3个黑球,2个红球,2个白球, 从中任取4个,以X表示取到黑球的个数, 以Y表示取到红球的个数,试求$P(X=Y)$
$$
\begin{align}
P(X=1,Y=1) &= \frac{\begin{pmatrix}
3 \\
1
\end{pmatrix}\begin{pmatrix}
2 \\
1
\end{pmatrix}}{\begin{pmatrix}
7 \\
4
\end{pmatrix}}  =\frac{6}{35} \\
P(X=2,Y=2) &= \frac{\begin{pmatrix}
3 \\
2
\end{pmatrix}\begin{pmatrix}
2 \\
2
\end{pmatrix}}{\begin{pmatrix}
7 \\
4
\end{pmatrix}}  = \frac{3}{35}
\end{align}
$$
$$
P(X=Y) = \frac{9}{35}
$$

3.1-3 口袋中有5个白球,8个黑球,从中不放回地一个接一个取出3个. 如果第$i$次取出的是白球,则令$X_{i}=1$, 否则令$X_{i}=0,i=1,2,3$,求
(1) $(X_{1},X_{2},X_{3})$的联合分布列
(2)$(X_{1},X_{2})$的联合分布

(1) 从中任意取3个, 一共有$$\begin{pmatrix} 13 \\3
\end{pmatrix}=286$$

| $X_{1}$ | $X_{2}$ | $X_{3}$ | $P$              |
| ------- | ------- | ------- | ---------------- |
| 0       | 0       | 0       | $\frac{28}{143}$ |
| 0       | 0       | 1       | $\frac{70}{429}$ |
| 0       | 1       | 0       | $\frac{70}{429}$ |
| 0       | 1       | 1       | $\frac{40}{429}$ |
| 1       | 0       | 0       | $\frac{70}{429}$ |
| 1       | 0       | 1       | $\frac{40}{429}$ |
| 1       | 1       | 0       | $\frac{40}{429}$ |
| 1       | 1       | 1       | $\frac{5}{143}$  |


| $X_{1}$ | $X_{2}$ | $P$             |
| ------- | ------- | --------------- |
| 0       | 0       | $\frac{14}{39}$ |
| 0       | 1       | $\frac{10}{39}$ |
| 1       | 0       | $\frac{10}{39}$ |
| 1       | 1       | $\frac{5}{39}$  |


3.1-6 设随机变量$(X,Y)$的联合密度函数为
$$
p(x,y) = \begin{cases}
ke^{-(3x+4y)},&x>0,y>0 \\
0,&其他
\end{cases}
$$
试求:
(1) 常数$k$
(2) $(X,Y)$的联合分布函数$F(x,y)$
(3) $P(0<X\leq 1,0<Y \leq 2)$

答:
(1) 
$$
\begin{align}
\int_{0} ^{\infty}ke^{-3x}dx\int_{0}^{\infty}e^{-4y}dy  &=1  \\
\frac{k}{12} &= 1  \\
k &=12
\end{align}
$$
(2) 
$$
\begin{align}
F(x,y) &= 12\int_{0}^xe^{-3x}dx \int_{0}^ye^{-4y}dy \\
&=(e^{-3x}-1)(e^{-4y}-1)
\end{align}
$$
(3)
$$
P(0<X\leq 1,0<Y \leq 2)=F(1,2)=(e^{-3}-1)(e^{-8}-1) \approx 0.95
$$


3.1-9 设二维随机变量$(X,Y)$的联合密度函数为
$$
p(x,y) = \begin{cases} 
 k,&0<x^2<y<x<1 \\ 
0,&其他
\end{cases}
$$
(1) 求常数$k$
(2)求$P(X>0.5)$和$P(Y<0.5)$
(1)
$$
\begin{align}
\int^{1}_{0} \int_{x^2}^{x} k dy  dx &= k\int^{1}_{0}(x-x^2)dx =1  \\
k&=6
\end{align}
$$
(2) $$
p_{X}(x) = \int_{x^2}^x 6dy =6(x-x^2)
$$
$$
\begin{align}
P(X>0.5) = 1-P(X \leq 0.5) = 1- \int^{0.5}_{0}6(x-x^2)dx = 1-\frac{1}{2} =\frac{1}{2}
\end{align}
$$
$$
p_{Y}(y) = \int_{y}^{\sqrt{ y }} 6dx =6(\sqrt{ y }-y)
$$
$$
\begin{align}
P(Y<0.5) =  \int^{0.5}_{0}6(\sqrt{ y }-y)dy \approx 0.66
\end{align}
$$


3.1-11 设随机变量$Y$服从参数为$\lambda=1$的指数分布, 定义随机变量$X_{k}$如下:
$$
X_{k} = \begin{cases}
0, & Y \leq k \\
1, & Y >k 
\end{cases}
, k=1,2
$$
求$X_{1}$和$X_{2}$的联合分布列

$X_{1}=0$, $P(Y\leq 1)= \int_{0}^1e^{-x}dx=1-e^{-1}$ 
$X_{2}=0$, $P(Y\leq 2)= \int_{0}^2e^{-x}dx=1-e^{-2}$ 
$X_{1}=1$, $P(Y> 1)= \int_{1}^\infty e^{-x}dx=e^{-1}$ 
$X_{2}=1$, $P(Y> 2)= \int_{2}^\infty e^{-x}dx=e^{-2}$ 
$X_{1}=1$, $X_{2}=0$ $P(1 <Y \le 2) =\int^{2}_{1}e^{-x}dx=e^{-1}-e^{-2}$

|                 | $X_{1}=0$(Y <=1) | $X_{1}=1$(Y>1)  |
| --------------- | ---------------- | --------------- |
| $X_{2}=0$(Y<=2) | $(1-e^{-1})$     | $e^{-1}-e^{-2}$ |
| $X_{2}=1$(Y>2)  | $0$              | $e^{-2}$        |



3.2-2 设二维随机变量$(X,Y)$的联合分布函数为
$$
F(x,y)= \begin{cases}
1-e^{-\lambda_{1}x}-e^{-\lambda_{2}y}+e^{-\lambda_{1}x -\lambda_{2}y-\lambda_{12}\max\{x,y\}}, x>0,y>0  \\
0, 其他
\end{cases}
$$
试求$X$和$Y$各自的边际分布函数

$$
F_{X}(x) = F(x,\infty) = \begin{cases}
1-e^{-\lambda_{1}x} ,&x>0 \\
0, & 其他
\end{cases}
$$
$$
F_{Y}(y) = F(\infty,y) = \begin{cases}
1-e^{-\lambda_{2}y} ,&y>0 \\
0, & 其他
\end{cases}
$$


3.2-3 试求以下二维均匀分布的边际分布:
$$
p(x,y) = \begin{cases}
\frac{1}{\pi}, & x^2+y^2 \leq 1  \\
0, &其他
\end{cases}
$$
答:
在$x>1$或者$x<-1$时, $p_{X}(x)=0$
在$-1 \le x \leq 1$时
$$
p_X(x) = \int_{-\sqrt{1-x^2} }^{\sqrt{ 1-x^2 }} \frac{1}{\pi} dy =\frac{2\sqrt{ 1-x^2 }}{\pi} 
$$
在$y>1$或者$y<-1$时, $p_{Y}(y)=0$
在$-1 \le y \leq 1$时

$$
p_Y(y) = \int_{-\sqrt{1-y^2} }^{\sqrt{ 1-y^2 }} \frac{1}{\pi} dx =\frac{2\sqrt{ 1-y^2 }}{\pi} 
$$




3.2-7 验证以下给出的两个不同的联合密度函数,它们有相同的边际密度函数
$$
\begin{align}
p(x,y) = \begin{cases}
x+y, & 0 \le x \le 1, 0 \le y \le 1\\
0, & 其他 \\
\end{cases} 
\end{align}
$$
$$
\begin{align}
g(x,y) = \begin{cases}
(0.5+x)(0.5+y), & 0 \le x \le 1, 0 \le y \le 1 \\
0, & 其他 \\
\end{cases} 
\end{align}
$$
答: 
$p_{X}(x) = \int_{0}^1(x+y)dy =x+0.5, 0\leq x \le 1$

$p_{Y}(y) = \int_{0}^1(x+y)dx =y+0.5, 0\leq y \le 1$

$g_{X}(x) = \int_{0}^1(0.5+x)(0.5+y)dy =0.5+x, 0\leq x \leq 1$

$g_{Y}(y) = \int_{0}^1(0.5+x)(0.5+y)dx =0.5+y, 0\leq y \leq 1$

3.2-12 设随机变量$(X,Y)$的联合密度函数为
$$
\begin{align}
p(x,y) = \begin{cases}
3x, & 0<y<x<1  \\
0, & 其他
\end{cases}
\end{align}
$$
(1) 边际密度函数$p_{X}(x)$和$p_{Y}(y)$
(2) $X$与$Y$是否独立?
答:
(1) $$
\begin{align}
p_{X}(x)= \begin{cases}
\int_{0}^x  3x dy =3x^2 , &0<x<1\\
0, &其他 \\
\end{cases}
\end{align}

$$
$$
\begin{align}
p_{Y}(y)= \begin{cases}
\int_{y}^1  3x dx =3\left( \frac{1}{2}- \frac{y^2}{2} \right) , &0<y<1\\
0, &其他 \\
\end{cases}
\end{align}
$$

(2)  不独立

3.2-14 设二维随机变量$(X,Y)$的联合密度函数如下, 试问$X$ 与 $Y$ 是否相互独立
(1)
$$
\begin{align}
p(x,y) = \begin{cases}
xe^{-(x+y)},&x>0,y>0, \\
0, &其他
\end{cases}
\end{align}
$$
独立

(2)
$$
\begin{align}
p(x,y) = \frac{1}{\pi^2(1+x^2)(1+y^2)}, -\infty<x,y<\infty
\end{align}
$$
独立


(3)
$$
\begin{align}
p(x,y) = \begin{cases}
2,& 0<x<y<1, \\
0, &其他
\end{cases}
\end{align}
$$
不独立

(4)
$$
\begin{align}
p(x,y) = \begin{cases}
24xy,&0<x<1,0<y<1,0<x+y<1  \\
0, &其他
\end{cases}
\end{align}
$$
不独立

$$
p_{X}(x) = \int_{0}^{1-x} 24xydy= 12x(1-x)^2, 0<x<1
$$
$$
p_{Y}(y) = \int_{0}^{1-y} 24xydx= 12y(1-y)^2, 0<y<1
$$

(5)
$$
\begin{align}
p(x,y) = \begin{cases}
12xy(1-x),&0<x<1,0<y<1, \\
0, &其他
\end{cases}
\end{align}
$$
独立


(6)
$$
\begin{align}
p(x,y) = \begin{cases}
\frac{21}{4}x^2y,& x^2<y<1, \\
0, &其他
\end{cases}
\end{align}
$$
不独立

