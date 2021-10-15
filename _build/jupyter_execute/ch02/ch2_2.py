#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import IFrame

IFrame(src="https://cdnapisec.kaltura.com/p/2356971/sp/235697100/embedIframeJs/uiconf_id/41416911/partner_id/2356971?iframeembed=true&playerId=kaltura_player&entry_id=1_3im0zbc7&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_5pdspks0" ,width='800', height='500')


# In[2]:


from IPython.display import IFrame

IFrame(src="https://cdnapisec.kaltura.com/p/2356971/sp/235697100/embedIframeJs/uiconf_id/41416911/partner_id/2356971?iframeembed=true&playerId=kaltura_player&entry_id=1_awemnq71&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_g1ldr79i" ,width='800', height='500')


# # Introduction to logistic regression
# 
# In this section, we introduce techniques related to basic logistic
# regression, see [@gelman2006data] for more details.
# 
# ## Logistic regression 
# 
# Assume that we are given $k$ linearly separable sets
# $A_1,A_2,\cdots,A_k\in \mathbb{R}^d$, we define the set of classifiable
# weights as
# $\Theta = \{\theta = (W,b): w_ix+b_i>w_jx+b_j,~\forall x\in A_i, j\neq i, i= 1,\cdots,k\}$
# which means those $(W,b)$ can separate $A_1,A_2,\cdots,A_k$ correctly.
# 
# Our linearly separable assumption implies that
# $\Theta\neq \emptyset$. Now we know the existence of linearly
# classifiable weights. But how can we find one element in $\Theta$?
# 
# ```{admonition} definition
# Given
# $s = (s_1,s_2,\cdots,s_k)^T\in R^k$, we define the soft-max
# mapping $\sigma: \mathbb{R}^k \rightarrow\mathbb{R}^k$ as
# $\sigma(s)  = \frac{e^{s}}{e^{s}\cdot 1} = \frac{1}{\sum\limits_{i=1}^k e^{s_i}}$.
# $
# \begin{pmatrix}
# e^{s_1}\\
# e^{s_2}\\
# \vdots\\
# e^{s_k}
# \end{pmatrix}
# $ 
# where $
# e^{s} = 
# \begin{pmatrix}
# e^{s_1}\\
# e^{s_2}\\
# \vdots\\
# e^{s_k}
# \end{pmatrix}$,
# $1 = 
# \begin{pmatrix}
#  1\\
#  1 \\
#  \vdots \\
#  1
# \end{pmatrix} \in\mathbb{R}^k$.
# ```
# 
# ```{admonition} definition
# Given parameter $\theta = (W,b)$, we define a feature mapping
# $ p: \mathbb{R}^d \rightarrow \mathbb{R}^k$ as
# $ p(x; \theta)  = \sigma(Wx+b) = \frac{1}{\sum\limits_{i=1}^k e^{w_i x+b_i}}
#  \begin{pmatrix}
# e^{w_1 x+b_1}\\
#  e^{w_2 x+b_2}\\
#  \vdots\\
#  e^{w_k x+b_k}
#  \end{pmatrix}
# = \begin{pmatrix}
#  p_1(x; \theta) \\
#  p_2(x; \theta) \\
#  \vdots \\
#  p_k(x; \theta)
# \end{pmatrix}$$ where the $i$-th component $$\label{key}
#  p_i(x; \theta) = \frac{e^{w_i x+b_i}}{\sum\limits_{i=1}^k e^{w_i x+b_i}}.$
# ```
# 
# The soft-max mapping have several important properties.
# 
# 1.  $\displaystyle 0< p_i(x;\theta) <1,~\sum_i p_i(x;\theta) = 1$.
# 
#     This implies that $ p(x;\theta)$ can be regarded as a
#     probability distribution of data points which means that given
#     $x\in \mathbb{R}^d$, we have $x\in A_i$ with probability
#     $p_i(x; {\theta})$, $i = 1,\cdots,k$.
# 
# 2.  $p_i(x;\theta)>p_j(x;\theta)\Leftrightarrow w_ix+b_i>w_j x+b_j.$
# 
#     This implies that the linearly classifiable weights have an
#     equivalent description as
#     $$\Theta = \left\{\theta: p_i(x; \theta)>p_j(x;\theta),~\forall x\in A_i, j\neq i, i= 1,\cdots,k\right\}$$
# 
# 3.  We usually use the max-out method to do classification. For a given
#     data point $x$, we first use a soft-max mapping to map it to
#     $ p(x; \theta)$, then we attach $x$ to the class
#     $i= \arg\max_j p_i(x; \theta)$.
# 
#     This means that we pick the label $i$ as the class of $x$ such that
#     $x\in A_i$ has the biggest probability $p_i(x; \theta)$.
# 
# More detailed discussion of logistic regression from the probability
# perspective will be presented in the nearly future.
# 
# From the above properties, we can define the following likelihood
# function to help find elements in $\Theta$: $P (\theta)=
# \prod\limits_{i = 1}^k \prod\limits_{x\in A_i} p_i(x; \theta).$
# Based on the property that $
# p_i (x;  \theta) = \max_{1\le j \le k} p_j(x;  \theta), \quad\forall x \in A_i,\ \theta \in \Theta,$
# we may use the next optimization problem $
# \max_{ \theta\in \Theta} P(\theta).$ to find an element in
# $\Theta$. More precisely, let us introduce the next lemmas
# (properties) of $P(\theta)$.
# 
# ```{admonition} lemma
# Assume that the sets
# $A_1,A_2,\cdots,A_k$ are linearly separable. Then we have
# $$\left\{ \theta:~P(\theta)>\frac{1}{2}\right\}\subset \Theta.$$
# ```
# 
# ```{admonition} proof
# *Proof.* It suffices to show that if $\theta \not\in \Theta$, we
# must have $P(\theta)\leq\frac{1}{2}$. For any $\theta \not\in
#     \Theta$, there must exist an $i_0$ ,an $x_0\in A_{i_0}$ and a
# $j_0\neq i_0$ such that
# $w_{i_0} x_0 + b_{i_0} \leq w_{j_0}x_0 + b_{j_0}.$ Then we have
# $p_{i_0}(x_0; \theta) \leq \frac{e^{w_{i_0} x_0 + b_{i_0}}}{e^{w_{i_0} x_0+b_{i_0}}+e^{w_{j_0} x_0+b_{j_0}}} \leq\frac{1}{2}.$
# Notice that $p_i(x;  \theta) < 1$ for all $i = 1,\cdots,k$, $x\in A$.
# So $P(\theta) <  p_{i_0}(x_0; \theta) \leq \frac{1}{2}.$ ◻
# ```
# 
# ```{admonition} lemma
# If $A_1,A_2,\cdots,A_k$ are linearly separable and
# $\theta \in \Theta$, we have
# $\lim_{\alpha\rightarrow +\infty}p_i(x; \alpha\theta) = 1\Leftrightarrow x\in A_i.$
# ```
# 
# ```{admonition} proof
# *Proof.* We first note that if $x\in A_i$,
# $p_i(x,\theta) = \frac{1}{1+\sum\limits_{j\neq i}e^{\alpha[(w_j x+ b_j)-(w_i x+b_i)]}} \to 1, \quad \text{as} \quad \alpha \to \infty.$
# 
# On the other hand, if $x\not\in A_i$,
# $p_i(x; \alpha\theta) = \frac{1}{1+\sum\limits_{j\neq i}e^{\alpha[(w_j x+ b_j)-(w_i x+b_i)]}} \leq \frac{1}{2}.$
# This implies that if $x\not\in A_i$,
# $\lim_{\alpha\rightarrow \infty}p_i(x; \alpha \theta)\neq 1$ which is
# equivalent to the proposition that if
# $\lim_{\alpha\rightarrow \infty}p_i(x; \alpha \theta)= 1$, then
# $x\in A_i$. ◻
# ```
# 
# ```{admonition} lemma
# If $A_1,A_2,\cdots,A_k$ are linearly
# separable,
# $\Theta = \left\{\theta: \lim_{\alpha\rightarrow +\infty}P(\alpha\theta) = 1\right\}.$
# ```
# 
# ```{admonition} proof
# *Proof.* We first note that if $\theta \in \Theta$, we have
# $\displaystyle\lim_{\alpha\rightarrow +\infty}p_i(x; \alpha \theta) = 1$
# for all $x\in A_i$. So
# $\lim\limits_{\alpha\rightarrow +\infty} P(\alpha\theta) = \lim\limits_{\alpha\rightarrow +\infty} \prod\limits_{i = 1}^k \prod\limits_{x\in A_i} p_i(x; \alpha\theta) = \prod\limits_{i = 1}^k \prod\limits_{x\in A_i} \lim\limits_{\alpha\rightarrow +\infty}p_i(x; \alpha\theta) = 1.$
# On the other hand, if
# $\lim\limits_{\alpha\rightarrow +\infty} P(\alpha\theta) = 1$, there
# must exist one $\alpha_0>0$ such that
# $P(\alpha_0\theta) >\frac{1}{2}$. From
# lemma , we have $\alpha_0\theta\in\Theta$, which
# means $\theta\in\Theta$. ◻
# ```
# 
# These properties above imply that if we can obtain a classifiable weight
# through maximizing $P(\theta)$, while lemma
#  tells us that
# $P(\theta)$ will not have a global minimum actually.
# 
# More specifically, we just need to find some $ \theta \in \Theta$
# such that $
# P( \theta) > \frac{1}{2} \Leftrightarrow  L( \theta) : = -\log P( \theta )  < \log(2).$
# 
# ## Regularized logistic regression
# 
# Here, we start from the regularization term
# $e^{-\lambda R(\|\theta\|)}$ with these next properties:
# 
# 1.  $\lambda > 0$.
# 
# 2.  $R(t)$ is a strictly increasing function on $\mathbb{R}^+$ with
#     $R(0) = 0$, $\lim\limits_{t\rightarrow +\infty} R(t) = +\infty$. For
#     example, $R(t) = t^2$.
# 
# 3.  $\|\cdot\|$ is a norm on $R^{k\times(d+1)}$, a commonly used norm is
#     the following Frobenius norm: $
#         \| \theta\|_F = \sqrt{\sum_{i,j}W_{ij}^2 + \sum_i b_i^2}.$
# 
# Based on this regularization term, we may consider the following
# regularized likelihood function $P_\lambda(\theta)$ as $
#  P_\lambda(\theta) = P(\theta)e^{-\lambda R(\|\theta\|)}.$
# 
# Here, let us define $
# \Theta_{\lambda} = \mathop{{\arg\max}}_{\theta}  P_\lambda(\theta),$
# where $
# \mathop{\arg\max}_{\theta}  P_\lambda(\theta) = \left\{ \theta ~:~ P_\lambda( \theta) = \max_{ \theta} P_\lambda( \theta) \right\}.$
# 
# The next lemma show that the maximal set of modified objective is not
# empty.
# 
# ```{admonition} lemma
# Suppose that $A_1,A_2, \cdots, A_k$ are linearly separable, then
# 
# 1.  if $\lambda = 0$, $\Theta_0 = \emptyset$,
# 
# 2.  $\Theta_{\lambda}$ must be nonempty for all $\lambda>0$.
# ```
# 
# ```{admonition} proof
# *Proof.* Lemma 
# shows the first proposition. For the second proposition, we notice that
# 
# 1.  $P_\lambda( 0) = \frac{1}{k^N}$.
# 
# 2.  $\exists\ M_{\lambda}>0$ such that
#     $e^{-\lambda R(\|\theta\|)}<\frac{1}{k^N}$ whenever
#     $\|\theta\|> M_{\lambda}$ because of the properties of
#     $R(\|\theta\|)$.
# 
# So a maxima on $\{\theta: \|\theta\| \le M_{\lambda}\}$ must be a
# global maxima. Then we can easily obtain the result in the lemma from
# the boundedness and closeness of
# $\{\theta: \|\theta\| \le M_{\lambda}\}$. ◻
# ```
# 
# Furthermore, we have the next theorem which shows that we can indeed get
# $\Theta$ by maximizing $P_\lambda( \theta)$.
# 
# ```{admonition} theorem
#  If
# $A_1,A_2,\cdots,A_k$ are linearly separable, $
#     \Theta_{\lambda} \subset \Theta,$ when $\lambda>0$ and
# sufficiently small.
# ```
# 
# ```{admonition} proof
# *Proof.* By Lemma , we can take $\theta_0\in \Theta$ such that
# $P(\theta_0)> \frac{3}{4}$. Then, for any
# $\lambda < \frac{\log \frac{3}{2}}{R(\|\theta_0\|)}$,
# $\theta_{\lambda}\in \Theta_{\lambda}$, we have
# $P(\theta_{\lambda}) \geq  P_\lambda(\theta_{\lambda})  \geq P_\lambda( \theta_0) = P(\theta_0)e^{-\lambda R(\|\theta_0\|)} > \frac{3}{4}\cdot \frac{2}{3} = \frac{1}{2},$
# which implies that $ \theta_{\lambda} \in \Theta$. Thus, for any
# $0< \lambda < \frac{\log \frac{3}{2}}{R(\|\theta_0\|)}$,
# $\Theta_{\lambda} \subset \Theta$. ◻
# ```
# 
# The design of logistic regression is that maximize
# $P_\lambda(\theta)$ is equivalent to minimize
# $-\log P_\lambda(\theta)$, i.e., $
# \max_{ \theta} \left\{ P_\lambda(\theta) \right\} \Leftrightarrow \min_{ \theta} \left\{ -\log   P_\lambda(\theta)\right\},$
# while the second one is more convenient to evaluate the gradient.
# Meanwhile, we add a regularization term $R(\theta)$ to the objective
# function which makes the optimization problem has a unique solution.
# 
# Mathematically, we can formulate Logistic regression as
# $\min_{\theta} L_\lambda( \theta),$ where
# $
# L_\lambda( \theta)  := -\log P_\lambda(\theta) = -\log P(\theta) + \lambda R(\|\theta\|) = L(\theta) + \lambda R(\|\theta\|),$
# with $\label{logistic}
# L( \theta) = - \sum_{i=1}^k \sum_{x\in A_i} \log p_{i}(x; \theta).$
# 
# Then we have the next logistic regression algorithm.
# 
# ```{admonition} algorithm
# Given data $A_1, A_2, \cdots, A_k$, find $
#     \theta^* = \mathop{\arg\min}_{\theta}  L_\lambda( \theta),$
# for some sufficient small $\lambda > 0$.
# ```
# 
# ```{admonition} remark
# Here $
#     L( \theta)  = -\log P(\theta),$ is known as the loss function
# of logistic regression model. The next reasons may show that why
# $L( \theta)$ is popular.
# 
# 1.  It is more convenient to take gradient for $L( \theta)$ than
#     $P( \theta)$.
# 
# 2.  $L( \theta)$ is related the so-called cross-entropy loss function
#     which will be discussed in the next section.
# 
# 3.  $L( \theta)$ is a convex function which will be discussed later.
# ```
# 

# In[ ]:





# In[ ]:




