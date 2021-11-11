#!/usr/bin/env python
# coding: utf-8

# # 3.4 Random, Variable, Mean, Variance
# 
# -   Recall:
# 
#     -   Set if outcomes: $\Omega$
# 
#     -   Event: Subset of outcomes: $E$
# 
#     -   Probability Distribution: $p(x)$
# 
# ## 3.4.1 Random Variable
# 
# -   Defin: A random variable X is a function $X: \Omega \rightarrow S$
#     Here $S=R, R^{d}$, but could be arbitrary.
# 
# -   Ex: Rolling a die:
# 
#     -   Outcomes: $\Omega={1,2,...,6}$
# 
#     -   Events are subsets of $\Omega$
# 
#     -   Distribution: $p(1)=p(2)=...=p(6)=\frac{1}{6}$ Suppose we roll
#         the die, then if the die comes up d times, you win d dollars,
#         minus 1 dollar if it's even. The amount you win is a random
#         variable. $\begin{array}{l}
#                 X_{1}: \Omega \rightarrow R\\
#                 X_{1}(1)=1 \\
#                 X_{1}(2)=1 \\
#                 X_{1}(3)=3 \\
#                 X_{1}(4)=3 \\
#                 X_{1}(5)=5 \\
#                 X_{1}(6)=5
#             \end{array}$ Can define multiple random variables on a
#         single outcome space $\Omega$.
# 
# -   Ex: Rolling a die. If the die comes up d times, you get d dollars.
#     If d is even, then you give a dollar to your friend.
#     $X_{1} \leftarrow$ your winnings, $X_{2}\leftarrow$ your friends
#     winnings. $$\begin{aligned}
#         X_{2}: \Omega \rightarrow \mathbb{R}, & X_{2}(1)=0, \quad X_{2}(2)=1 \\
#         & X_{2}(3)=0, \quad X_{2}(4)=1 \\
#         & X_{2}(5)=0, \quad X_{2}(6)=1
#     \end{aligned}$$ From here on out $\Omega$ will be fixed, we talk
#     about different random variables on $\Omega$.
# 
# ## 3.4.2 Mean of random variable
# 
# -   Defin: Mean of a random variable $X$. Expectation of $X$:
#     $$\mathbb{E}[X]=\sum_{\omega \in \Omega} p(\omega) X(\omega)\left(=\int_{\Omega} X(\omega) p(\omega) d \omega\right)$$
# 
# -   Ex: $$\begin{aligned}
#     & \mathbb{E}\left[X_{1}\right]=\frac{1}{6}(1+1+3+3+5+5)=3 \\
#     & \mathbb{E}\left[X_{2}\right]=\frac{1}{6}(0+1+0+1+0+1)=\frac{1}{2}
#     \end{aligned}$$
# 
# ## 3.4.3 Variance of Random Variables
# 
# -   Defin: Variance of a Random Variable $X$:
#     $$V[X]=\mathbb{E}\left[X^{2}\right]-\mathbb{E}[X]^{2}=\mathbb{E}\left[(X-\mathbb{E}[X])^{2}\right]$$
# 
# -   Ex:
#     $$\begin{array}{l} V\left[X_{1}\right]=\mathbb{E}\left[X_{1}^{2}\right]-(3)^{2}\\
#         = \frac{1}{6}\left(1^{2}+1^{2}+3^{2}+3^{2}+5^{2}+5^{2}\right)-9\\
#         =\frac{1}{3}(1+9+25)-9\\
#         =\frac{35}{3}-9=\frac{8}{3}\\
#     \end{array}$$ Variance measures \"how much $X$ deviates from it's
#     average\".
# 
#     ![image](../figures/probability4.png){width=".35\\textwidth"}
# 
# ## 3.4.4 Independenve of Random variables
# 
# -   Defin: Two random variables $X_{1},X_{2}$ are independent if for any
#     $\alpha, \beta,$
#     $E_{1}=\left\{w: X_{1}(\omega)<\alpha\right\}, E_{2}=\left\{w: X_{2}(\omega)<\beta\right\}$
#     are independent events.
# 
# -   Ex: $X_{1} , X_{2}$ are independent: if
#     $(\alpha, \beta) \quad \alpha=4, \quad \beta=\frac{1}{2}$,
#     $$\begin{array}{l} 
#     E_{1}=\left\{w: X_{1}(u)<4\right\}=\{1,2,3,4\} \\
#     E_{2}=\left\{w: X_{2}(\omega)<\frac{1}{2}\right\}=\{1,3,5\}
#     \end{array}$$ $$\begin{array}{l}
#     p\left(E_{1}\bigcap E_{2}\right)=p\left(E_{1}\right) p\left(E_{2}\right) \\
#     p(\{1,3\})=p\left(E_{1}\right) p\left(E_{2}\right)
#     \end{array}$$
# 
# ## 3.4.5 Properties of E, V, Independence
# 
#     -   If $X_{1}, X_{2}$ are random variable, then
#         $$\left(a_{1}X_{1}+a_{2} x_{2}\right)(w)=a_{1} x_{1}(w)+a_{2} x_{2}(w)$$
#         $$\mathbb{E}\left[a_{1}X_{1}+a_{2} X_{2}\right]=a_{1}\mathbb{E}\left[X_{1}\right]+a_{2} \mathbb{E}\left[X_{2}\right]$$

# In[ ]:




