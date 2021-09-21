#!/usr/bin/env python
# coding: utf-8

# # Relative Extrema

# In[1]:


get_ipython().run_line_magic('load_ext', 'itikz')


# ```{admonition} Definition
# :class: info
# 
# The relative extrema of a function $f$:
# 
# - A function $f$ has a **relative maximum** at $x=c$ if there exists an open interval $(a,b)$ containing $c$ such that $f(c) \geq f(x)$ for all $x$ in $(a,b)$.
# - A function $f$ has a **relative minimum** at $x=c$ if there exists an open interval $(a,b)$ containing $c$ such that $f(c) \leq f(x)$ for all $x$ in $(a,b)$.
# ```
# 
# ## Example 1
# 
# The relative extrema are highlighted on the following graph. Observe how the relative extrema appear at points on the curve where the increasing/decreasing behavior of the function changes.

# In[ ]:


get_ipython().run_cell_magic('itikz', '', "\\documentclass[tikz]{standalone}\n\\usetikzlibrary{arrows}\n\\usetikzlibrary{arrows.meta}\n\n\\begin{document}\n\n\\begin{tikzpicture}[scale = 1.2]\n\n  \\draw[white,fill=white] (-1,-1) rectangle (12.5,7.5);\n  \\draw[->] (-0.5,0) -- (12,0) node[below] {$x$};\n  \\draw[->] (0,-0.5) -- (0,7) node[right] {$y$};\n      \n  % draw curve\n  \\draw [ultra thick] \n  (1,1) parabola bend (2.5,4) (4,2) \n  .. controls (5.5,5) and (7,2) .. (8.5,5) \n  parabola bend (10,3) (11.5,6);\n\n  % draw points\n  \\draw [black,fill=red] (2.5,4) circle (2.5pt);\n  \\draw [black,fill=green] (4,2) circle (2.5pt);\n  \\draw [black,fill=red] (8.5,5) circle (2.5pt);\n  \\draw [black,fill=green] (10,3) circle (2.5pt);\n\n  % label extrema\n  \\draw [<-, >=stealth', shorten <=3pt] (2.5,4) -- (3.25,6) node[right] {\\bf \\large Relative Maxima}; \n  \\draw [<-, >=stealth', shorten <=3pt] (8.5,5) -- (7,6);\n  \\draw [<-, >=stealth', shorten <=3pt] (4,2) -- (5,1) node[right] {\\bf \\large Relative Minima}; \n  \\draw [<-, >=stealth', shorten <=3pt] (10,3) -- (8.7,1);\n\\end{tikzpicture}\n\\end{document} ")


# In other words, relative extrema appear at points on the graph of the function where the derivative changes sign.
# 
# ## How To Find Relative Extrema
# 
# The relative extrema of a function appear where $f'(x)$ changes from positive to negative or from negative to positive. Since $f'(x)$ changes sign when there is a relative extrema, it must be the case that either $f'(x)=0$ or $f'(x)$ does not exist at the relative extrema.
# 
# ## Example 2
# 
# Compare the graphs of $f(x) = x^2 - 1$ and $f'(x) = 2x$.
# 
# ````{panels}
# 
# ```{image} ../images/pic_optimization_relativeextrema_1.png
# :alt: graph of $f(x) = x^2 - 1$
# :height: 500px
# :align: center
# ```
# ---
# ```{image} ../images/pic_optimization_relativeextrema_2.png
# :alt: graph of $f'(x) = 2x$
# :height: 500px
# :align: center
# ```
# ````
# 
# Observe that $f(x)$ has a relative minimum at $x=0$, $f'(0) = 0$, and $f'(x)$ changes sign (from negative to positive) at $x=0$.
# 
# ## Example 3
# 
# Compare the graphs of $f(x) = x^3 + 1$ and $f'(x) = 3x^2$.
# 
# ````{panels}
# 
# ```{image} ../images/pic_optimization_relativeextrema_3.png
# :alt: graph of $f(x) = x^3 + 1$
# :height: 500px
# :align: center
# ```
# ---
# ```{image} ../images/pic_optimization_relativeextrema_4.png
# :alt: graph of $f'(x) = 3x^2$
# :height: 500px
# :align: center
# ```
# ````
# 
# Observe that $f(x)$ does not have any relative extrema despite the fact that $f'(0) = 0$.  Notice that $f'(x)$ does not change sign at $x=0$. In other words, in order for a function to have a relative extrema, there must be a change in sign of its derivative.
