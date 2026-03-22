## 1900 Hibert 23问题
第六问题: 概率和物理的公理化 

1930s 概率公理化 由Andrey Kolmogorov完成

## 样本空间
样本空间: 随机实验的所有可能的结果构成的集合

- 抛硬币 $\Omega=\{正, 反\}$ 
- 掷骰子$\Omega=\{1,2,3,4,5,6\}$
- 做物理试验 $\Omega=\mathbb{R}$

对于有限集: 
$\Omega={\omega_{1},\omega_{2},\dots,\omega_{n}}$

## 事件
事件: 样本空间的某些子集
(也可以看作一些样本点构成的集合)

当$\Omega$是有限集或可数集, $\Omega$的所有可能的子集都是事件

当$\Omega=\mathbb{R}或\mathbb{R}^n$, 此时若把$\Omega$所有子集都可以充当事件会出现大麻烦. 那这个麻烦是什么呢? 
(随便写点: $|\Omega|=2^{\aleph_0}$)

定义, $\Omega$为样本空间, 其中$A,B \subseteq \Omega$
1. $A \subseteq B$, 表示事件A必然导致事件B
2. $A \subseteq B$, $B \subseteq A$, 则$A=B$
3. $A \cap B=\emptyset$, 称A, B不相容
比如, A为偶数构成的集合, B为奇数构成的集合
4. $C=A \cup B \subseteq \Omega$, $C: A和B至少有一个发生$
5. $D=A \cap B \subseteq \Omega$
   $D: A和B都发生$
6. $\bar{A}=\{\omega \in \Omega | \omega \notin A\}$ 叫A的对立事件
7. 可数并: $A_{1},A_{2}, \dots.  \subseteq \Omega$, $A=\cup_{n=1}^{\infty}A_{n}=\{ \omega \in \Omega | 存在n \in N, 使得\omega \in A_{n} \}$
8. 可数交: $B_{1},B_{2}, \dots.  \subseteq \Omega$, $B=\cap_{n=1}^{\infty}B_{n}=\{ \omega \in \Omega | 对任意的n \in N, 有\omega \in B_{n} \}$
9. $A-B=\{ \omega \in A| \omega \notin B \}$
10. 对称差: $A \Delta B= (A-B) \cup (B-A)$ 
    $A$和$B$两个事件有且仅有一个发生.
	这类似于微积分中的$|x-y|$.

**Q: 为什么允许无穷多个事件去做运算?** 
之后会学到概率论中两个非常重要的定理: 大数定理以及中心极限定理. 这些定理关心的是**随机变量**的极限. 

Q: 从事件$A$出发, 做什么操作能发生事件$B$. 

Q: 什么是事件? 
幂集$\mathcal{P}(\Omega)$, 一个集合所有子集构成的集合. 
定义: $\Omega$是样本空间, $\mathcal{P}(\Omega)$表示$\Omega$的所有子集构成的集合, $\mathcal{F}$ 是$\Omega$的一些子集构成的集合, 这等价于$\mathcal{F} \subseteq \mathcal{P}(\Omega)$. 

若$\mathcal{F}$满足:
1. $\Omega \in \mathcal{F}$
2. 若$A \in \mathcal{F}$, 则$\bar{A} \in \mathcal{F}$
3. 若$A_{1},A_{2},\ldots \in \mathcal{F}$, 则$\cup_{n=1}^{\infty}A_{n} \in \mathcal{F}$ (集合的可数并是封闭的)
 则称$\mathcal{F}$是$\Omega$上的一个事件域. ($\sigma-代数$) 
 $\mathcal{F}$中的一些元素($\Omega$的子集)就称为**事件**. 
 
 小tips: 一个事件域意味着$\Omega$的事件域可以有很多.
这类似于讨论线性空间的一组基. 这意味着可以选取不同的基.

集合运算的性质:
De Morgon's laws
$\overline{A \cup B} = \bar{A} \cap \bar{B}$
$\overline{A \cap B} = \bar{A} \cup \bar{B}$
$\overline{\cup_{n=1}^{\infty}A_{n}}=\cap_{n=1}^{\infty}\bar{A_{n}}$
$\overline{\cap_{n=1}^{\infty}A_{n}}=\cup_{n=1}^{\infty}\bar{A_{n}}$

有限并和有限交
取$A_{1}=A$, $A_{2}=B$, $A_{3}=A_{4}=\ldots=\emptyset$
此时$\cup_{n=1}^{\infty}A_{n}= A \cup B$
取$B_{1}=A$, $B_{2}=B$, $B_{3}=B_{4}=\ldots=\emptyset$
此时$\cup_{n=1}^{\infty}B_{n}= A \cup B$

有限并和有限交可以理解为可数并和可数交的一种特殊情形. 

可数并的封闭性可以推出可数交的封闭性(closure). 
### 当$\Omega = \mathbb{R}$, 如何取$\mathcal{F}$
- $\Omega \in \mathcal{F}$
- 把形如$(-\infty,a)$的区间加入$\mathcal{F}$.
	- 先取补集 $\Longrightarrow$ $[a,\infty) \in \mathcal{F}$
	- 取$[a,\infty) \cap (-\infty,b)=[a,b) \in \mathcal{F}, a<b$
	- $[a,b]=\cap_{n=1}^{\infty}[a,b+\frac{1}{n}) \in \mathcal{F}$
	- $\{b\}=[a,b]-[a,b) \in \mathcal{F}$
	- $(a,b)=[a,b)-\{a\} \in \mathcal{F}$
	- 可数个不叫的开区间的并:
		例子: $\Omega=[0,1]$, 
		$I_{1}=(\frac{1}{3},\frac{2}{3})$
		$I_{2}=(\frac{1}{9},\frac{2}{9})$
		$I_{3}=(\frac{7}{9},\frac{8}{9})$
		$I=I_{1} \cup I_{2}\cup I_{3}\dots \in \mathcal{F}$
		$I的长度 =\frac{1}{3}+\frac{2}{9}+\frac{4}{27}+\ldots=1$
		首项为$\frac{1}{3}$, 公比为$\frac{2}{3}$的等比数列(geometric sequence)
			$k= \bar{I}$ Cantor集, $k$的长度是0, $k$与$\mathbb{R}$等势. 很短的集合也可以包含非常多的点.
		
		补充一下自己混淆的概念:
		测度与基数.
		从测度看$|\Omega|$和从集合论看$|\Omega|$ 是不同的.
		
		问题: $\mathcal{F}$中的集合长什么样? ---> 描述集合论
- $\mathcal{F}$ 是一个最小事件域	
	这称作$\mathbb{R}$的Borel代数
	
## 概率的定义及其确定方法
样本空间$\Omega$   事件域 $\mathcal{F}$
概率: 对每个事件$A \in \mathcal{F}$, 给了一个数$P(A)$表明$A$的概率
$P: \mathcal{F} \rightarrow \mathbb{R}$
满足: 
1. 非负
2. 正则 $P(\Omega)=1$
3. 可列可加性
 若$A_1, A_{2}, \ldots \in \mathcal{F}$ , 满足$A_{i} \cap A_{j}=\emptyset$, 只要$i \neq j$
 则有$P(\cup_{n=1}^{\infty} A_{n})=\sum_{n=1}^{\infty}P(A_{n})$
则称$P$是$\Omega$上的一个概率. 
$(\Omega,\mathcal{F})$叫可测空间
$(\Omega,\mathcal{F},P)$叫概率空间

推论1: 取$A_{1}=\Omega$, $A_{2}=A_{3}=\ldots=\emptyset$
则$A_i \cap A_j  = \emptyset, i \neq j$
$\Longrightarrow P(\cup_{n=1}^{\infty}A_{n})=\sum_{n=1}^{\infty}P(A_{n})$
$1=1+\sum_{n=2}^{\infty}P(\emptyset)$
$P(\emptyset)=0$

推论2: 取$A_{1}=A \in \mathcal{F}$,$A_{2}=\bar{A}$, $A_{3}=A_{4}=\ldots=\emptyset$
$\cup_{n=1}^{\infty}A_{n}=\Omega$
$\Longrightarrow 1 = P(\Omega)=P(A)+P(\bar{A})+\sum{P(\emptyset)}$
$\Longrightarrow P(\bar{A})=1-P(A) \geq 0$
$\Longrightarrow P(A) \leq 1$

### $(\Omega,\mathcal{F},P)$怎么取?
- $\Omega$: 所有实验的可能结果, 需要想清楚这个实验是什么
- $$\mathcal{F}: \begin{cases}
& \Omega 为有限集或可数集 & \mathcal{F}=\mathcal{P}(\Omega)\\
& \Omega=\mathbb{R} &\mathcal{F}: Borel集
\end{cases}$$
- $P$怎么取
	- 例子: 抛硬币, 掷骰子

在抛硬币
	假设$P(正)=P(反)=\frac{1}{2}$
掷骰子
	假设P(k)=$\frac{1}{6}$, $k=1,\ldots,6$
当$\Omega$有限时, 如果没有导致不等概率的因素, 就假设$P(\{\omega\})=\frac{1}{n}$, 其中$\Omega$中点的个数为$n$.

## 频率--->概率
$$
P(A)= \frac{n_A}{n}
$$
$n$是实验的次数, $n_{A}$是$A$发生的次数
比如: 英文字母出现的频率
其他例子: 自己找. (也要结合数据来源来分析)

## 主观概率
没有任何技术手段可以告诉你概率多少. 在决策问题中, 每一个问题和之前发生的不一样. 需要自己主观给出某个概率. 

频率派 vs 贝叶斯派

频率派: 关心的大量单一可重复事件. 有大数定律支撑.

贝叶斯派: 概率不是客观存在的, 而是通过人们主观不断更新的东西.

Laplace : 太阳照常升起的概率是多少
Hume: 关于归纳法的循环论证问题

Laplace先规定: $P(升)=\frac{1}{2}$
贝叶斯公式: 
$P(升)=\frac{n+1}{n+2}$ $n$是见过太阳升起的次数
当$n$趋于无穷时, $P(升)$趋于1.
