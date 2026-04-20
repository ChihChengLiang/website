---
title: "Lean 語言與實數"
date: 2026-04-19T23:37:43+08:00
draft: false
---

經濟學課本：我們來介紹一個新觀念，矩陣的「最大值範數 （supremum norm）」 。想像一個「實數值」的矩陣，他的「最大值範數」就是元素裡面最大的那個值。例如，矩陣 $\begin{bmatrix}1 & 3 \\\ 2 & 4\end{bmatrix}$ 的最大值範數是 4 。

我（腦內小劇場）：
> 好的，數學課本定義了最大值範數。數學上「範數 （Norm）」可以賦予一個數學物件一種「長度」的概念。矩陣是一種數學物件，我們可以給他一個數字當作長度，來和其他的矩陣比較。
>
> 矩陣 $\begin{bmatrix}1 & 3 \\\ 2 & 4\end{bmatrix}$ 有四個數字：$1, 3, 2, 4$。最大的數字是 $4$。我們就選他當這個矩陣的長度。

經濟學課本：作為習題，請證明最大值範數不符合三角不等式：$\|XY\| \leq \|X\| \cdot \|Y\|$。

我（腦內小劇場）：
> 一般作為「長度概念」的定義，要滿足人們某些對長度的直覺。這樣即使定義的長度概念很抽象，我們仍然能夠想像這個長度的行為。
>
> 一般想像的長度必須要符合「三角不等式」。假設三角形有 A B C 三個頂點，「從 A 出發走到 B 」應該要短於「從 A 走到 C ，再從 C 走到 B」。這意思是說直走的距離要比繞路的距離短，符合人們對長度與距離的生活直覺。
>
> 在矩陣抽象的類比中，$\|XY\|$ 內矩陣乘法像是直走的距離。而 $\|X\|$ 和 $\|Y\|$ 則是分別走過兩個矩陣各自定義的距離。
>
> 太驚訝了，原來最大值範數是一種比較不乖的長度概念。他沒有符合一般長度的直覺。

我：好的，讓我來想想怎麼證明。

我（腦內小劇場）：
> 要證明「不符合三角不等式」，我只需要舉一個反例即可。我要找到一個矩陣 $X$ 和一個矩陣 $Y$，使得相乘的範數比各自的都大。也就是 $\|XY\| > \|X\| \cdot \|Y\|$
>
> 也許 $X = Y = \begin{bmatrix}1 & 0 \\\ 0 & 1\end{bmatrix}$ 是不錯的起點。$X$ 和 $Y$ 各自有最大值範數為 $1$，這樣右邊兩個數字都是 $1$。
>
> 然而 $XY$ 也會是 $\begin{bmatrix}1 & 0 \\\ 0 & 1\end{bmatrix}$，這樣左邊的最大值範數也是 $1$，沒有大過右邊的。
>
> 不然試試 $X = Y = \begin{bmatrix}1 & 1 \\\ 1 & 1\end{bmatrix}$。這樣 $X$ 和 $Y$ 仍然有最大值範數為 $1$。
>
> 但是 $XY$ 變成 $\begin{bmatrix}2 & 2 \\\ 2 & 2\end{bmatrix}$ 了！$XY$ 的最大值範數變成 $2$。有達到違反三角不等式的目標了。

我：令 $X$ 和 $Y$ 為 $\begin{bmatrix}1 & 1 \\\ 1 & 1\end{bmatrix}$。這樣 $XY = \begin{bmatrix}2 & 2 \\\ 2 & 2\end{bmatrix}$。使得 $\|XY\| = 2 > \|X\| \cdot \|Y\| = 1 \cdot 1$。證明完成 QED

我：讓我用 Lean 語言把這段證明寫下來。

Lean 語言： Whoa, whoa, whoa 先等等，你要把兩個「實數值」的矩陣乘開？誰讓你們這樣瞎搞的？實數是不可判定，不可計算的

我：你確定嗎？我只是想要實數啊，就是那種有正數、有負數、有小數點的數啊！然後那些帶小數點的，我想要有理數 -- 那種可以用整數分母分子表達的數。再加個根號 2 這類的，有理數沒辦法表達的數。這樣有很過分嗎？

我（腦內小劇場）：

> Lean 語言提出了抗議，我最好問問某個專業人士，看到底發生了什麼事。

Claude: 誒，其實 Lean 裡面的實數是柯西序列（Cauchy completion of ℚ）或戴德金分割（Dedekind cuts）構造出來的。所以你的 $\sqrt 2$ 其實不存在，他實際上是一個序列 1, 1.4, 1.41, 1.414, ... 。或精確地來說是「所有」可以收斂到同一個地方的級數，所以你也可以用 1, 1.5, 1.41, 1.415, ... 來定義 $\sqrt 2$ 。

Lean 語言：對的，所以你硬要算的話，我勉強可以算這樣給你：

```lean
def C : Matrix (Fin 2) (Fin 2) ℝ :=
  !![1, 1; 1, 1]

#eval C * C
/- 
!![Real.ofCauchy (sorry /- 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, ... -/),
   Real.ofCauchy (sorry /- 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, ... -/);
   Real.ofCauchy (sorry /- 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, ... -/),
   Real.ofCauchy (sorry /- 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, ... -/)]
-/
```

Lean 語言：實數的 2 ，就是一串往 2 收斂的序列。不是柯西序列哦！只是序列。你要說他是柯西序列？ `sorry` ，請你補上額外的證明。

Claude: 你也可以屈就一下，使用有理數 ℚ

Lean 語言：有理數 ℚ 的話，我是最開心的。來，這裡是你要的矩陣乘法：

```lean
def C : Matrix (Fin 2) (Fin 2) ℚ :=
  !![1, 1; 1, 1]

#eval C * C
-- !![2, 2; 2, 2]
```

我：我不太開心

Claude: 不然浮點數 Float 怎麼樣？應用數學裡面，你寫程式也不會用「真正」的實數吧？不都是用浮點數代替的？

我：You are absolutely right. 我覺得實務上可以接受 Float 代替實數。

Lean 語言：（開始嘔吐）

```lean
def C : Matrix (Fin 2) (Fin 2) Float :=
  !![1, 1; 1, 1]

#eval C * C
/- 
failed to synthesize instance of type class
  HMul (Matrix (Fin 2) (Fin 2) Float) (Matrix (Fin 2) (Fin 2) Float) ?m.4
Error code: lean.synthInstanceFailed
-/
```

我： 啊 ... Lean 你怎麼了？ 通靈師！

Claude: 這是 Lean 語言老症頭了。 矩陣乘法需要裡面的元素具備半環（Semiring）結構。 Float 不具備半環結構。

我： 你確定嗎？我能驗證看看嗎？

Claude: 簡單。

```lean
def C : Matrix (Fin 2) (Fin 2) ℚ :=
  !![1, 1; 1, 1]

#check C * C
/-
在 VScode 介面，滑鼠滑到 * 處
@HMul.hMul (Matrix (Fin 2) (Fin 2) ℚ) (Matrix (Fin 2) (Fin 2) ℚ) (Matrix (Fin 2) (Fin 2) ℚ)
  Matrix.instHMulOfFintypeOfMulOfAddCommMonoid C C : Matrix (Fin 2) (Fin 2) ℚ
-/

#check @Matrix.instHMulOfFintypeOfMulOfAddCommMonoid
/-
@Matrix.instHMulOfFintypeOfMulOfAddCommMonoid : {l : Type u_4} →
  {m : Type u_5} →
    {n : Type u_6} →
      {α : Type u_3} → [Fintype m] → [Mul α] → [AddCommMonoid α] → HMul (Matrix l m α) (Matrix m n α) (Matrix l n α)
-/
```

Claude: 我錯了。乘法對元素的要求比半環再弱些，是 `AddCommMonoid` ，但這要求加法結合律等。 Float 沒加法結合律。

```lean
#print AddCommMonoid
/-
class AddCommMonoid.{u} (M : Type u) : Type u
...
fields:
  AddSemigroup.add_assoc : ∀ (a b c : M), a + b + c = a + (b + c)
...
-/

#eval ((0.1 + 0.2 : Float) + 0.3).toBits -- 4603579539098121012
#eval (0.1 + (0.2 + 0.3 : Float)).toBits -- 4603579539098121011
#eval ((0.1 + 0.2 : Float) + 0.3) == (0.1 + (0.2 + 0.3 : Float)) -- false
```

我：好吧，這樣看起來不能用 Float 拿來做矩陣乘法。

## 使用界

我：我看到 Timeroot 實作了一個函式庫 https://github.com/Timeroot/ComputableReal 。裡面常理可以計算出來的結果都可以算出來耶。

```lean
example : |√3 - 2 * exp 1 / π| < 0.002 := by
  native_decide
```

這個實作的原理是引入一個新的 `ComputableℝSeq`，這個結構會帶著序列的上界、下界、和柯西序列證明。雖然序列沒辦法直接相加，但是上界和下界可以！

只要告訴 Lean 新的上界和下界，以及說服新的序列是柯西序列，那 Lean 可以很開心的接受我們對「實數」的加減乘除。

但裡面有提到一個問題：要判斷正負號仍然是不可計算的。 $\sqrt 2 = \sqrt 2$ ？不能判斷。 $\sqrt 2 - \sqrt 2 = 0$ ？算不出來。 

```lean
example : Real.sqrt 2 = Real.sqrt 2 := by --hangs, never terminate
  native_decide

example : Real.sqrt 2 - Real.sqrt 2 = 0:= by --hangs
  native_decide
```

我：哇這太過分了吧。難道我不能證明 $\sqrt 2 - \sqrt 2$ 兩項都是一樣的序列，相減之後變成都是 0 的序列？通靈師！

Claude: 原因是系統還沒辦法判斷這兩個序列一樣，因此只能把他們當成兩個不同的序列運算。如專案 README 所說，$\sqrt 2 - \sqrt 2$ 上界用 `1/2ⁿ`，下界用 `-1/2ⁿ`。因此在有限的迭代中，無法知道這到底是收斂到正數還是負數。

Claude: 但如果你真的想要  $\sqrt 2 - \sqrt 2 = 0$ 這個結果的話，你可以用實數「環」的性質。**不是用「計算」得到結果，而是用「代數」。**

```lean
-- this works
example : Real.sqrt 2 - Real.sqrt 2 = 0 := by ring
```

Claude: `norm_num` 其實也可以

```lean
-- this works
example : Real.sqrt 2 - Real.sqrt 2 = 0 := by norm_num
```

我：啊等等。`norm_num` 看起來是個數值計算的方法耶，他有辦法駕馭實數嗎？

Claude: `norm_num` 其實中間有代數的偷吃步。他偵測到 `x - x` 這種形式，知道可以抵銷。但下面第二題這種 $\sqrt 2 + \sqrt 2 = 2 * \sqrt 2$ ，`norm_num` 就卡關了。可是對 `ring` 而言還是小菜一碟。這些都是代數，沒運算。

```lean
example : Real.sqrt 2 - Real.sqrt 2 = 0 := by norm_num
example : Real.sqrt 2 + Real.sqrt 2 = 2 * Real.sqrt 2 := by norm_num  -- fails
example : Real.sqrt 2 + Real.sqrt 2 = 2 * Real.sqrt 2 := by ring
```

## norm_num

我：我發現 norm_num 看起來可以乘開實數耶。他是靠運算還是靠代數？有什麼辦法檢視？

```lean
def C : Matrix (Fin 2) (Fin 2) ℝ :=
  !![1, 1; 1, 1]

example :  C * C = !![2, 2; 2,2] := by
  unfold C
  norm_num
```

Claude: 有數種做法，最快的是：

```diff
+ set_option trace.Tactic.norm_num true
example :  C * C = !![2, 2; 2,2] := by
  unfold C
  norm_num
```

Claude: norm_num 這裡做了很多失敗的嘗試。最後成功的地方是辨認出矩陣裡實數的 1 ，其實是自然數的 1 ，最後當成自然數乘開完成推論。
