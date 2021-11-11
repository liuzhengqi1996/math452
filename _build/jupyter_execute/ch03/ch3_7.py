#!/usr/bin/env python
# coding: utf-8

# # 3.7 Basic Statistical Learning Theory
# 
# -   Goal: Estimate an unknown probability distribution $D$ on a set $X$
#     from samples $(i,i,d)$ $x_{1}, \ldots, x_{n} \in X$
# 
# -   Introduce a family of distributions $P_{\theta}$ for
#     $\theta \in \Theta$ and try to choose $\theta$ to \"match\" the
#     samples.
# 
#     -   Maximum Likelihood Estimate: Choose $\theta$ to maximize the
#         probability of the samples.
# 
#     -   Example: Let $X=R$, have some samples $x_{1}, \ldots, x_{n}$
#         drawn from a distribution D, say $P_{\theta}$ is a Gaussian with
#         variance 1, centered at $\theta \in \mathbb{R}=\Theta$, i.e.
#         density
#         $p_{\theta}(x)=\frac{1}{\sqrt{2 \pi}} e^{-(x-\theta)^{2} / 2}$
# 
#         ![image](../figures/probabilityLR2.png){width=".55\\textwidth"}
# 
#     -   Use the samples to find the center $\theta$.
# 
# ## Maximum Likelihood Estimate(MLE)
# 
# -   Given $\theta \in \Theta (=\mathbb{R}$ for this example), what is
#     the probability of the data $\left\{x_{j}\right\}_{j=1}^{n}$?
# 
#     -   Samles independent: Likelihood function(as a function of
#         $\sigma$)
#         $$P_{\theta}\left(\left\{x_{j}\right\}_{j=1}^{n}\right)=\prod_{j=1}^{n} p_{\theta}\left(x_{j}\right)
#                 =\frac{1}{(\sqrt{2 \pi})^{n}}\prod_{j=1}^{n} e^{-\left(x_{j}-\theta\right)^{2} / 2}
#                 =\frac{1}{(2 \pi)^{n/ 2}} e^{-\sum_{j=1}^{n}\left(x_{j}-\theta\right)^{2} / 2}$$
# 
#     -   MLE: Choose $\theta$ to maximize this!
# 
#     -   Often it's useful to consider log likelihood function
#         $\log \left(P_{\theta}\left(\left\{x_{j}\right\}_{j=1}^{n}\right)\right)$
#         $$\begin{aligned} \theta^{*}= \operatorname{argmax} _{\theta \in \Theta}\log \left(P_{\theta}\left(\left\{x_{j}\right\}_{j=1}^{n}\right)\right) \\
#                 \left(\operatorname{argmin} _{\theta \in \Theta}-\log \left(P_{\theta}\left(\left\{x_{j}\right\}_{j=1}^{n}\right)\right)\right) \end{aligned}$$
# 
# -   For this example:
#     $$\log \left(P_{\theta}\left(\left\{x_{j}\right\}_{j=1}^{n}\right)\right)=-\log (2 \pi) \cdot\left(\frac{n}{2}\right)-\sum_{j=1}^{n} \frac{\left(x_{j}-\theta\right)^{2}}{2}$$
#     $$\theta^{*}=\operatorname{argmin}_{\theta \in \mathbb{R}} \sum_{j=1}^{n} \frac{\left(x_{j}-\theta\right)^{2}}{2}.$$
#     $$\theta^{*}=\frac{1}{n} \sum_{j=1}^{n} x_{j}.$$
# 
#     ![image](../figures/probabilityLR3.png){width=".55\\textwidth"}

# In[ ]:




