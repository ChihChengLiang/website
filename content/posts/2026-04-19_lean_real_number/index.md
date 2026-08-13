---
title: "Lean and the Real Real Numbers"
date: 2026-04-19T23:37:43+08:00
draft: false
---

{{< translation type="machine" from="Chinese" />}}

Economics textbook: Let's introduce a new concept, the "supremum norm" of a matrix. Imagine a "real-valued" matrix — its "supremum norm" is the largest [^abs] value among its entries. For example, the supremum norm of the matrix $\begin{bmatrix}1 & 3 \\\ 2 & 4\end{bmatrix}$ is 4.

[^abs]: Technically it should be the largest "absolute value" among all entries, but that's not the point here.

Me (internal monologue):
<div class="think">

Okay, the textbook just defined the supremum norm. Mathematically, a "norm" assigns some notion of "length" to a mathematical object. A matrix is a mathematical object, and we can give it a number as its length, so we can compare it with other matrices.

The matrix $\begin{bmatrix}1 & 3 \\\ 2 & 4\end{bmatrix}$ has four numbers: $1, 3, 2, 4$. The largest is $4$. We just pick that as this matrix's length.

</div>

Economics textbook: As an exercise, prove that the supremum norm doesn't satisfy the triangle inequality: $\lVert XY \rVert \leq \lVert X \rVert \cdot \lVert Y \rVert$.

Me (internal monologue):
<div class="think">

For something to be a "notion of length," it generally needs to satisfy certain intuitions people have about length. That way, even if the length concept being defined is abstract, we can still imagine how this length behaves.

Our usual notion of length has to satisfy the "triangle inequality." Suppose a triangle has vertices A, B, C — "going from A straight to B" should be shorter than "going from A to C, then from C to B." In other words, a direct path should be shorter than a roundabout one, matching our everyday intuition about length and distance.

In this matrix analogy, matrix multiplication $\lVert XY \rVert$ is like the direct path. $\lVert X \rVert$ and $\lVert Y \rVert$ are the distances traveled along each matrix's own leg of the trip.

How surprising — it turns out the supremum norm is a somewhat disobedient notion of length. It doesn't match our usual intuitions about length at all.
</div>

Me: Okay, let me think about how to prove this.

Me (internal monologue):
<div class="think">

To prove "doesn't satisfy the triangle inequality," I just need one counterexample. I need to find a matrix $X$ and a matrix $Y$ such that the norm of their product is bigger than the product of their individual norms. That is, $\lVert XY \rVert > \lVert X \rVert \cdot \lVert Y \rVert$.

Maybe $X = Y = \begin{bmatrix}1 & 0 \\\ 0 & 1\end{bmatrix}$ is a decent starting point. Both $X$ and $Y$ have a supremum norm of $1$, so the right-hand side is $1 \times 1$.

But $XY$ also comes out to $\begin{bmatrix}1 & 0 \\\ 0 & 1\end{bmatrix}$, so the left-hand supremum norm is also $1$ — not bigger than the right side.

Let me try $X = Y = \begin{bmatrix}1 & 1 \\\ 1 & 1\end{bmatrix}$ instead. Both $X$ and $Y$ still have a supremum norm of $1$.

But $XY$ becomes $\begin{bmatrix}2 & 2 \\\ 2 & 2\end{bmatrix}$! Its supremum norm is now $2$. That achieves what we needed — a violation of the triangle inequality.
</div>

Me: Let $X$ and $Y$ both be $\begin{bmatrix}1 & 1 \\\ 1 & 1\end{bmatrix}$. Then $XY = \begin{bmatrix}2 & 2 \\\ 2 & 2\end{bmatrix}$, giving $\lVert XY \rVert = 2 > \lVert X \rVert \cdot \lVert Y \rVert = 1 \cdot 1$. QED.

Me: Let me write this proof down in Lean.

Lean: Whoa, whoa, whoa, hold on — you want to multiply two "real-valued" matrices together? Who told you that was fine? Real numbers are undecidable, uncomputable. Their product exists mathematically, but you can't actually *compute* on them.

Me: Are you sure? I just want real numbers — you know, the ones with positives, negatives, and decimal points! And within those decimal ones, I want rational numbers — the kind you can express as an integer numerator over an integer denominator. And also things like the square root of 2, which rationals can't express. Is that really too much to ask?

Me (internal monologue):
<div class="think">
Lean is protesting. I'd better ask a professional what's actually going on.
</div>

Claude: Well, real numbers in Lean are actually constructed as either the Cauchy completion of ℚ, or via Dedekind cuts. So your $\sqrt 2$ doesn't literally "exist" — it's actually a sequence, like 1, 1.4, 1.41, 1.414, ... . Or more precisely, it's the equivalence class of "all" sequences that converge to the same value, so you could equally define $\sqrt 2$ using 1, 1.5, 1.41, 1.415, ... .

Lean: Yeah, so if you really insist, I can grudgingly give you this:

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

Lean: The real number 2, here, is just a sequence converging toward 2. Not a Cauchy sequence, mind you — just *a* sequence. If you want to claim it's a Cauchy sequence, that's a `sorry`, please supply the extra proof yourself.

Claude: You could also settle for the rationals, ℚ.

Lean: Rationals ℚ make me the happiest. Here, this is the matrix multiplication you asked for:

```lean
def C : Matrix (Fin 2) (Fin 2) ℚ :=
  !![1, 1; 1, 1]

#eval C * C
-- !![2, 2; 2, 2]
```

Me: I'm not thrilled about that. Math textbooks use square root of 2 all the time — I don't want to pretend it doesn't exist, like Pythagoras did.

Claude: How about floating point, `Float`, instead? In applied math, when you write actual code, you never use "true" real numbers anyway — it's always floats standing in for them, right?

Me: You are absolutely right. I think in practice it's fine to accept `Float` as a stand-in for real numbers.

Lean: (starts throwing up)

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

Me: Uh... Lean, what's wrong? Medium, please!

Claude: This is an old Lean affliction. Matrix multiplication requires the entries to have a semiring structure. `Float` doesn't have a semiring structure.

Me: Are you sure? Can I verify that myself?

Claude: Easy.

```lean
def C : Matrix (Fin 2) (Fin 2) ℚ :=
  !![1, 1; 1, 1]

#check C * C
/-
Hovering over * in VSCode shows:
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

Claude: I was wrong. Multiplication's requirement on the entry type is actually a bit weaker than a semiring — it's `AddCommMonoid`, which still requires things like additive associativity. `Float` doesn't have additive associativity.

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

Me: All right, so it looks like Float doesn't work for matrix multiplication.

## Computableℝ: upper bounds, lower bounds, and a bit of algebra

Me: I found a library that Timeroot implemented: https://github.com/Timeroot/ComputableReal. It can actually compute anything that would normally be computable by hand.

```lean
example : |√3 - 2 * exp 1 / π| < 0.002 := by
  native_decide
```

The idea behind this implementation is a new structure, `ComputableℝSeq`, which carries an upper bound, a lower bound, and a proof that it's a Cauchy sequence. You can't add sequences directly, but you *can* add upper and lower bounds!

As long as you tell Lean the new upper and lower bounds, and convince it that the new sequence is still Cauchy, Lean is happy to let you add, subtract, multiply, and divide "real numbers."

But there's a caveat mentioned in the project: determining the sign is still uncomputable. Is $\sqrt 2 = \sqrt 2$? Can't decide. Is $\sqrt 2 - \sqrt 2 = 0$? Can't compute it.

```lean
example : Real.sqrt 2 = Real.sqrt 2 := by --hangs, never terminate
  native_decide

example : Real.sqrt 2 - Real.sqrt 2 = 0:= by --hangs
  native_decide
```

Me: Wait, that's outrageous! Can't I just prove that both copies of $\sqrt 2 - \sqrt 2$ are the same sequence, so subtracting gives the zero sequence? Medium, please!

Claude: The reason is that the system can't yet tell these two sequences are the same, so it has to treat them as two independent sequences under computation. As the project's README says, for $\sqrt 2 - \sqrt 2$, the upper bound uses `1/2ⁿ` and the lower bound uses `-1/2ⁿ`. So within any finite number of iterations, there's no way to know whether this is converging to something positive or negative.

Claude: But if you actually want the result $\sqrt 2 - \sqrt 2 = 0$, you can use the ring structure of the reals instead. **Not by computing the result, but by algebra.**

```lean
-- this works
example : Real.sqrt 2 - Real.sqrt 2 = 0 := by ring
```

Claude: `norm_num` also works here.

```lean
-- this works
example : Real.sqrt 2 - Real.sqrt 2 = 0 := by norm_num
```

Me: Wait a second. `norm_num` looks like a numerical computation tactic — can it really handle real numbers?

Claude: `norm_num` actually cheats a bit with algebra under the hood. It detects the pattern `x - x` and knows it cancels. But the next example, $\sqrt 2 + \sqrt 2 = 2 * \sqrt 2$, trips `norm_num` up. For `ring`, though, it's still a piece of cake — this is all algebra, no computation involved.

```lean
example : Real.sqrt 2 - Real.sqrt 2 = 0 := by norm_num
example : Real.sqrt 2 + Real.sqrt 2 = 2 * Real.sqrt 2 := by norm_num  -- fails
example : Real.sqrt 2 + Real.sqrt 2 = 2 * Real.sqrt 2 := by ring
```

## norm_num: algebra and computation, combined magic

Me: It looks like `norm_num` can actually expand real matrix multiplication. Is it using computation, or algebra? Is there a way to see which?

```lean
def C : Matrix (Fin 2) (Fin 2) ℝ :=
  !![1, 1; 1, 1]

example :  C * C = !![2, 2; 2,2] := by
  unfold C
  norm_num
```

Claude: There are a few ways to check; the fastest is:

```diff
+ set_option trace.Tactic.norm_num true
example :  C * C = !![2, 2; 2,2] := by
  unfold C
  norm_num
```

Claude: `norm_num` tries lots of things here and fails at most of them. What finally succeeds is recognizing that the "1" in this real-valued matrix is actually the natural number 1, and it completes the reasoning by treating it as natural-number multiplication.

## Conclusion

In applied math, we casually and elegantly define real-valued functions all the time.

But to Lean, we're like people who time-traveled from the 18th century and have never actually seen a real number.

Under a rigorous definition of the real numbers, manipulating reals in Lean runs into challenge after challenge. This post is a summary of the various stopgap solutions I've come across so far, each with its own flaws.

We can roughly split the solutions into algebra and computation:

- Algebra: if two real numbers are symbolically identical, like x - x, they can cancel without any computation at all. Worth trying `ring`.
- Computation:
    - If the real numbers involved happen to be simple natural numbers like 1, 2, 3, Lean might be able to treat them as natural numbers.
    - The Computableℝ approach: compute on the upper and lower bounds of a Cauchy sequence, sidestepping direct computation on the real number itself. Drawback: can't determine sign.

But when you actually run into real numbers, throw `norm_num` at it first and see what happens. `norm_num` mixes algebra and computation, trying various approaches. If you don't like black-box behavior, you can wait for `norm_num` to solve it, then peek at exactly which step succeeded.

The bigger question is: if you want to formalize an applied-math textbook, should you naively follow the textbook and just use the real numbers ℝ?

One thing's for sure: `Float` is off the table. But can you get away with rationals ℚ instead? So far, I actually haven't hit a case where that broke.
