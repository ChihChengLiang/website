---
title: "What Do We Really Want From Open Source AI?"
date: 2025-02-10T17:04:18+08:00
draft: false
---

Recently, the release of Deepseek sparked a global discussion. It was released under an MIT license, which excited open source builders like me.

However, people also questioned the license and whether Deepseek is truly an open source project. After all, the so-called open-washing, the behavior of making a product look open-sourced but in fact is not, is too common, making people skeptical of new projects. Here are some precedents. OpenAI, the company behind ChatGPT, is ironically not "open" despite its name suggesting otherwise. Llama, released by Meta under a customized Meta license, which imposed certain restrictions on profiting with the model, is also considered not truly open-sourced.

People cite the newly defined OSI AI definition as a checklist to determine if an AI project is considered open source. This includes releasing the model weights, source code for training the model, and input parameters for the training code. The intention here is to let users reproduce the training process to obtain the same weights. However, the training data is not required to be released due to privacy and security concerns. OSI has been known for its focus on practicality.

All of these make me wonder, what makes a project open-sourced? Why do we want that? Is the OSI AI definition enough?

I remember in 2013, I was excited by the beginning of MOOC. Lots of high-quality courses from prestigious universities were released for free. Andrew Ng, the founder of Coursera, instructed a Machine Learning course. He proposed that GPU would be the future of machine learning. I also heard the term "Deep Learning" for the first time.

I was a new graduate with a Finance major back then. I explored different domains of statistics courses like economics, management, psychology, and electrical engineering. Most of them build models to describe the data or draw smart conclusions from data. Machine learning is not too different from that way in terms of predicting things from data. But it stands out with one idea, creating a program without manually writing it.

Now fast forward to 10 years later. Machine learning is no longer focusing on specific tasks like telling apples from oranges and cats from dogs. Nowadays, it is general-purpose and does everything. I've been practicing programming for almost 10 years. Nowadays, I tell GPT what I want to write, and then it spits out the code, and I decide whether to apply it. We'll soon see what Andrej Karpathy called [vibe coding](https://x.com/karpathy/status/1886192184808149383), where you just accept everything and leave it to AI to do the rest.

The point here is that the AI model we're using is a new breed of software. It takes some inputs and produces some outputs, but the behavior is no longer specified in readable English, like traditional software. So do the concepts derived from the 1980s, both free software and open source, still make sense in this new scene?

---

The lesson from "The twenty-six words that changed the internet" and the story of Section 230 is that our fancy new technology is actually under the ruling of ancient legal concepts. Let's trace the origin of the free software and open source movement.

The two movements were initiated in the 1980s when people used computers very differently from today.

In the past, people used software locally. Today, people mostly use software that interacts with servers. Software as a Service, or SaaS, is the term for that.

In this post, I wanted to explore the origin of the two movements and see what software use cases motivated them. I then look for their latest takes on AI projects. I'm also interested in their responses to all the computer histories like the Internet, SaaS, hardware, cryptography, etc. But those will be topics for future research.

## The Response from the Free Software Camp

### Complaint to Unix System

The story starts with the Unix system in 1969. Bell Labs from AT&T developed it. But then, under an antitrust lawsuit, AT&T was not allowed to operate a computer business. As a result, Bell Labs released the source code of Unix.

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

I've tried to dig deeper into the rationales behind the 4 freedoms. Let's say:

#### Solidarity of Users Reason

The GNU Manifesto says [^manifesto]

> I consider that the Golden Rule requires that if I like a program I must share it with other people who like it. Software sellers want to divide the users and conquer them, making each user agree not to share with others. I refuse to break solidarity with other users in this way. I cannot in good conscience sign a nondisclosure agreement or a software license agreement.

"antisocial system that prohibits cooperation and community" [^fsf_20yrs]

#### Security Reasons

The Free Software Foundation 20 years review [^fsf_20yrs] mentioned that software freedoms allow us to find nasty tricks or foolish bugs in the program.

I think the most interesting is the public good aspect. I couldn't find the discussion to frame software as goods of non-rivalrousness and non-exclusiveness. The GNU Manifesto [^manifesto] discusses extensively the economic aspect of software development like "Won't programmers starve?" or "Shouldn't a programmer be able to ask for a reward for his creativity?". Most of the answers didn't cite economic dilemmas but instead said the programmers would contribute in their leisure time and be rewarded with social contribution.

### What is the Free Software Movement About?

The software back then and most of the software today do not work too differently. We have human-readable source code, which gets compiled into unreadable executables, then run by machines.

Note that for all these to work, we need open-sourced compilers and operating systems. (TODO: What about hardware?)

A nasty compiler and a nasty operating system can block unauthorized code. I can see why Richard Stallman built the GNU project as the first step to counter the Unix situation. Although the vision of having a free operating system was first completed by Linux, which was built by Linus Torvalds in the 1990s.

## Open Source Camps

In 1997, Eric Raymond published "The Cathedral and the Bazaar."
In 1998, inspired by the writing, the Netscape browser was released as free software. Raymond considered the Netscape action a great chance to convince the business world to release their source code.

In a meeting in 1998, a group of people decided to rebrand free software as "open source" for the corporate world to adopt it. [^os_history] They modified the Debian Free Software Guidelines as open source definitions and founded the Open Source Initiative.

The open source definition has 10 points. [^osd] I don't intend to go into details. Unlike the software freedom definitions, which focus on what users can do with the software, the open source definition only qualifies what properties a license should satisfy.

The rationales of the 10 points, as the annotated version shows, are mostly defenses against open washing and ill-licensing tricks. The OSI-AI page [^osi_ai] cites the freedom to run, study, modify, and share.

So in the philosophical root, the open source movement is still free software but more means to ends. But let's say the pre-2000 era, the main goal was to let more businesses release their source code in a friendly way. Also, for businesses, they want to get the benefit of "more eyeballs and fewer bugs."

## Free Software Foundation's Take on AI

In October 2024, Free Software Foundation released a post on their view point of AI. [^fsf_ai]

It recognizes the difficulty of treating machine learning models like traditional software. "Machine learning applications are only partially software," it says.

"The model parameters are not comprehensible as such by humans, so it is not practical to study or adapt an ML application by analyzing or editing model parameters directly."

It also requires the training data to be released to be qualified as libre.

It further acknowledges that freedom may not equal justice.

> FSF considers all nonfree software to be unjust to its users because it denies them the freedom to control their own computing. A further question is whether all nonfree ML applications are ethically unjust. It may be that some nonfree ML have valid moral reasons for not releasing training data, such as personal medical data. In that case, we would describe the application as a whole as nonfree. But using it could be ethically excusable if it helps you do a specialized job that is vital for society, such as diagnosing disease or injury. For the FSF to consider usage of such a nonfree ML application to be just, its component software must be free, and the ML application as a whole would have to be distributed to users in a form and manner that reasonably and flexibly supports incremental training, or retraining differently from scratch, or both.

## Open Source Initiative's Take on AI

Released in October 2024, similar to the release of FSF's post, OSI also released an open source AI definition. [^osi_ai]

It cites the four freedoms. To qualify as open source AI, share data information of the training data, source code to train and run, and model weights.

A FAQ explains the decision to exclude opening the training data. [^osi_ai_faq] There are cases of definitely not sharable data like medical data, legally trainable but not sharable like copyrighted data. Even the most sharable data like open data and public domain data could have edge cases like countries having different definitions of them.

The FAQ also mentioned the OSI AI definition does not address ethical issues. It points the ethical and trustworthy issues to a separate OECD document.

## Why Do We Want Freedom?

- Development
- Justice
- Geopolitics

[^freedom]: https://www.gnu.org/bulletins/bull1.txt
[^modern_freedom]: https://www.gnu.org/philosophy/free-sw.en.html
[^life_and_death]: As a friend of mine commented vividly, it's the life and death control [生殺与奪の権利](https://ja.wikipedia.org/wiki/%E7%94%9F%E6%AE%BA%E4%B8%8E%E5%A5%AA%E3%81%AE%E6%A8%A9%E5%88%A9).
[^manifesto]: https://www.gnu.org/gnu/manifesto.html
[^fsf_20yrs]: https://www.gnu.org/philosophy/use-free-software.html
[^fsf_ai]: https://www.fsf.org/news/fsf-is-working-on-freedom-in-machine-learning-applications
[^os_history]: https://web.archive.org/web/20021001164015/http://www.opensource.org/docs/history.php
[^osd]: https://opensource.org/definition-annotated
[^osi_ai]: https://opensource.org/ai
[^osi_ai_faq]: https://hackmd.io/@opensourceinitiative/osaid-faq#Why-do-you-allow-the-exclusion-of-some-training-data
