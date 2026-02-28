---
title: "📝Quadratic Funding in plain words"
date: 2022-06-20T21:45:09.524Z
draft: false
---

This is my quick compilation of all the QF-related sources I've seen recently. The goal is to give high-level intuitions before diving into the math.

There are two challenges in public good funding:

- How do you get the money?
- How do you distribute the money when you get it?

In a private good situation, users pay for what they get. They can pay it now for the things they benefit from. Incentives send the right signal to the market.

In the public good situation. Free rider problem blocks that signal. The market is not able to get the signal of what public good is valuable.

We can tackle the two challenges with two types of money: Stupid money and smart money.

Stupid money is easily collected but hard to distribute. It solves problem 1 but not problem 2. Examples of stupid money are:

- The government collected tax.
- Blockchain new issuance. It is a Seigniorage tax, which means you print new money and make people's holding worthless as if you collecting tax from them.
- Transaction fee burnt.
- Burnt auction gain from the L2 sequencers.

Stupid money is collected forcibly. So we can't use it for opinioned usage. We need to use some credible neutral way to earn the legitimacy to collect it.

The other way to view the stupid money is that the collectors are uninformed on what specific valuable public good projects are. Examples of the collector could be CCCP, government, or even non-human actors like an on-chain contract.

On the other hand, the smart money is money from an individual's pocket and at their disposal. Individuals have deep insights into what public good is valuable because they might be the ones that use it every day. So they can make opinioned decisions. That's why we call the money smart.

When an individual sends their fund to a project, it has two effects:

1. The fund from the individual goes to the project.
2. It sways QF formula's decision on distributing more stupid money to the project.

The first effect partially mitigates problem one. What's more important is the second effect.

The first consequence of the second effect is it incentivizes the individual to "vote" for the public good they feel valuable, in the sense that the matching fund would invest more in the project that the individual enjoys.

Compared with sending direct funding to the project, the individual's funds now have the leverage effect from the matching pool.

Let's assume some scenarios: Suppose a marginal donation size `$X` can let the public goods benefit everyone by `0.9*$X` more. A public good that can benefit all people with $1. An individual can choose to donate X=0.1. After the donation, the project can benefit all people 1+0.9X = 1.09. We focus on the individual's payoff on direct funding and QF.

In directed funding, the donation canceled off the benefit of the public good the individual enjoys. The individual chooses to free ride.

```
donate: 1.09 - 0.1 = 0.99
free ride: 1
```

Say in the QF case, suppose the donation drain 0.05 from the matching pool to the project.

```
donate: 1(1+ 0.9*(0.1 + 0.05)) - 0.1 = 1.035
free ride: 1
```
Now donating to the project has more incentives. 


Once the individual has the incentive to donate. This leads to the second consequence of the second effect. The individual is now sharing their wisdom and sending the signal to the public good market, and guiding the stupid money to the right projects. The usage of stupid money is justified by market intelligence.

### A guide to user

Suppose you see a QF website listing some projects, what would be a rational way to participate?

- If none of the projects resonates with you and you have no interest in the field. Leave ASAP and do not spend anything there.
- If it's a field or a cause you feel important, and you want to see it grow. However, you are unfamiliar with any specific project. You can choose to donate to the matching pool.
- If you used and enjoyed specific projects or you feel some projects would be valuable in the future. Donate to the project to channel the matching pool's money to it.