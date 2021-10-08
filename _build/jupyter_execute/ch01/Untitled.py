#!/usr/bin/env python
# coding: utf-8

# # A basic machine learning problem: image classification .
# 
# ## A basic machine learning problem: image classification
# ```{admonition} Can a machine (function) tell the difference ?
#  Mathematically, gray-scale image can be just taken as matrix in $R^{n_0\times n_0}$.
# 
#  The next figure shows different result from: human vision and computer representation: (pic not found)
#  
#  An image is just a big grid of numbers between [0,255]
#   e.g. $800 \times 600 \times 3$ (3 channels RGB)
# 
#  Futhermore, color image can be taken as 3D tensor (matrix with 3 channel(RGB) ) in $R^{n_0\times n_0 \times 3}$. 
# 
#  Then, let us think about the general supervised learning case.
# 
#  Each image = a big vector of pixel values
# 
#  - $d = 1280\times 720 \times 3$(width $\times$ height $\times$ RGB channel) 
#  
#  ```
# 
#  ```{admonition} 3 different sets of points in $\mathbb{R}^d$, are they separable?
#  (cannot find three pictures here)
# ```
# 
#  ```{admonition} Convert into mathematical problem
# Find $f(\cdot; \theta): \mathbb{R}^d \to \mathbb{R}^3$ such that: (no picture)
# - Function interpolation
# - Data fitting
#  ```
# 
#  ```{admonition} How to formulate “learning”?
# - Data: $\{x_j, y_j\}_{j=1}^N$
# - Find $f^*$ in some function class s.t. $f^*(x_j) \approx y_j$.
# - Mathematically, solve the optimization problem by parameterizing the abstract function class
# $
# 	\min_{\theta} \mathcal L(\theta)
# $
# - where
# $
# 		\mathcal L( \theta):=
# 		{\mathbb E}_{(x,y)\sim \mathcal D}[\ell(f(x;  \theta), y)]\approx L( \theta) :=
# 		\frac{1}{N} \sum_{j=1}^N\ell(y_j, f(x_j;  \theta))
# $
# - Here
# $
# \ell(y_j,f(x_j;  \theta))
# $ 
# is a  general distance between real label $y_j$ and predicted label $f(x_j;\theta)$
# 
# Two commonly used distances are 
# - $l^2$ distance: 
# $
# 		\ell(y_j,f(x_j; \theta)) = \|y_j - f(x_j; \theta)\|^2.
# $		
# - KL-divergence distance:
# $
# \ell(y_j, f(x_j;  \theta)) = \sum_{i=1}^k [y_j]_i \log\frac{[y_j]_i }{[f(x_j; \theta)]_i}.
# $
# ```
#  ```{admonition} Application: image classification
# TBD (cannot find pictures)
#  ```

# In[1]:


from IPython.display import HTML
HTML('<iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/2356971/sp/235697100/embedIframeJs/uiconf_id/41416911/partner_id/2356971?iframeembed=true&playerId=kaltura_player&entry_id=1_b5pq3bnx&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_qcnp6cit" width="560" height="590" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="Kaltura Player"></iframe>')


# In[ ]:




