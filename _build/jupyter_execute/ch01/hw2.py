#!/usr/bin/env python
# coding: utf-8

# # Homework 1
# 

# ## Problem 1: 
# Consider $w ,b \in \mathbb{R}$ and the function that 
# for $x_1  \in \mathbb{R}$.

# 1: 
# 
# $$
# f(w,b) =  e^{x_1 w + b},
# $$
# for $x_1  \in \mathbb{R}$.
# 1.Consider the Hessian matrix of $f$ defined by
# 
# $$
#     H(w,b) = \nabla^2 f(w,b) = 
#     \begin{pmatrix}
#     \frac{\partial^2 f}{\partial w^2} & \frac{\partial^2 f}{\partial w \partial b}  \\
#     \frac{\partial^2 f}{\partial b \partial w}  & \frac{\partial^2 f}{\partial b^2} 
#     \end{pmatrix}.
# $$
#     
# Verify that 
# 
# $$
#     H(w,b) = f(w,b) x  x^T,
# $$
# 
# where 
# 
# $$
#     x = \begin{pmatrix}
#     x_1 \\
#     1
#     \end{pmatrix}.
# $$
# 
# 

# 2:
# Prove that
#     
# $$
#     v^T H(w,b) v \ge 0,
# $$
#     
# for any $ v = \begin{pmatrix}
# v_1 \\v_2
# \end{pmatrix}\in \mathbb{R}^2$ and $(w,b) \in \mathbb{R}^2$.

# ## Problem 2
# Think about the next data set $A_1, A_2 \subset \mathbb{R}^2$ with
# 
# $$
#     A_1 = \left\{ (0,1), (\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2}), (1,0), (-\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2}), 
#      (-1,0), (-\frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2}),  (0,-1), (\frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2})\right\},
# $$
# 
# and 
# 
# $$
#     A_2 = \left\{ (0,2), (\sqrt{2}, \sqrt{2}), (2,0), (-\sqrt{2}, \sqrt{2}), 
#     (-2,0), (-\sqrt{2}, -\sqrt{2}),  (0,-2), (\sqrt{2}, -\sqrt{2})\right\}.
# $$

# 1:
# Plot out $A_1$ and $A_2$ on $\mathbb{R}^2$.

# 2:
# Find a mapping 
# 
# $$
#     \varphi: \mathbb{R}^2 \mapsto \mathbb{R},
# $$ 
# 
# such that $\varphi(A_1)$ and $\varphi(A_2)$ are linearly separable where
# 
# $$
#     \varphi(A_1) := \{ \tilde x= \varphi(x) ~|~ x \in A_1\} \quad \text{and} \quad \varphi(A_2) := \{ \tilde x= \varphi(x) ~|~ x \in A_2\}.
# $$

# ## Problem 3

# Prove that if $A_1, A_2, A_3$ are all-vs-one linearly separable, then they are linearly separable.

# ## Problem 4

# Give an example of $A_1, A_2, A_3 \subset \mathbb{R}^2$ such that they are linearly separable but not  all-vs-one linearly separable.

# In[ ]:




