习题 2.6：2, 3, 8, 9, 12, 13

习题 2.7：1, 4, 5, 7

2.6-2 已知随机变量$X$的概率密度函数为
$$
p(x) = \frac{2}{\pi} \cdot \frac{1}{e^x+e^{-x}}, -\infty < x < \infty
$$
试求随机变量$Y=g(X)$的概率分布, 其中
$$
g(x)= \begin{cases}
-1,&当x<0 \\
1,&当x \geq 0
\end{cases}
$$
答:
当$Y=-1$时, 
$$
\begin{align*}
P(X<0) &= \int_{-\infty}^0  \frac{2}{\pi} \cdot \frac{1}{e^x+e^{-x}}dx \\
& = \frac{2}{\pi} \int_{-\infty}^0  \frac{e^x}{e^{2x}+1}dx
\end{align*}
$$
令$u=e^x$, 则

$$
\begin{align*}
P(X<0)  & = \frac{2}{\pi} \int_{0}^1  \frac{1}{u^2+1}du \\
&=\frac{2}{\pi}\arctan u|^{1}_{0} =\frac{1}{2}
\end{align*}
$$
当$Y=1$时, $$
\begin{align*}
P(X \geq 0) &= \int^{\infty}_{0}  \frac{2}{\pi} \cdot \frac{1}{e^x+e^{-x}}dx \\
& = \frac{1}{2}
\end{align*}
$$

| Y   | Y=-1          | Y=1           |
| --- | ------------- | ------------- |
| P   | $\frac{1}{2}$ | $\frac{1}{2}$ |




2.6-3 设随机变量$X$服从$(-1,2)$上的均匀分布,记
$$
Y= \begin{cases}
1, &X \geq 0 \\
-1, &X<0
\end{cases}
$$
求y的分布列.
答: 已知$X \sim U(-1,2)$

$Y=1$时, 
$$
P(X \geq 0) = \int_{0}^2 \left( \frac{1}{3} \right)dx =\frac{2}{3}
$$
$Y=-1$时,
$$
P(X < 0) = \int_{-1}^0 \left( \frac{1}{3} \right)dx =\frac{1}{3}
$$

| Y   | -1            | 1             |
| --- | ------------- | ------------- |
| P   | $\frac{1}{3}$ | $\frac{2}{3}$ |


2.6-8 设随机变量$X$服从区间$(0,2)$的均匀分布
(1) 求$Y=X^2$的密度函数
(2) 求$P(Y<2)$
答: (1) 
$$
P(Y \leq y) = P(-\sqrt{y} \leq X \leq \sqrt{y} )
$$
当$y<0$时, $P(Y \leq 0)=0$

当$y \leq 4$时,
$$
\begin{align*}
P(Y \leq y) &= P(-\sqrt{y} \leq X \leq \sqrt{y} )\\
&= \int_{0}^\sqrt{y} \frac{1}{2}dx\\
&= \frac{\sqrt{y}}{2}
\end{align*}
$$
当$y > 4$时,
$$
\begin{align*}
P(Y \leq y) &= P(-\sqrt{y} \leq X \leq \sqrt{y} )\\
&= \int_{0}^2 \frac{1}{2}dx\\
&= 1
\end{align*}
$$
所以,
$$
\begin{align*}
F_{Y}(y) = \begin{cases}  0,&y<0  \\
\frac{\sqrt{y}}{2},&  0 \leq y \leq 4 \\
1 , & y>4
\end{cases}
\end{align*}
$$
通过求导, 求出概率密度函数
$$
P_{Y}(y) = \begin{cases}0, &y<0\\
\frac{1}{4\sqrt{y}} , & 0 \leq y \leq 4 \\
0, &y>4
\end{cases}
$$
(2) 
$$
\begin{align*}
P(Y < 2) &= P(-\sqrt{2} < X < \sqrt{2} )\\
&= \int_{0}^\sqrt{2} \frac{1}{2}dx\\
&= \frac{\sqrt{2}}{2}
\end{align*}
$$

2.6-9 设随机变量$X$服从区间$(-1,1)$上的均匀分布,求:
(1) $P\left( |X|> \frac{1}{2} \right)$
(2) $Y=|X|$的密度函数
答: (1) 根据题意得$X \sim U(-1,1)$
$$
\begin{align*}
P\left( |X|> \frac{1}{2} \right) &= P\left( -\frac{1}{2}<X< \frac{1}{2} \right) \\
&=\int_{-\frac{1}{2}}^{\frac{1}{2}} \frac{1}{2} dx \\
& =\frac{1}{2}
\end{align*}
$$
(2)  
当$y<0$时, $P(Y \leq 0)=0$
当$0 \leq y \leq 1$时, 
$$
P(Y \leq y) = P(-y \leq X \leq y) = \int^{y}_{-y} \frac{1}{2}dx = {y}
$$
当$y>1$时,
$$
P(Y \leq y) = P(-1 \leq X \leq 1) = \int^{1}_{-1} \frac{1}{2}dx = 1
$$
所以,
$$
F_{Y}(y) = \begin{cases}
0, &y<0 \\ 
{y},&0 \leq y \leq 1 \\ 
1, &y>1
\end{cases}
$$
则求导得密度函数为
$$
P_{Y}(y) = \begin{cases}
0, &y<0 \\ 
1,&0 \leq y \leq 1 \\ 
0, &y>1
\end{cases}
$$

2.6-12 设随机变量$X \sim N(0,\sigma^2)$, 求$Y=X^2$的分布
答: 先求Y的分布函数$F_{Y}(y)$. 由于$Y=X^2 \geq 0$. 所以当$y \leq 0$时, 有$F_{Y}(y)=0$. 从而$p_{Y}(y)=0$. 当$y>0$时, 有
$$
\begin{align}
F_{Y}(y) &=P(Y \leq y)=P(X^2 \leq y) \\
         &=P(-\sqrt{y} \leq X \leq \sqrt{y}) \\
&=2\Phi(\sqrt{y})-1
\end{align}
$$
(习题 2.1-19 )
因此$Y$的分布函数为
$$
F_{Y}(y) = \begin{cases}
2\Phi(\sqrt{y})-1, &y>0 \\
0, & y \leq 0
\end{cases}
$$
$Y$的密度函数为
$$
P_{Y}(y) = \begin{cases}
\varphi(\sqrt{ y })y^{-\frac{1}{2}}, &y>0 \\
0, &y \leq 0
\end{cases}= \begin{cases}
\frac{1}{\sqrt{2 \pi }\sigma}y^{-\frac{1}{2}}e^{-\frac{y}{2 \sigma^2}}, &y>0 \\
0, &y \leq 0
\end{cases}
$$


2.6-13 设随机变量$X \sim N(0,\sigma^2)$, 求$Y=e^X$的数学期望与方差
答: 
随机变量$Y$的概率密度函数
$$
P_{Y}(y) = \begin{cases}
\frac{1}{\sqrt{2\pi} y\sigma}e^{- \frac{(\ln y-\mu)^2}{2\sigma^2}}dy ,y>0 \\ \\
0,y\leq 0
\end{cases}
$$
那么$Y$的期望为
$$
\begin{align}
 E(Y) &= \int_{0}^{\infty} y \frac{1}{\sqrt{2\pi} y\sigma}e^{- \frac{(\ln y-\mu)^2}{2\sigma^2}}dy \\
 &= \int_{0}^{\infty}  \frac{1}{\sqrt{2\pi} \sigma}e^{- \frac{(\ln y-\mu)^2}{2\sigma^2}}dy
\end{align}
$$
令$u=\ln y$
$$
\begin{align}
 E(Y)
 &= \int_{-\infty}^{\infty}  \frac{1}{\sqrt{2\pi} \sigma}e^{- \frac{(u-\mu)^2}{2\sigma^2}}e^udu \\
& = e^{\mu+\frac{1}{2}\sigma^2} \int^{\infty}_{-\infty} \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{-(u-(\mu+\sigma^2))^2}{2 \sigma^2} }du  \\
& = e^{\mu+\frac{1}{2}\sigma^2}
\end{align}
$$

$$
\begin{align}
E(Y^2) &= \int_{0}^{\infty} y^2 \frac{1}{\sqrt{2\pi} y\sigma}e^{- \frac{(\ln y-\mu)^2}{2\sigma^2}}dy \\
& = \int_{0}^{\infty} y \frac{1}{\sqrt{2\pi} \sigma}e^{- \frac{(\ln y-\mu)^2}{2\sigma^2}}dy
\end{align}
$$
令$u=\ln y$, 则$y = e^u$
$$
\begin{align}
E(Y^2) 
& = \int_{-\infty}^{\infty} e^u \frac{1}{\sqrt{2\pi} \sigma}e^{- \frac{(u-\mu)^2}{2\sigma^2}}e^udu  \\
& = e^{2\mu+2\sigma^2} \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi} \sigma} e^{-\frac{ (u-(\mu+2\sigma^2))^2}{2\sigma^2}}du  \\
& = e^{2\mu+2\sigma^2}
\end{align}
$$
$Var(Y) = E(Y^2)-(E(Y))^2 = e^{2\mu+\sigma^2}(e^{\sigma^2}-1)$


2.7-1 设随机变量$X \sim U(a,b)$, 对$k=1,2,3,4$, 求$\mu_{k}=E(X^k)$与$v_{k}=E(X-E(X))^k$. 进一步求此分布的偏度系数与峰度系数
$$
\mu_{k} = E(X)= \int_{a}^bx^k \frac{1}{b-a} dx =\frac{1}{b-a}(\frac{b^{k+1}-a^{k+1}}{k+1})
$$
$$
\begin{align}
\mu_{1} &= E(X)= \int_{a}^bx \frac{1}{b-a} dx =\frac{a+b}{2} \\
\mu_{2} &= \frac{1}{b-a} \frac{b^3-a^3}{3}=\frac{a 
^2+ab+b^2}{3}  \\
\mu_{3} &= \frac{1}{b-a}\frac{b^4-a^4}{4} = \frac{(b^2+a^2)(b+a)}{4} \\
\mu_{4} &= \frac{1}{b-a}\frac{b^5-a^5}{5} = \frac{(b^5-a^5)}{5(b-a)} 
\end{align}
$$
$$
v_k =E(X-E(X))^k = E(x-\mu_{1})^k =\sum_{i=0}^k \begin{pmatrix}
k \\
i
\end{pmatrix}\mu_{i}(-\mu_{1})^{k-i}
$$
$$
\begin{align}
v_{1} & = 0  \\
v_{2} &= \mu_{2}-\mu_{1}^2 = \frac{a 
^2+ab+b^2}{3}  -\frac{a^2+2ab+b^2}{4} = \frac{(a-b)^2}{12}  \\
 v_{3} &= \mu_{3} - 3\mu_{2}\mu_{1}+2\mu_{1}^3  \\
&= \frac{(b^2+a^2)(b+a)}{4}-\frac{(a+b)(a^2+ab+b^2)}{2} +\frac{(a+b)^3}{4}=0 \\

\end{align}
$$
令$Y=X-E(X)=X-\frac{a+b}{2}$
令$L =\frac{b-a}{2}$
则$Y \sim U(-L,L)$
则对于所有的奇数阶矩必然为0. 
$$
v_{k} = E(Y)= \int_{-L}^L x^k \frac{1}{2L} dx =\frac{1}{2L}(\frac{L^{k+1}-(-L)^{k+1}}{k+1})
$$
若$k$为偶数, 则
$$
v_{k} = \frac{L^{k}}{k+1}
$$
$$
v_{4} = \frac{\frac{(b-a)^4}{16}}{5}= \frac{(b-a)^4}{80}
$$

偏度系数: 
$$
\beta_{s} = \frac{v_{3}}{v_{2}^{3/2}} = 0
$$
峰度系数:
$$
\beta_{k} = \frac{v_{4}}{v_{2}^2}-3 = \frac{(b-a)^4}{80} \frac{144}{(a-b)^4}-3 =1.8-3 =-1.2
$$
2.7-4 设随机变量$X \sim Ga(\alpha,\lambda)$, 对$k=1,2,3$, 求$\mu_{k}=E(X^k)$与$v_{k}=E(X-E(X))^k$
答:  Gamma分布的k阶原点矩
$$
\begin{align}
\mu_{1} &= \frac{\alpha}{\lambda} \\
\mu_{2} &= \frac{(\alpha+1)(\alpha)}{\lambda^2} \\
\mu_{3} &= \frac{(\alpha+2)(\alpha+1)(\alpha)}{\lambda^3}
\end{align}
$$
Gamma分布的1,2,3中心矩
$$
\begin{align}
 v_1 &= 0 \\
v_2 &= \frac{\alpha}{\lambda^2} \\
v_{3} &= \frac{2\alpha}{\lambda^3} 
\end{align}
$$


2.7-5设随机变量$X \sim Exp(\alpha,\lambda)$, 对$k=1,2,3,4$,  求$\mu_{k}=E(X^k)$与$v_{k}=E(X-E(X))^k$. 进一步求此分布的变异系数,偏度系数和峰度系数
答:
根据定义
$$E(X^k) = \int_{0}^{\infty} x^k \cdot \lambda e^{-\lambda x} dx$$
利用分布积分得,
$$
\begin{align}
E(X^k) &= \left[ -x^k e^{-\lambda x} \right]_{0}^{\infty} + \int_{0}^{\infty} (e^{-\lambda x}) \cdot kx^{k-1} dx  \\
&= \frac{k}{\lambda} \int^{\infty}_{0} e^{-\lambda x} \lambda x^{k-1}dx \\
&=\frac{k}{\lambda}E(X^{k-1})
\end{align}

$$

$$
\begin{align}
\mu_{1} &= \frac{1}{\lambda}  \\
\mu_{2} &= \frac{2}{\lambda^2} \\ 
\mu_{3} &= \frac{6}{\lambda^3} \\ 
\mu_{4} &= \frac{24}{\lambda^4}
\end{align}
$$
前四阶中心矩为:
$$
\begin{align}
v_1 &= 0  \\
v_2 &= \mu_{2}-\mu^2_{1} = \frac{1}{\lambda^2} \\
v_3 & = \mu_{3}-3\mu_{2}\mu_{1} + 2\mu_{1}^3  \\
&= \frac{6}{\lambda^3}-\frac{6}{\lambda^3}+ \frac{2}{\lambda^3} = \frac{2}{\lambda^3} \\
v_{4} & = \mu_{4} -4\mu_{3}\mu_{1}+6\mu_{2}\mu_{1}^2-3\mu_{1}^4  \\
&= \frac{24}{\lambda^4} -\frac{24}{\lambda^4}+\frac{12}{\lambda^4}-\frac{3}{\lambda^4} \\
&=\frac{9}{\lambda^4}
\end{align}
$$
变异系数:
$$
C_{v} = \frac{\sqrt{Var(X)}}{E(x)} =\frac{\sqrt{v_{2}}}{\mu_{1}} =1 
$$
偏度系数:
$$
\beta_{s} = \frac{v_3}{v_{2}^{3/2}} = 2
$$
峰度系数:
$$
\beta_{k} = \frac{v_{4}}{v_{2}^2}-3 = 9-3 =6
$$




2.7-7 设随机变量$X$服从双参数韦布尔分布, 其分布函数为
$$
F(x) = 1-exp\left( -\left( \frac{x}{\eta} \right)^m \right), x>0,
$$
其中$\eta>0$, $m >0$. 试写出该分布的p分位数$x_{p}$的表达式, 且求出当$m=1.5$, $\eta=1000$时的$x_{{0.1}}$,$x_{{0.5}}$, $x_{{0.8}}$的值
答:

$$
\begin{align}
F(x_{p}) &= p   \\
1-e^{-\left( \frac{x_{p}}{\eta} \right)^m} &= p  \\
1-p &= e^{-\left( \frac{x_{p}}{\eta} \right)^m}  \\
-\ln(1-p) &= \frac{x_{p}^m}{\eta^m} \\
\eta \left( \ln\left( \frac{1}{1-p} \right) \right)^\left( \frac{1}{m} \right) &=x_{p}
\end{align}
$$

$$
x_{0.1} = 1000\left( \ln \frac{10}{9} \right)^\left( \frac{1}{1.5} \right) \approx 223.08
$$
$$
x_{0.5} = 1000\left( \ln 2\right)^\left( \frac{1}{1.5} \right) \approx 783.22
$$
$$
x_{0.8} = 1000\left( \ln 5\right)^\left( \frac{1}{1.5} \right) \approx 1373.36
$$

