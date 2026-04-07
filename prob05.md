$$
P(|X-E(X)|\geq \varepsilon) \leq \frac{Var(X)}{\varepsilon^2}
$$

由于左侧$\leq 1$, 若右边$>1$, 那么实际上没有给出有用的信息.

## 常用离散分布

### 一. 二项分布
对应于n重Bernoulli实验

对于随机实验
有$(\Omega,\mathcal{F},P)$, 
我们关心的是一个事件$A \in \mathcal{F}$有没有发生.

$\Omega_{A}=\{\omega_{A},\omega_{\bar{A}}\}$
$\mathcal{F}=\mathcal{P}(\Omega_{A})$ ($\Omega_{A}$的幂集)
$P(\omega_{A})=p$
$P(\omega_{\bar{A}})=1-p$
那么多次实验, 可以写成如下形式
$\Omega^n=\Omega_{A}^n=\{\omega=(\omega_{1},\omega_{2},\ldots,\omega_{n})| \omega_{i} \in \Omega_{A}   \}$
$$
X(\omega) =\text{card}(\{i \in \{1,\dots,n\}|\omega_{i}=\omega_{A}\})
$$
$$
P(X=k)=\begin{pmatrix}
n \\
k
\end{pmatrix} (1-p)^{n-k}p^k
$$

| X   | 0         | 1                                                | 2                                                  | ... | n     |
| --- | --------- | ------------------------------------------------ | -------------------------------------------------- | --- | ----- |
| P   | $(1-p)^n$ | $\begin{pmatrix}n \\1\end{pmatrix} (1-p)^{n-1}p$ | $\begin{pmatrix}n \\1\end{pmatrix} (1-p)^{n-2}p^2$ |     | $p^n$ |
当$n=1$时

| X   | 0   | 1   |
| --- | --- | --- |
| P   | 1-p | p   |
这个$X$的分布叫二项分布, 记为$b(n,p)$. $X \sim b(n,p)$

 $$
 \sum_{k=0}^{n}P(x=k)=1 \Longleftrightarrow \text{二项式定理} 
$$
$$
E(X)=\sum_{k=1}^n k \begin{pmatrix}
n \\
k
\end{pmatrix}(1-p)^{n-k}
$$
其中,$$k \begin{pmatrix}
n \\
k  \end{pmatrix} =k\frac{n!}{k!(n-k)!}=\frac{n(n-1)!}{(k-1)!((n-1)-(k-1))}= \sum_{k=0}^nn\begin{pmatrix}n-1\\k-1 \end{pmatrix}(1-p)^{n-k}p^k
$$
取$l=k-1$, 所以上式可以转换为下式:
$$
E(X)= np \sum_{l=0}^{n-1}  \begin{pmatrix}
n-1 \\
l
\end{pmatrix} (1-p)^{(n-1)-l}p^l =np
$$
接下来计算方差: 
$$
Var(X) = E(X^2)-(E(X))^2
$$
$$
\begin{align} 
E(X^2) &= \sum_{k=1}^n k^2\begin{pmatrix}
n \\
k
\end{pmatrix}(1-p)^{n-k}  \\
&= n\sum_{k=1}^nk\begin{pmatrix}n-1\\k-1 \end{pmatrix}(1-p)^{n-k}p^k \\
&=n[\sum_{k=1}^n (k-1)\begin{pmatrix}n-1\\k-1 \end{pmatrix}(1-p)^{n-k}p^k +\sum_{k=1}^n\begin{pmatrix}n-1\\k-1 \end{pmatrix}(1-p)^{n-k}p^k] \\
&= n[(n-1)p^2\sum_{l=0}^{n-2}\begin{pmatrix}n-2\\l \end{pmatrix}(1-p)^{n-2-l} p^l+p    ] \\
&=n(n-1)p^2+np
\end{align} 
$$
所以, 
$$
Var(X) = E(X^2)-(E(X))^2 = n(n-1)p^2+np-n^2p^2 =np[(n-1)p+1-np]=np(1-p)
$$



### 二. Poisson分布

1837 Poisson发现在$b(n,p)$中, 如果$n$很大, p很小, $\lambda=np$不大不小. 此时二项分布$P(X=k)$有一个近似的公式.
$b(n, \frac{\lambda}{n})$
$$
P_{k}=P(X=k)=\begin{pmatrix}
n \\
k
\end{pmatrix}(1-\frac{\lambda}{n})^{n-k}(\frac{\lambda}{n})^k
$$
固定$k$, 固定$\lambda$
$$\begin{align}
P_{k}=P(X=k)&=\begin{pmatrix}
n \\
k
\end{pmatrix}\left( 1-\frac{\lambda}{n} \right)^{n-k}\left( \frac{\lambda}{n} \right)^k \\
&= \frac{n(n-1)\cdots(n-k+1)}{k!}\left( 1-\frac{\lambda}{n} \right)^n\left( 1-\frac{\lambda}{n} \right)^{-k} \frac{\lambda^k}{n^k}  \\
& \rightarrow^{n\to\infty} \frac{\lambda^k}{k!}e^{-\lambda} 
\end{align}
$$
$$
\sum_{k=0}^{\infty} \frac{\lambda^k}{k!}=e^{\lambda}
$$
	Poisson分布: 特别大的人群以及特别小的概率
### 三. 超几何分布
袋中有$M$个红球, $N-M$个白球, **不放回地**摸$n$次, 其中红球的个数记为$X$
$$
P(X=k) =\frac{\begin{pmatrix} M \\k
\end{pmatrix}\begin{pmatrix} N-M \\n-k
\end{pmatrix}}{\begin{pmatrix} N \\n
\end{pmatrix}
}, k=0,\ldots,min(n,M)
$$
$$
\sum_{l \geq 0} \begin{pmatrix} M-1 \\l 
\end{pmatrix} \begin{pmatrix} (N-1)-(M-1) \\ (n-1)-l 
\end{pmatrix}
$$

### 四. 几何分布与负二项分布.
无限Bernoulli实验.
$$
\Omega=\{\omega=(\omega_{1},\omega_{2},\ldots)|\omega_{i} \in \{ \omega_{A},\omega_{\bar{A}} \}     \}
$$

设$X_{1}$是首次出现$\omega_{A}$的实验次数.
$$
P(X=k)= (1-p)^{k-1} p, k=1,2,\ldots
$$
$$
\sum_{k=1}^{\infty} (1-p)^{k-1}p = \frac{1}{p}  p=1
$$

负二项分布
$$
X_{r}是事件A第r次发生时的实验次数
$$
$$
\omega = (\omega_{1},\ldots,\omega_{k})
$$
其中$\omega_{k}=\omega_{A}$, 也就是A发生了第$r$次, 前面$k-1$次实验里发生了$r-1$次.
$$
P(X_{r}=k)=\begin{pmatrix} k-1\\r-1
\end{pmatrix}(1-p)^{k-r}p^{r}
$$
$$
\sum_{k=r}^{\infty} \begin{pmatrix} k-1\\r-1
\end{pmatrix}(1-p)^{k-r}p^{r}
$$



## 常用连续分布

### 一. 正态分布
$$
p(x)= \frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$
1. $p(x) \geq 0$
2. $\int_{\mathbb{R}}\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(x-\mu)^2}{2\sigma^2}} dx=1$

