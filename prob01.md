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
