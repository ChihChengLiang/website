---
title: "What Do We Really Want From Open Source AI?"
date: 2025-02-10T17:04:18+08:00
draft: false
---

Recently, the release of Deepseek sparked a global discussion. It was released under an MIT license, which excited open source builders like me.

However, people also questioned the license and whether Deepseek is truly an open source project. After all, the so-called open-washing, the behavior of making a product look open-sourced but in fact is not, is too common, making people skeptical of new projects. Here are some precedents. OpenAI, the company behind ChatGPT, is ironically not "open" despite its name suggesting otherwise. Llama, released by Meta under a customized LLaMA license, which forbids commercial use (i.e., a 'research-only' restriction), is also considered not truly open-sourced.

People cite the newly defined OSI AI definition as a checklist to determine if an AI project is considered open source. This includes releasing the model weights, source code for training the model, and input parameters for the training code. The intention here is to let users reproduce the training process to obtain the same weights. However, the training data is not required to be released due to privacy and security concerns. OSI has been known for its focus on practicality.

All of these make me wonder, what makes a project open-sourced? Why do we want that? Is the OSI AI definition enough?

In 2013, I took my first Machine Learning class, instructed by Andrew Ng, on Coursera. Like other statistical fields—economics, management, psychology, or engineering—machine learning involves building models to describe data or make predictions. Yet it stands out by **creating a program automatically from data, rather than having every instruction written by hand.**

Now fast forward to 10 years later. Machine learning is no longer focusing on specific tasks like telling apples from oranges and cats from dogs. Nowadays, it is general-purpose and does everything. I've been practicing programming for almost 10 years. Nowadays, I tell GPT what I want to write, and then it spits out the code, and I decide whether to apply it. We'll soon see what Andrej Karpathy called [vibe coding](https://x.com/karpathy/status/1886192184808149383), where you just accept everything and leave it to AI to do the rest.

The point here is that the AI model we're using is a new breed of software. It takes some inputs and produces some outputs, but the behavior is no longer specified in readable English, like traditional software. So do the concepts derived from the 1980s, both free software and open source, still make sense in this new scene?

---

The lesson from "The twenty-six words that changed the internet" and the story of Section 230 is that our fancy new technology is actually under the ruling of ancient legal concepts. Let's trace the origin of the free software and open source movement.

The two movements were initiated in the 1980s when people used computers very differently from today.

In the past, people used software locally. Today, people mostly use software that interacts with servers. Software as a Service, or SaaS, is the term for that.

In this post, I wanted to explore the origin of the two movements and see what software use cases motivated them. I then look for their latest takes on AI projects. I'm also interested in their responses to all the computer histories like the Internet, SaaS, hardware, cryptography, etc. But those will be topics for future research.

## The Response from the Free Software Camp

### Complaint to Unix System

The story starts with the Unix system in 1969. Bell Labs from AT&T developed it. But then, under an antitrust lawsuit, AT&T was not allowed to operate a computer business. As a result, Bell Labs licensed Unix to academic and research institutions, which created a culture of sharing the Unix source among universities.

The Unix system gained popularity. Researchers started to use it. But then in 1984, AT&T divested Bell Labs. Bell Labs now had no restriction to operate a computer business. Bell Labs started to sell Unix as a for-profit product. Users were not allowed to modify the code.

In response, Richard Stallman tried to re-create a stack of software, the GNU project, in 1983. The GNU project contains an editor GNU EMACs, the GNU Debugger, and a GNU C compiler.

In 1986, the first version of software freedom was published [^freedom]. The modern version of freedom, which adds freedom 0 as a more fundamental one, is defined as follows: [^modern_freedom]

> - The freedom to run the program as you wish, for any purpose (freedom 0).
> - The freedom to study how the program works, and change it so it does your computing as you wish (freedom 1). Access to the source code is a precondition for this.
> - The freedom to redistribute copies so you can help others (freedom 2).
> - The freedom to distribute copies of your modified versions to others (freedom 3). By doing this you can give the whole community a chance to benefit from your changes. Access to the source code is a precondition for this.

To summarize, you should be able to run, study, modify, and share the code.

### Rationales Behind the Freedoms

The movement was motivated by the legal and business environment of AT&T, causing the enterprise to hold the power to make your life as a software user and developer miserable. [^life_and_death]

I tried to dig deeper into the rationales behind the 4 freedoms. [^means_ends] Let's say:

#### Solidarity of Users Reason

The GNU Manifesto says [^manifesto]:

> I consider that the Golden Rule requires that if I like a program I must share it with other people who like it. Software sellers want to divide the users and conquer them, making each user agree not to share with others. I refuse to break solidarity with other users in this way. I cannot in good conscience sign a nondisclosure agreement or a software license agreement.

Furthermore, the Free Software Foundation (FSF) 20-year review elaborates more:

> Nonfree software carries with it an antisocial system that prohibits cooperation and community. You are typically unable to see the source code; you cannot tell what nasty tricks, or what foolish bugs, it might contain. If you don't like it, you are helpless to change it. Worst of all, you are forbidden to share it with anyone else. To prohibit sharing software is to cut the bonds of society.
[^fsf_20yrs]

#### Security Reasons

From the quote above, we see the security concerns for nasty tricks and bugs in the program.

I think the most interesting aspect is the public good. I couldn't find a discussion framing software as goods of non-rivalrousness and non-exclusiveness. The GNU Manifesto [^manifesto] discusses extensively the economic aspect of software development, like "Won't programmers starve?" or "Shouldn't a programmer be able to ask for a reward for his creativity?". Most of the answers didn't cite economic dilemmas but instead said the programmers would contribute in their leisure time and be rewarded with social contribution.

### What is the Free Software Movement About?

The software back then and most of the software today do not work too differently. We have human-readable source code, which gets compiled into unreadable executables, then run by machines.

Note that for all these to work, we need open-sourced compilers and operating systems. (TODO: What about hardware?)

A nasty compiler and a nasty operating system can block unauthorized code. I can see why Richard Stallman built the GNU project as the first step to counter the Unix situation. Although the vision of having a free operating system was first completed by Linux, which was built by Linus Torvalds in the 1990s.

## Open Source Camps

In 1997, Eric Raymond published "The Cathedral and the Bazaar."
In 1998, inspired by the writing, the Netscape browser source code was released. Raymond considered the Netscape action a great chance to convince the business world to release their source code.

In a meeting in 1998, a group of people decided to rebrand free software as "open source" for the corporate world to adopt it. [^os_history] They modified the Debian Free Software Guidelines as open source definitions and founded the Open Source Initiative.

The open source definition has 10 points. [^osd] I don't intend to go into details. Unlike the software freedom definitions, which focus on what users can do with the software, the open source definition only qualifies what properties a license should satisfy.

The rationales of the 10 points, as the annotated version shows, are mostly defenses against open washing and ill-licensing tricks. The OSI-AI page [^osi_ai] cites the freedom to run, study, modify, and share.

So in the philosophical root, the open source movement is still free software but more means to ends. But let's say the pre-2000 era, the main goal was to let more businesses release their source code in a friendly way. Also, for businesses, they want to get the benefit of "more eyeballs and fewer bugs."

Now that we've seen how free software and open source principles took shape under very different computing conditions, let's see why these old frameworks hit roadblocks when applied to AI models.

## Free Software Foundation's Take on AI

In October 2024, the Free Software Foundation released a post on their viewpoint of AI. [^fsf_ai]

It recognizes the difficulty of treating machine learning models like traditional software. "Machine learning applications are only partially software," it says.

"The model parameters are not comprehensible as such by humans, so it is not practical to study or adapt an ML application by analyzing or editing model parameters directly."

But it is the training data that creates a dilemma for the FSF. For a long time, nonfree equals unjust because users' freedom to control their own computing is deprived.

Now AI has created a case to justify nonfree. If an AI is trained on private medical data, it is hard to call it free because you cannot retrain and reproduce the weights. But if you use such a nonfree model to diagnose a disease, then it might be ethical.

## Open Source Initiative's Take on AI

Released in October 2024, similar to the release of FSF's post, OSI also released an open source AI definition. [^osi_ai] [^osi_ai_news]

It cites the four freedoms. To qualify as open source AI share the follows:

1. Model weights
2. Data information of the training data
3. Source code to train and run the model.

A FAQ explains the decision to exclude opening the training data. [^osi_ai_faq] There are cases of definitely not sharable data like medical data, legally trainable but not sharable like copyrighted data. Even the most sharable data like open data and public domain data could have edge cases like countries having different definitions of them.

The FAQ also mentioned the OSI AI definition does not address ethical issues. It points the ethical and trustworthy issues to a separate OECD document.

## Why the 1980s Freedoms Struggle to Apply to AI

We've seen how the FSF defines freedom and the OSI focuses on licensing practicality. However, AI—especially large models—presents new obstacles that these older frameworks didn't anticipate.

### The Cost of Computation

A key shift is that the "cost" of freedom has changed. In traditional software, freedoms were relatively cheap to exercise, with legal barriers (e.g., closed source) being the main hurdle. Both the FSF and OSI therefore placed much emphasis on licensing and legal issues.

In contrast, AI can be computationally expensive. Advanced LLMs run on powerful servers, making it costly to exercise the freedom to run them. Training can also require millions of dollars, so the freedom to modify or reproduce a model can feel like a luxury. That said, the rise of smaller, more efficient models could make these freedoms more practical in the future.

### The Cost of Comprehension

Because an AI model's behavior is defined by a blob of weights, "Freedom 1" (the freedom to study how the program works) becomes more complicated. If we treat source code as the human-readable form needed for modifications, then model weights—like binary executables—arguably don't qualify.

Of course, those weights are what reproduce the AI's logic, and we do have interpretability techniques that can shed light on a model's inner workings. However, these techniques don't match the transparency offered by traditional software source code. In other words, we might have to relax or partially forgo "Freedom 1." [^io]

"Changing the program" also works differently in AI. For example, some people try to alter DeepSeek's default pro-China stance so it recognizes Taiwan as a country. They can do this through prompt engineering, model fine-tuning, or other creative hacks. Audrey Tang famously demonstrated a "hijack" in the chain-of-thought process to extract an honest historical account from DeepSeek. [^au_ds] Prompt engineering and Audrey's trick function more like "tweaking parameters" than editing code, whereas fine-tuning is a closer analogue to a real software modification.

Finally, the clause "does your computing as you wish" can be a monkey's paw—even in traditional software. From smart contract security work, we know that having human-readable source code doesn't guarantee it reflects human intent. [^value_complexity] While source code is more transparent than binary, it's not 100%. Perhaps this realization nudges us toward incremental improvements in AI transparency rather than expecting complete control.

### The Cost of Conscience

Software freedom was originally defined to be value-neutral. It doesn't address whether software is used for good or evil. Likewise, the OSI definition contains "No Discrimination Against Persons or Groups" and "No Discrimination Against Fields of Endeavor."

This philosophy has sometimes conflicted with attempts at imposing moral clauses. For instance, the JSON license famously stated "The software shall be used for Good, not Evil," which the FSF deemed non-free. [^fsf_json] [^evil] In practice, requiring users to consider ethical implications can become a significant legal hurdle.

Historically, this was straightforward: freedom was prioritized over morality. But as AI becomes more advanced—potentially facilitating weapons development—people may feel compelled to put ethical concerns above unqualified freedom. The Manhattan Project provides a precedent: scientists voluntarily stopped publishing research to avoid helping enemy forces.

In an extreme scenario, the survival of humanity itself could supersede both software freedom and commercial interests.

## Conclusion

AI has changed the nature of software, particularly when it comes to source code. Potential paths forward include:

1. **Adapting the technology** so it fits the original freedoms set out in the 1980s.
2. **Revising or extending the freedoms** to accommodate newer AI paradigms.
3. **Combining both approaches** in a way that balances openness, practicality, and ethical considerations.

[^freedom]: https://www.gnu.org/bulletins/bull1.txt
[^modern_freedom]: https://www.gnu.org/philosophy/free-sw.en.html
[^life_and_death]: As a friend of mine commented vividly, it's the life and death control [生殺与奪の権利](https://ja.wikipedia.org/wiki/%E7%94%9F%E6%AE%BA%E4%B8%8E%E5%A5%AA%E3%81%AE%E6%A8%A9%E5%88%A9).
[^means_ends]: I remember a friend's discussion on "Why do we need decentralization?" If we double click a mean to get an end, and keep double clicking that end, what would we get? Eventually, we should get something that is both a mean and an end. Does that motivate us not to double click on Decentralization and Software Freedoms?
[^manifesto]: https://www.gnu.org/gnu/manifesto.html
[^fsf_20yrs]: https://www.gnu.org/philosophy/use-free-software.html
[^fsf_ai]: https://www.fsf.org/news/fsf-is-working-on-freedom-in-machine-learning-applications
[^os_history]: https://web.archive.org/web/20021001164015/http://www.opensource.org/docs/history.php
[^osd]: https://opensource.org/definition-annotated
[^osi_ai]: https://opensource.org/ai
[^osi_ai_news]: https://opensource.org/blog/the-open-source-initiative-announces-the-release-of-the-industrys-first-open-source-ai-definition
[^osi_ai_faq]: https://hackmd.io/@opensourceinitiative/osaid-faq#Why-do-you-allow-the-exclusion-of-some-training-data
[^io]: [IO](https://en.wikipedia.org/wiki/Indistinguishability_obfuscation) is not there yet to completely disrupt this whole discussion.
[^evil]: https://web.archive.org/web/20170608034900/http://dev.hasenj.org/post/3272592502/ibm-and-its-minions
[^fsf_json]: https://www.gnu.org/licenses/license-list.html#JSON
[^au_ds]: https://x.com/NOTonlywater/status/1884262704149586000/photo/3
[^value_complexity]: https://blog.ethereum.org/2016/06/19/thinking-smart-contract-security
