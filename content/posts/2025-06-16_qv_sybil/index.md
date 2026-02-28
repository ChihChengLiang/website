---
title: "Sybil Advantage in Quadratic Voting"
date: 2025-06-16T09:10:37+08:00
draft: false
---

## Quick Quadratic Voting Recap

Quadratic Voting is a voting mechanism that allows voters to express different level of support by spending "voice credits" (VC) at an increasing cost. The key feature is that casting $X$ votes costs $X^2$ voice credits. For example, 1 vote costs 1 VC, 2 votes costs 4, and 3 votes costs 9.

This quadratic cost structure creates a crucial trade-off: voters can express strong preferences on issues they care deeply about, but at a rapidly increasing price.

## The Identity Problem

Quadratic Voting relies on a robust identity system to work. Without it, the mechanism breaks down because the quadratic cost structure can be circumvented through identity manipulation.

Consider the difference between these scenarios:

- **Single identity**: Casting 2 votes costs 4 VC
- **Two identities**: Casting 2 votes (1 from each identity) costs only 2 VC total

The latter is cheaper. The quadratic cost structure breaks if the voting system can't count people's heads properly.

Faking an identity might take some effort, but let's explore this: with $N$ identities under your control, how much advantage can you get in quadratic voting?

## Optimal Vote Allocation Strategy

For a simple case, consider you have a goal to cast 4 votes with 2 identities, A and B. What would be the cheapest way to complete it?

- **Single identity approach**: 4 votes cost 16 VC
- **Uneven split (3+1)**: 9 + 1 = 10 VC total
- **Even split (2+2)**: 4 + 4 = 8 VC total

It's tempting to say that splitting the votes evenly minimizes the cost.

That's indeed the case! We can see this by observing the marginal cost of each extra vote:

| Vote Number| Total VC Cost| Extra Cost |
| -- | -- | -- |
| 1 | 1 | 1 |
| 2 | 4 | 3 |
| 3 | 9 | 5 |
| 4 | 16 | 7 |

Notice that the marginal cost grows linearly.

Let's allocate the 4 votes one by one, first one to A.

| Total votes| A Votes | B Votes | Total VC | Comment|
| ---------- | ------- | ------- | -------- | ------ |
| 1 | 1 (1 VC) | 0 (0 VC) | 1 | |
| 2 | 1 (1 VC) | 1 (1 VC) | 2 | Allocating the second vote to A would cost additional 3 VC, while to B costs 1 |
| 3 | 2 (4 VC) | 1 (1 VC) | 5 | |
| 4 | 2 (4 VC) | 2 (4 VC) | 8 | Allocating the 4th vote to A would cost additional 5 VC, while to B costs 3|

Following the same reasoning, you would let N identities share equal votes. Otherwise, the identity with more votes would incur higher marginal cost than the one with fewer votes. Taking one vote from the higher contributor and giving it to the lower one would improve the situation, until you can't improve it anymore.

### The General Pattern

In general, to cast $X$ votes with $N$ identities, each contributes $\frac{X}{N}$ votes and costs $(\frac{X}{N})^2$ VC, for a total cost of $\frac{X^2}{N}$.

In other words, with a budget of $Y$ VC:

- Solving $Y = X^2$ allows an individual to cast $\sqrt{Y}$ votes
- Solving $Y = \frac{X^2}{N}$, allows an N-identity coalition to cast $\sqrt{NY}$ votes.

## Comparing Different Voting Systems

Let's compare quadratic voting (QV) with one-person-one-vote (1P1V) and one-dollar-one-vote (1$1V). Here assume 1 VC is worth 1 dollar for comparison.

|Method| Marginal cost | Single Identity Influence (budget Y)| N Identities Influence (budget Y) |
| -- | -- | -- | -- |
| 1P1V | $\infty$ (after first vote) | 1 | $N$ |
| QV | $2X - 1$ (at $X$ votes) | $\sqrt{Y}$ | $\sqrt{N}\sqrt{Y}$ |
| 1$1V | $1$ | $Y$| $Y$ |

## The Bottom Line

In summary, with N people in your control, you can ask them to cast N votes in 1P1V. The advantage is smaller in QV -- you only multiplying your inflences by $\sqrt{N}$. There's no effect for 1$1V, which is sybil-safe since it doesn't care where a dollar comes from.

So quadratic voting provides some resistance to identity manipulation, but it's not perfect. The square root relationship means that while having more fake identities helps, the advantage grows much more slowly than in traditional democratic voting.
