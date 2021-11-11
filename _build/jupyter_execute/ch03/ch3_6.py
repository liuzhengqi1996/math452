#!/usr/bin/env python
# coding: utf-8

# # 3.6 Maximamum Likelihood
# 
# If parameters $A$ and $b$ are known, for any data $x_1\in \mathbb{R}^n$,
# model gives softmax $\left( Ax_1+b\right)$
# 
# $$
#     \frac{1}{\sum_{i=1}^{k} e^{\vec{a_{i}}\cdot x_{i}+b_{i}}} 
#     \left(\begin{array}{c}e^{\vec{a}_{1}\cdot x_{1} +b_{1}} \\ \vdots \\ e^{a_{k} \cdot x_{1}+b_{k}}\end{array}\right)
#     =
#     \left(\begin{array}{c}
#     p(1)
#      \\ \vdots \\ 
#     p(k)
#     \end{array}\right)$$ This means that the probability that the model 
#     assigns to $l_{1}$ is
# $$
# 
# p(l)=\frac{1}{\sum_{i=1}^{k} e^{a_{i}\cdot x_{i}+b_{i}}} \cdot e^{\vec{a}_{l} \cdot x_{1}+b_{l}}$$
# Instead of considering this probability, we consider its negtive
# logarithm:
# 
# $$
#     -\log p(l)=\log \left(\sum_{i=1}^{k} e^{a_{i} \cdot x_{i}+b_{i}}\right)-\left(\vec{a}_{l} \cdot x_{1}+b_{l}\right)
# $$
# 
# Since data points are independent, so we take product of the probability
# which leads to the logistic regression loss. Logistic Regression Loss:
# 
# $$
#     L_{D}(A, b)=\sum_{(x, l) \in D}\left[\log \left(\sum_{i=1}^{k} a_{i} \cdot x+b_{i}\right)-\left(\vec{a}_{l} \cdot x+b_{l}\right)\right]
# $$
# 
# We want to maximize the probability that the model assigns to $l$, that
# means we need to minimize $-\log p(l)$. So we need to find
# 
# $$
#     (A, b)=\min _{A, b} L_{D}(A, b).
# $$

# In[ ]:




