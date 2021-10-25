## Convergence of Gradient Descent method

Now we are ready to study the rate of convergence of unconstrained
minimization schemes. For the optimization problem
[\[optmodel\]](#optmodel){reference-type="eqref" reference="optmodel"},
$$\label{key}
\min_{x\in \mathbb{R}^n} f(x).$$ We assume that $f(x)$ is convex. Then
we say that $x^*$ is a minimizer if
$$f(x^*) = \min_{x \in \mathbb{R}^n} f(x).$$ For minimizer $x^*$, we
have $$\label{key}
\nabla f(x^*) = 0.$$ We have the next two properties of the minimizer
for convex functions:

1.  If $f(x) \ge c_0$, for some $c_0 \in \mathbb{R}$, then we have
    $$\label{key}
        \mathop{\arg\min} f \neq \emptyset.$$

2.  If $f(x)$ is $\lambda$-strongly convex, then $f(x)$ has a unique
    minimizer, namely, there exists a unique $x^*\in \mathbb{R}^n$ such
    that $$\label{key}
        f(x^*) = \min_{x\in \mathbb{R}^n }f(x).$$

To investigate the convergence of gradient descent method, let us recall
the gradient descent method:

::: algorithm
**For**: $t = 1, 2, \cdots$ $$\label{equ:fgd-iteration}
    x_{t+1} =  x_{t} - \eta_t \nabla f(x_t),$$ where $\eta_t$ is the
stepsize / learning rate.
:::

We have the next theorem about the convergence of gradient descent
method under the Assumption [\[ass:GD\]](#ass:GD){reference-type="ref"
reference="ass:GD"}.

::: theorem
For Gradient Descent Algorithm
[\[alg:FGD\]](#alg:FGD){reference-type="ref" reference="alg:FGD"}, if
$f(x)$ satisfies Assumption [\[ass:GD\]](#ass:GD){reference-type="ref"
reference="ass:GD"}, then
$$\|x_t - x^*\|^2 \le  \alpha^t \|x_0 - x^*\|^2$$ if
$0<\eta_t <\frac{2\lambda}{L^2}$ and $\alpha < 1$.

Particularly, if $\eta_t = \frac{\lambda}{L^2}$, then
$$\|x_t - x^*\|^2 \le  \left(1 - \frac{\lambda^2}{L^2}\right)^t \|x_0 - x^*\|^2.$$
:::

::: proof
*Proof.* Note that $$x_{t+1} - x =  x_{t} - \eta_t \nabla f(x_t)  - x.$$
By taking $L^2$ norm for both sides, we get
$$\|x_{t+1} - x \|^2 = \|x_{t} - \eta_t \nabla f(x_t) - x \|^2.$$ Let
$x = x^*$. It holds that $$\begin{aligned}
    \|x_{t+1} - x^* \|^2 &=  \| x_{t} - \eta_t \nabla f(x_t) - x^* \|^2 \\
    &= \|x_t-x^*\|^2 - 2\eta_t \nabla f(x_t)^\top (x_t - x^*) + \eta_t^2 \|\nabla f(x_t) - \nabla f(x^*)\|^2 \qquad \mbox{\scriptsize (by $\nabla f(x^*)=0$)}\\
    &\le \|x_t - x^*\|^2 - 2\eta_t \lambda \|x_t - x^*\|^2 + \eta_t ^2 L^2 \|x_t - x^*\|^2  \quad \mbox{\scriptsize (by $\lambda$- strongly convex \eqref{strongConvIneq} and Lipschitz)}\\
    &\le (1 - 2\eta_t \lambda + \eta_t^2 L^2) \|x_t - x^*\|^2
    =\alpha \|x_t - x^*\|^2,
    \end{aligned}$$ where
$$\alpha = \left(L^2 (\eta_t  -{\lambda\over L^2})^2 + 1-{\lambda^2\over L^2}\right)<1\  \mbox{if } 0< \eta_t<\frac{2\lambda}{L^2}.$$
Particularly, if $\eta_t =\frac{\lambda}{L^2}$,
$$\alpha=1-{\lambda^2\over L^2},$$ which finishes the proof. ◻
:::

This means that if the learning rate is chosen appropriatly,
$\{x_t\}_{t=1}^\infty$ from the gradient descent method will converge to
the minimizer $x^*$ of the function.

There are some issues on Gradient Descent method:

-   $\nabla f(x_{t})$ is very expensive to compute.

-   Gradient Descent method does not yield generalization accuracy.

The stochastic gradient descent (SGD) method in the next section will
focus on these two issues.
