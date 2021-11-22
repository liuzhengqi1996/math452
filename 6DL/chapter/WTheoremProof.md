::: {.theorem}
Let $\Omega\subset R^n$ be a closed and bounded set. Given any
continuous function $f(x)$ on $\Omega$, there exists a sequence of
polynomials $\{p_n(x)\}$ such that
$$\displaystyle \lim_{n\rightarrow \infty} \max_{x\in \Omega}|f(x)-p_n(x)|=0$$
:::

::: {.proof}
*Proof.* Let us first give the proof for $d=1$ and $\Omega=[0,1]$. Given
$f:[0,1]\rightarrow R$ be a continuous function.

Let $$\tilde f(x)=f(x)-l(x)$$ where $l(x)=f(0)+x(f(1)-f(0))$. Then
$\tilde f(0)=\tilde f(1)=0$. Noting that $l(x)$ is a linear function,
hence without lose of generality, we can only consider the case
$f:[0,1]\rightarrow R$ with $f(0)=f(1)=0$. Since $f$ is continuous on
the closed interval $[0,1]$, then $f$ is uniformly continuous on
$[0,1]$.

First we extend $f$ to be zero outside of $[0,1]$ and obtain
$f: R\rightarrow R$, then it is obviously that $f$ is still uniformly
continuous.

Next for $0\le x\le 1$, we construct
$$p_n(x)=\int_{-1}^1f(x+t)Q_n(t)dt=\int_{-x}^{1-x}f(x+t)Q_n(t)dt=\int_{0}^{1}f(t)Q_n(t-x)dt$$
where $Q_n(x)=c_n(1-x^2)^n$ and $$\label{intq}
\int_{-1}^1 Q_n(x) dx=1.$$ Thus $\{p_n(x)\}$ is a sequence of
polynomials.

Since $$\begin{aligned}
\int_{-1}^1 (1-x^2)^n dx&=2\int_{0}^1 (1-x^2)^n dx=  2\int_{0}^1 (1-x)^n(1+x)^n dx\\ 
&\ge 2\int_{0}^1 (1-x)^n dx=\frac{2}{n+1}> \frac{1}{n}.\end{aligned}$$
Combing with $\int_{-1}^1 Q_n(x) dx=1$, we obtain $c_n< n$ implying that
for any $\delta>0$ $$\label{qest}
 0\le Q_n(x)\le n(1-\delta^2)^n \quad (\delta\le |x|\le 1),$$ so that
$Q_n\rightarrow 0$ uniformly in $\delta\le |x|\le 1$ as
$n\rightarrow \infty$.

Given any $\epsilon >0$, since $f$ in uniformly continuous, there exists
$\delta>0$ such that for any $|y-x|<\delta$, we have $$\label{fcont}
|f(y)-f(x)|< \frac{\epsilon}{2}.$$ Finally, let $M=\max |f(x)|$, using
[\[fcont\]](#fcont){reference-type="eqref" reference="fcont"},
[\[intq\]](#intq){reference-type="eqref" reference="intq"} and
[\[qest\]](#qest){reference-type="eqref" reference="qest"}, we have
$$\begin{aligned}
\big| p_n(x)-f(x)\big|&=\big|\int_{-1}^1(f(x+t)-f(t))Q_n(t)dt\big|\le \int_{-1}^1 \big| f(x+t)-f(t)\big| Q_n(t)dt\\
&\le 2M \int_{-1}^{-\delta} Q_n(t)dt+ \frac{\epsilon}{2}\int_{-\delta}^{\delta} Q_n(t)dt+ 2M\int_{\delta}^1 Q_n(t)dt\\
&\le 4M n(1-\delta^2)^n + \frac{\epsilon}{2}< \epsilon\end{aligned}$$
for all large enough $n$, which proves the theorem.

The above proof generalize the high dimensional case easily. We consider
the case that $$\Omega=[0,1]^d.$$ By extension and using cut off
function, W.L.O.G. that we assume that $f=0$ on the boundary of $\Omega$
and we then extending this function to be zero outside of $\Omega$.

Let us consider the special polynomial functions $$\label{Qn}
Q_n(x)=c_n\prod_{k=1}^d(1-x_k^2)$$ Similar proof can then be applied. ◻
:::
