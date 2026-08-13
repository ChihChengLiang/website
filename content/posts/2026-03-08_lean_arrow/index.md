---
title: "Writing Arrow's Impossibility Theorem in Lean"
date: 2026-03-08T21:45:15+08:00
draft: false
---

{{< translation type="machine" from="Chinese" />}}

Last time I talked about learning to write math proofs in the Lean 4 language.

The game website the developers built is a lot of fun, and I really wanted to finish every topic in it.

But I felt like it was time to try something a bit more real.

A game is carefully designed so the difficulty ramps up gradually, keeping players hooked without letting them give up. A real project can slap you in the face with reality — you get a better feel for what challenges you'll actually run into using this language.

I wanted to pick something with a bit of difficulty, but not too much, to try proving. The task: turn a formula on paper into Lean 4 code.

I ended up picking "Arrow's Impossibility Theorem." It's a theorem every economics textbook mentions, and quite a few popular-science channels have covered it too.

I found a 2012 paper ([Yu 2012](https://sites.math.rutgers.edu/~zeilberg/EM22/yu2012.pdf)) — short, with a proof that's only a page long. Very self-contained.

Nothing could go wrong, right?

## About Arrow's Impossibility Theorem

Kenneth Arrow proved: it's impossible to design an ideal voting mechanism that rationally reflects voters' preferences.

You can think of a voting mechanism as a machine: the input is everyone's preference ordering over the options, written on their ballots. The output is some kind of social preference — as if society itself were a single person with its own preference ordering over the options.

Once the ballot box swallows the ballots, people open it up, run some algorithm to crunch through them (e.g. counting who got the most votes), and arrive at society's consensus — say, which candidate voters like best.

Suppose your ballot lets you write down not just your favorite, but your second favorite, all the way down to your least favorite. It also lets you mark some options as tied. Can you design an algorithm that takes everyone's ballot information and produces a decent social preference?

First we need to define what "decent" even means.

Arrow laid out three very basic requirements for such a voting mechanism:

First, the mechanism should respect voters' **unanimity**: if every voter prefers option A over option B, then the social preference the mechanism produces should also prefer A over B.

Next, **Independence of Irrelevant Alternatives**: if the ballot box produces a result where A is preferred to B, and you then dump all the ballots back out, keeping everyone's relative ranking of A and B exactly the same but shuffling around where option C sits on each ballot — where C is an option unrelated to A and B — the outcome for A versus B shouldn't change.

Finally, **no dictator**. No single voter should be so "special" that the outcome always just matches whatever that voter's preference happens to be.

Sadly, Arrow proved that these three innocuous, basic requirements can't all be satisfied at once.

The overall shape of the proof: assume a voting mechanism satisfies both "respects unanimity" and "independence of irrelevant alternatives." This leads to a conclusion — the mechanism must have a dictator who can single-handedly determine the outcome.

## The implementation process

Before starting, I had Claude take a look at the paper first. I told it to give me some pointers but not to write any code for me — the point of this project was to practice the language.

In the first few hours of day one, guided by the AI, I finished the three definitions: "respects unanimity," "independence of irrelevant alternatives," and "no dictator."

I felt super confident — I thought I might finish the whole project in a single day.

However...

By the time I'm writing this post, two painful weeks have gone by. Countless moments of wanting to give up, begging the AI to just write the whole thing for me. The little swimming rat in my head was already sinking underwater.

I could really relate to what middle school teachers describe — that helpless feeling of a student going in circles in front of an AI, saying "can you explain that more simply..."

Begging the AI didn't help either. On small problems — say, a well-defined lemma — the AI could brute-force out a pile of ugly code that actually completed the proof. But once the problem got bigger and more complex, the AI could still brute-force out a pile of ugly code — it just didn't prove anything.

In Lean, you can write out a lemma's statement and leave the proof part as a placeholder called `sorry`. Once the compiler sees `sorry`, it suppresses all the error messages but leaves a yellow warning, meaning some proof is still incomplete.

The AI would often flail around for a while, leave a pile of `sorry`s scattered through the code, and hand the mess back to me.

Its plain-language replies weren't nearly as apologetic. I learned to recognize the sentence where it started going in circles:
"But actually the cleanest approach..."
Whenever that sentence showed up, the problem was probably beyond its ability.

Let me mention which AIs I actually used. Mainly these three:
Sonnet 4.6: general-purpose brain matter — for everyday confusion, weird bugs, syntax questions, dumb questions, ask Sonnet.
Opus 4.6: premium brain matter, more expensive to run. For complex problems Sonnet can't handle, ask Opus.

Claude Code: for when I actually wanted the AI to do the implementation, or to debug. It can actually change code, run the compiler, and read the error messages. It also has a longer internal monologue.

## Where the difficulty came from

The difficulty seemed to come from two places: the subject matter, and the language.

First, Arrow's Impossibility Theorem — you can barely find a rigorous proof of it anywhere. Almost every paper or YouTube video "proving" or introducing it uses some kind of example and plain English description. Very few use heavily symbolic mathematical notation.

That's understandable — the point of knowing this theorem is usually to stop fantasizing about designing a perfect voting mechanism, or, if you insist on trying anyway, to know there's a mountain blocking the way so you don't waste effort going down dead ends.

Those mathematical details might get in the way of a high-level intuitive understanding, but they turn out to be extremely useful when you're trying to reconstruct the proof in code.

On the language side, early on I really struggled to tell apart what was the "computer" part and what was the "math" part.

The paper writes "Consider any preference profile... such that..." — I can't just "consider" it, I have to actually construct it. But should that construction be a computational example built the computer's way, or a mathematical set containing all such elements built the math way?

I tried both, painfully.
I learned about Decidability, noncomputable, and the axiom of choice — if you want to put some proposition into an if/else and check whether it's true or false, you have to assume there's some efficient algorithm that can decide it. These are all rabbit holes I still don't quite dare to look into.

On a computer, dealing with off-by-one counting issues like adding or subtracting one has lots of workarounds. Doing this in a math proof becomes a massive pain. You either have to assume some natural number isn't zero and then separately prove it's greater than zero, or you have to handle every possible "is it zero or not" case separately.

## The proof details

Various papers say there are two mainstream ways to prove Arrow's Impossibility Theorem, but I've almost never seen the other one covered in any textbook or video. So maybe it only really counts as one mainstream way.

The 2012 paper is a condensed, streamlined version of the mainstream approach.

Arrow's Impossibility Theorem has an assumption that there must be three or more options.

Suppose we number the voters. Every ballot in the box starts out preferring A over B, and then voters, one after another, flip their preference to like B more than A.

The "respects unanimity" principle says: at the start of this process, the social consensus is A over B. By the end, it's B over A. That's because at both of those two points in the process, every voter agrees.

And somewhere in the middle of this process, the social consensus on A vs. B must flip. There must be some critical voter — let's call him A-Ts'ai — such that before A-Ts'ai changes his ballot, the social consensus is still A over B; and right after A-Ts'ai changes it, the consensus flips to B over A.

The paper then pulls out two new sets of magic ballots, inserting an unrelated option C in the middle. After a magical sequence of operations, the paper states a lemma set apart in its own centered font, flagged with an invincibility star (*):

It turns out that A-Ts'ai, the critical voter for options A and B, can also control the outcome between options B and C.

After a bit more manipulation of this invincibility-star lemma, A-Ts'ai keeps gaining power, step by step, until: for any two arbitrary options X and Y, if A-Ts'ai prefers X over Y, the outcome is X over Y.

We discover that A-Ts'ai, the guy whose word freezes water, is actually the Dictator-Ts'ai.

## Getting stuck at the very end

I got seriously stuck with only two sentences of the paper left.

The first sentence says that some result related to B and C generalizes "easily" to any arbitrary options X and Y. I never quite grasped what made that step "easy," and even my premium brain matter, Opus, couldn't figure it out either.

What I finally ended up with required splitting into 13 separate cases, about 80 lines of code. I have no idea whether that matches anyone's definition of "easily."

Lean 4 has a really cool `wlog` (without loss of generality) tactic. Say you want to prove that for `x y : ℕ` with `x ≠ y`, `min x y ≠ max x y`. Without special handling, you'd need to prove it separately for x and for y, the same way, twice. But "without loss of generality" lets you swap the x and y arguments and reuse the conclusion you already proved once, so you don't have to prove it twice.

Unfortunately, I wasn't sharp enough to spot any "generality" I could exploit across those 13 cases.

## AI rescue, successfully

But when I asked my premium brain matter one question, it came through with a huge assist. I asked: we're stuck on this proof — did I do something wrong earlier? Or is there anything I could do now that would make our lives easier?

It said my critical voter's index was being obtained through an "existence" proof. Because of that, this variable and its associated properties (that this voter controls the social consensus) couldn't be shared across other lemmas. I should instead define the critical voter's index using Mathlib's `Fin.Find` API, making it a proper "definitional" object — that way every lemma could reference the exact same variable.

This change took a day to carry through, and the effect was dramatic. Before, the crucial invincibility-star lemma later on needed a pile of miscellaneous variables and conditions every time it was cited.

After turning the critical voter into a definition, every important lemma only needed a handful of assumptions: three options A, B, C, all pairwise distinct (A ≠ B ≠ C), "respects unanimity," and "independence of irrelevant alternatives."

Once I made this change, the rest of the proof opened right up. And it became clear that the whole proof is really just about manipulating three distinct options, across different arrangements, to satisfy "respects unanimity" and "independence of irrelevant alternatives" simultaneously — and in the process, we successfully crown A-Ts'ai as dictator.

## Gaps left uncovered

The compiler checks whether every step of every proof is correct.

Any lemma or theorem with a completed proof gets a blue checkmark in the VSCode editor's margin.

Once the proof is done, pushing to GitHub gets you a green checkmark from CI too.

But as another paper on formal verification pointed out: after all this flailing around, did what I actually proved turn out to be Arrow's Impossibility Theorem?

How do I know that the problem statement I wrote is actually the same as the one in the paper?

Taken to the extreme, I could just as easily prove that 1+1=2, then claim that's Arrow's theorem, and still collect every checkmark the machinery has to offer.

Maybe I set some condition too loosely? Maybe what I proved just looks like Arrow's theorem without actually being it?

There is, in fact, a bit of technical debt I haven't paid off. The mathematical order structure I used isn't the same as economic preference. So the "weak preference" used in the paper isn't actually reflected in my code.

But I'm honestly glad I let this debt slide — if I'd insisted on faithfully handling weak preference from the start, I doubt I'd have finished this project at all.

There is one upside I noticed here: once a proof becomes code, you can actually see how properties depend on each other. For example, my order structure accidentally had an "antisymmetric relation" property it shouldn't have had; once I removed it, I could trace exactly where the error propagated to and which downstream conclusions broke.

## Conclusion

Did I come away with any deep insight into democracy from working through one of the most important mathematical results about voting?

Absolutely none!

I just came away thinking formal verification is grunt work. If you can get the AI to do it, let the AI do it. Humans shouldn't have to suffer through this.

Finished project: https://github.com/ChihChengLiang/arrow

Feedback and corrections welcome.

And if you've got AI credits to burn, I'd love to hear roughly how long it takes an AI to build this project from scratch.
