---
title: "The Fiscal Theory of Price Level book"
date: 2023-09-14T14:19:03+08:00
draft: false
---

I fell into this rabbit hole of the fiscal theory of price level (FTPL). Professor John Cochrane published the book ["The Fiscal Theory of the Price Level"](https://press.princeton.edu/books/hardcover/9780691242248/the-fiscal-theory-of-the-price-level) earlier this year. I learned about the book on Twitter before it was renamed to X. After reading some introduction, I pre-ordered a copy.

The book's content can help us better understand the crypto-currency and design systems. The theory looks sophisticated enough to address many academic challenges in macroeconomics but simultaneously simple enough to reason with some project ideas.

I progressed slowly and still need to finish the book. The book is math-heavy and text-heavy, in a good way! I reviewed Prof. Cochrane's blog, interviews, the "Money is stock" paper, and course materials. That helps get some motivation before diving into the book. I also tried to equip myself with some backgrounds of ["rational expectations" revolution](https://johnhcochrane.blogspot.com/2023/05/bob-lucas-and-his-papers.html) and "general equilibrium" to appreciate the book better.

I might miss many things, and I'm happy to learn feedback.

Let me summarize the idea of the FTPL, then share some thoughts.

## What is The Fiscal Theory of Price Level?

The FTPL says tax gives money value. A government collects taxes on a particular day, and people need to get some money to pay their tax, which gives money value.

FTPL also says the value of money is the expected discounted present value of future government surplus.

The one-period model looks like this.

$$
\begin{equation}
  \frac{B_0}{P_1} = s_1
\end{equation}
$$

Where $B_0$ is a zero coupon bond at day 0 that pays 1 dollar at day 1, $P_1$ is the day price level, and $s_1$ is the real value of tax collected by the government. Economists use the terms "nominal" and "real" to differentiate the value before and after the price level adjustment.

I first felt unfamiliar seeing a bond in the equation, but then I realized that a bond is the money printer that prints today's money.

If rearranged, we see the right-hand side is the nominal value of the tax. In equilibrium, the money printed out on day 0 got soaked up by the tax.

$$
\begin{equation}
  B_0 = P_1 s_1
\end{equation}
$$

The generalized formula looks like this.

$$
\begin{equation}
  \frac{B_{t-1}}{P_t} = E_t \sum_{j=0}^{\infty}{\beta^j s_{t+j}}
\end{equation}
$$

Here the $0< \beta < 1$ is a subjective discount factor to reflect how people prefer $1 received today over tomorrow. Future cash flows are valued less today.

The equation says the real value of money on time t is the expected discounted present value of the future government surplus. Surplus is the tax collected minus the government spending. Note that the equation is also a government bond pricing equation.

The theory might look weird because we usually treat money like goods or services. The money demand and supply determined the "quantity" and the "price" of money. People hold money because they keep cash to buy stuff, pay something unexpectedly, or speculate for profit. On the other hand, central banks create some base money; commercial banks magically created more money through some weird multiplier effects.

In the cryptocurrency world, we reason money similarly. Token price is determined by the [supply and demand](https://dankradfeist.de/ethereum/2023/01/31/rai-crypto-experiment.html) so that if we want to maintain a stable value of a token, we adjust the supply accordingly to maintain the price of the token denominated in dollar.

The FTPL is prepared for the cashless society. The theory we are familiar with is based on an old worldview, which is best described in a quote from Prof. Cochrane's [presentation](https://youtu.be/SgVEnDvxznc?si=mwU58M2dcyQHXiZB&t=656)[^1].

> When I was very young, if you wanted to go out to dinner on Saturday night, you had to go to the bank on Friday, write a check, and get cash. If you did not have cash, you go to the restaurant and you don't get any food. Now, you might say let them use credit cards. Money doesn't matter at all in that sense, you can just use a credit card if you need to.
>
> The link between holding cash and deposits and economic activity disappeared 20 years ago. Money supply doesn't matter anymore.

Back in the days when money demand and supply still mattered, we have this Quantity Theory of Money(QTM) equation.

$$
\begin{equation}
  M_t V = P_t Y_t
\end{equation}
$$

Where
- $M_t$ is the money supply
- $V$ is the "velocity", i.e., how many times money is transferred to the next person in a period. The velocity is usually assumed to be constant
- $Y_t$ is the real consumption.

I like how [Money as stock](https://www.sciencedirect.com/science/article/pii/S0304393205000140) put the QTM together with the bond pricing equation, which gives insights on how central bank and treasury collaborate.

$$
\begin{align}
  M_t V &= P_t Y_t \newline
  \frac{B_{t-1}}{P_t} &= E_t \sum_{j=0}^{\infty}{\beta^j s_{t+j}}
\end{align}
$$

The first equation is a central bank equation, and the second is the treasury equation. Note that we have two equations with one variable $P_t$. That means the central bank and the treasury must coordinate to determine the stable price level. Either in a "monetary regime", the central bank determines the money supply($M_t$), and then the treasury adjusts the fiscal surplus. It could also be a "fiscal regime", where the treasury fixes the surplus and the bond price, and then the central bank adjusts money supply to maintain the price level. 

But when the money demand and supply disappeared, the QTM equation disappeared too. Only the bond pricing equation is left.

This doesn't mean the central bank disappeared, too. Let me quote another equation from the book (page 10, equation 1.9)

$$
\begin{equation}
  \frac{1}{1+ i_0} = \beta E_0(\frac{P_0}{P_1})
\end{equation}
$$

This is a two-period model. $i_0$ is the interest rate. The right-hand side is the price level of this period over the next period, so it is the inverse of the expected inflation. The modern central banks control the price level with interest rates.

Where are we getting from all the above theories and equations? How can we apply these to cryptocurrency projects?

## Can we apply FTPL on crypto?

### We can pay less attention to money supply and demand

The first benefit from the FTPL is that the money demand and supply are gone. QTM equation exists no more. This means we no longer need to care about the issuance or justify how users will hold crypto. We can just assume users get crypto only to do whatever they like to do on chain, then dump all their holdings once they got the business done. 

It turns out Vitalik has had this insight all the time. I was planning to quote his [On Medium-of-Exchange Token Valuations](https://vitalik.ca/general/2017/10/17/moe.html) post, because that's where I remember I see the QTM equation in the cryptocurrency context. Vitalik proposed the applications should burn the token instead of making it a "medium of exchange"(MOE) token. The MOE token "depends crucially on the holding time" and creates an easily manipulatable multi-equilibrium game. He proposed

> If developers want to front-load revenue to fund initial development, then they can sell a token, with the property that all fees paid are used to buy back some of the token and burn it; this would make the token backed by the future expected value of upcoming fees spent inside the system.

We see the FTPL equation here. Vitalik interpreted the "price level" as the inverse of the currency's price. If we apply this reasoning to the bond pricing equation, the lefthand side becomes the coin market cap, and the right-hand side becomes the future expected value.

### We can focus on the fiscal aspect and public goods funding

The other great thing about FTPL is that we see the fiscal side of the story. Does the protocol capture some surplus? How do we or can we spend those surpluses?

Let's start by examining the fiscal spending of the protocol. I categorize the spending into two types: automatable and non-automatable. The protocol can enforce the automatable type of spending. We can commit an algorithm or policy for them. The non-automatable type is mostly an open question.

The most obvious automatable type is the block reward to pay for the block proposer. Blockchains prevent centralization of block creation by randomly distributing the block creation job to a group of strangers, weighted by a specific asset they hold. In a mining blockchain, the stranger holds mining machines as the asset and wastes energy to prove this fact. In Ethereum, we don't do that here now. We ask block proposers to stake ETH. The chain knows the weight of the stake, so we waste no energy. But in both cases, the protocol pays the block proposer to compensate the cost for dedicating their asset to the system. The new issuance pays this block reward.

The non-automatable spending is the constant maintenance and research required to keep the chain chugging along.

A blockchain protocol is not something we can release and forget. Wild bugs hurt the protocol, novel mechanisms emerge to improve scalability and privacy, next-generation hardware reshapes the computation pricing calculus, and quantum computing threatens cryptographic protection in an unforeseeable future. These kinds of research, development, upgrades, and governance activities have the public-good nature. Users can free-ride the benefit, and the market mechanism underfunds developers.

Blockchain builders have been thinking about how to solve this sustainability problem for a long time. The issuance is a gold pot we've been sitting on, and it is more than enough to fund everything we need(Ethereum network issues roughly [1 billion USD/year](https://ultrasound.money/), and Ethereum Foundation spends almost [50 million USD/year](https://ethereum.foundation/report-2022-04.pdf)). The problem is how to distribute the funding in a sensible way. To the date of writing, Zcash people fund development with [20% of the issuance](https://z.cash/network/) controlled by three entities. Ethereum people are exploring a market-ish mechanism called "quadratic funding" and haven't done anything with the issuance yet.

### A fee market reform transformed the transaction fee as the fiscal surplus for the protocol

Does Ethereum have a fiscal foundation like a tax that can give the government/protocol some revenue stream $s_{t+j}$? Yes, we have. [EIP1559](https://eips.ethereum.org/EIPS/eip-1559) transaction base fee is! EIP1559 is a proposal for "Fee market change" that went production on 2021. The size of software change is decent, but the proposal achieves many goals: congestion control, block stability, UX improvement, and now I'd argue it establishes a fiscal revenue stream for Ethereum.

In the old transaction fee model, a user pays a block proposer some fee to include their transaction. Normally, the user specifies a tiny bit of their value to send through the transaction as the fee, denominated in the native token. But users don't have to pay the block proposer exactly like that. In theory, they can swipe the credit card if they want. In this model, the transaction fee is between the block proposer and the user, and the protocol receives nothing from the transaction fee.

Now that with EIP1559, the protocol decides on a "base fee" to receive based on the congestion of the previous block. The protocol raises the fee if the previous block includes many transactions and lowers the fee if the block looks empty. The base fee is burned, which decreases the money supply. People usually celebrate the supply decrease and called ETH the [ultra sound money](https://ultrasound.money/). But focusing on the supply misses the point.

Barnabe [puts it](https://barnabe.substack.com/p/congestion-control-and-eip1559) in a more positive way.

> With the burn proportional to the demand for the network, a link is created between ETH the asset and the network value of Ethereum.

Overall, we are heading to a good fiscal foundation based on the expected value of future network usage. We should explore this line of thinking on the application side, too, especially rollups.


## Summary

The FTPL book is a gold mine for me. I've been struggling to get a systematic review of the frontier of monetary theory. Most of the research or textbooks I could find were central bank policy analysis, which is knowledge hard to transfer to the cryptocurrency world. The FTPL itself makes reasoning the monetary problem and crypto designs easier. The book also covered broad topics ranging from the gold standard to a list of monetary innovation ideas. I'm excited about what we can build from all the insight we can get from the book.


[^1]: if you are in the crypto world because of Bitcoin Genesis Block and the financial crisis, prof. Cochrane has a great [take](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2425883) on the financial crisis and regulatory system.
