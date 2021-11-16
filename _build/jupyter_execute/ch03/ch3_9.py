#!/usr/bin/env python
# coding: utf-8

# # 3.9 Bayesian Approach to Machine Learning
# 
# ## 3.9.1 Goal
# 
# -   Goal: Estimate an unknown distribution on X from data
#     $\left\{x_{j}\right\}_{j=1}^{n}$
# 
#     -   Build a model
# 
#         -   Set of parameters $\Theta$
# 
#         -   Family of distribution on X,
#             
#             $$
#                 p(x|\theta)\quad \mbox{with}\quad \theta \in \Theta
#             $$
# 
#         -   Prior distribution on the parameters $\Theta$,
#         
#             $$
#                 q(\theta).
#             $$
# 
#     -   Use Bayes' Law
#         
#         $$
#             p(\theta|x) p(x)=p(x \  and \   \theta )=p(x | \theta) p(\theta)
#         $$
# 
#     -   Recall if $A_{1} , A_{2}$ are events:
#         
#         $$
#             p\left(A_{1} | A_{2}\right)=\frac{P\left(A_{1} \cap A_{2}\right)}{P\left(A_{2}\right)}
#         $$
#         
#         $$
#             p(\theta | x)=\frac{p(x | \theta) q(\theta)}{p(x)}
#         $$
#         
#         $$
#             p(\theta |x) \sim p(x | \theta) q(\theta)
#         $$ 
#         
#         where
#         $p(\theta |x)$ is the posteriori distribution, $q(\theta)$ is
#         the prior distribution and $p(x | \theta)$ is the likelihood
#         function.
# 
# -   Stant with: prior $q(\theta)$
# 
# -   Add data $x$, replace $q$ with the posterior
# 
#     $$
#         p(\theta | x) \sim p(x | \theta) q(\theta)
#     $$
# 
# -   More data: multiply by likelihood function and then normalize
# 
# -   Left with a posterior distribution
# 
#     -   Sample from posterion distribution to approximate
#     
#         $$
#             P_{pred}(x)=\int_{\Theta} p(x | \theta) p(\theta) d \theta
#         $$
# 
#     -   Choose $\theta$ to maximize posterior distribution
#         
#         $$
#             \begin{aligned}
#             \theta^{*}&=\arg \max _{\theta \in \Theta} p(\theta|x)\\
#             &=\arg \min _{\theta \in \Theta}-\log p(\theta|x)\\
#             &=\arg \min _{\theta \in \Theta}-\log (p(x | \theta))-\log (q(\theta))+\log (p(x))\\
#             &=\arg \min _{\theta \in \Theta}-\log (p(x | \theta))-\log (q(\theta))\end{aligned}
#         $$
#         
#         where $-\log (p(x | \theta))$ is the negative log likelihood and
#         $-\log (q(\theta))$ is the regularization coming from prior.
# 
# ## 3.9.2 Example: Image Classification/ Logistic Regression
# 
# -   Images $x \in X=\mathbb{R}^{d}$
# 
# -   Labels $y \in Y=\left\{e_{1}, \ldots, e_{k}\right\}$ with $k$ is the
#     dimension of labels
# 
# -   Data $\left\{(x_{j},y_{j})\right\}_{j=1}^{n}$
# 
# -   Model
#     $\theta=(W, b) \in \mathbb{R}^{k \times d} \times \mathbb{R}^{k}$.
#     By [refernce before],
#     
#     $$
#         p(y | x, \theta)=\frac{e^{Wx+b} \cdot y}{e^{Wx+b} \cdot \mathbb{I}}
#     $$
# 
# -   Prior distribution: suppose it is a Gaussian,
# 
#     $$
#         q(W, b)=C e^{-\alpha\left(\left\|W\right\|_{2}^{2}+ \left\|b\right\|_{2}^{2}\right)}
#     $$
# 
#     -   Calculate the posterior: here $q(W,b)=p(W, b|x)$,
#         
#         $$
#             p(W, b | x, y)=\frac{p(y | x, W, b) p(W, b|x) }{p(y | x)}
#         $$
#         
#         $$
#             p(y | x)=\int_{\Theta} p(y|x, W, b) q(W, b) d \theta
#         $$
#         
#         $$
#             \begin{aligned}
#             (W, b)^{*}&=\underset{W,b}{\arg \min }-\log \left( p\left(W, b |\left\{x_{j},y_{j}\right\}_{j=1}^{n}\right)\right) \\
#         &=\underset {W,b}\arg  \min -\log \left( p\left(\left\lbrace y_{j}\right\rbrace _{j=1}^{n} | \left\lbrace x_{j}\right\rbrace _{j=1}^{n}, W, b\right)\right)-\log (q(W, b))\\
#         &=\underset {W,b}\arg  \min -\log \left(\prod_{i=1}^{n} p\left(y_{j} | x_{j}, W, b\right)\right)-\log (q(W, b))\\
#         &=\underset{W, b}{\operatorname{argmin}} \sum_{j=1}^{n} \log \left(e^{Wx+b} \cdot \mathbb{I}\right)-\log \left(e^{Wx_j+b} \cdot y_{j}\right)+\alpha\left(\|W\|_{2}^{2}+\| b\|_{2}^{2}\right).
#             \end{aligned}
#          $$
# 

# In[ ]:




