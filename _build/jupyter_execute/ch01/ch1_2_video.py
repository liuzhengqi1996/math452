#!/usr/bin/env python
# coding: utf-8

# # Image classification problem 

# ## Image classification problem 
# We consider a basic machine learning problem for classifying a collection of images
# into k distinctive classes. As an example, we consider a two-dimensional image
# which is usually represented by a tensor $x \in R^{n_0\times n_0 \times c} = R^d$
# Here $n_0 \times n_0$ is the original image resolutuon and
# 
# $
# c=
# 	\left \{
# 	\begin{array}[rl]{rl}
# 	1 & \mbox{for grayscale image},\\    
# 	3 & \mbox{for color image}.
# 	\end{array}
# 	\right.
# $
# 
# A typical supervised machine learning problem begins with a data set (training
# data)
# 
# $
# \begin{aligned}
# D &= \{(x_j, y_j)\}_{j=1}^N, \quad \text{and} \quad A = \{ x_1, x_2, \cdots, x_N\}  \\
# A &= A_1\cup A_2\cup \cdots \cup A_k, ~A_i\cap A_j = \emptyset, \forall i \neq j
# \end{aligned}
# $
# and $y_j \in R^k$ is the label for data $x_j$, with $y_i[i]$ as the probability for $x_i$ in classes $i$ or $x_j \in A_i$.
# Here for image classification problem, $y_j = e_{i_j}$, 
# if $x_j \in A_{i_j}$ or we say $x_j$ has real label $i_j$.
# Roughly speaking, a supervised learning problem can be thought as a data fitting
# problem in a high dimensional space $R^d$. 
# Namely, we need to find a mapping such that, for any $x_j \in A$
# $
# f(x_j)\approx y_j = e_{i_j} \in \mathbb R^k.
# $
# 
# 
# for data $x_j \in A$. For general setting above, we use a probatillistic model for understanding the output $f(x) \in R^k$ as a discrete distribution on $\{1,\cdots ,k\}$,
# with $[f(x)]_{i}$ as the probability for x in the class i, namely
# $
# 0 \leq [f(x)]_i \leq 1
# $, 
# $
# \sum_{i=1}^{k}[f(x)]_{i} =1
# $.
# At last, we finish our model with a simple strategy to choose 
# $
# argmax_i\{ [f(x)]_i :  i = 1:k\}
# $
# as the label for a test data $x$, which ideally is close to . The remaining key issue is the construction of the classification mapping $f$.
# Generally speaking, there will be a test set
# $T = \{(x_j,y_j)\}_{j=1}^{M}$,
# with the same dimension of training data $D$, but is not known before we finish the
# training process. That is to say, we can use this test data $T$ to verify the performance
# of trained model $f$ .

# In[ ]:




