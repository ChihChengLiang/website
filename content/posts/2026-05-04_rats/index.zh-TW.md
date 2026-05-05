---
title: "老鼠之事 與鼠無關"
date: 2026-05-05T08:56:40+08:00
draft: false
---


台北現在老鼠的議題發酵中

我不是台北居民，這其實不關我的事

我沒有任何生態、公衛專業。這不是正經的公共議題討論。這篇想談的比較是數學建模的議題。

我們想用一些極端簡化的模型，討論一些嚇人的政策建議。如果這些建議聽起來有問題，是因為模型做的假設太單純？還是單純的是我們對現實的想像？

---

事情的起因是我聽到有種批評。台北市因應所謂「鼠害」，下了老鼠藥。猛禽協會指出，老鼠藥會造成反效果。

這是因為老鼠藥雖然殺死了老鼠，但也毒害了吃老鼠的老鷹。
老鼠在極短時間內可以大量繁殖。而老鷹生得少，要長大需要很長時間。

因此過一段時間後，生出來的老鼠沒有老鷹捕食去抑制數量。老鼠將到處橫行。

因為這是一個稍微複雜的動態和因果關係。我感到背後有些數學在運作。

另外，與老鼠藥相對的政策建議是「不讓鼠來、不讓鼠住、不讓鼠吃」。意圖是從源頭減少老鼠的數量。這會是比較好的做法嗎？

我問了 AI 這是可以數學算出來的嗎？

AI 端出了今天的主角： Lotka–Volterra 方程式

這方程式其實沒想像中可怕。讀者腦中數學 Token 夠的話不妨燒一下

dR/dt = r_b R - r_c R P

dP/dt = p_b RP - p_d P

其中 R 是老鼠的數量， P 是其獵食者的數量。
dR/dt 意思是明天老鼠數量的變化，dP/dt 是獵食者數量的變化。

明天老鼠的數量變化，會是新出生的老鼠減去被獵食者吃掉的老鼠。

新的老鼠是老鼠的出生率 rb 乘上現有幾隻老鼠。

老鼠有幾隻會被吃掉，要看今天上菜幾隻鼠條，以及有幾隻老鷹要服務。我們加個捕食率的參數，調整這個數量。捕食率可以詮釋為老鼠在路上逛來逛去，運氣有多差而被吃掉。

再來看明天老鷹數量的變化。老鷹的增長來自於食物是否充足，減少來自於自然死亡。

今天晚餐吃的老鼠，會變成孵寶貝的養分。食物來源充足的情況會生比較多老鷹。我們用 pb R P 表達。pb 可以看作出生率。

老鷹的自然死亡，用死亡率 pd 乘上老鷹數量表示。

我們用個實際的例子：

假設初始狀態有 40 隻老鼠 和 10 隻老鷹。

Todo: 完成例子

這個模型告訴我們的第一件事是捕食者與獵物的數量，會呈現週期性的變化。

Todo: add representative photo 

老鷹在食物充足的時候會數量增加，這導致老鼠被大量捕食而數量減少。老鼠的減少造成老鷹的食物變少，老鷹數量也會因此降下來。在老鷹數量降下來時，老鼠的捕食又變少了，因此老鼠的數量又回到一開始的水準。

因此我們在討論老鼠數量的時候，不應該假設他們是一個常數。老鼠的數量會波動。

模型告訴我們的第二件事，是這個模型有個老鼠數量與老鷹數量的均衡。雖然老鼠和老鷹的數量一直在波動，幾乎永遠不會停在均衡處。但均衡數量在這模型裡剛好等於一個週期的平均數量。這讓我們可以用均衡來討論政策建議。

註：模型加料就會壞掉。

在毫無人類干預之下，這個模型的均衡這樣解。

假設鷹鼠雙方的數量，剛好停在一個完全不會動的地方，明天的增減都是零。 dR/dt = 0 ，且 dP/dt = 0 。

這可以解

dR/dt = r_b R - r_c R P = 0
得 R = 0 或 P = rb /rc

dP/dt = p_b RP - p_d P = 0 
得 P = 0 或 R = pd /pb

這邊只有這兩個組合是合理的

(R, P) = (0, 0)

(R, P) = (pd/pb, rb/rc)

第一個均衡是老鼠老鷹全滅。老鼠一隻都沒有，所以也不會生新的老鼠。老鷹沒老鼠吃，所以也不會生出新的老鷹來。

這個均衡比較特別，也比較不實際。

第二個均衡則是正常狀況。

我的數學經驗學到的是，看到一坨 a b c d 的代數組在一起時，要看這個式子裡有哪些變數，而且更重要的是：**沒有哪些變數**

在這個均衡裡，老鼠的均衡數量，「完全是由老鷹的參數決定的！」裡面沒有任何老鼠的參數。所以讓老鼠生少一點，或容易被捕食之類的完全不會影響老鼠的數量。

老鼠的參數都影響到誰了？影響到了老鷹！

老鼠基本上就是老鷹的存糧。

老鷹生得少、死得快時，老鼠的均衡數量就會增加。

而老鼠生得多、不容易被捕食時，老鷹的存糧消耗比較慢，老鷹的均衡數量增加。

除了均衡以外，我們還有什麼可以干預呢？像流行病之類的，可能我們想控制波峰的高度。但這個模型的週期是非線性的，波峰的高度沒解析解。

然而由於均衡是波動的中心點，控制均衡其實可以間接控制波峰高度。

週期是我們可以想辦法干預的，也許讓老鼠爆發的週期長一點可以降低鼠疫爆發的風險。

## 政策一：使用老鼠藥

首先，我們得討論老鼠藥是怎麼使用。

我們又要分種類和干預頻率討論。

種類上

第一種是完美的老鼠藥，只會消滅老鼠，不會害到老鷹。

第二種是比較實際的老鼠藥，他會生物累積。老鼠吃多了，老鷹會容易死。

干預頻率的話，我們可以討論一次性的大灑藥，移除現有的老鼠和老鷹。又或是常態性的灑藥，在每期移除動物。

一次性的大灑藥，移除現有的老鼠或老鷹，在模型的效果是調整初始狀態的位置。也許讀者會想把波動壓平似乎是功德一樁，但基本上想直接去微調狀態是不實際的。

但我們的模型並不是實驗室裡的砝碼和彈簧，也不是示波器上面的訊號。這是一個高度簡化的模型，他並不是用來捕捉真實數據並做量化處理的，而是用其參數的性質做質性的討論。

週期性的灑藥，才有對微分方程內的變數產生變化。

我們看第一種完美的藥

dR/dt = r_b R - r_c R P - k R

這個藥的效果是每期移除一些老鼠，以滅鼠率 k 乘上當下老鼠數量 R 表達

dR/dt = (r_b - k) R - r_c R P

但我們整理變數後發現，實際上灑藥在數學上的效果，相當於降低出生率的值。我們只是讓下期增加的老鼠變少。

(R, P) = (pd/pb, (rb - k) /rc)

均衡打開來看，哇老鼠沒減少，但老鷹減少了。這個數學上的毒藥效果是把老鷹的食物減少。

再來看第二種老鼠藥，我們假設他傷害老鼠和老鷹的效果分別是 k 和 l

dR/dt = r_b R - r_c R P - k R

dP/dt = p_b RP - p_d P - l P

老鼠效果一樣，老鷹變數一合併，相當於死亡率增加

我們再看均衡

(R, P) = ((pd + l)/pb, (rb - k) /rc)

哇，灑了藥之後，老鼠不減反增了！越灑越多。這是怎麼回事？

因為老鷹死得多，少了一些老鷹在吃老鼠。

我們都還不用假設老鷹和老鼠生育時間、數量的差別，就已經得到這樣的結論了。

維基百科有個頁面叫做殺蟲藥的悖論，就是在講這個結論。 https://en.wikipedia.org/wiki/Paradox_of_the_pesticides

註：有加入時間的 delay differential equation 可以做，但沒解析解。

dR/dt = αR(t) − βR(t)P(t)
dP/dt = δR(t−τ)P(t−τ) − γP(t)

## 「不讓鼠來、不讓鼠住、不讓鼠吃」

這句話我們需要拆解一下，到底具體是哪些面向

https://www.cdc.gov.tw/Bulletin/Detail/t7U_mzNHOLqp8jDXZLkyhg?typeid=9
疾管署的網頁顯示

> 民眾平時應留意環境中老鼠可能入侵的路徑，家中廚餘或動物飼料應妥善處理，並隨時做好環境清理，防火巷、排水設施（下水道、水溝蓋）、雜物堆、牆垣為鼠類族群活動熱區，請針對該等特定環境加強捕鼠與滅鼠工作。
另有

> 漢他病毒症候群為人畜共通傳染病，在自然界的傳播宿主為鼠類等齧齒類動物，人類吸入或接觸遭帶有漢他病毒鼠類排泄物或分泌物(包括糞便、尿液、唾液)污染之塵土、物體，或被帶有病毒的齧齒類動物咬傷，就有感染的風險。

疾管署的目的主要是為了避免人們得到漢他病毒。雖然提到捕鼠和滅鼠，但目的是避免老鼠接近住宅。避免民眾接觸鼠類排泄物而感染。這是合理行動。

這目的不是減少都市裡老鼠的總數量。

我們可以討論一下以減少老鼠總量為目的的捕鼠或滅鼠。不管是用藥或用陷阱，目的都是移除下一期的老鼠。這在數學上的呈現是一樣的，最後就是老鷹去承受這些後果。

## 環境負載

有趣的是「不讓鼠吃」這個點。疾管署的建議看起來是避免老鼠進入民宅或人類活動空間，造成感染。但也有許多新聞強調，都市中處理不善的食物和垃圾，讓老鼠有很多食物可以吃，得以增長族群。

讓老鼠找不到食物，可以減少老鼠總量嗎？

目前我們的模型假設老鼠有無限充足的食物，沒有獵食者的情況下，想生多少就生多少。

這讓我們的模型陷入雞肉模型的問題。我們已經在假設中下了結論了，這樣不好。

幸好我們的模型就像一碗原味豆花一樣，可以想加什麼料就加。

我們可以加上一個馬爾薩斯天花板 K，假設都市裡有個老鼠的環境負載力上限。老鼠數量快碰到天花板，鼠口就會成長緩慢。穿越天花板時，鼠口會負成長。

這樣我們可以討論假設垃圾和廚餘控制住了，壓低天花板，對鼠口有什麼影響。

更新的公式如下，老鼠的出生受到 (1-R/K) 項的抑制。

dR/dt = r_b R (1-R/K) - r_c R P

dP/dt = p_b RP - p_d P

照前面重複的步驟

獵食者那條仍然可以算出 P = 0 或 R = pd/pb

dR/dt = r_b R (1-R/K) - r_c R P = 0
得
R =0 或
P = r_b (1-R/K)/r_c = rb/rc (1-(pd/pb)/K)
哇，老鼠的均衡數量沒受到影響耶！環境負載力的後果還是老鷹在承受
而且這裡還有個**恐怖生態後果**。如果我們要均衡老鷹數量是正的，也就是 P* > 0 ，這要求 (1 - R*/K) 要是正的。也就是老鼠總量不能超越環境負載力，又或是環境負載力不能對老鼠數量有約束力。
如果太激進的廚餘與垃圾政策壓迫到了老鼠數量，最後均衡會變成 (P, R) = (0,K) ，老鷹都餓死了，老鼠長到負載力天花板。
負載力天花板的甜蜜點應該要剛好在 老鼠均衡數量的上方一點點 K > R* 。這樣可以壓制老鼠波動的高峰，又不影響老鷹的生存。

## 政策目標

我們其實要問，我們消滅老鼠的目標是什麼？

是人們目擊老鼠心生畏懼，心中產生負效用？

難道我們不能學法國人說，整個城市都是為人類設計的，難道老鼠沒有與我們分享一樣日光的空間嗎？（TODO: add source and fix tone）

The pro-rat argument in Paris
The main voices are a Paris councillor Douchka Marcovitch of the Parti animaliste and a pressure group called Paris Animaux Zoopolis (PAZ). Their arguments cluster around a few themes:
The waste disposal argument
Supporters claim rats eat around 100 tons of waste in Paris every day, thus preventing the city's sewer system from clogging up. The framing is that rats are a free waste management service the city is trying to kill. France 24
The poison inefficiency argument
Gentler methods than traditional rat poison exist — poison is both cruel and ultimately inefficient because rodents become immune to its toxicity and often learn to avoid the bait in the first place. This is actually consistent with our model — ~40% of Paris rats have developed resistance to anticoagulants. France 24
The paradigm shift argument
Marcovitch argues rats are auxiliaries in the disposal of waste, saying "we must change the paradigm" and ask about "the way of life of rats, so that we can find efficacious and ethical ways of dealing with them." City Journal
The rights argument (more radical)
PAZ argues urban space is exclusively reserved to humans and that we must end this anthropocentric idea — asking "by what right do we deprive certain animals of all access to the light of day?" City Journal


目前我聽到幾個合理的理由：
- 老鼠帶來疾病：我們下面討論疾病的部分。
- 老鼠會咬壞電線，造成設備的財務損失。

咬壞電線，以老鼠均衡作為控制目標似乎合適。因為其代表平均曝鼠數量。

假設目標是避免疾病。除了把老鼠趕離人們居住處，和模型相關的點是控制峰值。
結論

我們其實透過模型看到許多違反直覺的事。
TODO: add recap
Toso: add policy table 

老鼠問題看起來不是一件頭痛醫頭的事。反而是要頭痛醫腳，腳痛醫頭。

要處理老鼠的事，先照顧好老鷹。

## 附錄

### 老鼠討論

有學者建議，我們討論老鼠問題不應該只講老鼠，應該區分：溝鼠、小黃腹鼠、亞洲家鼠、玄鼠等等。每種鼠有不同的棲地習性。

但在模型的場景中，我們其實需要的是一隻抽象的代表性老鼠就夠。除非上述老鼠在數學上是不一樣的老鼠，我們不需要分開討論。

獵食者也是，我們只講一隻抽象的老鷹。但讀者腦袋可以自行代換喜歡的動物：鳳頭蒼鷹、黑鳶、貓頭鷹、或 Python 。會吃老鼠即可。

### 平均數量

我們這邊證明均衡數量是平均數量

Todo: change to Chinese 
我們用獵食者方程式
dP/dt = δRP − γP
兩邊同除 P:
(1/P) dP/dt = δR − γ
The left side is d(ln P)/dt. Integrate over one full period T: 這代表百分比變化率
[ln P]₀ᵀ = δ∫R dt − γT
Since P is periodic, ln P(T) = ln P(0), so the left side is zero:
0 = δ∫R dt − γT
∫R dt / T = γ/δ
Therefore:
⟨R⟩ = γ/δ = R*
R* is the time average of R. Exactly. Same argument applied to the rat equation gives ⟨P⟩ = P*.

### 週期


The System

dR/dt = αR − βRP
dP/dt = δRP − γP

───

1. Equilibrium

Set both derivatives to zero:

Rat equation:
αR − βRP = 0
R(α − βP) = 0

So either R = 0 or P = α/β

Predator equation:
δRP − γP = 0
P(δR − γ) = 0

So either P = 0 or R = γ/δ

This gives two equilibria:
• (R*, P*) = (0, 0) — trivial, both extinct
• (R*, P*) = (γ/δ, α/β) — the coexistence equilibrium

───

2. Stability — Linearization

To understand behavior near the coexistence equilibrium, linearize. Let:

R = R* + r, P = P* + p

Where r, p are small perturbations. Substituting into the equations and dropping second-order terms (rp ≈ 0):

Rat equation:
d(R*+r)/dt = α(R*+r) − β(R*+r)(P*+p)
dr/dt = αR* + αr − βR*P* − βR*p − βrP*

Since αR* = βR*P* at equilibrium (they cancel):
dr/dt = αr − βR*p − βrP*

Wait — at equilibrium P* = α/β, so βP* = α:
dr/dt = αr − αr − βR*p
dr/dt = −βR*p

Predator equation:
dp/dt = δ(R*+r)(P*+p) − γ(P*+p)
dp/dt = δR*P* + δR*p + δrP* − γP* − γp

Since δR*P* = γP* at equilibrium (they cancel):
dp/dt = δR*p + δrP* − γp

And since δR* = γ:
dp/dt = γp + δrP* − γp
dp/dt = δP*r

───

3. The Linearized System

Collecting the two linearized equations:

dr/dt = −βR* · p
dp/dt = δP* · r

Write as a matrix:



───

4. Eigenvalues

The characteristic equation of the matrix:

det(A − λI) = 0
(0−λ)(0−λ) − (−βR*)(δP*) = 0
λ² + βδR*P* = 0
λ² = −βδR*P*

Since R*, P*, β, δ are all positive, the right side is negative:

λ = ±i√(βδR*P*)

Pure imaginary eigenvalues — this confirms the equilibrium is a center, meaning the system orbits around it neither spiraling in nor out. Neutral stability.

───

5. The Oscillation Period

The imaginary part of λ is the angular frequency:

ω = √(βδR*P*)

Substituting R* = γ/δ and P* = α/β:

ω = √(βδ · γ/δ · α/β)
ω = √(γα)
ω = √(αγ)

The period is:

T = 2π/ω = 2π/√(αγ)

───

6. The Conserved Quantity

To confirm orbits are closed, we find V such that dV/dt = 0. Divide the two equations:

dP/dR = (δRP − γP) / (αR − βRP)
dP/dR = P(δR − γ) / R(α − βP)

Separate variables:

(α − βP)/P · dP = (δR − γ)/R · dR

Integrate both sides:

∫(α/P − β)dP = ∫(δ − γ/R)dR
α ln P − βP = δR − γ ln R + constant

Rearranging:

V(R,P) = δR − γ ln R + βP − α ln P = constant

This is the conserved quantity. Every trajectory is a level curve of V.

───

7. Why V has a minimum at equilibrium

Take partial derivatives:

∂V/∂R = δ − γ/R = 0 → R = γ/δ = R*
∂V/∂P = β − α/P = 0 → P = α/β = P*

The Hessian at (R*, P*):

∂²V/∂R² = γ/R*² > 0
∂²V/∂P² = α/P*² > 0
∂²V/∂R∂P = 0

Positive definite — so (R*, P*) is a strict minimum of V. Moving away in any direction increases V. The level curves around this minimum are the closed orbits.

───

Summary of results


Result
Expression
Depends on

Rat equilibrium
R* = γ/δ
Predator params only

Predator equilibrium
P* = α/β
Rat params only

Angular frequency
ω = √(αγ)
One param from each

Period
T = 2π/√(αγ)
One param from each

Conserved quantity
V = δR − γ lnR + βP − α lnP
All params



The period T = 2π/√(αγ) is particularly elegant — it's the geometric mean of the rat birth rate and predator death rate, which are the two "restoring force" parameters that drive the cycle in opposite directions.

### 疾病

The basic reproduction number for the disease is:
R₀ = λS / ν · R
R₀ > 1 means epidemic takes off. Crucially, R₀ scales linearly with rat population R. So both interventions matter, but differently:

A rat population oscillating between 20 and 80 (mean 50) is more dangerous than one sitting steadily at 50
This is because the spike to 80 may push R₀ above 1 and trigger an outbreak, even if the average is fine. Epidemics don't care about averages — they care about threshold crossings.

因此在避免疾病這塊，我們可能不在乎平均曝鼠時間，而是希望峰值不要太高。

但峰值在方程式裡沒有解析解，所以也不太好討論。另一種可能是用環境負載力去壓。
