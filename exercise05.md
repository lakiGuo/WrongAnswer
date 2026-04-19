习题 2.4：5, 8, 10, 17, 19

习题 2.5：1, 7, 10, 15, 30

2.4-5 设随机变量$X \sim b(n,p)$, 已知$E(X)=2.4$, $Var(X)=1.44$, 求两个参数$n$和$p$各为多少?
答: $E(X)=np=2.4$
$Var(X)=np(1-p)=1.44$
则$1-p= 0.6$
所以$p=0.4$, $n=6$

2.4-8 设$X$服从泊松分布,且已知$P(X=1)=P(X=2)$, 求$P(X=4)$
答: $X \sim P(\lambda)$
$$
\begin{align*}
P(X=1)=\frac{\lambda}{1}e^{-\lambda}=\frac{\lambda^2}{2}e^{-\lambda}=P(X=2)
\end{align*}
$$
根据上式得$\lambda=2$
$$
P(X=4) = \frac{2^4}{24}e^{-2} =\frac{2}{3}e^{-2}
$$


2.4-10 设一个人一年内患感冒的次数服从参数$\lambda=5$的泊松分布. 现有某种预防感冒的药物对75%的人有效(能将泊松分布的参数减少为$\lambda=3$), 对另外的25%的人不起作用. 如果某人服用了此药, 一年内患了两次感冒,那么该药对ta有效的可能性多少
答: 由题可知 $P(感冒药有效)=0.75$
$P(感冒药无效)=0.25$
设$X$为某人一年内患感冒的次数
$$
\begin{align*}
P(感冒药有效|X=2)&= \frac{P(X=2|感冒药有效)P(感冒药有效)}{P(X=2)} \\
&=\frac{\frac{9}{2}e^{-3}*0.75}{\frac{9}{2}e^{-3}*0.75+\frac{25}{2}e^{-5}*0.25} \\
& \approx 0.889
\end{align*}
$$


2.4-17 设随机变量$X$服从参数为$\lambda$的泊松分布,试证明
$$
E(X^n)=\lambda E[(X+1)^{n-1}]
$$
利用此结果计算$E(X^3)$
答:


2.4-19 设随机变量$X$服从参数为$p$的几何分布,试证明:
$$
E\left( \frac{1}{X} \right)=\frac{-plnp}{1-p}
$$
证明:
令$q=1-p$
$$
\begin{align}
E\left( \frac{1}{X} \right) &= \sum_{k=1}^{\infty} \frac{1}{k}pq^{k-1} \\
&=\frac{p}{q}\sum_{k=1}^{\infty}  \frac{q^k}{k} \\
&=\frac{p}{q} \sum_{k=1}^{\infty} \int_{0}^qt^{k-1}dt \\
&=\frac{p}{q}\int^{q}_{0} \sum^{\infty}_{k=1}t^{k-1} dt \\
&=\frac{p}{q}\int_{0}^q \frac{1}{1-t}dt \\
&=\frac{-p\ln p}{1-p}
\end{align}
$$


(为什么这里积分号和求和号可以换序)


2.5-1 设随机变量$X$服从区间$(2,5)$上的均匀分布, 求对$X$进行3次独立观测中, 至少有2次的观测值大于3的概率
答: 设随机变量$Y$是3次独立观测中观测值大于3的次数.则$Y \sim b(3,p)$. 其中$p=P(X>3)$. 由$X \sim U(2,5)$
得$X$的概率密度函数为
$$
\begin{align}
p(x)=\begin{cases}  
 \frac{1}{3}, &2<x<5\\ 
  0,&其他\\
\end{cases}
\end{align}
$$
则
$$
p=P(X>3)=\int_{3}^{5} \left( \frac{1}{3} \right)dx=\frac{2}{3}
$$
于是
$$
\begin{align}
P(Y \geq 2) &=  \begin{pmatrix}
3  \\
2
\end{pmatrix}p^2(1-p) +  \begin{pmatrix}
3  \\
3
\end{pmatrix}p^3 \\
&=3*\left( \frac{4}{9} \right)*\left( \frac{1}{3} \right)+\frac{8}{27} \\
&=\frac{20}{27}
\end{align}
$$
2.5-7 设某种商品每周的需求量服从区间$(10,30)$上均匀分布, 而商品进货数为区间$(10,30)$中的某一整数, 商店每销售1单位商品可获利500元; 若供大于求则降价处理, 每处理1单位商品亏损100元 ; 若供不应求, 则可从外部调剂供应,此时每一单位商品仅获利300元. 为使商店所获利润期望值不少于9280元, 试确定最少进货量.
答: 设$X$为商品每周的需求量, 且$X \sim U(10,30)$ , 进货数为$a \in (10,30)$
则$X$的概率密度函数为
$$
\begin{align}
p(x) = \begin{cases}
\frac{1}{20}, &10<x<30 \\
0,& 其他
\end{cases}
\end{align}
$$
- 情形 1: 供大于求 ($10 < X < a$)
$$g(X) = 500X - 100(a - X) = 600X - 100a$$
- 情形 2：供不应求 ($a \le X < 30$)
$$g(X) = 500a + 300(X - a) = 200a + 300X$$
$$
\begin{align*}
E[g(X)] &= \int_{10}^{30} g(x)p(x) dx \\
&= \int_{10}^{a} \frac{600x - 100a}{20} dx + \int_{a}^{30} \frac{200a + 300x}{20} dx \\
&=-7.5a^2+350a+5250
\end{align*}
$$
根据题目要求
$$-7.5a^2 + 350a + 5250 \geq 9280$$
得$a_{1} \approx 20.67$ , $a_{2}=26$
由于$a$为整数, 所以最小进货量为21. 

2.5-10 某种设备的使用寿命$X$(以年计)服从指数分布, 其平均寿命为4年.制造此种设备的厂家规定, 若设备在使用一年之内损坏, 则可以予以调换. 如果设备厂每出售一台设备可赢利100元, 而调换一台设备制造厂需花费300元.试求每台设备的平均利润.
答: 
根据题意, $X \sim Exp(\lambda)$.
所以 $E(X)=\frac{1}{\lambda}=4$, $\lambda=\frac{1}{4}$
设每台的平均利润为Y.
$Y$ 实际上是一个离散型随机变量, 
- 若 $X \in [0, 1]$，利润 $Y = 100 - 300 = -200$
- 若 $X \in (1, +\infty)$，利润 $Y = 100$

$$
\begin{align}
E(Y) &=(100-300)P(X \leq 1)+100P(X>1) \\
&=-200 \int^{1}_{0}\left( \frac{1}{4} \right)e^{-\frac{1}{4}x}dx + 100 \int_{1}^{\infty}\left( \frac{1}{4} \right)e^{-\frac{1}{4}x}dx \\
&=-200(1-e^{-\frac{1}{4} })+100e^{-\frac{1}{4}} \\
&\approx 33.64
\end{align}
$$


2.5-15  试写出一下正态分布的均值和标准差
$p_{1}(x)=\frac{1}{\sqrt{\pi}}e^{-(x^2+4x+4)}$
$p_{2}(x)=\frac{\sqrt{2  }}{\sqrt{\pi}}e^{-2x^2}$
$p_{3}(x)=\frac{1}{\sqrt{\pi}}e^{-x^2}$

(1) $p_{1}(x)=\frac{1}{\sqrt{\pi}}e^{-(x^2+4x+4)}$
$\mu=-2, \sigma=\frac{\sqrt{2}}{2}$
(2) $p_{2}(x)=\frac{\sqrt{2  }}{\sqrt{\pi}}e^{-2x^2}$
$\mu=0, \sigma=\frac{1}{2}$
(3) $p_{3}(x)=\frac{1}{\sqrt{\pi}}e^{-x^2}$
$\mu=0, \sigma=\frac{\sqrt{2}}{2}$

2.5-30 设随机变量$X \sim N(\mu,\sigma^2)$, 求$E(|X-\mu|)$
答: 
$$
\begin{align*}
E(|x-\mu|)&=\int_{-\infty}^\infty |x-\mu| \left( \frac{1}{\sqrt{2 \pi}\sigma} \right)e^{-\frac{(x-\mu)^2}{2 \sigma^2}} dx \\
&= \int_{-\infty}^\mu (\mu-x) \left( \frac{1}{\sqrt{2 \pi}\sigma} \right)e^{-\frac{(x-\mu)^2}{2 \sigma^2}} dx+  \int_{\mu}^\infty (x-\mu) \left( \frac{1}{\sqrt{2 \pi}\sigma} \right)e^{-\frac{(x-\mu)^2}{2 \sigma^2}} dx \\
& = \frac{\sigma}{\sqrt{2\pi}} +  \frac{\sigma}{\sqrt{2\pi}} \\
&=\frac{2\sigma}{\sqrt{2\pi}}

\end{align*}

$$