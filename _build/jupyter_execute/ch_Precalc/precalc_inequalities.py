#!/usr/bin/env python
# coding: utf-8

# # Solving Inequalities
# 
# ## How to Solve an Inequality
# 
# In order to find all values of $x$ such that $f(x)>0$ or $f(x)<0$, use the following procedure.
# 
# ```{admonition} Solving an inequality
# :class: info
# 
# - Find all values of $x$ such that $f(x) = 0$ or $f(x)$ is not defined.
# - Use the values found to break up the number line into intervals and select one number from each interval to plug into $f(x)$ to determine if $f(x)$ is positive or negative on that interval.
# 
# **OR**
# 
# - Use the values found to help draw the graph of $f(x)$.  Portions of the graph that are above the $x$-axis correspond to values of $x$ where $f(x)>0$ while portions of the graph that are below the $x$-axis correspond to values of $x$ where $f(x) < 0$.
# ```
# 
# (01_05_example1)=
# ### Example 1
# 
# Find all values of $x$ such that $x^2 + 2x - 3 > 0$.
# 
# 
# ```{dropdown} **Step 1:** Find all values of $x$ such that $x^2 + 2x - 3 = 0$.
# 
# Use the AC method to factor $x^2 + 2x - 3$.
# 
# $$ x^2 + 2x - 3 = (x+3)(x-1)  $$
# 
# since $3$ and $-1$ are two numbers that multiply to $-3$ and sum to $2$.  Now set each factor equal to zero and solve for $x$.
# 
# \begin{align*}
# x + 3 = 0 ~~~~&\Rightarrow~~~~ x = -3 \\
# x - 1 = 0 ~~~~&\Rightarrow~~~~ x = 1 
# \end{align*}
# ```
# 
# Use one of the following two methods to solve the inequality.

# In[1]:


get_ipython().run_line_magic('load_ext', 'itikz')


# ```{admonition} Method 1
# :class: tip
# 
# - Use the values of $x$ found in **Step 1** to break up the number line and plug in one value from each interval into $f(x) = (x+3)(x-1)$. 
# 
# - Since $f(-3) = 0$ and $f(1) = 0$, pick one value less $-3$, one value between $-3$ and $1$, and one value greater than $1$.  For example, since $f(-4) = 5 > 0$, $f(x) >0 $ for all $x < -3$.  And since $f(2) = 5 > 0$, $f(x)>0$ for all $x > 1$.  However, $f(0) = -3 < 0$, and therefore $f(x) < 0$ for all $-3<x<1$. 
# ```
# 
# The calculations of method 1 are summarized in the following diagram.

# In[ ]:


get_ipython().run_cell_magic('itikz', '', '\\documentclass[tikz]{standalone}\n\\begin{document}\n\\begin{tikzpicture}[scale=1]\n\\draw[white,fill=white] (-9.5,-1) rectangle (4,1);\n\\draw[->](-6,0) -- (4,0) ;\n\\foreach \\x in {-3, 1}\n\t\\draw (\\x, 6pt) -- (\\x, -6pt) node[below, scale=1.5] {$\\x$};\n\t\n\\node[above, scale=1.5] at (-4,0){$+$};\n\\node[above, scale=1.5] at (0,0){$-$};\n\\node[above, scale=1.5] at (2,0){$+$};\n\n\t\\draw (-4, 3pt) -- (-4, -3pt) node[below, scale=1.5] {$-4$} ;\n\t\\draw (0, 3pt) -- (0, -3pt) node[below, scale=1.5] {$0$} ;\n\t\\draw (2, 3pt) -- (2, -3pt) node[below, scale=1.5] {$2$} ;\n\n\\node[left, scale=1.5] at (-6,0.5){sign of $f(x)$};\n\\end{tikzpicture} \n\\end{document}')


# Therefore, $x^2+2x-3 >0$ whenever $x<-3$ or $x>1$.
# 
# 
# ```{admonition} Method 2
# :class: tip
# 
# Sketch the graph of $y=x^2+2x-3$ by drawing a parabola that opens upward and goes through the points $(-3,0)$ and $(1,0)$.
# ```

# In[ ]:


get_ipython().run_cell_magic('itikz', '', '\\documentclass[tikz]{standalone}\n\\begin {document}\n\\begin{tikzpicture}[xscale=1,yscale=0.6]\n\n\\draw[white,fill=white] (-5.3,-5.3) rectangle (3.3,5.3);\n%\\draw[very thin,color=lightgray,step=1] (-4.9,-4.9) grid (2.9,4.9);\n\n\\draw[->] (-5,0) -- (3,0) node[below] {$x$};\n\\draw[->] (0,-5) -- (0,5) node[right] {$y$};\n       \n\\draw [fill=black] (-3,0) ellipse [x radius = 0.15, y radius = 0.25];\n\\draw [fill=black] (1,0) ellipse [x radius = 0.15, y radius = 0.25];\n\n% tick marks\n\\foreach \\x in {-4,-2,2} \n\t\\draw [thick] (\\x cm,6pt) -- (\\x cm,-6pt) node[below] {$\\x$};\n\\foreach \\y in {} \n\t\\draw [thick] (-2pt,\\y cm) -- (2pt,\\y cm) node[right] {$\\y$};\n\t\n\\clip (-6,-5) rectangle (6,5);\n\\draw[domain=-4:2,smooth,variable=\\x,black,ultra thick] plot ({\\x},{\\x*\\x + 2*\\x - 3}); \n%\\node at (4.1, 4.5){$y = x^2 + 2x - 3$};\n\\end{tikzpicture}\n\\end{document}')


# Finding values of $x$ such that $x^2+2x-3 > 0$ is equivalent to identifying the portions of the graph of $x^2+2x-3$ that are above the $x$-axis.  Based on the graph shown above, $x^2+2x-3 >0$ whenever $x<-3$ or $x>1$.
# 
# 
# 
# 
# 
# ### Example 2
# Find all values of $x$ such that $\dfrac{x^2(x^2+3)}{(4-x^2)^3} < 0$.
# 
# 
# 
# ```{dropdown} **Step 1:** Find all $x$ such that $\frac{x^2(x^2+3)}{(4-x^2)^3} = 0$ or is not defined. 
# 
# $\frac{x^2(x^2+3)}{(4-x^2)^3} = 0$ whenever the numerator is equal to zero, which only happens when $x=0$ (since $x^2+3$ is never equal to zero).
# 
# $\frac{x^2(x^2+3)}{(4-x^2)^3}$ is not defined whenever the denominator is equal to zero, which only happens when $x=-2$ or $x=2$.
# ```
# 
# 
# Use one of the following two methods to solve the inequality. 
# 
# ```{admonition} Method 1
# :class: tip
# 
# Break up the number line at $x=-2$, $x=0$, and $x=2$ and plug in one value from each interval to determine the sign of $f(x) = \frac{x^2(x^2+3)}{(4-x^2)^3}$ on that interval.
# ```

# In[ ]:


get_ipython().run_cell_magic('itikz', '', '\\documentclass[tikz]{standalone}\n\\begin {document}\n\\begin{tikzpicture}[scale=1.5]\n\\draw[white,fill=white] (-6.5,-0.6) rectangle (4,0.6);\n\\draw[->](-4,0) -- (4,0) ;\n\\foreach \\x in {-2,0,2}\n\t\\draw (\\x, 3pt) -- (\\x, -3pt) node[below, scale=1.5] {$\\x$} ;\n\t\n\\node[above, scale=1.5] at (-3,0){$-$};\n\\node[above, scale=1.5] at (-1,0){$+$};\n\\node[above, scale=1.5] at (1,0){$+$} ;\n\\node[above, scale=1.5] at (3,0){$-$} ;\n\n\t\\draw (-3, 2pt) -- (-3, -2pt) node[below, scale=1.5] {$-3$} ;\n\t\\draw (-1, 2pt) -- (-1, -2pt) node[below, scale=1.5] { $-1$} ;\n\t\\draw (1, 2pt) -- (1, -2pt) node[below, scale=1.5] { $1$} ;\n\t\\draw (3, 2pt) -- (3, -2pt) node[below, scale=1.5] {$3$} ;\n\n\\node[left, scale=1.5] at (-4,0.25){sign of $f(x)$};\n\n\\end{tikzpicture} \n\\end{document}')


# Therefore, $\frac{x^2(x^2+3)}{(4-x^2)^3} < 0$ when $x<-2$ or $x>2$.
# 
# 
# ```{admonition} Method 2
# :class: tip
# 
# Break up the number line at $x=-2$, $x=0$, and $x=2$ and plug in one value from each interval to determine the sign of $f(x) = \frac{x^2(x^2+3)}{(4-x^2)^3}$ on that interval.
# 
# Notice that $x^2$ and $x^2+3$ are both positive for $x\neq 0$, therefore $\frac{x^2(x^2+3)}{(4-x^2)^3}<0$ whenever $4-x^2 < 0$.
# ```

# In[ ]:


get_ipython().run_cell_magic('itikz', '', '\\documentclass[tikz]{standalone}\n\\begin {document}\n\\begin{tikzpicture}[xscale=1,yscale=0.6]\n\n\\draw[white,fill=white] (-4.3,-5.3) rectangle (4.3,5.3);\n%\\draw[very thin,color=lightgray,step=1] (-4.9,-4.9) grid (2.9,4.9);\n\n\\draw[->] (-4,0) -- (4,0) node[below] {$x$};\n\\draw[->] (0,-5) -- (0,5) node[right] {$y$};\n       \n\\draw [fill=black] (-2,0) ellipse [x radius = 0.15, y radius = 0.25];\n\\draw [fill=black] (2,0) ellipse [x radius = 0.15, y radius = 0.25];\n\n% tick marks\n\\foreach \\x in {-3,-1,1,3} \n\t\\draw [thick] (\\x cm,6pt) -- (\\x cm,-6pt) node[below] {$\\x$};\n\\foreach \\y in {} \n\t\\draw [thick] (-2pt,\\y cm) -- (2pt,\\y cm) node[right] {$\\y$};\n\t\n\\clip (-6,-5) rectangle (6,5);\n\\draw[domain=-3:3,smooth,variable=\\x,black,ultra thick] plot ({\\x},{4 - \\x*\\x}); \n%\\node at (4.1, 4.5){$y = x^2 + 2x - 3$};\n\\end{tikzpicture}\n\\end{document}')


# The graph of $y = 4-x^2$ as shown above is below the $x$-axis (i.e., $4-x^2 < 0$) if $x<-2$ or $x>2$.  Therefore, $\frac{x^2(x^2+3)}{(4-x^2)^3} < 0$ when $x<-2$ or $x>2$.
