---
title: "What Do We Really Want From Open Source AI?"
date: 2025-02-10T17:04:18+08:00
draft: false
---

Recently, the release of Deepseek sparked a discussion in the whole world. Especially, it was released under a MIT license, which excited open source builders like me.

However, people also questions the license, and whether Deepseek is really an open source project. Afterall, the so-called open-washing, the behavior of making a product looks like open sourced but in fact the otherwise, is too common so people became skeptical on new projects. Here are some precedences. OpenAI, the company behind ChatGPT, is ironically not "open" despite of its name sugguests. Llama, released by Meta under a customized meta license, which imposed certain restrictions on profiting with the model, is also considered not true open sourced.

People cite the newly defined OSI AI defintion as a checklist to determine if an AI project is considered open source. This includes releasing the model weights, source code for training the model, and input parameters for the traning code. The intention here is to let the users to reproduce the training process to obtain the same weights. However, the training data is not required to be released, due to the privacy and security concerns. OSI has been known for its focus on practicality.

All of these make me wonder, what makes a project open sourced? Why do we want that? Is the OSI AI defintion enough?

I remembered in 2013, I was excited by the beginning of MOOC. Lots of high-quality courses from the prestigious universities, just released for free. Andrew Ng, the founder of Coursera, instructed a Machine learning course. He proposed that GPU would be the future of machine learning. I also heard the term "Deep Learning" first time.

I was a new graduate of Finance major back then. I've explored different domain of statistics courses like economics, managements, psychology, and electrical engineering. Most of them build models to describe the data or draw smart conclusion from data. Machine learning is not too much different from that way in terms of predicting things from data. But it stands out from them with one idea, creating a program without manually writing it.

Now fastforward to 10 years later. Machine learning is no longer focusing on specific tasks like telling apple from oranges, and cats from dogs. Nowadays it is general purpose and it does everything. I've been practicing programming for almost 10 years. Nowadays I tell GPT what I want to write and then it spit out the code and I decide whether to apply. We'll soon see what Andrej Karpathy called the [vibe coding](https://x.com/karpathy/status/1886192184808149383), which you just accept everything and omakase to AI to do the rest.

The point here is that the AI model we're using is a new breed of software. It takes some inputs and spits some outputs, but the behavior is no longer specified in the readable english, like the software in the traditional sense. So do the concepts derived from 1980s, both free software and open source, still make sense in the new scene?


---

The lesson from "The twenty-six words that changed the internet" and the story of Section 230 is that our fancy new technology is actually under the ruling of ancient legal concepts. Let's trace the origin of the free software and open source movement.

The two movements are initiated in 1980s, when people use computers very different from today.

In the past, people use the software locally. Today, people mostly use softwares that interact with servers, Software as a Service, or SaaS is the term for that.

In this post, I wanted to explore the origin of the two movements and see what was the software use cases that motivates them for the movements. I then look for their latest takes on AI projects. I'm also interested in their responses to all the computer histories like Internets, SaaS, hardwares, cryptographies, etc. But those will be topics for future researches.


## The response from Free software camp

### complaint to Unix system

The story starts from the Unix system in 1969. The Bell Labs from AT&T developed it. But then under the antitrust law suit, the AT&T is not allowed to operate computer business. As a result, Bell Labs released the source code of Unix. 

The Unix system gained popularity. Researchers started to use it. But then in 1894, AT&T divest Bell Labs. The Bell Labs now has no restriction to operate a computer business. The Bell Labs start to sell Unix as for profit products. The users are not allowed to modify the code.

In response, Richard Stallman tried to re-create a stack of software, the GNU project in 1983. The GNU project contains an editor GNU EMACs, the GNU Debugger, and a GNU C compiler.

In 1986, the first version of software freedom is published [^freedom]. The modern version of freedom, which adds freedom 0 as a more fundamental one, is defined as follows: [^modern_freedom]

> - The freedom to run the program as you wish, for any purpose (freedom 0).
> - The freedom to study how the program works, and change it so it does your computing as you wish (freedom 1). Access to the source code is a precondition for this.
> - The freedom to redistribute copies so you can help others (freedom 2).
> - The freedom to distribute copies of your modified versions to others (freedom 3). By doing this you can give the whole community a chance to benefit from your changes. Access to the source code is a precondition for this.

To summarize, you should be able to run, study, modify, and share the code.

### Rationales behind the freedoms

The movement was motivated by the legal and business environment of AT&T, causing the enterprise to hold the power to make your life as software user and developer miserable. [^life_and_death]

I've tried to dig deeper rationales behind the 4 freedoms. Lets say:

#### Solidarity of users reason

The GNU Manifesto says [^manifesto]

> I consider that the Golden Rule requires that if I like a program I must share it with other people who like it. Software sellers want to divide the users and conquer them, making each user agree not to share with others. I refuse to break solidarity with other users in this way. I cannot in good conscience sign a nondisclosure agreement or a software license agreement.

"antisocial system that prohibits cooperation and community" [^fsf_20yrs]

#### Security reasons

The Free Software Foundation 20 years review [^fsf_20yrs] mentioned the software freedoms allow us to find nasty tricks or foolish bugs in the program.

I think the most interesting is the public good aspect. I couldn't find the discussion to frame software as goods of non-rivalrousness and non-exclusiveness. The GNU Manifesto [^manifesto] discuss extensively on the economic aspect of the software development like "Won't programmers starve?" or "Shouldn't a programmer be able to ask for a reward for his creativity?". Most of the answer didn't cite economic dilemma, but instead says the programmers would contribute in their lesure time and rewarded with social contribution.

### What is free software movement about?

The software back then and the most of the software today do not work too differently. We have a human readable source code, which got compiled into unreabable executables, then run by machines.

Note that the for all these to work, we need open sourced copmilers and operating systems. (TODO: What about hardwares?)

A nasty compiler and a nasty operating system can block unauthorized code. I can see why Richard Stallman builds GNU project as the first step to counter the Unix situation. Although the vision of having a free operating system, is first completed by Linux, which was built by Linus Torvalds in 1990s.

## Open source camps

1997, Eric Raymond published the "The Cathedral and the Bazaar."
1998, inspired by the writing, Netscape browser is released as a free software. Raymond considered the Netscape action is a great chance to convince the business world to release their source code.

In a meeting of 1998, the group of people decided to rebrand the free-software as "open source" for the coprate world to adopt it. [^os_history] They modified the Debian Free Software Guidelines as open source definitions and founded the open source initiative.

The open source definition has 10 points. [^osd] I don't intend to go into details. Unlike the Software freedom definitions, which focusing on what users can do with the software, the open source definition only qualify what properties of a license should satisfy.

The rationales of the 10 points, as the annotated version shows, are mostly defenses against open washing and ill-licensing tricks. The OSI-AI page [^osi_ai] cites the freedom of run, study, modify, and share.

So in the philosophical root, the open source movement is still free software but more means to ends. But let's say the pre-2000 era, the main goal is to let more business release their source code in a friendly way. Also, for business, they want to get the benefit of "more eye balls and less bugs."

## Free Software Foundation's take on AI

In October 2024, Free Software Foundation released a post on their view point of AI. [^fsf_ai]

It recognizes the difficulty to treat machine learning model like the good old software. "Machine learning applications are only partially software," it says. 

"The model parameters are not comprehensible as such by humans, so it is not practical to study or adapt an ML application by analyzing or editing model parameters directly."

It also requires the training data to be released to be qualified as libre.

It further acknowledged that freedom may not equal to justice.

> FSF considers all nonfree software to be unjust to its users because it denies them the freedom to control their own computing. A further question is whether all nonfree ML applications are ethically unjust. It may be that some nonfree ML have valid moral reasons for not releasing training data, such as personal medical data. In that case, we would describe the application as a whole as nonfree. But using it could be ethically excusable if it helps you do a specialized job that is vital for society, such as diagnosing disease or injury. For the FSF to consider usage of such a nonfree ML application to be just, its component software must be free, and the ML application as a whole would have to be distributed to users in a form and manner that reasonably and flexibly supports incremental training, or retraining differently from scratch, or both.

## Open source Initiative's take on AI

Released October 2024, similar to the release of FSF's post, OSI also released an open source AI definition. [^osi_ai]

It cites the four freedoms. To qualify for open sourced AI, share Data Information of the training data, source code to train and run, and model weights. 

A FAQ explains the decision to exclude opening the training data. [^osi_ai_faq] There are cases of definitly not sharable data like Medical data, legally trainable but not sharable like copy-righted data. Even the most sharable data like open data and public domain data could have edge cases like countries have different definitions on them.

The FAQ also mentioned the OSI AI definition does not care about ethical issues. It points the ethical and trustworthy issue to a separate OECD document.

## Why do we want freedom?


- Developement
- Justice
- Geopolitics



[^freedom]:https://www.gnu.org/bulletins/bull1.txt
[^modern_freedom]:https://www.gnu.org/philosophy/free-sw.en.html
[^life_and_death]: As a friend of mine commented vividly, it's the life and death control [生殺与奪の権利](https://ja.wikipedia.org/wiki/%E7%94%9F%E6%AE%BA%E4%B8%8E%E5%A5%AA%E3%81%AE%E6%A8%A9%E5%88%A9).
[^manifesto]:https://www.gnu.org/gnu/manifesto.html
[^fsf_20yrs]: https://www.gnu.org/philosophy/use-free-software.html
[^fsf_ai]: https://www.fsf.org/news/fsf-is-working-on-freedom-in-machine-learning-applications
[^os_history]:https://web.archive.org/web/20021001164015/http://www.opensource.org/docs/history.php
[^osd]:https://opensource.org/definition-annotated
[^osi_ai]: https://opensource.org/ai
[^osi_ai_faq]:https://hackmd.io/@opensourceinitiative/osaid-faq#Why-do-you-allow-the-exclusion-of-some-training-data
