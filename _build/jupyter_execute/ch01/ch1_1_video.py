#!/usr/bin/env python
# coding: utf-8

# # A basic machine learning problem: image classification

# In[1]:


from IPython.display import IFrame

IFrame(src="https://cdnapisec.kaltura.com/p/2356971/sp/235697100/embedIframeJs/uiconf_id/41416911/partner_id/2356971?iframeembed=true&playerId=kaltura_player&entry_id=1_z2ldie17&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[mediaProxy.mediaPlayFrom]=0&amp;flashvars[mediaProxy.mediaPlayTo]=600&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_27z0chwl" ,width='800', height='500')


# ## Can a machine (function) tell the difference ?
# ```{image} /figures/cat-dog-1.png
# :name: label
# :height: 150px
# ```
#  Mathematically, gray-scale image can be just taken as matrix in $R^{n_0\times n_0}$.
#  ```{image} /figures/gray-1.png
# :height: 250px
# ```
#  The next figure shows different result from: human vision and computer representation: 
#  ```{image} /figures/ImagePixels.png
# :name: label
# :height: 150px
# ```
#  An image is just a big grid of numbers between [0,255]
#   e.g. $800 \times 600 \times 3$ (3 channels RGB)
# 
#  Futhermore, color image can be taken as 3D tensor (matrix with 3 channel(RGB) ) in $R^{n_0\times n_0 \times 3}$.
#  ```{image} /figures/corlor-1.png
# :name: label
# :height: 150px
# ```

# ## Supervised learning
# Then, let us think about the general supervised learning case.
# 
#  Each image = a big vector of pixel values
# 
#  - $d = 1280\times 720 \times 3$(width $\times$ height $\times$ RGB channel) 
#  
# 
# 
# 3 different sets of points in $\mathbb{R}^d$, are they separable?
# ```{image} /figures/cat-dog-2.png
# :height: 250px
# ```
# ```{image} /figures/cat-dog-3.png
# :height: 250px
# ```
# 
# - Mathematical problem
# Find $f(\cdot; \theta): \mathbb{R}^d \to \mathbb{R}^3$ such that: 
#         
# $f(cat,\theta) \approx \begin{pmatrix}
# 	1\\ 0 \\ 0 
# 	\end{pmatrix} $
#     
# $f(dog,\theta)\approx \begin{pmatrix}
# 	0\\ 1 \\ 0 
# 	\end{pmatrix} 
#     $
#     
# $
# f(rabbit,\theta)
# \approx 
# 	\begin{pmatrix}
# 	0\\ 0 \\ 1
# 	\end{pmatrix} 
# $
# - Function interpolation
# - Data fitting
# 
# 
#  

# ## Formulate “learning”
# - Data: $\{x_j, y_j\}_{j=1}^N$
# - Find $f^*$ in some function class s.t. $f^*(x_j) \approx y_j$.
# - Mathematically, solve the optimization problem by parameterizing the abstract function class
# $
# 	\min_{\theta} \mathcal L(\theta)
# $
# 
# where
# $
# 		\mathcal L( \theta):=
# 		{\mathbb E}_{(x,y)\sim \mathcal D}[\ell(f(x;  \theta), y)]\approx L( \theta) :=
# 		\frac{1}{N} \sum_{j=1}^N\ell(y_j, f(x_j;  \theta))
# $
# 
# Here
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
# 
# 
#  

# In[ ]:




