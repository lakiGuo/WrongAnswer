参考教材:  茆诗松 程依明 濮晓龙编著 <概率论与数理统计教程 第三版>

#### 分治
$\Omega=B_{1}\cup\ldots\cup B_{n}, B_{k}\cap B_{l}=\emptyset, k\neq l$

$A=\cup_{k=1}^n(A \cap B_{k}), (A \cap B_{k})\cap(A \cap B_{l})=\emptyset$

$$
P(A)=\sum_{k=1}^{n}P(A \cap B_{k})=\sum^{n}_{k=1}P(B_{k})P(A|B_{k})
$$

$$
\sum_{k=0}^nP(B_{k}) = P(\Omega)=1
$$

#### 例 敏感问题调查
- 安全问题 (是,否的概率为$\frac{1}{2}$)
- 敏感问题

见书(P42页)

#### 例 分层抽样
失业率?
分层: 城市, 乡村, 省市区县, 年龄, 性别, 学历

$\Omega:$全国人口
$\Omega=\{B_{1}\cup \cdots\cup B_{k}  \}$

$P(失业)=\sum_{k=1}^nP(B_{k})P(失业|B_{k})$, 其中 $P(B_{k})$ 的数据已知

$(\Omega,\mathcal{F},P)$
- $(\Omega,\mathcal{F},P(\cdot|B)$
- $(B,\mathcal{F_{B}},P(|B))$
	$\mathcal{F}_{B}=\{A \cap B|A \in \mathcal{F}\}$

### 贝叶斯公式
$$
P(A)=\sum_{k=1}^n P(B_{k})P(A|B_{k})
$$
乘法公式
$$
\begin{align}
P(A \cap B_{k}) &=P(B_{k})P(A|B_{k}) \\
&=P(A)P(B_{k}|A)
\end{align}
$$
$$
\begin{align} \\
P(B_{k}|A) &=\frac{P(A \cap B_{k})}{P(A)} \\ \\
&= \frac{P(B_{k})P(A|B_{k})}{\sum_{l=1}^n P(B_{l})P(A|B_{l})}
\end{align}

$$
$n=2$, $\Omega=B \cup \bar{B}$
$$
P(B|A)=\frac{P(B)P(A|B)}{P(B)P(A|B)+P(\bar{B})P(A|\bar{B})}
$$
历史上称为逆概率公式. 贝叶斯的观点: 信息更新, 概率更新

最初
$$
\Omega = B_{1}\cup B_{2}\cdots \cup B_{n}
$$
$P(B_{k})$ 为先验的概率, 有了$A$之后, 得后验概率 $P(B|A)$ 

注意例题中, 假设独立性.

## 独立性
有一个随机实验有两个步骤. 
- $(\Omega_{1},\mathcal{F}_{1},P_{1})$
- $(\Omega_{2},\mathcal{F}_{2},P_{2})$

$\Omega=\{(x,y)| x \in \Omega_{1},y \in \Omega_{2}\}=\Omega_{1} \times \Omega_{2}$

有一个定理可以保证在整个$\mathcal{F}$上都可以定义出$P$来.
(Carathéodory Extension Theorem（卡拉西奥多里扩张定理）)


定义: 设$(\Omega,\mathcal{F},P)$是一个概率空间, 若有$A,B \in \mathcal{F}$. 满足$P(A \cap B)=P(A)P(B)$ 则称$A,B$相互独立. 注意, 这里的相互独立指代的是二元关系.


**$A$和$A$相互独立吗?

即P$(A \cap A)$是否等于

**$A$和$\bar{A}$相互独立吗?

**$A \cap B=\emptyset$ , $A$和$B$是否互相独立?**

硬币抛两次

定义一些事件, 看这些事件是否独立?

定义: 对于$A_{1},A_{2},\ldots A_{n} \in \mathcal{F}$

例: 某抽卡概率是$P=0.7%$
$

$P_{k}$表示前$k-1$次不中,$k$次中
$P_{k}=(1-p)^{k-1}p$



## 随机变量及其分布
$(\Omega,\mathcal{F},P)$ 其中样本空间$\Omega$可以看成抽象的集合.

例子: 三个骰子
$\Omega=\{(x,y,z)|x,y,z \in\{1,2,3,4,5,6\}  \}$
$S(x,y,z)=x+y+z$
可以利用上式去定义一些事件
$A = \{(x,y,z)|S(x,y,z)>3\}$
$B = \{(x,y,z)| 2 | S\}$
若 $X, \Omega \to \mathbb{R}$满足
对于任意的$x \in \mathbb{R}$
$$
A=X \leq x =\{\omega \in \Omega | X(\omega) \leq x \} \in \mathcal{F}
$$
则称$X$是一个随机变量

对所有区间$I$, 都有定义
$X \in I = \{\omega \in \Omega | X(\omega) \in I \} \in \mathcal{F}$

定义: 若$X: \Omega \to \mathbb{R}$是$(\Omega,\mathcal{F},P)$上的随机变量, 则可以定义
$$
F(x)=P(X \leq x)
$$
$F: \mathbb{R} \to \mathbb{R}$

- $0 \leq F(x) \leq 1$
- 单调增
- $F$一定是右连续的

$$
\begin{align}
P(a \le X\leq b) &=P(X \leq b)-P(X <a) \\
&=F(b)-F(a-b)
\end{align}


$$

- 离散随机变量 $X:\Omega \to \mathbb{R}$
	若$X(\Omega)$是可数(或有限的), 则称$X$是一个离散的随机变量
- 连续随机变量
	若$X(\Omega)$是$\mathbb{R}$中的区间, 则称$X$是连续的是随机变量
  有可能是既不连续的也不是离散的

离散: 记$X$取值为$x_{1},x_{2},\ldots \in \mathbb{R}$
记$P(X=x_{k})=P_{k}$ 于是$F$就是一个阶梯函数, 它在每个$x_{k}$处, 向上跳了$P_{k}$那么高
$\{P_{k}\}_{k=0}^{\infty}$叫$\{x_{k}\}$的分布列

性质:
1. $0 \leq P_k \leq 1$
2. $\sum_{k=1}^{\infty}P_{k}=1$ 这是一个收敛的正向级数

已知有理数集$\mathbb{Q}$可数, 记为$r_{1}$, $r_{2}$, $r_{3}$, $\cdots$
取$P_{k}=\frac{1}{2^k}$, $\sum_{k=1}^\infty\frac{1}{2^k}=1$
$$
F(x)=\sum_{k,x_{k}\leq x}\frac{1}{2^k}
$$
$F(x)$是一个单调函数, 且在所有有理点都不连续

连续: 若$F(x)$可写为
$$
F(x)=\int_{-\infty}^{x} p(t)dt
$$
其中$P$为非负可积函数. 则称$p(t)$为$X$的概率密度函数.
粗略地说 $F'(x)=p(x)$.

性质:
1. $p(x) \geq 0$
2. $\int_{-\infty}^{\infty}p(x)dx =1$

