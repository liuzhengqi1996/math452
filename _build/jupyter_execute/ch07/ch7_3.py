#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 7.3 Definition of deep neural networks (DNN)

In this section, we will give a brief introduction to a special function
class related to deep neural networks (DNN) used in machine learning. We
then explore the relationship between DNN (with ReLU as activation
function) and linear finite element methods.

Given $n, m\ge 1$, the first ingredient in defining a deep neural
network (DNN) is (vector) linear functions of the form
$$\label{thetamap1}
\theta:\mathbb{R}^{n}\to\mathbb{R}^{m} ,$$as $\theta(x)=Wx+b$ where
$W=(w_{ij})\in\mathbb{R}^{m\times n}$, $b\in\mathbb{R}^{m}$. The second
main ingredient is a nonlinear activation function, usually denoted as
$$\label{sigma}
\sigma: \mathbb{R} \to \mathbb{R}.$$ By applying the function to each
component, we can extend this naturally to
$$\sigma:\mathbb R^{n}\mapsto \mathbb R^{n}.$$

## 7.3.1 Definition of neurons

1.  Primary variables $n_0=d$ $$x^0=x=
        \begin{pmatrix}
        x_1\        x_2\        \vdots \\  
        x_{d}
        \end{pmatrix}$$

2.  $n_1$ hyperplanes $\theta^{0}(x^0) = W^0 x + b^0$ where
    $W^0: \mathbb{R}^{d} \mapsto \mathbb{R}^{n_1}$: $$W^0x+b^0=
        \begin{pmatrix}
        w^0_1x+b^0_1\        w^0_2x+b^0_2\        \vdots \\  
        w^0_{n_1}x+b^0_{n_1}
        \end{pmatrix}\quad \mbox{with }\quad W^0=
        \begin{pmatrix}
        w^0_1\        w^0_2\        \vdots \\  
        w^0_{n_1}
        \end{pmatrix},\quad b^0=
        \begin{pmatrix}
        b^0_1\        b^0_2\        \vdots \\  
        b^0_{n_1}
        \end{pmatrix}$$

3.  $n_1$-neurons: $$x^1=\sigma(W^0x+b^0)
        =\begin{pmatrix}
        \sigma(w^0_1x+b^0_1)\        \sigma(w^0_2x+b^0_2)\        \vdots \\  
        \sigma(w^0_{n_1}x+b^0_{n_1})
        \end{pmatrix}$$

4.  $n_2$-hyperplanes $\theta^{1}(x^1) = W^1 x + b^1$ where
    $W^1: \mathbb{R}^{n_1} \mapsto \mathbb{R}^{n_2}$: $$W^1x^1+b^1=
        \begin{pmatrix}
        w^1_1x^1+b^1_1\        w^1_2x^1+b^1_2\        \vdots \\  
        w^1_{n_2}x^1+b^1_{n_2}
        \end{pmatrix}\quad \mbox{with }\quad 
        W^1=
        \begin{pmatrix}
        w^1_1 \        w^1_2 \        \vdots \\  
        w^1_{n_2} 
        \end{pmatrix},\ 
        b^1=
        \begin{pmatrix}
        b^1_1\        b^1_2\        \vdots \\  
        b^1_{n_2}
        \end{pmatrix}$$

5.  $n_2$-neurons: $$x^2=\sigma(W^1x+b^1)
        =\begin{pmatrix}
        \sigma(w^1_1x+b^1_1)\        \sigma(w^1_2x+b^1_2)\        \vdots \\  
        \sigma(w^1_{n_2}x+b^1_{n_2})
        \end{pmatrix}$$

6.  $\cdots$

## 7.3.2 Definition of deep neural network functions {#sec:DNN}

Given $d, k\in\mathbb{N}^+$ and
$$n_1,\dots,n_{k}\in\mathbb{N} \mbox{ with }n_0=d, n_{k+1}=1,$$ a
general DNN function from $\mathbb{R}^d$ to $\mathbb{R}$ is given by
$$\begin{aligned}
f^0(x)   &=\theta^0(x) \\ 
f^{\ell}(x) &= [  \theta^{\ell} \circ \sigma ](f^{\ell-1}(x)) \quad \ell = 1:k \f(x) &= f^k(x). \end{aligned}$$ The following more concise notation is
often used in computer science literature: $$\label{compress-dnn}
f(x) = \theta^{k}\circ \sigma \circ \theta^{k-1} \circ \sigma \cdots \circ \theta^1 \circ \sigma \circ \theta^0(x),$$
here $\theta^i: \mathbb{R}^{n_{i}}\to\mathbb{R}^{n_{i+1}}$ are linear
functions as defined in
[\[thetamap1\]](#thetamap1){reference-type="eqref"
reference="thetamap1"}. Such a DNN is called a $(k+1)$-layer DNN, and is
said to have $k$-hidden layers. The size of this DNN is
$n_1+\cdots+n_k$.

Thus, we have the following connection of neurons and DNN functions
$$f^k(x) = \theta^{k}(x^k) = \theta^{k} \circ \sigma \circ \theta^{k-1}(x^{k-1}) = [\theta^{k} \circ \sigma ] (f^{k-1}),$$
or we can see that
$$x^k = \sigma(f^{k-1}) = \sigma \circ \theta^{k-1} \circ \sigma (f^{k-2}) = [\sigma \circ \theta^{k-1}] (x^{k-1}).$$
Based on these notation and connections, we have the following
definition of general artificial neural network functions.

Shallow (one hidden layer) neural network functions: $$\label{NN1}
\dnn(\sigma; n_1) 
=\bigg\{ f^1(x) = \theta^1 (x^1), \mbox{ with } W^\ell\in \mathbb R^{n_{\ell+1}\times
    n_{\ell}}, b^\ell\in\mathbb R^{n_\ell}, \ell=0, 1, n_0=d, n_2 = 1\bigg\}$$
Deep neural network functions: $$\label{NNL}
\dnn(\sigma; n_1,n_2,\ldots, n_L)=\bigg\{ f^{L}(x) = \theta^L (x^{L}), 
 \mbox{ with } W^\ell\in \mathbb R^{n_{\ell+1}\times
    n_{\ell}}, b^\ell\in\mathbb R^{n_\ell}, \ell=0:L, n_0=d, n_{L+1}=1\bigg\}$$
If we ignore the width (number of neurons) of network functions, we may
denote the general deep neural network functions with certain layers.

The 1-hidden layer (shallow) neural network is defined as:
$$\dnn=\dnn(\sigma) = \dnn^1(\sigma)
=\bigcup_{n_1\ge 1} \dnn(\sigma;n_1,1)$$ Generally, we can define the
L-hidden layer neural network as:
$$\dnn^L(\sigma) := \bigcup_{n_1, n_2, \cdots, n_{L}\ge 1} \dnn(\sigma;n_1,n_2,\cdots,n_L, 1).$$

## 7.3.3 ReLU DNN

In this section, we mainly consider a special activation function, known
as the *rectified linear unit* (ReLU), and defined as $\rm
ReLU: \mathbb R\mapsto \mathbb R$, $$\label{relu}
 {\rm ReLU}(x):=\max(0,x), \quad x\in\mathbb{R}.$$ A ReLU DNN with $k$
hidden layers might be written as: $$\label{relu-dnn}
f(x) = \theta^{k}\circ {\rm ReLU} \circ \theta^{k-1} \circ {\rm ReLU} \cdots \circ \theta^1 \circ {\rm ReLU} \circ \theta^0(x).$$

We note that $\rm ReLU$ is a continuous piecewise linear (CPWL)
function. Since the composition of two CPWL functions is still a CPWL
function, we have the following observation [@arora2016understanding].

::: {.lemma}
[\[dnn-cpwl\]]{#dnn-cpwl label="dnn-cpwl"} Every ReLU DNN:
$\mathbb{R}^d\to\mathbb{R}^c$ is a continuous piecewise linear function.
More specifically, given any ReLU DNN, there is a polyhedral
decomposition of $\mathbb R^d$ such that this ReLU DNN is linear on each
polyhedron in such a decomposition.
:::

Here is a simple example for the "grid\" created by some 2-layer ReLU
DNNs in $\mathbb{R}^2$.

get_ipython().system('[Projections of the domain partitions formed by 2-layer ReLU DNNs with')
sizes
$(n_0, n_1, n_2, n_3)= (2, 5, 5, 1), (2, 10, 10, 1) \text{and}\ (2, 20, 20, 1)$
with random
parameters.](figures/2to5to5to1-eps-converted-to.pdf "fig:"){#fig:dnn-region
width=".3\\textwidth"} ![Projections of the domain partitions formed by
2-layer ReLU DNNs with sizes
$(n_0, n_1, n_2, n_3)= (2, 5, 5, 1), (2, 10, 10, 1) \text{and}\ (2, 20, 20, 1)$
with random
parameters.](figures/2to10to10to1-eps-converted-to.pdf "fig:"){#fig:dnn-region
width=".3\\textwidth"} ![Projections of the domain partitions formed by
2-layer ReLU DNNs with sizes
$(n_0, n_1, n_2, n_3)= (2, 5, 5, 1), (2, 10, 10, 1) \text{and}\ (2, 20, 20, 1)$
with random
parameters.](figures/2to20to20to1-eps-converted-to.pdf "fig:"){#fig:dnn-region
width=".3\\textwidth"}

For convenience of exposition, we introduce the following notation:
Namely $\dnn^L({\sigma})$ represents the DNN model with $L$ hidden
layers and ReLU activation function with arbitrary size, if
$\sigma = {\rm ReLU}$.


# ## 7.3.4 Fourier transform of polynomials
# 
# We begin by noting that an activation function $\sigma$, which satisfies
# a polynomial growth condition $|\sigma(x)| \leq C(1 + |x|)^n$ for some
# constants $C$ and $n$, is a tempered distribution. As a result, we make
# this assumption on our activation functions in the following theorems.
# We briefly note that this condition is sufficient, but not necessary
# (for instance an integrable function need not satisfy a pointwise
# polynomial growth bound) for $\sigma$ to be represent a tempered
# distribution.
# 
# We begin by studying the convolution of $\sigma$ with a Gaussian
# mollifier. Let $\eta$ be a Gaussian mollifier
# $$\eta(x) = \frac{1}{\sqrt{\pi}}e^{-x^2}.$$ Set
# $\eta_\epsilon=\frac{1}{\epsilon}\eta(\frac{x}{\epsilon})$. Then
# consider $$\label{sigma-epsilon}
# \sigma_{\epsilon}(x):=\sigma\ast{\eta_\epsilon}(x)=\int_{\mathbb{R}}\sigma(x-y){\eta_\epsilon}(y)dy$$
# for a given activation function $\sigma$. It is clear that
# $\sigma_{\epsilon}\in C^\infty(\mathbb{R})$. Moreover, by considering
# the Fourier transform (as a tempered distribution) we see that
# $$\label{eq_278}
#  \hat{\sigma}_{\epsilon} = \hat{\sigma}\hat{\eta}_{\epsilon} = \hat{\sigma}\eta_{\epsilon^{-1}}.$$
# 
# We begin by stating a lemma which characterizes the set of polynomials
# in terms of their Fourier transform.
# 
# ::: {.lemma}
# [\[polynomial_lemma\]]{#polynomial_lemma label="polynomial_lemma"} Given
# a tempered distribution $\sigma$, the following statements are
# equivalent:
# 
# 1.  $\sigma$ is a polynomial
# 
# 2.  $\sigma_\epsilon$ given by
#     [\[sigma-epsilon\]](#sigma-epsilon){reference-type="eqref"
#     reference="sigma-epsilon"} is a polynomial for any $\epsilon>0$.
# 
# 3.  $\text{\normalfont supp}(\hat{\sigma})\subset \{0\}$.
# :::
# 
# ::: {.proof}
# *Proof.* We begin by proving that (3) and (1) are equivalent. This
# follows from a characterization of distributions supported at a single
# point (see [@strichartz2003guide], section 6.3). In particular, a
# distribution supported at $0$ must be a finite linear combination of
# Dirac masses and their derivatives. In particular, if $\hat{\sigma}$ is
# supported at $0$, then
# $$\hat{\sigma} = \displaystyle\sum_{i=1}^n a_i\delta^{(i)}.$$ Taking the
# inverse Fourier transform and noting that the inverse Fourier transform
# of $\delta^{(i)}$ is $c_ix^i$, we see that $\sigma$ is a polynomial.
# This shows that (3) implies (1), for the converse we simply take the
# Fourier transform of a polynomial and note that it is a finite linear
# combination of Dirac masses and their derivatives.
# 
# Finally, we prove the equivalence of (2) and (3). For this it suffices
# to show that $\hat{\sigma}$ is supported at $0$ iff
# $\hat{\sigma}_\epsilon$ is supported at $0$. This follows from equation
# [\[eq_278\]](#eq_278){reference-type="ref" reference="eq_278"} and the
# fact that $\eta_{\epsilon^{-1}}$ is nowhere vanishing. ◻
# :::
# 
# As an application of Lemma
# [\[polynomial_lemma\]](#polynomial_lemma){reference-type="ref"
# reference="polynomial_lemma"}, we give a simple proof of the result in
# the next section.
# 

# In[ ]:




