#!/usr/bin/env python
# coding: utf-8

# # Introduction to logistic regression
# 
# In this section, we introduce techniques related to basic logistic
# regression, see [@gelman2006data] for more details.
# 
# ## Logistic regression {#sec:LR}
# 
# Assume that we are given $k$ linearly separable sets
# $A_1,A_2,\cdots,A_k\in \mathbb{R}^d$, we define the set of classifiable
# weights as
# $$\bm\Theta = \{\bm\theta = (W,b): w_ix+b_i>w_jx+b_j,~\forall x\in A_i, j\neq i, i= 1,\cdots,k\}$$
# which means those $(W,b)$ can separate $A_1,A_2,\cdots,A_k$ correctly.
# 
# Our linearly separable assumption implies that
# $\bm\Theta\neq \emptyset$. Now we know the existence of linearly
# classifiable weights. But how can we find one element in $\bm\Theta$?
# 
# ::: definition
# [\[softmax\]]{#softmax label="softmax"} Given
# $s = (s_1,s_2,\cdots,s_k)^T\in \mathbb{R}^k$, we define the soft-max
# mapping $\sigma: \mathbb{R}^k \rightarrow\mathbb{R}^k$ as
# $$\sigma(s)  = \frac{e^{s}}{e^{s}\cdot \bm{1}} = \frac{1}{\sum\limits_{i=1}^k e^{s_i}}
#  \begin{pmatrix}
#  e^{s_1}\\
#  e^{s_2}\\
#  \vdots\\
#  e^{s_k}
#  \end{pmatrix}$$ where $e^{s} = 
#  \begin{pmatrix}
#  e^{s_1}\\
#  e^{s_2}\\
#  \vdots\\
#  e^{s_k}
#  \end{pmatrix}$, $\bm{1} = 
#  \begin{pmatrix}
#  1\\
#  1 \\
#  \vdots \\
#  1
#  \end{pmatrix} \in\mathbb{R}^k$.
# :::
# 
# ::: definition
# Given parameter $\bm\theta = (W,b)$, we define a feature mapping
# $\bm p: \mathbb{R}^d \rightarrow \mathbb{R}^k$ as
# $$\bm p(x; \bm\theta)  = \sigma(Wx+b) = \frac{1}{\sum\limits_{i=1}^k e^{w_i x+b_i}}
#  \begin{pmatrix}
#  e^{w_1 x+b_1}\\
#  e^{w_2 x+b_2}\\
#  \vdots\\
#  e^{w_k x+b_k}
#  \end{pmatrix}
#  = \begin{pmatrix}
#  p_1(x; \bm\theta) \\
#  p_2(x; \bm\theta) \\
#  \vdots \\
#  p_k(x; \bm\theta)
#  \end{pmatrix}$$ where the $i$-th component $$\label{key}
#  p_i(x; \bm\theta) = \frac{e^{w_i x+b_i}}{\sum\limits_{i=1}^k e^{w_i x+b_i}}.$$
# :::
# 
# The soft-max mapping have several important properties.
# 
# 1.  $\displaystyle 0< p_i(x; \bm\theta) <1,~\sum_i p_i(x; \bm\theta) = 1$.
# 
#     This implies that $\bm p(x; \bm\theta)$ can be regarded as a
#     probability distribution of data points which means that given
#     $x\in \mathbb{R}^d$, we have $x\in A_i$ with probability
#     $p_i(x; \bm{\theta})$, $i = 1,\cdots,k$.
# 
# 2.  $p_i(x; \bm\theta)>p_j(x; \bm\theta)\Leftrightarrow w_ix+b_i>w_j x+b_j.$
# 
#     This implies that the linearly classifiable weights have an
#     equivalent description as
#     $$\bm{\Theta} = \left\{\bm\theta: p_i(x; \bm\theta)>p_j(x; \bm\theta),~\forall x\in A_i, j\neq i, i= 1,\cdots,k\right\}$$
# 
# 3.  We usually use the max-out method to do classification. For a given
#     data point $x$, we first use a soft-max mapping to map it to
#     $\bm p(x; \bm\theta)$, then we attach $x$ to the class
#     $i= \arg\max_j p_i(x; \bm\theta)$.
# 
#     This means that we pick the label $i$ as the class of $x$ such that
#     $x\in A_i$ has the biggest probability $p_i(x; \bm\theta)$.
# 
# More detailed discussion of logistic regression from the probability
# perspective will be presented in the nearly future.
# 
# From the above properties, we can define the following likelihood
# function to help find elements in $\bm{\Theta}$: $$P (\bm\theta)=
# \prod\limits_{i = 1}^k \prod\limits_{x\in A_i} p_i(x; \bm\theta).$$
# Based on the property that $$\label{key}
# p_i (x; \bm \theta) = \max_{1\le j \le k} p_j(x; \bm \theta), \quad\forall x \in A_i,\ \bm \theta \in \Theta,$$
# we may use the next optimization problem $$\label{key}
# \max_{\bm \theta\in \bm{\Theta}} P(\bm \theta).$$ to find an element in
# $\bm{\Theta}$. More precisely, let us introduce the next lemmas
# (properties) of $P(\bm \theta)$.
# 
# ::: lemma
# [\[lemm:H1/2\]]{#lemm:H1/2 label="lemm:H1/2"} Assume that the sets
# $A_1,A_2,\cdots,A_k$ are linearly separable. Then we have
# $$\left\{\bm \theta:~P(\bm\theta)>\frac{1}{2}\right\}\subset \bm{\Theta}.$$
# :::
# 
# ::: proof
# *Proof.* It suffices to show that if $\bm\theta \not\in \bm\Theta$, we
# must have $P(\bm\theta)\leq\frac{1}{2}$. For any $\bm\theta \not\in
#     \bm\Theta$, there must exist an $i_0$ ,an $x_0\in A_{i_0}$ and a
# $j_0\neq i_0$ such that
# $$w_{i_0} x_0 + b_{i_0} \leq w_{j_0}x_0 + b_{j_0}.$$ Then we have
# $$p_{i_0}(x_0; \bm\theta) \leq \frac{e^{w_{i_0} x_0 + b_{i_0}}}{e^{w_{i_0} x_0+b_{i_0}}+e^{w_{j_0} x_0+b_{j_0}}} \leq\frac{1}{2}.$$
# Notice that $p_i(x; \bm \theta) < 1$ for all $i = 1,\cdots,k$, $x\in A$.
# So $$P(\bm\theta) <  p_{i_0}(x_0; \bm\theta) \leq \frac{1}{2}.$$ ◻
# :::
# 
# ::: lemma
# If $A_1,A_2,\cdots,A_k$ are linearly separable and
# $\bm\theta \in \bm\Theta$, we have
# $$\lim_{\alpha\rightarrow +\infty}p_i(x; \alpha\bm\theta) = 1\Leftrightarrow x\in A_i.$$
# :::
# 
# ::: proof
# *Proof.* We first note that if $x\in A_i$,
# $$p_i(x,\bm \theta) = \frac{1}{1+\sum\limits_{j\neq i}e^{\alpha[(w_j x+ b_j)-(w_i x+b_i)]}} \to 1, \quad \text{as} \quad \alpha \to \infty.$$
# On the other hand, if $x\not\in A_i$,
# $$p_i(x; \bm\alpha\bm\theta) = \frac{1}{1+\sum\limits_{j\neq i}e^{\alpha[(w_j x+ b_j)-(w_i x+b_i)]}} \leq \frac{1}{2}.$$
# This implies that if $x\not\in A_i$,
# $\lim_{\alpha\rightarrow \infty}p_i(x; \alpha\bm \theta)\neq 1$ which is
# equivalent to the proposition that if
# $\lim_{\alpha\rightarrow \infty}p_i(x; \alpha\bm \theta)= 1$, then
# $x\in A_i$. ◻
# :::
# 
# ::: lemma
# [\[thm2\]]{#thm2 label="thm2"} If $A_1,A_2,\cdots,A_k$ are linearly
# separable,
# $$\bm\Theta = \left\{\bm\theta: \lim_{\alpha\rightarrow +\infty}P(\alpha\bm\theta) = 1\right\}.$$
# :::
# 
# ::: proof
# *Proof.* We first note that if $\bm\theta \in\bm\Theta$, we have
# $\displaystyle\lim_{\alpha\rightarrow +\infty}p_i(x; \alpha\bm\theta) = 1$
# for all $x\in A_i$. So
# $$\lim\limits_{\alpha\rightarrow +\infty} P(\alpha\bm\theta) = \lim\limits_{\alpha\rightarrow +\infty} \prod\limits_{i = 1}^k \prod\limits_{x\in A_i} p_i(x; \alpha\bm\theta) = \prod\limits_{i = 1}^k \prod\limits_{x\in A_i} \lim\limits_{\alpha\rightarrow +\infty}p_i(x; \alpha\bm\theta) = 1.$$
# On the other hand, if
# $\lim\limits_{\alpha\rightarrow +\infty} P(\alpha\bm\theta) = 1$, there
# must exist one $\alpha_0>0$ such that
# $P(\alpha_0\bm\theta) >\frac{1}{2}$. From
# Lemma [\[lemm:H1/2\]](#lemm:H1/2){reference-type="ref"
# reference="lemm:H1/2"}, we have $\alpha_0\bm\theta\in\bm\Theta$, which
# means $\bm\theta\in\bm\Theta$. ◻
# :::
# 
# These properties above imply that if we can obtain a classifiable weight
# through maximizing $P(\bm\theta)$, while lemma
# [\[thm2\]](#thm2){reference-type="ref" reference="thm2"} tells us that
# $P(\bm\theta)$ will not have a global minimum actually.
# 
# More specifically, we just need to find some $\bm \theta \in \Theta$
# such that $$\label{key}
# P(\bm \theta) > \frac{1}{2} \Leftrightarrow  L(\bm \theta) : = -\log P(\bm \theta )  < \log(2).$$
# 
# ## Regularized logistic regression
# 
# Here, we start from the regularization term
# $e^{-\lambda R(\|\bm\theta\|)}$ with these next properties:
# 
# 1.  $\lambda > 0$.
# 
# 2.  $R(t)$ is a strictly increasing function on $\mathbb{R}^+$ with
#     $R(0) = 0$, $\lim\limits_{t\rightarrow +\infty} R(t) = +\infty$. For
#     example, $R(t) = t^2$.
# 
# 3.  $\|\cdot\|$ is a norm on $R^{k\times(d+1)}$, a commonly used norm is
#     the following Frobenius norm: $$\label{key}
#         \|\bm \theta\|_F = \sqrt{\sum_{i,j}W_{ij}^2 + \sum_i b_i^2}.$$
# 
# Based on this regularization term, we may consider the following
# regularized likelihood function $P_\lambda(\bm\theta)$ as $$\label{key}
#  P_\lambda(\bm\theta) = P(\bm\theta)e^{-\lambda R(\|\bm\theta\|)}.$$
# 
# Here, let us define $$\label{key}
# \bm\Theta_{\lambda} = \mathop{{\arg\max}}_{\bm\theta}  P_\lambda(\bm\theta),$$
# where $$\label{key}
# \mathop{\arg\max}_{\bm\theta}  P_\lambda(\bm\theta) = \left\{\bm \theta ~:~ P_\lambda(\bm \theta) = \max_{\bm \theta} P_\lambda(\bm \theta) \right\}.$$
# 
# The next lemma show that the maximal set of modified objective is not
# empty.
# 
# ::: lemma
# Suppose that $A_1,A_2, \cdots, A_k$ are linearly separable, then
# 
# 1.  if $\lambda = 0$, $\bm\Theta_0 = \emptyset$,
# 
# 2.  $\bm\Theta_{\lambda}$ must be nonempty for all $\lambda>0$.
# :::
# 
# ::: proof
# *Proof.* Lemma [\[thm2\]](#thm2){reference-type="ref" reference="thm2"}
# shows the first proposition. For the second proposition, we notice that
# 
# 1.  $P_\lambda(\bm 0) = \frac{1}{k^N}$.
# 
# 2.  $\exists\ M_{\lambda}>0$ such that
#     $e^{-\lambda R(\|\bm\theta\|)}<\frac{1}{k^N}$ whenever
#     $\|\bm\theta\|> M_{\lambda}$ because of the properties of
#     $R(\|\bm\theta\|)$.
# 
# So a maxima on $\{\bm\theta: \|\bm\theta\| \le M_{\lambda}\}$ must be a
# global maxima. Then we can easily obtain the result in the lemma from
# the boundedness and closeness of
# $\{\bm\theta: \|\bm\theta\| \le M_{\lambda}\}$. ◻
# :::
# 
# Furthermore, we have the next theorem which shows that we can indeed get
# $\Theta$ by maximizing $P_\lambda(\bm \theta)$.
# 
# ::: theorem
# [\[thm-L-Theta\]]{#thm-L-Theta label="thm-L-Theta"} If
# $A_1,A_2,\cdots,A_k$ are linearly separable, $$\label{key}
#     \bm\Theta_{\lambda} \subset \bm\Theta,$$ when $\lambda>0$ and
# sufficiently small.
# :::
# 
# ::: proof
# *Proof.* By Lemma [\[lemm:H1/2\]](#lemm:H1/2){reference-type="ref"
# reference="lemm:H1/2"}, we can take $\bm\theta_0\in \bm\Theta$ such that
# $P(\bm\theta_0)> \frac{3}{4}$. Then, for any
# $\lambda < \frac{\log \frac{3}{2}}{R(\|\bm\theta_0\|)}$,
# $\bm\theta_{\lambda}\in \bm\Theta_{\lambda}$, we have
# $$P(\bm\theta_{\lambda}) \geq  P_\lambda(\bm\theta_{\lambda})  \geq P_\lambda(\bm \theta_0) = P(\bm\theta_0)e^{-\lambda R(\|\bm\theta_0\|)} > \frac{3}{4}\cdot \frac{2}{3} = \frac{1}{2},$$
# which implies that $\bm \theta_{\lambda} \in \Theta$. Thus, for any
# $0< \lambda < \frac{\log \frac{3}{2}}{R(\|\bm\theta_0\|)}$,
# $\bm\Theta_{\lambda} \subset \bm\Theta$. ◻
# :::
# 
# The design of logistic regression is that maximize
# $P_\lambda(\bm\theta)$ is equivalent to minimize
# $-\log P_\lambda(\bm\theta)$, i.e., $$\label{key}
# \max_{\bm \theta} \left\{ P_\lambda(\bm\theta) \right\} \Leftrightarrow \min_{\bm \theta} \left\{ -\log   P_\lambda(\bm\theta)\right\},$$
# while the second one is more convenient to evaluate the gradient.
# Meanwhile, we add a regularization term $R(\bm\theta)$ to the objective
# function which makes the optimization problem has a unique solution.
# 
# Mathematically, we can formulate Logistic regression as
# $$\min_{\bm\theta} L_\lambda(\bm \theta),$$ where
# $$\label{eq:logisticlambda}
# L_\lambda(\bm \theta)  := -\log P_\lambda(\bm\theta) = -\log P(\bm\theta) + \lambda R(\|\bm\theta\|) = L(\bm\theta) + \lambda R(\|\bm\theta\|),$$
# with $$\label{logistic}
# L(\bm \theta) = - \sum_{i=1}^k \sum_{x\in A_i} \log p_{i}(x;\bm \theta).$$
# 
# Then we have the next logistic regression algorithm.
# 
# ::: algorithm
# Given data $A_1, A_2, \cdots, A_k$, find $$\label{key}
#     \bm \theta^* = \mathop{\arg\min}_{\bm \theta}  L_\lambda(\bm \theta),$$
# for some sufficient small $\lambda > 0$.
# :::
# 
# ::: remark
# Here $$\label{key}
#     L(\bm \theta)  = -\log P(\bm\theta),$$ is known as the loss function
# of logistic regression model. The next reasons may show that why
# $L(\bm \theta)$ is popular.
# 
# 1.  It is more convenient to take gradient for $L(\bm \theta)$ than
#     $P(\bm \theta)$.
# 
# 2.  $L(\bm \theta)$ is related the so-called cross-entropy loss function
#     which will be discussed in the next section.
# 
# 3.  $L(\bm \theta)$ is a convex function which will be discussed later.
# :::
# 

# In[ ]:




