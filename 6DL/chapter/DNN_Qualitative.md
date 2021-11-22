## Fourier transform of polynomials

We begin by noting that an activation function $\sigma$, which satisfies
a polynomial growth condition $|\sigma(x)| \leq C(1 + |x|)^n$ for some
constants $C$ and $n$, is a tempered distribution. As a result, we make
this assumption on our activation functions in the following theorems.
We briefly note that this condition is sufficient, but not necessary
(for instance an integrable function need not satisfy a pointwise
polynomial growth bound) for $\sigma$ to be represent a tempered
distribution.

We begin by studying the convolution of $\sigma$ with a Gaussian
mollifier. Let $\eta$ be a Gaussian mollifier
$$\eta(x) = \frac{1}{\sqrt{\pi}}e^{-x^2}.$$ Set
$\eta_\epsilon=\frac{1}{\epsilon}\eta(\frac{x}{\epsilon})$. Then
consider $$\label{sigma-epsilon}
\sigma_{\epsilon}(x):=\sigma\ast{\eta_\epsilon}(x)=\int_{\mathbb{R}}\sigma(x-y){\eta_\epsilon}(y)dy$$
for a given activation function $\sigma$. It is clear that
$\sigma_{\epsilon}\in C^\infty(\mathbb{R})$. Moreover, by considering
the Fourier transform (as a tempered distribution) we see that
$$\label{eq_278}
 \hat{\sigma}_{\epsilon} = \hat{\sigma}\hat{\eta}_{\epsilon} = \hat{\sigma}\eta_{\epsilon^{-1}}.$$

We begin by stating a lemma which characterizes the set of polynomials
in terms of their Fourier transform.

::: {.lemma}
[\[polynomial_lemma\]]{#polynomial_lemma label="polynomial_lemma"} Given
a tempered distribution $\sigma$, the following statements are
equivalent:

1.  $\sigma$ is a polynomial

2.  $\sigma_\epsilon$ given by
    [\[sigma-epsilon\]](#sigma-epsilon){reference-type="eqref"
    reference="sigma-epsilon"} is a polynomial for any $\epsilon>0$.

3.  $\text{\normalfont supp}(\hat{\sigma})\subset \{0\}$.
:::

::: {.proof}
*Proof.* We begin by proving that (3) and (1) are equivalent. This
follows from a characterization of distributions supported at a single
point (see [@strichartz2003guide], section 6.3). In particular, a
distribution supported at $0$ must be a finite linear combination of
Dirac masses and their derivatives. In particular, if $\hat{\sigma}$ is
supported at $0$, then
$$\hat{\sigma} = \displaystyle\sum_{i=1}^n a_i\delta^{(i)}.$$ Taking the
inverse Fourier transform and noting that the inverse Fourier transform
of $\delta^{(i)}$ is $c_ix^i$, we see that $\sigma$ is a polynomial.
This shows that (3) implies (1), for the converse we simply take the
Fourier transform of a polynomial and note that it is a finite linear
combination of Dirac masses and their derivatives.

Finally, we prove the equivalence of (2) and (3). For this it suffices
to show that $\hat{\sigma}$ is supported at $0$ iff
$\hat{\sigma}_\epsilon$ is supported at $0$. This follows from equation
[\[eq_278\]](#eq_278){reference-type="ref" reference="eq_278"} and the
fact that $\eta_{\epsilon^{-1}}$ is nowhere vanishing. ◻
:::

As an application of Lemma
[\[polynomial_lemma\]](#polynomial_lemma){reference-type="ref"
reference="polynomial_lemma"}, we give a simple proof of the result in
the next section.
