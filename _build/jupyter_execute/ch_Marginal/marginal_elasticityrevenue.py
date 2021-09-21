#!/usr/bin/env python
# coding: utf-8

# # Elasticity & Total Revenue
# 
# 
# ```{admonition} Relationship between Elasticity and Total Revenue
# :class: info
# 
# 1. Total Revenue is increasing for those values of $p$ where $E(p) < 1$, that is, when demand is inelastic.
# 2. Total Revenue is decreasing for those values of $p$ where $E(p) > 1$, that is, when demand is elastic.
# 3. Total Revenue is maximized for those values of $p$ where $E(p) = 1$, that is, when demand is unitary. 
# ```

# In[1]:


get_ipython().run_line_magic('load_ext', 'itikz')


# In[ ]:


get_ipython().run_cell_magic('itikz', '', '\\documentclass[tikz]{standalone}\n\\usetikzlibrary{decorations.pathreplacing}\n\n\\begin{document}\n\\begin{tikzpicture}[scale=1.5]\n\n% create a white background, with a black frame\n\\draw [fill=white] (-1.5,-2.5) rectangle (8.5,7.5);  % black border\n\n% define point of tangency and second point on the curve\n\\coordinate (pointA) at (1,1.4);   \n\\coordinate (pointB) at (4,3.8416); \n\n% draw axes\n\\draw[->,thick] (-1,0) -- (8,0) node[below] {$p$}; \n\\draw[->,thick] (0,-1) -- (0,7) node[right] {$y$};\n\n% plot function\n\\draw[ultra thick,variable=\\x] plot [domain=0:7,samples=100] (\\x,{(7*\\x - \\x*\\x)/2});\n\\node at (6,5) {\\Large $y = R(p)$};\n\n% \\plot dashed lin\n\\draw[dashed] (3.5,0) -- (3.5,6.125);\n%% plot tangent line\n%\\draw[ultra thick,variable=\\x,blue]\n%plot [domain=-1:5] (\\x,{0.471 * (\\x - 1) + 1.4}) node[right] {tangent line};\n%% plot secant line\n%\\draw[ultra thick,variable=\\x,red]\n%plot [domain=-1:5] (\\x,{0.815*(\\x - 1) + 1.4}) node[right] {secant line};\n\n%% dashed lines and corresponding labels\n%\\draw[dashed] (0,1.4) node[left] {$f(a)$} -| (1,0) node[below] {$a$};\n%\\draw[dashed] (0,3.8416) node[left] {$f(a+h)$} -| (4,0) node[below] {$a+h$};\n\n%% draw points\n%\\fill[black] (pointA) circle (2pt);\n%\\fill[red] (pointB) circle (2pt);\n\n% E(p) < 1\n\\draw [ultra thick,decorate,decoration={brace,amplitude=10pt},yshift=0pt]\n(3.5,0) -- (0,0) node [black,midway,yshift=-20pt] {\\large $E(p) < 1$};\n\n% E(p) > 1\n\\draw [ultra thick,decorate,decoration={brace,amplitude=10pt},yshift=0pt]\n(7,0) -- (3.5,0) node [black,midway,yshift=-20pt] {\\large $E(p) > 1$};\n\n\n\\node at (2,3) {\\Large Inelastic};\n\\node at (2,2.5) {\\Large Demand};\n\\node at (5,3) {\\Large Elastic};\n\\node at (5,2.5) {\\Large Demand};\n\n\n%% label max revenue\n\\draw[<-] (3.5,6.125) -- (4,6.5) node[right] {\\Large Maximum Revenue};\n\n%% label unitary point\n\\draw[<-] (3.5,0) -- (4,0.375) node[right] {\\large $E(p) = 1$};\n\n\n\\node[right] at (-1,-1.5) {Any price movement {\\bf towards} the unitary price {\\bf increases} total revenue.};\n\n\\node[right] at (-1,-2.0) {Any price movement {\\bf away} from the unitary price {\\bf decreases} total revenue.};\n\n\\end{tikzpicture}\n\\end{document}')


# ## Example 1
# 
# The demand equation for widgets is given by
# 
# $$
# p = 2 - \frac{x}{10}.
# $$
# 
# Compute $E(0.5)$ and $E(1.5)$ and interpret the results.
# 
# ```{dropdown} **Step 1:** Determine $x = f(p)$.
# 
# In other words, solve for demand $x$, in terms of price $p$, using the demand equation, if possible.
# 
# \begin{align*}
# p &= 2 - \frac{x}{10} && \hbox{demand equation}\\
# 10p &= 20 - x && \hbox{multiply both sides by $10$}\\
# x + 10p &= 20  && \hbox{add $x$ to both sides}\\
# x &= 20 - 10p  && \hbox{subtract $10p$ from both sides}
# \end{align*}
# 
# Therefore, $f(p) = 20-10p$.
# ```
# 
# ```{dropdown} **Step 2:** Compute $f'(p)$.
# 
# \begin{align*}
#     f'(p) &= \frac{d}{dp}(20-10p) = -10
# \end{align*}
# ```
# 
# 
# ```{dropdown} **Step 3:** Compute $E(p)$.
# 
# \begin{align*}
# E(p) = -\frac{pf'(p)}{f(p)} 
# &= -\frac{p(-10)}{20-10p}\\
# &= \frac{10p}{20-10p}
# \end{align*}
# ```
# 
# 
# ```{dropdown} **Step 4:** Calculate $E(0.5)$.
# 
# \begin{align*}
#     E(0.5) 
#     &= \frac{10\cdot0.5}{20-10\cdot 0.5}\\
#     &= \frac{5}{20-5}\\
#     &= \frac{1}{3}
# \end{align*}
# 
# Since $E(0.5) < 1$, demand is inelastic when the price is \$0.50 and total revenue would increase if the price increases. 
# ```
# 
# 
# ```{dropdown} **Step 5:** Calculate $E(1.5)$.
# 
# \begin{align*}
#     E(1.5) 
#     &= \frac{10\cdot1.5}{20-10\cdot1.5}\\
#     &= \frac{15}{20-15}\\
#     &= 3
# \end{align*}
# 
# Since $E(1.5) > 1$, demand is elastic when the price is \$1.50 and total revenue would increase if the price decreases. 
# ```
# 
# 
# ## Example 2
# 
# Given the demand equation 
# 
# $$x + \frac{p}{6} -50 = 0$$ 
# 
# where $p$ represents the price in dollars and $x$ the number of units, determine the value of $p$ where demand is unitary and interpret the result.
# 
# 
# 
# ```{dropdown} **Step 1:** Determine $x = f(p)$. 
# 
# In other words, solve for demand $x$, in terms of price $p$, using the demand equation, if possible.
# 
# \begin{align*}
# x + \frac{p}{6} -50 &= 0 && \hbox{demand equation}\\
# x + \frac{p}{6} &= 50 && \hbox{add $50$ to both sides}\\
# x &= 50 - \frac{p}{6} && \hbox{subtract $p/6$ from both sides}
# \end{align*}
# 
# Therefore, $f(p) = 50 - \dfrac{p}{6}$.
# ```
# 
# ```{dropdown} **Step 2:** Compute $f'(p)$.
# 
# \begin{align*}
# f'(p) 
# &= \frac{d}{dp}\left(50 - \frac{p}{6}\right)\\
# &= \frac{d}{dp}\left(50 - \frac{1}{6}p\right)\\
# &= -\frac{1}{6}    
# \end{align*}
# ```
# 
# ```{dropdown} **Step 3:** Compute $E(p)$.
# 
# \begin{align*}
#     E(p) = -\frac{pf'(p)}{f(p)}
#     &= -\frac{p(-1/6)}{50 - p/6}\\
#     &= \frac{p(1/6)}{50 - p/6}\\
#     &= \frac{p}{50 - p/6} \cdot \frac{1}{6} \\
#     &=\frac{p}{(50 - p/6)6}\\
#     &= \frac{p}{300 - p}
# \end{align*}
# ```
# 
# 
# ```{dropdown} **Step 4:** Recall that demand is unitary when $E(p) = 1$.
# 
# Therefore, set $E(p) = 1$ and solve for $p$.
# 
# \begin{align*}
#     \frac{p}{300 - p} &= 1 && \hbox{set $E(p) = 1$}\\
#     p &= 300 - p && \hbox{multiply both sides by $300-p$}\\
#     2p &= 300 && \hbox{add $p$ to both sides}\\
#     p &= 150 && \hbox{divide both sides by $2$}
# \end{align*}
# 
# Therefore, when the price is \$150, demand is unitary and total revenue is maximized.  
# ```
# 
# 
# ## Example 3
# 
# Given the demand equation 
# 
# $$x^2 + 6p = 180$$ 
# 
# where $p$ represents the price in dollars and $x$ the number of units, determine the value of $p$ where demand is unitary and interpret the result.
# 
# 
# ```{dropdown} **Step 1:** Determine $x = f(p)$. 
# 
# In other words, solve for demand $x$, in terms of price $p$, using the demand equation, if possible.
# 
# \begin{align*}
#     x^2 + 6p &= 180 && \hbox{demand equation}\\
#     x^2 &= 180-6p && \hbox{subtract $6p$ from both sides}\\
#     x&= \sqrt{180-6p} && \text{take the square root of both sides, $x\geq 0$}
# \end{align*}
# 
# Therefore, $f(p) = \sqrt{180-6p}$.
# ```
# 
# ```{dropdown} **Step 2:** Compute $f'(p)$.
# 
# \begin{align*}
#     f'(p) &= \frac{d}{dp}\sqrt{180-6p}\\
#     &= \frac{d}{dp}(180-6p)^{1/2} && \text{}\\
#     &=\frac{1}{2}(180-6p)^{-\frac{1}{2}} (-6) && \text{using the generalized power rule}\\
#     &=\frac{-3}{\sqrt{180-6p}} && \text{simplify}
# \end{align*}
# ```
# 
# ```{dropdown} **Step 3:** Compute $E(p)$.
# 
# \begin{align*}
#     E(p) = -\frac{p f'(p)}{f(p)}
#     &=-\frac {p(-3 / \sqrt{180-6p})}{\sqrt{180-6p}}\\    
#     &= \frac {p}{\sqrt{180-6p}} \cdot \frac{3}{\sqrt{180-6p}}\\    
#     &= \frac {3p}{(\sqrt{180-6p})(\sqrt{180-6p})}\\
#     &= \frac{3p}{180-6p} && \text{combine the square roots}
# \end{align*}
# ```
# 
# 
# ```{dropdown} **Step 4:** Recall that demand is unitary when $E(p) = 1$.
# 
# Therefore, set $E(p) = 1$ and solve for $p$.
# 
# \begin{align*}
#     \frac{3p}{180-6p} &= 1 && \hbox{set $E(p) = 1$}\\
#     3p &= 180-6p && \hbox{multiply both sides by $180-6p$}\\
#     9p &= 180 && \hbox{add $6p$ to both sides}\\
#     p &=20 && \hbox{divide both sides by $9$}
# \end{align*}
# 
# Therefore, when the price is \$20, demand is unitary and total revenue is maximized. 
# ```
