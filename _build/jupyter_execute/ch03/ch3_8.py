#!/usr/bin/env python
# coding: utf-8

# # 3.8 Classfication/ Logistic Regression
# 
# -   For Classification: X is feature space and Y is label space
# 
#     $$
#         \widetilde{X}=X \times Y
#     $$
# 
# -   We have samples $\left\{\left(x_{j}, y_{j}\right)\right\}_{j=1}^{n}$
# 
# -   Suppose that D is an unknown distribution on $\widetilde{X}$, but
#     we're only trying to estimate $D_{Y|X}$ as a function of X. (Given
#     the feature $X$, what is the possible label.)
# 
# -   Introduce parameters $\theta\in \Theta$, we define $p(y|x, \theta)$
#     (called the model)
# 
# -   Now choose $\theta$ to match the data
#     $\left\{\left(x_{j}, y_{j}\right)\right\}_{j=1}^{n}$
# 
# -   MLE: 
# 
# $$
#     \begin{aligned}
#     \theta^{*}&=\operatorname{argmax}_{\theta \in\Theta} p\left(\left\{y_{i}\right\}_{j=1}^{n} |\left\{x_{j}\right\}_{j=1}^{n}, \theta\right)\\
#     &=\operatorname{argmax}_{\theta \in\Theta}  \prod_{j=1}^{n} p\left(y_{j} | x_{j}, \theta\right)   \\
#     &=\operatorname{argmin}_{\theta \in\Theta}  \sum_{j=1}^{n}-\log \left(p\left(y_{j} |x_{j},\theta\right)\right) \end{aligned}
# $$
# 
# -   Example: Logistic Regression:
# 
#     -   Model
#     
#     $$
#         p(y | x, \theta)=p(y | x, w, b)
#     $$
#    
#     with
#     $W\in \mathbb{R}^{d\times d}$ and $b\in \mathbb{R}^k$
#     (parameters for affine linear map)
# 
#    -   d: dimension of features, i.e. number of pixels
# 
#    -   k: number of classes
# 
# $$
#     p(y | x, w, b)=\mbox{ softmax} \left( W x+b\right)=\frac{1}{\sum_{i=1}^{k} e^{w_{i}\cdot x+b_{i}}}\left(\begin{array}{c}e^{w_{1}\cdot x +b_{1}}  \\ \vdots \\ e^{w_{k} \cdot x +b_{k}}\end{array}\right)
# $$
# 
# -  Need to calculate: 
# 
# $$
#     \begin{split}
#     &-\log \left(p\left(y_{i} | x_{i}, w, b\right)\right)\\
#     &=-\log \left(\frac{1}{e^{w  x_i+b} \cdot \mathbb{I}} e^{w x_i+b} \cdot y_{i}\right)\\
#     &=\log \left(e^{w x_i  +b} \cdot 1\right)-\log \left(e^{w x_i+b} \cdot y_{i}\right)
#     \end{split}
# $$
# 
# with $y_i=(0,\cdots, 0,1,0,\cdots, 0)$(only the $i$-th entry is 1, all others are 0) and all the entries of $\mathbb{I}$ are 1.
#     
# $$
#     (w, b)^{*}=\underset{w,b}{\operatorname{argmin}} \sum_{i=1}^{n} \log \left(e^{wx_{i}+b} \cdot \mathbb{I}\right)-\log \left(e^{wx_{i}+b} \cdot y_{i}\right)
# $$

# In[ ]:




