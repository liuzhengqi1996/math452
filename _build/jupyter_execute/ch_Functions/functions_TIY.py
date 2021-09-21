#!/usr/bin/env python
# coding: utf-8

# # Try It Yourself
# 
# ## Exercise 1
# Let $f(x) = \dfrac{x - 1}{2x - 6}$ and $g(x) = \sqrt{2x + 1}$.  
# 
# Determine the domain for $f+g$, $f-g$, $fg$, and $f/g$.
# 
# ```{dropdown} Show answer
# Answer: Domain for $f+g$, $f-g$, $fg$: $[-1/2,3) \cup (3,\infty)$; Domain for $f/g$: $(-1/2,3) \cup (3,\infty)$
# ```
# 
# 
# ## Exercise 2
# Let $f(x) = 3\sqrt{x}$ and $g(x) = \dfrac{x}{2x-1}$.  
# 
# Determine the rule for the composite functions $f \circ g$ and $g \circ f$. 
# 
# ```{dropdown} Show answer
# Answer: $(f\circ g)(x) = 3\sqrt{x/(2x-1)}$; $(g\circ f)(x) = 3\sqrt{x}/(6\sqrt{x}-1)$
# ```
# 
# 
# ## Exercise 3
# A manufacturer of Everlasting LED lightbulbs has fixed monthly costs of \$25,000 and a processing cost of \$3 for each lightbulb produced. Assuming each lightbulb sells for \$5, compute the break-even point.
# 
# ```{dropdown} Show answer
# Answer: 12,500 lightbulbs
# ```
# 
# 
# ## Exercise 4
# Determine the degree of the polynomial 
# 
# $$(x^4 + x)^2(x^3 + x + 1)^5.$$
# 
# ```{dropdown} Show answer
# Answer: $23$
# ```
# 
# ## Exercise 5
# Write 
# 
# $$\dfrac{x}{x^2-4} - \dfrac{2x+1}{x+5}$$ 
# 
# as a ratio of polynomials and determine its domain.
# 
# ```{dropdown} Show answer
# Answer: $(-2x^3 + 13x + 4)/(x^3 + 5x^2 - 4x - 20)$, Domain: $(-\infty,-5) \cup (-5,-2) \cup (-2,2) \cup (2,\infty)$
# ```
# 
# ## Exercise 6
# The demand and supply functions for {\em The Best of Math 110: A DVD Collection} are: 
# 
# \begin{align*}
# p = d(x) &= -x^2 - 2x + 100\\
# p = s(x) &= 2x^2 + 4x - 140
# \end{align*}
# 
# where $x$ is the number of thousands of DVDs and $p$ is in dollars.  Determine the market equilibrium values.
# 
# ```{dropdown} Show answer
# Answer: Equilibrium quantity = 8000; Equilibrium price = \$20
# ```
# 
# 
# ## Exercise 7
# A rectangular field is to be enclosed by 200 feet of fence. One side of the field is a building, so fencing is not required on that side.

# In[1]:


get_ipython().run_line_magic('load_ext', 'itikz')


# In[ ]:


get_ipython().run_cell_magic('itikz', '', '\\documentclass[tikz]{standalone}\n\\begin{document}\n\\begin{tikzpicture}[scale = 8]\n\\draw[fill = yellow,opacity=0.5] (0,0) rectangle (1,.5);\n\\draw[ultra thick] (-.2,0)--(1.2,0) node[midway,below] {Building};\n\\draw (0,0) -- (0,0.5) node[midway,left] {$x$} \n-- (1,0.5) %node[midway,above] {} \n-- (1,0) node[midway,right] {$x$};\n\\node at (.5,.25) {Fenced Area};\n\\end{tikzpicture}\n\\end{document}')


# If $x$ denotes the length of one side of the rectangle perpendicular to the building, determine the function in the variable $x$ giving the area (in square feet) of the fenced-in region and state the appropriate domain.
# 
# 
# ```{dropdown} Show answer
# Answer: Area: $200x - 2x^2$, Domain: $[0,100]$
# ```
# 
# 
# ## Exercise 8
# A game box manufacturer determines that in order to sell $x$ units, the price per unit in dollars must be $p(x) = 250 - x$. The manufacture also determines that the total cost of producing $x$ units is given by $C(x) = 2500 + 10x$.  Determine the profit as a function of $x$ and state the appropriate domain.
# 
# ```{dropdown} Show answer
# Answer: Profit: $240x - x^2 - 2500$, Domain: $[0,250]$
# ```
# 
# ## Exercise 9
# A printer needs to make a poster that has a total area of $200$ in$^2$, $1$ inch margins on the sides, a $2.5$ inch margin on the top, and a $1.5$ inch margin on the bottom.  If $x$ denotes the width (in inches) of the poster, find a function in the variable $x$ giving the area of the printed (i.e., shaded) region and state the appropriate domain.

# In[ ]:


get_ipython().run_cell_magic('itikz', '', '\\documentclass[tikz]{standalone}\n\\begin{document}\n\\def\\bbWidth{6}\n\\def\\bbHeight{4.5}\n\\def\\bbSideMargin{1.0}\n\\def\\bbTopMargin{1.1}\n\\def\\bbBottomMargin{0.9}\n\\begin{tikzpicture}[scale=1.3]\n\\draw [thick,fill=white] (0,0) rectangle (\\bbWidth,\\bbHeight);\n\\draw [thick,fill=yellow,opacity=0.5] (\\bbSideMargin,\\bbBottomMargin) rectangle (\\bbWidth - \\bbSideMargin, \\bbHeight - \\bbTopMargin);\n%\\draw [<->] (0,\\bbHeight + 0.25) -- +(\\bbWidth,0) node [midway,fill=white] {$x$};\n\\draw [<-] (0,\\bbHeight/2) -- +(-0.5,0); \n\\draw [<-] (\\bbSideMargin,\\bbHeight/2) -- +(0.5,0);\n\\node at (\\bbSideMargin/2,\\bbHeight/2) {\\small 1 in.};\n\\draw [<->] (\\bbWidth/2,\\bbHeight) -- +(0,-\\bbTopMargin) node [midway,fill=white] {\\small 2.5 in.};\n\\draw [<->] (\\bbWidth/2,0) -- +(0,\\bbBottomMargin) node [midway,fill=white] {\\small 1.5 in.};\n\n%label\n\\draw [|-|] (0,-0.4) -- (\\bbWidth,-0.4) node [midway,fill=white] {$x$};\n\\end{tikzpicture}\n\\end{document}')


# ```{dropdown} Show answer
# Answer: Area: $(x-2)(200/x-4)$, Domain: $[2,50]$
# ```
