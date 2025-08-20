---
title: "Data Derivatives"
date: 2025-08-18T16:19:12+08:00
draft: false
---

> The world was so recent that many things lacked names, and in order to indicate them it was necessary to point.
> -- Gabriel García Márquez

Two things I've been doing recently: exploring AI and reflecting on communications.

I vibe coded a [map](https://chihchengliang.github.io/scimap/) to explore life events of 18 century mathematicians and a [brainstorming app](https://brainstorm-claude-d1vhb9vpv-chih-cheng-liangs-projects.vercel.app/) for my favorite ritual without subscribing Figma.

I tried Suno AI and got mindblown by the music quality of v4.5 model.

By spitting out images, code, and music, LLMs empower skill-less users to craft stunning work. What determines the outcome quality is how well the users express themselves and figure out their desire. Fluency in the domain language matters. 

<figure>
  <img src="image_prompt.png" >
  <figcaption>
  Questions to consider when prompting an image 
  <a target="_blank" href="https://dallery.gallery/wp-content/uploads/2022/07/The-DALL%C2%B7E-2-prompt-book-v1.02.pdf
  ">[source]</a>
  </figcaption>
</figure>


The prompts for images are somehow straigteforward. One might not know what is a "dutch angle," but it could be illustrated with an image, or a text description like "shot from a weird bottom up angle."

For coding, modern people are well versed in the languages of buttons and text. Minor expertise might be required to tell what is a "navbar". Major expertise help you diagnosis the deep JavaScript and CSS issues and unstuck the LLM from an unproductive bug fixing. A trained person is also more likely to foresee the complexcity involving multi-user interaction.

Music frustrates me, but mostly that's due to my lack of training. Music genres are many and you have to register them by listening one by one. If you know the name of your favorite sound, you can get what you want quickly. If you don't know, then you wait till you encounter a similar song that has prompts attached to it, labelling that sound for you.

In general, things you can see or point, like UI, are somehow manageable. Invisible things are somehow less trackable, but audible things are still okay. All you have to do is train an embedding of ideas in your brain, and summon one with a good name.

---

The experience of prompting makes me wonder, what about the language of the blockchain domain? If we are only allowed to build products with prompts, what would that developer experience feel like?

Many might agree, our language is terrible. Like, how do we even call our domain? 

- A blockchain domain? It is bad because it's not the definitive feature, some might explore a technical design without blocks and chains.
- distributed ledger technology? It doesn't capture the computing part.
- Decentralized computing? It is better but it includes project requires no strong consensus.
- World computer is something I like, but it says almost nothing.
- Ethereum is the one I would use, because it captures an instance with all required elements. But it is also a label of a very specific project and excludes all the relative projects.

More over, most of our terms, especially the values delivered to users, decribe something abstract, intangible, and invisible. Decentrailization, trustless, privacy, security.

Many terms are poorly defined. Notably, a ZK rollup has no zero-knowledge property.

Terms are judged because they exist, could there be potential inexistent terms remain to be coined, or minted?

Before we getting into that, maybe we can talk about what makes a good name. I haven't found a systemetic method for naming things, but I find the following points reasonable:

- You're repeatedly encountering something that requires lengthy explanation each time
- A name would help you notice patterns or make distinctions that matter
- It enables better coordination between people working on something together
- The act of naming itself forces useful clarity about what you're actually dealing with

Immediately comes up to my mind is the concept that I'm going to name it "derivatives." This concept is usually introduced with a "age>18 proof" -- a zero knowledge proof that convinces a verifier that your age is greater than 18 years old. You present a QR code to a bouncer and walked into a night club. Behind that QR code is a machine verifiable cryptographic message, derived from your government issued digital identity that attest to your legal name, age, and other attributes, reveals only the fact you are older than 18 but nothing else.

The setup is benefitial because alternatively, you have to present your full ID to the bouncer and reveal information unneeded for the application. Selective disclosure is the main featured offered by the tool.

The tools achiving the "age>18 proof" are sometime called zkID, anonynous credentials, due to the project AnonCred.

But that seems not the full picture. Both zkID and anonynous credential suggest the scope is limited to one type of data -- ID, and only one ID.

I'm grateful to be invited to 0xPARC residency in 2024 and witnessed the birth of the ideas detailed in [this blog post](https://0xparc.org/blog/programmable-cryptography-1).

In the blog post we see two ideas defined:
- Universal Protocol:
- Universal Cryptographic Adapters:
- pod https://pod.org/

![](https://0xparc.org/static/universal_adapter.png)
Universal Cryptographic Adapters. Source: [0xparc blog](https://0xparc.org/blog/programmable-cryptography-1)

In the diagram, we see an universal cryptographic adapters takes three sources of inputs from the left, digitally signed data from the IRS, signed data from your bank, and a state proof from the Ethereum blockchain. On the right, an aggregated claim that this person has a financial score 96.

- Universal Protocol
- Naming the tools but not the application. 0xparc has this humility to avoid the later. We are early in the internet and could not predict the TikTok.
  - pattern: programmable but not software


- [zkemail](https://zk.email/)
  - [zkp2p](https://www.zkp2p.xyz/)
  - Account recovery
- [zkpdf](https://pse.dev/blog/zkpdf-unlocking-verifiable-data)
- [tlsnotary](https://tlsnotary.org/) / [zk tls](https://github.com/the3cloud/zktls)


offensive defensive


zk wrapped ID https://vitalik.eth.limo/general/2025/06/28/zkid.html