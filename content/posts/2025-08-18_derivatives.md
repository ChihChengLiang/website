---
title: "Data Derivatives"
date: 2025-08-18T16:19:12+08:00
draft: false
---


I'm proposing to name the class of applications like "age > 18" proof as "Derivatives."

### Examples

- **ID Derivatives** are claims derived from your ID. A "age > 18" proof is a claim about your age derived from an age attribute of your digitally issued identity.
- **Portfolio Derivatives** are claims derived from your financial assets. A credit score about your financial health can be derived from multiple sources of asset your own -- IRS signed tax statement, a bank balance from a TLS secured webpage, and a merkle proof of your crypto balance. [^0xparc]
- **Email Derivatives** are claims extracted from your email, with tools like [zkemail](https://zk.email/). The applications are massive here but I show just one: You can recover your crypto account by presenting your recovery email derivative.
- **Composite Derivatives**: Remix the aboves to unlock new interesting applications.

### Definitions

An **explicit claim** is a non-trivial fact about a person, recorded in the form of data. For example, these are consider explicit claims: your name or date of birth on your ID, the bank balance from your banking website, or your account balance from Ethereum blockchain. The degree that people can treat an explicit claim as fact depends on the quality the data being generated and registered. A merkle proof of balance on Ethereum is certainly a fact. But a date of birth registered with bribery would be a corrupted claim.

An **Implicit claim** is a fact deducted from the application mechanism. For example, proving knowledge of a secret field in an ID establishs the implicit claim that you are the holder of the ID -- you are the only person on the earth capable of crafting the deriviative passing the verification. If your secret is stolen, then the implicit claim is considered invalid.

A **Derivable** is a piece of data contains one or multiple explicit claims.

A **Derivative** is a piece of computationally verifiable data, encapsulating claims derived from derivables.

Foundamentally, a derivative offers a statement pieced together from one or multiple explicit and implicit claims, sliced and diced from the derivables the claims belong to.

### Properties

A derivative is useful because of the following properties:

- **Splittable**: a.k.a. Selective Disclosure. A derivable is usually a bundle of multiple explicit claims. A splitting property means you can expose just a subset of them. The main benefit is privacy, you reveal your age without revealing your name together.
- **Transformable**: A derivative should not be limited to the face value of the data, they should able to compute from that data. Your ID only register your date of birth. It requires computation to derive age from the date of birth. Another cheap step of computation to tell age greater than 18 or not gives you the benefit of privacy by covering the actual age. Note that the computation step is not arbitrary on the runtime, it is a verification process agreed beforehand.
- **Jointable**: A derivative can be derived from multiple derivables like the credit score use case mentioned above.
- **Second Derivatives**: A derivative can be a derivable for another new derivative. Just like what you can do in calculus.


## Motivation

Problem with exising terms

- Existing terms are defined around the toolings and the cryptographic technics, but not the inner workings of applications. 
- Good cryptography is hidden cryptography. You no longer see "https" in browser url bar unless you deliberately do so. You don't say let me text my friend with end-to-end encryption, you say "let me text my friend." If the cryptography is opening a new set of application, we should name that application and leave that technicallity behind. Users have no bandwidth and no reason to verify the use of the cryptography.



- You're repeatedly encountering something that requires lengthy explanation each time
- A name would help you notice patterns or make distinctions that matter
- It enables better coordination between people working on something together
- The act of naming itself forces useful clarity about what you're actually dealing with

- limited 

## Inspiration


It's like financial derivative, where you have derivatives assets -- futures and options -- from the underlying assets -- stocks or commodities.

It's also like the derivatives in the field of copyright and art, where people derive new works from their predecessor.

The Zk derivatives are facts derived from the your underlying private digital assets -- ID card, bank statements, and emails.


## Alternatives

Here we'll argue the limitation of potential alternatives.


- selective disclosure: too restrictive on the imagination. People only think about fields on an ID but not the networks of possibility you can derive from the basic secrets.

- Anonymous credentials
- ZK ID / ZK wrapped ID
- Universal Protocol / Universal Cryptographic Adapters / PODs

