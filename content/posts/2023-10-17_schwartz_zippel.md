---
title: "Schwartz-Zippel Note"
date: 2023-10-17T21:15:02+08:00
draft: true
---

Schwartz-Zippel Lemma is frequently used in Snark interactive proofs.

For a *non-zero*, $m$-variate polynomial $P: \mathbb{F}^m \to \mathbb{F}$ with degree $d$, defined on a finite field $\mathbb{F}$, the lemma states

$$
\Pr_{X \in \mathbb{F}^m}{[P(X) = 0]} \le \frac{d}{|\mathbb{F}|}
$$

The $|\mathbb{F}|$ is the size of the field, i.e. number of elements in it.

Let's forget what $m$-variate polynomial is and focus on the univariate case.

$$
\Pr_{X \in \mathbb{F}}{[P(X) = 0]} \le \frac{d}{|\mathbb{F}|}
$$

The lemma says if we define a polynomial on a very big field, and randomly choose a point from the field to evaluate the polynomial, then it would be improbable for the polynomial to evaluate zero.

The degree d polynomial has d solutions, so d out of $|\mathbb{F}|$ elements can make the polynomial evaluates to zero.

### Example

$$
P(X) = X^2 - 3X + 2
$$

We define $P(X)$ on $\mathbb{Z}_{101} = \lbrace 0, 1, 2, 3, \dots, 100 \rbrace$

Note that $P(X)$ evaluates to zero on $X=1$ and $X=2$

Since $P(X)$ is a degree two polynomial and $\mathbb{Z}_{101}$ is a prime field, only 1 and 2 from the 101 elements can make $P(X)$ evaluate to zero.

## Applications

### Zero Check

We know a polynomial $P$ with degree $d$ but none of its coefficients. We have an API to evaluate the polynomial on some points, and we want to determine if $P(X) := 0$. To check that for sure, we have to check $d+1$ points and see the evaluations are all zero. But with Schwartz-Zippel, we can check just one point to conclude with high confidence.

In usual Snarks settings, the field size is roughly 256 bits, so $|\mathbb{F}| \approx 2^{255}$. The polynomial we use has a degree usually $2^{20}$. So the probability of the polynomial evaluating to zero would be

$$
\frac{d}{|\mathbb{F}|} = \frac{2^{20}}{2^{235}} = \frac{1}{2^{235}}
$$

Which is practically a very tiny probability.

Suppose $P(X)$ is a non-zero polynomial. Randomly sampling a $x$ on $\mathbb{F}$ and then getting $P(x) = 0$ is like finding a needle in the ocean. We can reasonably believe $P(X)$ is a zero polynomial, i.e. $P(X) := 0$

### Equality Check

We can apply the same idea to check if $P_1 = P_2$, for polynomials $P_1$ and $P_2$.

Define $P(X) := P_1(X) - P_2(X)$, then checking $P_1 = P_2$ is the same as checking $P(X) = 0$

### Source

[1] J. Thaler, “Proofs, Arguments, and Zero-Knowledge,” p. 28.
