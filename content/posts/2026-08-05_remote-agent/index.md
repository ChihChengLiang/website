---
title: "My AI Experience, August 2026"
date: 2026-08-05T23:47:40+08:00
draft: false
---

{{< translation type="machine" from="Chinese" />}}

I've deliberately kept some distance from AI — not using the most powerful models or the latest tech. My expectation is that it won't be long before all of this becomes like the "basic attack magic" in *Frieren*: universal, unremarkable, everyday.

Because I never kept up, the gap that built up meant I ended up going through what felt like several months' worth of a technology upgrade all at once.

A personal web development and deployment need happened to come up right around this time.

My starting point: VSCode, with the Claude Code extension, model set to the plain, reliable Sonnet — not the smartest option, Opus or Fable.

I opened a folder, ran `git init`. I'd already gone back and forth on requirements with the web version, and had a single markdown spec doc revised. Handed it off in planning mode, divisions assigned, all forces advancing by land and sea.

This time I noticed Claude Code's memory has gotten a lot better — the tasks I handed off never collapsed mid-way. Looking at the dev logs, TODOs, and conventions it wrote, the wording was genuinely tight and precise. I was glad I'd never bothered learning all those elaborate prompt-engineering tricks or writing skill.md files — turns out I barely need any of that now anyway.

While it worked, I reviewed and approved commands as they came up, adding the common ones to an auto-approve list. Code edits were already on auto-approve from the start. Of course, that's easy to do because this was a brand-new project with nothing real riding on it — I could afford to let it run wild.

After Claude Code had been working for a while, it suddenly tried to run something like `chromium-cli`.

I coldly replied: "Sorry, I don't have chromium-cli installed."

Claude Code: "Oh, the webpage is done then, go ahead and check it."

I looked over the page, clicked around simulating a user's typical workflow, then went back and told it what needed fixing.

Suddenly it clicked for me.

Me: "Why do you need chromium-cli?"

Claude Code: "So I can write a script that automatically simulates user clicks, to check the implementation of the page."

That way I wouldn't have to manually check the page myself.

I immediately broke into a grin: "Ah, of course! I'll get chromium-cli set up for you right away! Anything else you need? Want a massage while I'm at it?"

In a separate web-version conversation, I learned that chromium-cli is last-generation Playwright-based tech. Now there's a browser MCP. The difference: the former requires the model to script out a whole sequence of actions before it can see the result; the latter maintains a "live" browser connection, so the model can decide its next move based on how the screen actually changes.

After some fumbling around, I got a Firefox MCP installed for Claude Code.

Now it can open a webpage in a browser just like I would, click buttons, and improve the code based on real-time feedback.

At this point, the whole setup started to feel a bit like calling a plumber or electrician to fix something at your house: we point out where the main power switch is, help open a few doors and windows, and leave the rest to the expert.

Once the webpage was mostly done, next came deploying it to some actual machine. I opened up the AWS console, which I hadn't touched in years, with a real sense of dread.

Amazon's console is like the Amazon jungle — there might be hundreds of services laid out in there, each with a pile of configuration and permissions to set. I'm terrified to touch any of it; every time I venture into that jungle, my human tokens burn out fast.

Thankfully AWS has an MCP too. After installing it and talking it over with Claude Code, it knew exactly what permissions to set, what instances to spin up, what firewall rules to configure.

As the human, my job was to set up a project-scoped account with permissions specific to this project — things like starting, stopping, and resizing EC2 instances — and periodically run the `aws login` command for it to log into that project account. That pops up a link, which I open in a browser, log in with my credentials, and paste back a verification code.

Spinning up machines and deploying turned into a tedious cycle of waiting and approving. I suddenly realized I'd been glued to my chair for an entire day, which felt more than a little pathetic.

That's when it hit me: it was time to move Claude Code out of my house. On my laptop, someone has to physically sit there and keep the screen unlocked for it to work. So I set it up with a cloud virtual machine (I call it "the little box") as its command center, letting it work around the clock.

Around this point I also discovered a remote-control command that lets me direct it remotely from my phone.

Up to this point, though, I was still basically that gif of someone slack-jawed, mashing the lever on a slot machine over and over — constantly approving whatever command Claude Code wanted to run next. Switching from laptop to phone for giving directions didn't really improve this workflow much.

![](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbjN1anVrYzlubjR5bXVycDhjeWdyM203dmY2eDdhOTFraGNrb3dqMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3GchqRqSKE14gDDxu0/giphy.gif)

If Claude Code left my laptop, I actually stopped worrying it might run some command that accidentally deleted something important. If it accidentally trashed the little box, I could just spin up a new one.

The next morning, I discovered the experimental `auto` command — commands get automatically approved directly, no more manual intervention needed.

Around this time I also noticed, to my surprise, that I'd basically forgotten "compact" was even a thing. In the past, as a work session dragged on, the model's performance would degrade, it would automatically run a context compact, and even after compacting, performance wasn't guaranteed to bounce back.

Looking closer now, compact still runs — it's just that after compacting, the model's performance actually does come back.

At this point I felt like I'd fully shed the engineer persona and become more of a demanding boss. A day later, I realized I could just hand off whatever requirement popped into my head, without needing to wait for it to finish the previous one first. It handled everything perfectly fine — nothing collapsed, nothing got dropped.

The only recurring hiccup: its AWS permissions would occasionally expire, requiring me to re-run `! aws login` on its little box. One time, my laptop's IP had changed, so the little box's firewall blocked my SSH connection, and I couldn't log into the box to run the command for it.

We went back and forth in circles a few times. I asked it to run the command and give me the login link, I'd give it back the verification code, we tried several times without success. It kept asking me to run `! aws login` again. I told it I literally couldn't SSH in — how was I supposed to run that command on your box? And since the command it gave me started with an exclamation mark, I briefly misread it as attached to the end of its previous sentence, making it sound like it was yelling at me. In reality, it stayed perfectly, professionally composed the whole time.

It reminded me of the [American Chopper chair-throwing meme](https://knowyourmeme.com/memes/american-chopper-argument).

Of course, the eventual fix was me remembering that a human could just go directly into the AWS console and update the firewall's allowed IP — and then I could SSH in successfully.

All in all, the development went smoothly, and I got the result I wanted in the end. At the start, I got a bit overconfident from AI's high-speed micro-execution and planned a larger scope than I should have. There were some detours in the middle — at one point I felt like AI had basically solved the hallucination problem, and at another point I felt like it had just stretched the hallucinations out longer instead. I'm still caught somewhere inside the illusion.

The one thing I still haven't worked up the nerve to try is voice mode. When typing, I can think something through before saying it; the few times I tried voice, I either stammered or just couldn't get any words out. Talking to a machine just feels awkward.

By the end, this whole style of development started to feel like playing a very long game of Dungeons & Dragons. The AI hands you a long reading-comprehension passage; some decisions get presented to you as dialogue options you can pick from, or you can just respond in your own open-ended way. No GM, no dice rolls — the ability checks are invisible. High stats let you dodge some landmines ahead of time; low stats mean you just have to take the damage in person.

My takeaway so far: if collaborating with AI gets stuck, and the root cause is me, then go improve and sharpen myself now. If the root cause is the AI and its tooling, then just lie down and wait for the people in California to keep working hard. Give it half a year and the problem usually disappears.

If a job would take two days to finish if you started today, but only one day if you started tomorrow — which day would you rather start?
