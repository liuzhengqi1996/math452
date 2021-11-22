#### Nodal value interpolant

For any continuous function $u$, we define its linear finite element
interpolation, $(I_h u)(x)\in V_{h,0}$, as follows: $$\label{u-interp}
(I_h u)(x)= \sum_{i=1}^{n_h}u(x_i)\varphi_i(x).$$ Usually, we also
denote $(I_h u)(x)$ as $u_I(x)$. Using interpolation, we can obtain the
following approximation property of linear finite element space.

::: {.center}
![Approximation of finite element
space.](figures/fdsolutions.pdf){#Interpolation height="2.5in"
width="3in"}
:::

::: {.theorem}
[\[interp00\]]{#interp00 label="interp00"} Assume that $\mathcal T_h$ is
quasi-uniform and $V_h$ is the linear finite element space associated
with $\mathcal T_h$, then $$\label{error0}
\inf_{v_h\in V_h} \|v-v_h\|+h |v-v_h|_{1}\lc h^2 |v|_2
        \qall v\in H^2(\Om).$$
:::

::: {.proof}
*Proof.* Let us first prove Theorem
[\[interp00\]](#interp00){reference-type="ref" reference="interp00"} for
$d=1, 2, 3$. This proof presented here follows from Xu [@xu1982estimate]
(see also Xu [@xu2013estimate]). Let $x=(x^1,\ldots, x^d)$ and
$a_i=(a^1_{i}, \ldots, a^d_{i})$. Introducing the auxiliary functions
$$g_i(t)=v(a_i(t)),\mbox{  with  }  a_i(t)=a_i+t(x-a_i),$$ we have
$$g_i'(t)=(\nabla v)(a_i(t))\cdot (x-a_i)
=\sum_{l=1}^d(\partial_lv)(a_i(t))(x^l-a_i^l)$$ and $$\label{gpp}
g_i''(t)=\sum_{k,l=1}^d\partial^2_{kl}v)(a_i(t))(x^k-a_i^k)(x^l-a_i^l).$$
Note Taylor expansion $$g_i(0)=g_i(1)-g_i'(1)+\int_0^1tg''_i(t)dt,$$
namely $$\label{Taylor_vi}
v(a_i)=v(x)-(\nabla v)(x)\cdot (x-a_i)+\int_0^1tg''_i(t)dt,$$ and note
that
$$(I_hv)(x)=\sum_{i=1}^{d+1}v(a_i)\lambda_i(x), \quad \sum_{i=1}^{d+1}\lambda_i(x)=1,$$
and $$\sum_{i=1}^{d+1}(x-a_i)\lambda_i(x)=0.$$ It follows that
$$\label{Ihvv}
(I_hv-v)(x)=\sum_{i=1}^{d+1}\lambda_i(x)\int_0^1tg''_i(t)dt.$$ Using and
the trivial fact that $|x^l-a_i^l|\le h$, we obtain $$\begin{aligned}
\|g''_i(t)\|_{L^2(\tau)}\le h^2
\sum_{k,l=1}^d\|(\partial^2_{kl}v)(a_i(t))\|_{L^2(\tau_i^t)}
\le h^2t^{-d/2}\sum_{k,l=1}^d\|\partial^2_{kl}v\|_{L^2(\tau)},\end{aligned}$$
where we have used the following change of variable
$$y=a_i+t(x-a_i): \tau\mapsto \tau_i^t\subset\tau \mbox{ with } dy=t^ddx.$$
Now taking the $L^2(\tau)$ norm on both hand of sides of , we get
$$\begin{aligned}
\|I_hv-v\|_{L^2(\tau)}
&\le& h^2\sum_{i=1}^{d+1}\max_{x\in\tau}|\lambda_i(x)|
\int_0^1t\|g''_i(t)\|_{L^2(\tau)}\;dt\\
&\le& (d+1)\int_0^1t^{-d/2}dt\;h^2\;
\sum_{k,l=1}^d\|\partial^2_{kl}v\|_{L^2(\tau)}\\
&\le&\frac{2(d+1)}{4-d}h^2
\sum_{k,l=1}^d\|\partial^2_{kl}v\|_{L^2(\tau)}\\
&\le&\frac{4d(d+1)}{4-d}h^2|v|_{H^2(\tau)}.\end{aligned}$$ Now we prove
the $H^1$ error estimate. Notice that
$$[\partial_{j}( I_{h} v - v)](x) = \sum_{i} (\partial_{j} \lambda_{i} )(x) \int_{0}^{1} t g''_{i}(t) dt + \sum_{i} \lambda_{i}(x) \partial_{j} \int_{0}^{1} t g''_{i}(t) dt.$$
By ,
$$\int_0^1tg''_i(t)dt = v(a_i) - v(x) + (\nabla v)(x)\cdot (x-a_i)$$
therefore, $$\begin{aligned}
\lefteqn{\partial_{j} \int_0^1tg''_i(t)dt} \\
& = & - \partial_{j} v + (\nabla \partial_{j} v )(x) (x - a_{i}) + \nabla v \cdot e_{j} 
\hcomment{$e_{j}$ is the $j$-th standard basis}  \\
& = & (\nabla \partial_{j} v )(x) (x - a_{i}).\end{aligned}$$ Noting
that $\sum_{i} \lambda_{i}( \nabla \partial_{j} v )(x) (x - a_{i}) = 0$,
we have
$$[\partial_{j}( I_{h} v - v)](x) = \sum_{i} (\partial_{j} \lambda_{i} )(x) \int_{0}^{1} t g''_{i}(t) dt.$$
Then the estimate for $|\nabla(I_hv-v)|_{L^2(\tau)}$ follows by a
similar argument and the following obvious estimate
$$|(\nabla\lambda_i)(x)|\lc\frac{1}{h}.$$

On the proof of Theorem [\[interp0\]](#interp0){reference-type="ref"
reference="interp0"} for $d\ge 4$, the above proof does not apply for
$d \ge 4$. This is because when $d \ge 4$, the embedding relation
between $H^{2}(\Om) \hookrightarrow C(\bar{\Om})$ is no longer true.
Only continuous functions can have interpolations. In this case, one
approach is to use the so-called Scott-Zhang interpolation
[@scott1990finite], the details can be found in [@Xu.J2015a]. ◻
:::

As a result of Theorem [\[interp00\]](#interp00){reference-type="ref"
reference="interp00"}, we have

::: {.theorem}
[\[interp0\]]{#interp0 label="interp0"} Let $V_N$ be linear finite
element space on a quasi-uniform triangulation consisting of $N$
element. Then $$\label{error0N}
\inf_{v_h\in V_N} \|v-v_h\|+N^{-{1\over d}} |v-v_h|_{1}\lc N^{-{2\over d}} |v|_2
        \qall v\in H^2(\Om).$$
:::
