#!/usr/bin/env python
# coding: utf-8

# # Graphing
# 
# ## Equations for a Line
# 
# ### Slope-Intercept Form
# The equation of the line with slope $m$ and $y$-intercept equal to $b$ is
# 
# $$
# \boxed{y = mx + b}
# $$

# In[1]:


get_ipython().run_line_magic('load_ext', 'itikz')


# In[ ]:


get_ipython().run_cell_magic('itikz', '', '\\documentclass[tikz]{standalone}\n\\begin{document}\n\\begin{tikzpicture}[scale=2.5]\n    \\draw[white,fill=white] (-2,-1.5) rectangle (2.2,2.2);\n    \\draw[->] (-2,0) -- (2,0) node[below] {$x$};\n    \\draw[->] (0,-1.5) -- (0,2) node[right] {$y$};\n    \\draw[domain=-2:2,smooth,variable=\\x,black,ultra thick] plot ({\\x},{0.75*\\x+0.5});\n    \\draw (0.2,0.5) -- (-0.2,0.5) node[left] {$b$};\n\\end{tikzpicture}\n\\end{document}')


# ### Point-Slope Form
# The equation of the line with slope $m$ that goes through the point $(a,b)$ is
# 
# $$
# \boxed{y - b = m(x-a)}
# $$

# In[ ]:


get_ipython().run_cell_magic('itikz', '', '\\documentclass[tikz]{standalone}\n\\begin{document}\n\\begin{tikzpicture}[scale=2.5]\n\\draw[white,fill=white] (-1.5,-1.5) rectangle (2.7,2.2);\n      \\draw[->] (-1.5,0) -- (2.5,0) node[below] {$x$};\n      \\draw[->] (0,-1.5) -- (0,2) node[right] {$y$};\n      \\draw[domain=-1.5:2,smooth,variable=\\x,black,ultra thick] plot ({\\x},{0.75*\\x+0.5});\n      \\fill (1,1.25) circle [radius = 2pt] node[below right] {$(a,b)$};\n    \\end{tikzpicture}\n\\end{document}')


# Recall that a positive slope means that the line goes up from left-to-right and a negative slope means that the line goes down from left-to-right.
# 
# 
# ### Example 1
# Sketch the graph of the line defined by  $y = 2x + 3$.
# 
# ```{admonition} Step 1: Determine slope and $y$-intercept
# :class: tip
# 
# Since $y=2x+3$ is in slope-intercept form, the line has slope $2$ and a $y$-intercept of $3$. 
# ```
# 
# Once we know slope and $y$-intercept, we can draw the graph.

# In[ ]:


get_ipython().run_cell_magic('itikz', '', '\\documentclass[tikz]{standalone}\n\\begin{document}\n\\begin{tikzpicture}[scale=1.0]\n\\draw[black,fill=white] (-6.5,-4.5) rectangle (6.5,8.5);\n%\\draw[very thin,color=darkgray,step=3] (-8,-5) grid (8,8.9);\n\\draw[very thin,color=lightgray,step=1] (-5.9,-3.9) grid (5.9,7.9);\n\\draw[->] (-6,0) -- (6,0) node[below] {$x$};\n\\draw[->] (0,-4) -- (0,8) node[right] {$y$};\n\\node at (3.8, 6.5){$y = 2x+3$};\n\n% draw slope\n\\draw[dashed,red,thick] (-3,-3) -| ++(1,2) -| ++(1,2) -| ++(1,2) -| ++(1,2) -| ++(1,2);\n% draw line and point\n\\draw[domain=-3.5:2.5,smooth,variable=\\x,black,ultra thick] plot ({\\x},{2*\\x+3});\n\n% tick marks\n\\foreach \\x in {-3,3} \n\t\\draw [thick] (\\x cm,3pt) -- (\\x cm,-3pt) node[below] {$\\x$};\n\\foreach \\y in {-3,3,6} \n\t\\draw [thick] (3pt,\\y cm) -- (-3pt,\\y cm) node[left] {$\\y$};\n\\end{tikzpicture}\n\\end{document}')


# Note that the red dashed lined is not part of the graph and is used only as a guide for drawing a line with slope 2.  In particular, in order for a line to have slope equal to $2$, if the $x$-coordinate of any point on the line is increased by 1 unit, then the $y$-coordinate must be increased by 2 units.
# 
# 
# 
# ### Example 2
# 
# Sketch the graph of the line defined by  $y - 3 = -2(x - 4)$.
# 
# ```{admonition} Step 1: Determine the slope and a point on the line.
# :class: tip
# 
# Since $y - 3 = -2(x - 4)$ is in point-slope form, the line has slope $-2$ and goes through the point $(4,3)$. 
# ```
# 
# Now draw a graph with slope $-2$ that goes through the point $(4,3)$.

# In[ ]:


get_ipython().run_cell_magic('itikz', '', '\\documentclass[tikz]{standalone}\n\\begin{document}\n\\begin{tikzpicture}[scale=1.0]\n\\draw[black,fill=white] (-2.5,-2.5) rectangle (8.5,14.5);\n\\draw[very thin,color=lightgray,step=1] (-1.9,-1.9) grid (7.9,13.9);\n\\draw[->] (-2,0) -- (8,0) node[below] {$x$};\n\\draw[->] (0,-2) -- (0,14) node[right] {$y$};\n\\node at (4.5, 10.5){$y - 3 = -2(x-4)$};\n\n% draw slope\n%\\draw[dashed,red,thick] (-1,13)|- ++(1,-2) |- ++(1,-2) |- ++(1,-2) |- ++(1,-2) |- ++(1,-2) |- ++(1,-2) |- ++(1,-2);\n\\draw[dashed,red,thick] (-1,13) -| ++(1,-2) -| ++(1,-2) -| ++(1,-2) -| ++(1,-2) -| ++(1,-2) -| ++(1,-2) -| ++(1,-2);\n\n\n% draw line and point\n\\draw[domain=-1.5:6.5,smooth,variable=\\x,black,ultra thick] plot ({\\x},{-2*\\x + 11});\n\\draw [fill=black,thick] (4,3) circle [radius=0.15] node [below left] {$(4,3)$};\n\n% tick marks\n\\foreach \\x in {2,4} \n\t\\draw [thick] (\\x cm,3pt) -- (\\x cm,-3pt) node[below] {$\\x$};\n\\foreach \\y in {3,6,9,12} \n\t\\draw [thick] (-6pt,\\y cm) -- (0pt,\\y cm) node[right] {$\\y$};\n\\end{tikzpicture}\n\\end{document}')


# In order for a line to have slope equal to $-2$, if the $x$-coordinate of any point on the line is increased by 1 unit, then the $y$-coordinate must be decreased by 2 units.
# 
# 
# 
# ### Example 3
# 
# Sketch the graph of the line defined by $y - 1 = \dfrac{2}{5}(x + 2)$.
# 
# 
# ```{admonition} Step 1: Determine the slope and a point on the line.
# :class: tip
# 
# Since $y - 1 = \frac{2}{5}(x + 2)$ is in point-slope form, the line has slope $2/5$ and goes through the point $(-2,1)$. 
# ```
# 
# Draw the line with slope equal to $2/5$ that goes through the point $(-2,1)$

# In[ ]:


get_ipython().run_cell_magic('itikz', '', '\\documentclass[tikz]{standalone}\n\\begin{document}\n\\begin{tikzpicture}[scale=1.0]\n\\draw[black,fill=white] (-8.5,-3.5) rectangle (10.5,7.5);\n\\draw[very thin,color=lightgray,step=1] (-7.9,-2.9) grid (9.9,6.9);\n\\draw[->] (-8,0) -- (10,0) node[below] {$x$};\n\\draw[->] (0,-3) -- (0,7) node[right] {$y$};\n\\node at (4.5, 5.5){$y - 1 = \\frac{2}{5}(x+2)$};\n\n% draw slope\n\\draw[dashed,red,thick] (-7,-1) -| ++(5,2) -| ++(5,2) -| ++(5,2);\n\n% draw line and point\n\\draw[domain=-8:10,smooth,variable=\\x,black,ultra thick] plot ({\\x},{0.4*\\x+9/5});\n\\draw [fill=black,thick] (-2,1) circle [radius=0.15] node [above left] {$(-2,1)$};\n\n% tick marks\n\\foreach \\x in {-6,-4,-2,2,4,6,8} \n\t\\draw [thick] (\\x cm,3pt) -- (\\x cm,-3pt) node[below] {$\\x$};\n\\foreach \\y in {-2,2,4} \n\t\\draw [thick] (3pt,\\y cm) -- (-3pt,\\y cm) node[left] {$\\y$};\n\\end{tikzpicture}\n\\end{document}')


# In order for a line to have slope equal to $2/5$, if the $x$-coordinate of any point on the line is increased by 5 units, then the $y$-coordinate must be increased by 2 units.
# 
# 
# 
# ## Graphing Quadratic Polynomials
# 
# The general form of a quadratic polynomial (i.e., a polynomial of degree two) is
# 
# $$y = ax^2 + bx + c$$
# 
# where $a$, $b$, and $c$ are real numbers and $a\neq 0$.  The graph of a quadratic polynomial has the shape of a parabola.  If $a>0$, then the parabola opens upward (i.e., looks like the letter ``U'') and if $a<0$, then the parabola opens downward.
# 
# 
# ### Example 4
# 
# Compare the graphs of $y = x^2$ and $y=-x^2$.

# In[ ]:


get_ipython().run_cell_magic('itikz', '', '\\documentclass[tikz]{standalone}\n\\begin{document}\n\\begin{tikzpicture}[scale=1.5]\n\n\\draw[black,fill=white] (-3.75,-1.25) rectangle (3.75,5.25);\n\\draw[very thin,color=lightgray,step=0.5] (-3.4,-0.9) grid (3.4,4.9);\n%\\draw[very thin,color=gray,step=2] (-3.5,-1) grid (3.5,5);\n\n\\draw[->] (-3.5,0) -- (3.5,0) node[below] {$x$};\n\\draw[->] (0,-1) -- (0,5) node[right] {$y$};\n\\draw[domain=-2.23:2.23,smooth,variable=\\x,black,ultra thick] plot ({\\x},{\\x*\\x});%  node[right] {$y=x^2$};\n       \n\\node[right] at (1.7, 3){$y = x^2$};\n\n% tick marks\n\\foreach \\x in {-2,2} \n\t\\draw [thick] (\\x cm,2pt) -- (\\x cm,-2pt) node[below] {$\\x$};\n\\foreach \\y in {2,4} \n\t\\draw [thick] (-2pt,\\y cm) -- (2pt,\\y cm) node[right] {$\\y$};\n\\end{tikzpicture}\n\\end{document}')


# In[ ]:


get_ipython().run_cell_magic('itikz', '', '\\documentclass[tikz]{standalone}\n\\begin{document}\n\\begin{tikzpicture}[scale=1.5]\n\n\\draw[black,fill=white] (-3.75,-5.25) rectangle (3.75,1.25);\n\\draw[very thin,color=lightgray,step=0.5] (-3.4,-4.9) grid (3.4,0.9);\n%\\draw[very thin,color=gray,step=2] (-3.5,-5) grid (3.5,1);\n\n\\draw[->] (-3.5,0) -- (3.5,0) node[below] {$x$};\n\\draw[->] (0,-5) -- (0,1) node[right] {$y$};\n\\draw[domain=-2.23:2.23,smooth,variable=\\x,black,ultra thick] plot ({\\x},{-\\x*\\x});%  node[right] {$y=x^2$};\n       \n\\node[right] at (1.7, -3){$y = -x^2$};\n\n% tick marks\n\\foreach \\x in {-2,2} \n\t\\draw [thick] (\\x cm,2pt) -- (\\x cm,-2pt) node[below] {$\\x$};\n\\foreach \\y in {-2,-4} \n\t\\draw [thick] (-2pt,\\y cm) -- (2pt,\\y cm) node[right] {$\\y$};\n\\end{tikzpicture}\n\\end{document}')


# Notice how the graph of $y=x^2$ is a parabola that goes through the point $(0,0)$ and opens upward while the graph of $y=-x^2$ is a parabola that also goes through the point $(0,0)$ but opens downward.
# 
# 
# ### Example 5
# 
# Compare the graphs of $y=x^2-4$ and $y=4-x^2$

# In[ ]:


get_ipython().run_cell_magic('itikz', '', '\\documentclass[tikz]{standalone}\n\\begin{document}\n\\begin{tikzpicture}[scale=1.5]\n\\draw[black,fill=white] (-3.75,-5.25) rectangle (3.75,1.25);\n\\draw[very thin,color=lightgray,step=0.5] (-3.4,-4.9) grid (3.4,0.9);\n%\\draw[very thin,color=gray,step=2] (-3.5,-5) grid (3.5,1);\n\n\\draw[->] (-3.5,0) -- (3.5,0) node[below] {$x$};\n\\draw[->] (0,-5) -- (0,1) node[right] {$y$};\n\\draw[domain=-2.23:2.23,smooth,variable=\\x,black,ultra thick] plot ({\\x},{\\x*\\x- 4});%  node[right] {$y=x^2$};\n       \n\\node[right] at (0.9, -3.5){$y = x^2-4$};\n\n% tick marks\n\\foreach \\x in {-3,-1,1,3} \n\t\\draw [thick] (\\x cm,2pt) -- (\\x cm,-2pt) node[below] {$\\x$};\n\\foreach \\y in {-2} \n\t\\draw [thick] (-2pt,\\y cm) -- (2pt,\\y cm) node[right] {$\\y$};\n\\end{tikzpicture}\n\\end{document}')


# In[ ]:


get_ipython().run_cell_magic('itikz', '', '\\documentclass[tikz]{standalone}\n\\begin{document}\n\\begin{tikzpicture}[scale=1.5]\n\\draw[black,fill=white] (-3.75,-1.25) rectangle (3.75,5.25);\n\\draw[very thin,color=lightgray,step=0.5] (-3.4,-0.9) grid (3.4,4.9);\n%\\draw[very thin,color=gray,step=2] (-3.5,-1) grid (3.5,5);\n\n\\draw[->] (-3.5,0) -- (3.5,0) node[below] {$x$};\n\\draw[->] (0,-1) -- (0,5) node[right] {$y$};\n\\draw[domain=-2.23:2.23,smooth,variable=\\x,black,ultra thick] plot ({\\x},{4 - \\x*\\x});%  node[right] {$y=x^2$};\n       \n\\node[right] at (0.9, 3.5){$y = 4-x^2$};\n\n% tick marks\n\\foreach \\x in {-3,-1,1,3} \n\t\\draw [thick] (\\x cm,2pt) -- (\\x cm,-2pt) node[below] {$\\x$};\n\\foreach \\y in {2} \n\t\\draw [thick] (-2pt,\\y cm) -- (2pt,\\y cm) node[right] {$\\y$};\n\\end{tikzpicture}\n\\end{document}')


# Notice how the graph of $y=x^2-4$ looks like the graph of $y=x^2$ with each point shifted down $4$ units.  Also, the graph of $y=4-x^2$ looks like the graph of $y=-x^2$ with each point shifted up $4$ units.
# 
# 
# (precalc:graphing:example6)=
# ### Example 6
# 
# Sketch the graph of $f(x) = x^2 - 4x -12$.
# 
# ```{dropdown} **Step 1:** Determine the $y$-intercept by evaluating $f(0)$.
# 
# \begin{align*}
#   f(0)
#   &= 0^2 - 4(0) - 12 \\
#   &= -12
# \end{align*}
# 
# Therefore the graph of $y=f(x)$ goes through the point $(0,-12)$.
# ```
# 
# ```{dropdown} **Step 2:** Determine the $x$-intercepts by setting $f(x)=0$ and solving for $x$.
# 
# Recall from [Factoring, Example 8](01_02_example8)  and [Solving Equations, Example 1](01_03_example1) that
# 
# $$x^2 - 4x - 12 = (x+2)(x-6)$$
# 
# Now set each factor equal to zero and solve for $x$.
# \begin{align*}
# x + 2 = 0 ~~~~&\Rightarrow~~~~ x = -2 \\
# x - 6 = 0 ~~~~&\Rightarrow~~~~ x = 6 
# \end{align*}
# 
# Therefore the graph of $y=f(x)$ goes through the points $(-2,0)$ and $(6,0)$.
# ```
# 
# Draw the graph of a parabola that opens upward (since the coefficient of $x^2$ in $f(x)$ is positive) and goes through the points found in **Steps 1** and **2**.

# In[ ]:


get_ipython().run_cell_magic('itikz', '', '\\documentclass[tikz]{standalone}\n\\begin{document}\n\\begin{tikzpicture}[xscale=0.8,yscale=0.5]\n\n\\draw[black,fill=white] (-6.6,-19) rectangle (12.6,11);\n\\draw[very thin,color=lightgray,xstep=1,ystep=2] (-5.9,-17.9) grid (11.9,9.9);\n\n\\draw[->] (-6,0) -- (12,0) node[below] {$x$};\n\\draw[->] (0,-18) -- (0,10) node[right] {$y$};\n\\draw[domain=-3:7,smooth,variable=\\x,black,ultra thick] plot ({\\x},{\\x*\\x - 4*\\x - 12});\n       \n\\node[right] at (5, -9){$y = x^2-4x-12$};\n\n%\\draw [fill=black,thick] (-2,0) circle [radius=0.15];\n%\\draw [fill=black,thick] (6,0) circle [radius=0.15];\n%\\draw [fill=black,thick] (0,-12) circle [radius=0.15];\n\\draw [fill=black] (-2,0) ellipse [x radius = 0.15, y radius = 0.225];\n\\draw [fill=black] (6,0) ellipse [x radius = 0.15, y radius = 0.225];\n\\draw [fill=black] (0,-12) ellipse [x radius = 0.15, y radius = 0.225];\n\n% tick marks\n\\foreach \\x in {-3,3,9} \n\t\\draw [thick] (\\x cm,6pt) -- (\\x cm,-6pt) node[below] {$\\x$};\n\\foreach \\y in {-12} \n\t\\draw [thick] (-2pt,\\y cm) -- (2pt,\\y cm) node[right] {$\\y$};\n\t\n\\clip (-8,-20) rectangle (12,10);\n\\draw[domain=-4:8,smooth,variable=\\x,black,ultra thick] plot ({\\x},{\\x*\\x - 4*\\x - 12});\n\n\\end{tikzpicture}\n\\end{document}')


# ## Graphing Power and Root Functions
# 
# Any function of the form
# 
# $$y = x^r$$
# 
# where $r$ is any real number is called a power function.  Thus $x^2$, $x^3$, $x^4$, etc. are examples of power functions.  Root functions, like the square root (i.e., $\sqrt{x}$ or $x^{1/2}$) and cube root (i.e., $\sqrt[3]{x}$ or $x^{1/3}$) are also examples of power functions
# 
# 
# ### Example 7
# 
# Sketch the graph of $y = x^3$.

# In[ ]:


get_ipython().run_cell_magic('itikz', '', '\\documentclass[tikz]{standalone}\n\\begin{document}\n\\begin{tikzpicture}[scale=2]\n\n\\draw[black,fill=white] (-3.5,-4.3) rectangle (3.5,4.3);\n\\draw[very thin,color=lightgray,step=1] (-2.9,-3.9) grid (2.9,3.9);\n\n      \\draw[->] (-3,0) -- (3,0) node[below] {$x$};\n      \\draw[->] (0,-4) -- (0,4) node[right] {$y$};\n      \\draw[domain=-1.57:1.57,smooth,variable=\\x,black,ultra thick,samples=100] plot ({\\x},\\x^3);\n      \\node at (2.4,3.2){$y = x^3$};\n       \n      % tick marks\n\\foreach \\x in {-2,-1,1,2} \n\t\\draw [thick] (\\x cm,2pt) -- (\\x cm,-2pt) node[below] {$\\x$};\n\\foreach \\y in {-3,-2,-1,1,2,3} \n\t\\draw [thick] (2pt,\\y cm) -- (-2pt,\\y cm) node[left] {$\\y$};\n\n    \\end{tikzpicture}\n\\end{document}')


# Notice how the graph of $y=x^3$ always increases from left-to-right and looks like a horizontal line as it goes through the origin.
# 
# 
# ### Example 8
# 
# Sketch the graph of the square root function, $y = \sqrt{x}$.

# In[ ]:


get_ipython().run_cell_magic('itikz', '', '\\documentclass[tikz]{standalone}\n\\begin{document}\n\\begin{tikzpicture}[scale=2]\n\n\\draw[black,fill=white] (-0.8,-0.8) rectangle (10.3,4.3);\n\\draw[very thin,color=lightgray,step=1] (0,0) grid (9.9,3.9);\n\n      \\draw[->] (-0.5,0) -- (10,0) node[below] {$x$};\n      \\draw[->] (0,-0.5) -- (0,4) node[right] {$y$};\n      \\draw[domain=0:1,smooth,variable=\\x,black,ultra thick,samples=100] plot ({\\x},\\x^0.5);\n      \\draw[domain=1:10,smooth,variable=\\x,black,ultra thick,samples=36] plot ({\\x},\\x^0.5);\n      \\node at (7,3.2){$y = \\sqrt{x}$};\n       \n      % tick marks\n\\foreach \\x in {1,...,9} \n\t\\draw [thick] (\\x cm,2pt) -- (\\x cm,-2pt) node[below] {$\\x$};\n\\foreach \\y in {1,2,3} \n\t\\draw [thick] (2pt,\\y cm) -- (-2pt,\\y cm) node[left] {$\\y$};\n\n    \\end{tikzpicture}\n\\end{document}')


# Notice how the graph of $y=\sqrt{x}$ looks like the upper half of a parabola that opens to the right.
