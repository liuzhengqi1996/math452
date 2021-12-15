#!/usr/bin/env python
# coding: utf-8

# # 7.2 Why we need deep neural networks via composition {#whydeep}
# 
# ## 7.2.1 FEM ans ${\rm DNN}_1$ in 1D
# 
# Thanks to following connection between $\varphi(x)$ in
# [\[def_g\]](#def_g){reference-type="eqref" reference="def_g"} and
# ${\rm ReLU}(x) = \max(0,x )=x_+$ $$\label{key}
# \varphi(x) = 2{\rm ReLU}(x) - 4{\rm ReLu}({x-\frac{1}{2}}) + 2{\rm ReLU}(x-1),$$
# it suffices to show that each basis function $\varphi_{\ell,i}$ can be
# represented by a ReLU DNN. We first note that the basis function
# $\varphi_{\ell,i}$ has the support in $[x_{\ell,i-1},
# x_{\ell,i+1} ]$ can be easily written as $$\label{1d-basisu}
# \varphi_{\ell,i}(x) = \frac{1}{h_{\ell}}{\rm ReLU}(x-x_{\ell,i-1}) -\frac{2}{h_{\ell}}{\rm ReLU}(x-x_{\ell,i}) +\frac{1}{h_\ell}{\rm ReLU}(x-x_{\ell,i+1}).$$
# More generally, consider a general grid with vertex $\{x_i\}$, which is
# not necessarily uniform. The basis function $\varphi_i$ of the linear
# element with support $[x_{i-1},
# x_{i+1} ]$ can be easily written as $$\label{1d-basis}
# \varphi_i(x) = \frac{1}{h_{i-1}}{\rm ReLU}(x-x_{i-1}) -(\frac{1}{h_{i-1}}+\frac{1}{h_i}){\rm ReLU}(x-x_i) +\frac{1}{h_i}{\rm ReLU}(x-x_{i+1}),$$
# where $h_i = x_{i+1} - x_i$.
# 
# Thus is to say, we have the next theorem.
# 
# ::: {.theorem}
# [\[thm:1dLFEMDNN\]]{#thm:1dLFEMDNN label="thm:1dLFEMDNN"} For $d=1$, and
# $\Omega\subset \mathbb R^d$ is a bounded interval, then ${\rm DNN}_1$
# can be used to cover all linear finite element function in on $\Omega$.
# :::
# 
# ## 7.2.2 Linear finite element cannot be recovered by ${\rm DNN}_1$ for $d\ge2$
# 
# In view of
# Theorem [\[thm:1dLFEMDNN\]](#thm:1dLFEMDNN){reference-type="ref"
# reference="thm:1dLFEMDNN"} and the fact that ${\rm{DNN}_J}
# \subseteq {\rm{DNN}_{J+1}}$, it is natural to ask that how many layers
# are needed at least to recover all linear finite element functions in
# $\mathbb{R}^d$ for $d\ge2$. In this section, we will show that
# $$\label{key}
# J_d \ge 2, \quad \text{if} \quad d\ge 2,$$ where $J_d$ is the minimal
# $J$ such that all linear finite element functions in $\mathbb R^d$ can
# be recovered by ${\rm DNN}_J$.
# 
# In particular, we will show the following theorem [@he2020relu].
# 
# ::: {.theorem}
# [\[lowerbound\]]{#lowerbound label="lowerbound"} If
# $\Omega\subset \mathbb R^d$ is either a bounded domain or
# $\Omega=\mathbb{R}^d$, ${\rm DNN}_1$ can not be used to recover all
# linear finite element functions on $\Omega$.
# :::
# 
# ::: {.proof}
# *Proof.* We prove it by contradiction. Let us assume that for any
# continuous piecewise linear function $f: \Omega \to \mathbb{R}$, we can
# find finite $N \in \mathbb{N}$, $w_i \in \mathbb{R}^{1,d}$ as row vector
# and $\alpha_i, b_i, \beta \in \mathbb{R}$ such that
# $$f =  \sum_{i=1}^N \alpha_i {\rm ReLU}(w_i\cdot  x +b_i) + \beta,$$
# with $f_i = \alpha_i {\rm ReLU}(w_i\cdot  x +b_i)$, $\alpha_i \neq 0$
# and $w_i
# 	\neq 0$. Consider the finite element functions, if this one hidden
# layer ReLU DNN can recover any basis function of FEM, then it can
# recover the finite element space. Thus let us assume $f$ is a locally
# supported basis function for FEM. Furthermore, if $\Omega$ is a bounded
# domain, we assume that $$\label{distcondi}
# 	d({\rm supp}(f), \partial \Omega) > 0,$$with
# $$d(A, B) = \inf_{x\in A, y\in B} \|x-y\|,$$ as the distance of two
# closed sets.
# 
# A more important observation is that $\nabla f: \Omega \to
# 	\mathbb{R}^d$ is a piecewise constant vector function. The key point is
# to consider the discontinuous points for $$g := \nabla
# 	f = \sum_{i=1}^N \nabla f_i.$$ For more general case, we can define the
# set of discontinuous points of a function by
# $$D_{g} := \{x \in \Omega~|~ x ~ \text{is a discontinuous point of} ~ g\}.$$
# Because of the property that $$\label{eq:disfun}
# 	D_{f+g} \supseteq D_{f} \cup D_{g} \backslash (D_{f} \cap D_{g}),$$ we
# have $$\label{eq:dis_fn}
# 	D_{\sum_{i=1}^N g_i} \supseteq \bigcup_{i=1}^N D_{g_i} \backslash \bigcup_{i\neq j}\left( D_{g_i}\cap D_{g_j} \right).$$
# Note that $$\label{eq:def_gi}
# 	g_i = \nabla f_i(x) =  \nabla \left( \alpha_i {\rm ReLU}(w_i\cdot   x +b_i)  \right) =\left(\alpha_iH(w_i \cdot  x +b_i)\right)w_i \in \mathbb{R}^d,$$
# for $i=1:N$ with $H$ be the Heaviside function defined as:
# $$H(x) = \begin{cases}
# 	0 &\text{if} ~ x \le 0, \\
# 	1 &\text{if} ~ x > 0.
# 	\end{cases}$$ This means that $$\label{eq: D_gi}
# 	D_{g_i} = \{ x ~|~ w_i\cdot   x + b_i = 0\}$$ is a $d-1$ dimensional
# affine space in $\mathbb{R}^d$.
# 
# Without loss of generality, we can assume that $$\label{eq:assumD_gi}
# 	D_{g_i} \neq D_{g_j}.$$ When the other case occurs, i.e.
# $D_{g_{\ell_1}} = D_{g_{\ell_2}} = \cdots= D_{g_{\ell_k}}$, by the
# definition of $g_i$ in
# [\[eq:def_gi\]](#eq:def_gi){reference-type="eqref"
# reference="eq:def_gi"} and $D_{g_i}$ in
# [\[eq: D_gi\]](#eq: D_gi){reference-type="eqref" reference="eq: D_gi"} ,
# this happens if and only if there is a row vector $(w, b)$ such that
# $$\label{eq:Dfcondition}
# 	c_{\ell_i}\begin{pmatrix}
# 	w &
# 	b
# 	\end{pmatrix} =  
# 	\begin{pmatrix}
# 	w_{\ell_i} &
# 	b_{\ell_i}
# 	\end{pmatrix},$$ with some $c_{\ell_i} \neq 0$ for $i = 1:k$. We
# combine those $g_{\ell_i}$ as $$\begin{aligned}\label{mergeH}
# 	%	\begin{split}
# 	\tilde g_{\ell} &= \sum_{i=1}^k g_{\ell_i} = \sum_{i=1}^k \alpha_{\ell_i} H(w_{\ell_i} \cdot  x + b_{\ell_i}) w_{\ell_i}, \\
# 	&= \sum_{i=1}^k \left( c_{\ell_i}\alpha_{\ell_i} H\left(c_{\ell_i}(w\cdot   x + b)\right) \right) w, \\
# 	&=\begin{cases}
# 	\displaystyle \left(\sum_{i=1}^k  c_{\ell_i}\alpha_{\ell_i} H(c_{\ell_i}) \right) w  \quad &\text{if} \quad w x + b > 0,\\
# 	\displaystyle \left(\sum_{i=1}^k  c_{\ell_i}\alpha_{\ell_i} H(-c_{\ell_i}) \right) w  \quad &\text{if} \quad w x + b \le 0.\\
# 	\end{cases}
# 	%	\end{split}
# 	\end{aligned}$$ Thus, if
# $$\left(\sum_{i=1}^k  c_{\ell_i}\alpha_{\ell_i} H(c_{\ell_i}) \right)  = \left(\sum_{i=1}^k  c_{\ell_i}\alpha_{\ell_i} H(-c_{\ell_i}) \right),$$
# $\tilde g_\ell$ is a constant vector function, that is to say
# $D_{\sum_{i=1}^k g_{\ell_i}} = D_{\tilde g_\ell} = \emptyset$.
# Otherwise, $\tilde g_\ell$ is a piecewise constant vector function with
# the property that
# $$D_{\sum_{i=1}^k g_{\ell_i}} = D_{\tilde g_\ell} = D_{g_{\ell_i}} = \{ x ~|~ w\cdot  x + b = 0\}.$$
# This means that we can use condition
# [\[eq:Dfcondition\]](#eq:Dfcondition){reference-type="eqref"
# reference="eq:Dfcondition"} as an equivalence relation and split
# $\{g_i\}_{i=1}^N$ into some groups, and we can combine those
# $g_{\ell_i}$ in each group as what we do above. After that, we have
# $$\sum_{i=1}^N g_i = \sum_{\ell=1}^{\tilde N} \tilde g_{\ell},$$ with
# $D_{\tilde g_s} \neq D_{\tilde g_t}$. Finally, we can have that
# $D_{\tilde g_s} \cap D_{\tilde g_t}$ is an empty set or a $d-2$
# dimensional affine space in $\mathbb{R}^d$. Since $\tilde N \le N$ is a
# finite number,
# $$D := \bigcup_{i=1}^N D_{\tilde g_\ell} \backslash \bigcup_{s\neq t}\left( D_{\tilde g_s}\cap D_{\tilde g_t} \right)$$
# is an unbounded set.
# 
# -   If $\Omega = \mathbb{R}^d$,
#     $${\rm supp(f)} \supseteq D_{g} = D_{\sum_{i=1}^N g_i} = D_{ \sum_{\ell=1}^{\tilde N} \tilde g_{\ell}} \supseteq D,$$
#     is contradictory to the assumption that $f$ is locally supported.
# 
# -   If $\Omega$ is a bounded domain, $$d(D, \partial \Omega) = 
#     		\begin{cases}
#     		s > 0 \quad &\text{if}\quad  D_{\tilde g_i} \cap \Omega = \emptyset, \forall i\\
#     		0 \quad &\text{otherwise}.
#     		\end{cases}$$ Note again that all $D_{\tilde g_i}$'s are $d-1$
#     dimensional affine spaces, while
#     $D_{\tilde g_i} \cap D_{\tilde g_j}$ is either an empty set or a d-2
#     dimensional affine space. If $d(D, \partial \Omega) > 0$, this
#     implies that $\nabla f$ is continuous in $\Omega$, which contradicts
#     the assumption that $f$ is a basis function in FEM. If
#     $d(D, \partial \Omega) = 0$, this contradicts the previous
#     assumption in [\[distcondi\]](#distcondi){reference-type="eqref"
#     reference="distcondi"}.
# 
# Hence ${\rm DNN}_1$ cannot recover any piecewise linear function in
# $\Omega$ for $d \ge 2$. ◻
# :::
# 
# Following the proof above, we have the following theorem [@he2020relu].
# 
# ::: {.theorem}
# [\[linearindep\]]{#linearindep label="linearindep"}
# $\{{\rm ReLU}(w_i\cdot x+b_i)\}_{i=1}^m$ are linearly independent if
# $(w_i,
# 	b_i)$ and $(w_j, b_j)$ are linearly independent in
# $\mathbb{R}^{1\times (d+1)}$ for any $i \neq j$.
# :::
# 

# In[ ]:




