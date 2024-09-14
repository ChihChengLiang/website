---
title: "📘池化檢驗量能"
date: 2022-05-18T09:50:12.381Z
draft: false
---

> mcdlee: 如果陽性率是 p，總共有 N個檢體。每 n 個檢體做一次池化檢驗，一旦陽性，則該批 n 支各自重做。這樣消耗的檢驗量能的期望值會是...

可以把檢驗分成確定性和不確定性的部分

### 確定性的部分

共有 $\frac{N}{n}$ 個池，每個池驗一次的話，總共需要 $\frac{N}{n}$ 次檢驗

### 不確定性的部分

這是來自因為一個池子中驗出陽性時，需要池子裡全員檢測的檢測數

定義陰性率 

$$
q := 1 -p
$$

一個池會驗出陽性的機率為

$$
1 - q^n
$$

考量所有池，因為驗出陽性，而要 n 個檢體都檢驗，所需檢驗次數的期望值

$$
\frac{N}{n} \times (1 - q^n) \times n = (1 - q^n) N
$$

所以確定性的  $\frac{N}{n}$ 加上不確定性的 $(1 - q^n) N$ ，總共預期要做的檢驗次數是

$$
\frac{N}{n} + (1 - q^n) N
$$

### 問題：最佳的分組人數 n 是多少呢？

n 越多的話，代表分組比較少，確定性的的檢驗會變少。但組裡面出現陽性者的機率就會變高，不確定性的檢驗就會變多。所以看起來有個平衡點，有個最適的 n 能夠讓檢驗能量的消耗最小

我們把前面的期望檢驗次數定義為 n 的函數 F

$$
F(n) := \frac{N}{n} + (1 - q^n) N = N(\frac{1}{n}+ 1 - q^n)
$$

這一階微分不好得到解析解，可以用圖表去做。但從式子可以看得到的是，最適的 n 與總人數 N 無關，只會受到陰性率（或陽性率）影響。

$$
-\frac{1}{n^2} + (-\ln{q}) q^n
$$


我們做一個對陽性率的函數的圖，去觀察陽性率對最適群組大小的影響

$$
\frac{1}{n}+ 1 - (1-p)^n
$$

<iframe src="https://www.desmos.com/calculator/gotutacjcd?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

仔細觀察圖中曲線的最低點。在 p = 0.3 以前時，曲線有個 n 在 2~5 之間的最低點。但 p > 0.3 之後，曲線的最低點變成在圖右側邊界處。

我們也可以用 Python 去找出最適的 n

```python
def f(n, p):
    return 1.0/n + 1.0 - (1.0- p)**n

def argmin_f(keys, f):
    return min(keys, key=f)

def main():
    interval = 20
    max_people = 100
    print("| positive rate $p$ | optimal group size $n$ |")
    print("| -- | -- |")
    for i in range(interval):
        p = i/interval
        best = argmin_f(range(1, max_people + 1), lambda x: f(x, p))
        print(f"| {p} | {best}|")

main()


```

作出的表格如下。給定第一欄的陽性率，第二欄列出能夠最小化期望篩檢數的池子大小。

| positive rate $p$ | optimal group size $n$ |
| -- | -- |
| 0.0 | 100|
| 0.05 | 5|
| 0.1 | 4|
| 0.15 | 3|
| 0.2 | 3|
| 0.25 | 3|
| 0.3 | 3|
| 0.35 | 100|
| 0.4 | 100|
| 0.45 | 100|
| 0.5 | 100|
| 0.55 | 100|
| 0.6 | 100|
| 0.65 | 100|
| 0.7 | 100|
| 0.75 | 100|
| 0.8 | 100|
| 0.85 | 100|
| 0.9 | 100|
| 0.95 | 100|

這表格一開始看會覺得怪怪，有幾個看起來不連續的斷點。我們依陽性率分區來看：

在陽性率 0 是一個極端的狀況。可以想像在 Covid 之前的世界。反正沒人會得病，完全不會有池子需要重測。但因為模型的規定一個池子還是要測一次，因此把池子人數拉到最大，測一次。

在陽性率 0.05~0.3 之間時有最適群組大小 3~5 人。

在陽性率超過 0.3 的情況下，模型會突然把池子人數拉到最大。精確而言，可以把 `interval` 調高，得到細緻的 0.307 這個邊界。我們下面花一點篇幅討論這個詭異的情況。

### 陽性率超過 0.3 的特別情況


不管池子大小如何，出現全陰避開全篩的效果，比不過減少池子數省下的篩檢量。這邊詳細的論證我無法給出數學分析，但作圖可以看到確定性部分和非確定性部分的一階導函數，在陽性率大於 0.3 之前，兩個一階導函數有黃金交叉。但在陽性率大於 0.3 之後，前者處處大於後者

<iframe src="https://www.desmos.com/calculator/nfypkqyxos?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

陽性率超過 0.3 時的情況，也可以說是池化沒有比直接每個人個別篩檢好。

## 針對 n=1 的特別處理


這邊我和 mcdlee 有些來回討論。mcdlee 的觀點是當陽性率 p 上升時，n 應該要遞減，這邊 n 突然飆升的情況不合理。但為什麼要遞減呢？這是因為池化最能發揮威力的情況是，一個檢測就能發給一團人全陰，省下許多試劑。但那個池子只要一個陽性出現，就變成 n+1 次檢驗，會比沒池子純粹個別篩檢還要多 1 。盛行率高時池子全陰的機率很低，所以應該盡量減少池子大小，換成符號上的說法是 p 上升時 n 要降低。

但其實這個爭論的核心在於模型設定的問題。在本文的模型中 n=1 時，每個池子都只有一個人，但池子要篩一次，如果池子陽性，人又要再篩一次。但實際而言，第二次是白篩。我們用下例來表達凸顯這種古怪情況。

假設 N 100 人，陽性率 1 ，代表所有人全中。 n=100 代表只有一個池子。所以池子的 1 次加上 100 個人各自驗一次，共 101 次。
但 n=1 則是有 100 個池子。所以 100 個池子各驗一次，100 個人再驗一次。共驗 200 次

mcdlee 認為應該針對 n=1 的例外情況特別處理。mcdlee 修正後的 Python code 也呈現出 n 對 p 遞減的現象  https://hackmd.io/4yhRwYXnRtqGymnnir2WKg 。但我認為應該保留原本模型 n=1 的古怪行為，因為針對 n=1 做特別處理其實就是從「池化」偷偷換成「個別篩檢」了。這是兩個不同的政策，保留古怪行為比較能夠凸顯池化這個政策的限制。

## 結論

池化檢測相對於個別檢測的優點在於，幸運的情況下，一次檢測就能發給一團人全陰，節省許多試劑。但該優勢只有在於盛行率小於 0.3 的情況下才能發揮。