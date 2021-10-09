#!/usr/bin/env python
# coding: utf-8

# # KL divergence and cross-entropy
# 
# Cross-entropy minimization is frequently used in optimization and
# rare-event probability estimation. When comparing a distribution against
# a fixed reference distribution, cross-entropy and KL divergence are
# identical up to an additive constant. See more details in
# [@murphy2012machine; @kullback1951information; @kullback1997information]
# and the reference therein.
# 
# The KL(Kullback--Leibler) divergence defines a special distance between
# two discrete probability distributions $$p=\left( \begin{array}{ccc}
# p_1\\
# \vdots \\
# p_k
# \end{array} \right),\quad  q=\left( \begin{array}{ccc}
# q_1\\
# \vdots \\
# q_k
# \end{array} \right)$$ with $0\le p_i, q_i\le1$ and
# $\sum_{i=1}^{k}p_i=\sum_{i=1}^{k}q_i=1$ by $$\label{KL-divergence}
# D_{\rm KL}(q,p)= \sum_{i=1}^k q_i\log \frac{q_i}{p_i}.$$
# 
# ::: lemma
# $D_{\rm KL}(q,p)$ works like a "distance\" without the symmetry:
# 
# 1.  $D_{\rm KL}(q,p)\ge0$;
# 
# 2.  $D_{\rm KL}(q,p)=0$ if and only if $p=q$;
# :::
# 
# ::: proof
# *Proof.* We first note that the elementary inequality
# $$\log x \le x - 1, \quad\mathrm{for\ any\ }x\ge0,$$ and the equality
# holds if and only if $x=1$.
# $$-D_{\rm KL}(q,p) = - \sum_{i=1}^c q_i\log \frac{q_i}{p_i}   = \sum_{i=1}^k q_i\log \frac{p_i}{q_i} \le \sum_{i=1}^k q_i( \frac{p_i}{q_i}  - 1) = 0.$$
# And the equality holds if and only if
# $$\frac{p_i}{q_i} = 1 \quad \forall i = 1:k.$$ ◻
# :::
# 
# Define cross-entropy for distribution $p$ and $q$ by
# $$\label{Cross-Entropy}
# H(q,p) = - \sum_{i=1}^k q_i \log p_i,$$ and the entropy for distribution
# $q$ by $$\label{Entropy}
# H(q) = - \sum_{i=1}^k q_i \log q_i.$$ Note that
# $$D_{\rm KL}(q,p)= \sum_{i=1}^k q_i\log \frac{q_i}{p_i} =  \sum_{i=1}^k q_i \log q_i - \sum_{i=1}^k q_i \log p_i$$
# Thus, $$\label{KLandEntropy}
# H(q,p) = H(q) + D_{\rm KL}(q,p).$$ It follows from the relation
# [\[KLandEntropy\]](#KLandEntropy){reference-type="eqref"
# reference="KLandEntropy"} that $$\label{EntropyandKL}
# \mathop{\arg\min}_p D_{\rm KL}(q,p)=\mathop{\arg\min}_p H(q,p).$$
# 
# The concept of cross-entropy can be used to define a loss function in
# machine learning and optimization. Let us assume $y_i$ is the true label
# for $x_i$, for example $y_i = e_{k_i}$ if $x_i \in A_{k_i}$. Consider
# the predicted distribution $$\label{key}
# \bm p(x; \bm \theta) = \frac{1}{\sum\limits_{i=1}^k e^{w_i x+b_i}}
# \begin{pmatrix}
# e^{w_1 x+b_1}\\
# e^{w_2 x+b_2}\\
# \vdots\\
# e^{w_k x+b_k}
# \end{pmatrix}
# = \begin{pmatrix}
# p_1(x; \bm\theta) \\
# p_2(x; \bm\theta) \\
# \vdots \\
# p_k(x; \bm\theta)
# \end{pmatrix}$$ for any data $x \in A$. By
# [\[EntropyandKL\]](#EntropyandKL){reference-type="eqref"
# reference="EntropyandKL"}, the minimization of KL divergence is
# equivalent to the minimization of the cross-entropy, namely
# $$\mathop{\arg\min}_{\theta} \sum_{i=1}^N D_{\rm KL}(y_i,\bm p(x_i; \bm \theta)) = \mathop{\arg\min}_{\theta} \sum_{i=1}^N H(y_i, \bm p(x_i; \bm \theta)).$$
# Recall that we have all data
# $D = \{(x_1,y_1),(x_2,y_2),\cdots, (x_N, y_N)\}$. Then, it is natural to
# consider the loss function as following:
# $$\sum_{j=1}^N H(y_i, \bm p(x_i; \bm \theta)),$$ which measures the
# distance between the real label and predicted one for all data. In the
# meantime, we can check that $$\begin{aligned}
# \sum_{j=1}^N H(y_j, \bm p(x_j; \bm \theta))&=-\sum_{j=1}^N y_j  \cdot \log  \bm p(x_j; \bm \theta )\\
# &=-\sum_{j=1}^N  \log p_{i_j}(x_i; \bm \theta) \quad (\text{because}~y_j = e_{i_j}~\text{for}~x_j \in A_{i_j})\\
# &=-\sum_{i=1}^k \sum_{x\in A_i}  \log p_{i}(x; \bm \theta) \\
# &=-\log \prod_{i=1}^k \prod_{x\in A_i}   p_{i}(x; \bm \theta)\\
# & = L(\theta)
# \end{aligned}$$ with $L(\theta)$ defined in
# [\[logistic\]](#logistic){reference-type="eqref" reference="logistic"}
# as
# $$L(\bm \theta) = - \sum_{i=1}^k \sum_{x\in A_i} \log p_{i}(x;\bm \theta).$$
# 
# That is to say, the logistic regression loss function defined by
# likelihood in [\[logistic\]](#logistic){reference-type="eqref"
# reference="logistic"} is exact the loss function defined by measuring
# the distance between real label and predicted one via cross-entropy. We
# can note $$\label{key}
# \min_{\bm \theta} L_\lambda(\bm \theta) \Leftrightarrow \min_{\bm \theta} \sum_{j=1}^N H(y_i, \bm p(x_i; \bm \theta)) + \lambda R(\|\bm \theta\|) 
# \Leftrightarrow \min_{\bm \theta} \sum_{j=1}^N D_{\rm KL}(y_i, \bm p(x_i; \bm \theta)) + \lambda R(\|\bm \theta\|).$$
# 

# In[ ]:




