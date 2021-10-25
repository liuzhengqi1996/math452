# Weierstrass Theorem

To approximate any continuous function, a very simple idea is to
approximate the function in a polynomial space. An important property of
this space is that polynomials can approximate any reasonable function!

-   $P_n(\mathbb{R}^d)$ is dense in $C(\Omega)$ \[Weierstrass theorem\]

-   $P_n(\mathbb{R}^d)$ is dense in all Sobolev spaces:
    $L^2(\Omega), W^{m,p}(\Omega), \ldots$

## Curse of dimensionality

Number of coefficients for polynomial space $P_n(\mathbb{R}^d)$ is
$$N = \binom{d+n}{n} = \frac{(n+d)!}{d!n!}.$$ For example $n = 100$:

   $d =$        $2$              $4$                $8$
  ------- --------------- ----------------- --------------------
   $N=$    $5\times10^3$   $4.6\times10^6$   $3.5\times10^{11}$

As the this table shows, the dimension of the polynomial space
$P_n(\mathbb{R}^d)$ increases rapidly as the degree $n$ increases. This
leads to an extremely large space therefore very expensive to
approximate functions in polynomial spaces in high dimensions.
