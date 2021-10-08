# General Covariance

Let $X \in V$ be a random variable living in an inner product space V
with $E\left[ X\right] = 0$ Define: The covariance of X is the quadratic
form $\operatorname{Cov}(X): V \rightarrow R$ defined by
$$\operatorname{Cov}(X)(v)=E\left[\langle X, v\rangle^{2}\right]$$ If V
is finite dimensional and $e_{1}, \dots, e_{n}$ is an orthonormal matrix
then $$\langle X, v\rangle=X^{\top} v=v^{\top} X$$ and so
$$\operatorname{Cov}(X)(v)=\mathbb{E}\left[v^{\top} X X^{\top} v\right]=v^{\top} \mathbb{E}\left[X X^{\top}\right] v$$
Sometimes, we may define a scalar variance
$$\operatorname{Var}(X)=\mathbb{E}\left[\|X\|^{2}\right]=\operatorname{tr}\left(\mathbb{E}\left[X X^{\top}\right]\right)$$

## Whitening

Consider transforming the random variable X with a linear transformation
matrix A. Then
$$Cov(A X)=\mathbb{E}\left[AXX^{\top} A^{\top}\right]=A \mathbb{E}\left[X X^{\top}\right] A^{\top}=A V A^{T}$$
where $V= \mathbb{E}\left[X X^{\top}\right]$ is the coveriance of $X$.
So if we choose A s.t.
$$A VA^{\top}=I \Leftrightarrow V=A^{-1} A^{-T},$$ then $$Cov(A X)= I,$$
so $AX$ is \"white noise\". Clearly there are many choice for $A$.
Namely given an $A$, $OA$ also works for any orthonormal $O$.

## Batch Normalization

-   Calculating an appropriate A is generally competationally too
    expensive. The most efficient way to do it is likely a Cholesky
    factorization.

-   In BN, we instead choose A diagonal so that
    $$\operatorname{diag}\left(A \cup A^{T}\right)=(1,1, \ldots, 1)$$

-   Of course the off-diagonal entries of $A \cup A^{T}$ will generally
    not be $O$.

## Central Limiting Theorem

Let $X_{1}, X_{2}, \ldots, X_{n}$ be independent copies of $X\in \Omega$
with $E\left[ X\right] = 0$. Then $V=E\left[ XX^T\right]$. Consider
$$\bar{X}_{n}=\frac{1}{\sqrt{n}} \sum\limits_{i=1}^{n} X_{i}.$$ As
$n\rightarrow \infty$, $\bar{X}_{n}$ converges to a Gaussian
distribution, namely,
$$\lim_{n \rightarrow \infty} \bar{X}_{n}= {\rm Gaussian}(0, V)$$ with
distribution
$$P(X)=\frac{1}{(\sqrt{2 n}\ {\rm det}(V))^{d}} e^{\frac{-x^{T}V^{-1}x}{2}}d x.$$
