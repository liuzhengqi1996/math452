#!/usr/bin/env python
# coding: utf-8

# # Examples: Computing Limits from Graphs
# 
# ## Example (First Graph)

# In[1]:


get_ipython().run_line_magic('load_ext', 'itikz')


# Let $f(x)$ be defined by the following graph.

# In[ ]:


get_ipython().run_cell_magic('itikz', '', '\\documentclass[tikz]{standalone}\n\\begin{document}\n\\begin{tikzpicture}[scale=1.5]\n\\tikzstyle{every node}=[font=\\large]\n\n% create a white background, with a black frame\n%\\draw [fill=white,white] (-7,-5) rectangle (7,5); \n\n% draw a grid\n\\draw[step=10mm, lightgray, thin] (-6.49,-4.49) grid (6.49,4.49); \n%\\draw[step=1cm, gray] (0,-0) grid (6.5,3.5); \n\n% draw axes\n\\draw [->,thick] (-6.5,0) -- (6.5,0) node[below] {$x$}; \n\\draw [->,thick] (0,-4.5) -- (0,4.5) node[right] {$y$};\n\n% tick marks\n\\foreach \\x in {-6,-5,...,-1,1,2,...,6} \n\t\\draw [thick] (\\x cm,2pt) -- (\\x cm,-2pt) node[below] {\\x};\n\\foreach \\y in {-4,-3,...,-1,1,2,...,4} \n\t\\draw [thick] (2pt,\\y cm) -- (-2pt,\\y cm) node[left] {\\y};\n\n% plot curve\n\\clip (-7,-4.5) rectangle (7,4.5);\n\\draw [ultra thick] (-6,10) to [out=-85,in=160] (-3,2) to [out=-20,in=95] (0,-6);\n\\draw [ultra thick] (0,0) -- (2,2);\n\\draw [ultra thick] (2,-4) parabola (6,12);\n\n% \\plot points\n\\fill (0,0) circle (3pt);\n\\draw [fill=white] (2,2) circle (3pt);\n\\fill (2,-2) circle (3pt);\n\\draw [fill=white] (2,-4) circle (3pt);\n\n\\end{tikzpicture}\n\\end{document}')


# Evaluate $\lim\limits_{x \to a^-} f(x)$, $\lim\limits_{x \to a^+} f(x)$, and $\lim\limits_{x \to a} f(x)$ for $a = -3, 0, 2$.
# 
# 
# ```{admonition} $\mathbf{a=-3} \quad$ (Click to show solution)
# :class: tip, dropdown
# 
# The two one-sided limits both exist and are both equal to 2.
# 
# $$\lim_{x\to -3^-} f(x)=2  ~~~~~ \hbox{and} ~~~~~ \lim_{x\to -3^+} f(x)=2$$
# 
# Therefore, the limit exists and $\lim\limits_{x\to -3} f(x) = 2.$
# ```
# 
# ```{admonition} $\mathbf{a=0} \quad$ (Click to show solution)
# :class: tip, dropdown
# 
# The limit from the left does not exist and the limit from the right exists and is equal to 0.
# 
# $$\lim_{x\to 0^-} f(x) = -\infty ~~~~~ \hbox{and} ~~~~~ \lim_{x\to 0^+} f(x)=0$$
# 
# Therefore, $\lim\limits_{x\to 0} f(x)$ does not exist. Observation: If either of the one-sided limits does not exist (DNE) as $x$ approaches $a$, then the $\lim_{x\to a} f(x)$ does not exist.
# ```
# 
# ```{admonition} $\mathbf{a=2} \quad$ (Click to show solution)
# :class: tip, dropdown
# 
# The two one-sided limits both exist, but are not equal to each other.
# 
# $$\lim_{x\to 2^-} f(x)= 2 ~~~~~ \hbox{and} ~~~~~ \lim_{x\to 2^+} f(x)=-4$$
# 
# Therefore, $\lim\limits_{x\to 2} f(x)$ does not exist.
# ```

# ## Example (Second Graph)
# 
# Let $f(x)$ be defined by the following graph.

# In[ ]:


get_ipython().run_cell_magic('itikz', '', '\\documentclass[tikz]{standalone}\n\\begin{document}\n\\begin{tikzpicture}[scale=1.5]\n\\tikzstyle{every node}=[font=\\large]\n\n% create a white background, with a black frame\n%\\draw [fill=white,white] (-4,-3) rectangle (10,7); \n\n% draw a grid\n\\draw[step=10mm, lightgray, thin] (-3.49,-2.49) grid (9.49,6.49); \n%\\draw[step=1cm, gray] (0,-0) grid (6.5,3.5); \n\n% draw axes\n\\draw [->,thick] (-3.5,0) -- (9.5,0) node[below] {$x$}; \n\\draw [->,thick] (0,-2.5) -- (0,6.5) node[right] {$y$};\n\n% tick marks\n\\foreach \\x in {-3,-2,...,-1,1,2,...,9} \n\t\\draw [thick] (\\x cm,2pt) -- (\\x cm,-2pt) node[below] {\\x};\n\\foreach \\y in {-2,-1,1,2,...,6} \n\t\\draw [thick] (2pt,\\y cm) -- (-2pt,\\y cm) node[left] {\\y};\n\n\n% plot curve\n\\clip (-3.5,-2.5) rectangle (9.5,6.5);\n\\draw [ultra thick,blue,dashed] (6,-3) -- (6,7);\n\\draw [ultra thick] (-4,4) parabola bend (-2,0) (-1,1);\n\\draw [ultra thick] (-1,1) to [out=63,in=200] (0,2) to [out=20,in=243] (1,3);\n\\draw [ultra thick] (1,3) to [out=0,in=180] (4,1);\n%\\draw[ultra thick,domain=3:1,smooth,samples=300] plot (\\x,{2+pow((3-\\x)/2,0.33)});\n%\\draw[ultra thick,domain=3:4,smooth,samples=100] plot (\\x,{2-pow(\\x-3,0.33)});\n\\draw [ultra thick] (4,4) to [out=25,in=270] (6,10);\n\\draw [ultra thick] (6,-6) to [out=85,in=200] (10,5);\n\n% \\plot points\n\\draw [fill=white] (-1,1) circle (3pt);\n\\draw [fill=white] (1,3) circle (3pt);\n\\fill (1,4) circle (3pt);\n\\draw [fill=white] (4,4) circle (3pt);\n\\fill (4,1) circle (3pt);\n\n\\end{tikzpicture}\n\\end{document}')


# Evaluate $\lim\limits_{x \to a^-} f(x)$, $\lim\limits_{x \to a^+} f(x)$, and $\lim\limits_{x \to a} f(x)$ for $a = -1, 1, 4, 6$.
# 
# 
# ```{admonition} $\mathbf{a=-1} \quad$ (Click to show solution)
# :class: tip, dropdown
# 
# The two one-sided limits both exist and are both equal to 1.
# 
# $$\lim_{x\to -1^-} f(x)=1  ~~~~~ \hbox{and} ~~~~~ \lim_{x\to -1^+} f(x)=1$$
# 
# Therefore, the limit exists and $\lim\limits_{x\to -1} f(x) = 1$.  Observation: Although $f(-1)$ is not defined, the limit as $x$ approaches $-1$ still exists.
# ```
# 
# ```{admonition} $\mathbf{a=1} \quad$ (Click to show solution)
# :class: tip, dropdown
# 
# The two one-sided limits both exist and are both equal to 3.
# 
# $$\lim_{x\to 1^-} f(x)=3  ~~~~~ \hbox{and} ~~~~~ \lim_{x\to 1^+} f(x)=3$$
# 
# Therefore, the limit exists and $\lim\limits_{x\to 1} f(x) = 3$.  Observation: Although $f(1)$ is defined, it is not equal to the value of the limit as $x$ approaches $1$.
# ```
# 
# ```{admonition} $\mathbf{a=4} \quad$ (Click to show solution)
# :class: tip, dropdown
# 
# The two one-sided limits both exist, but are not equal to each other.
# 
# $$\lim_{x\to 4^-} f(x)= 1 ~~~~~ \hbox{and} ~~~~~ \lim_{x\to 4^+} f(x)=4$$
# 
# Therefore, $\lim\limits_{x\to 4} f(x)$ does not exist.
# ```
# 
# 
# ```{admonition} $\mathbf{a=6} \quad$ (Click to show solution)
# :class: tip, dropdown
# 
# Neither one-sided limit exists.
# 
# $$\lim_{x\to 6^-} f(x) = \infty ~~~~~ \hbox{and} ~~~~~ \lim_{x\to 6^+} f(x)= -\infty$$
# 
# Therefore, $\lim\limits_{x\to 6} f(x)$ does not exist.
# ```
