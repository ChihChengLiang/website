---
title: "🗒️全節點 Demo"
date: 2021-02-28T13:35:56.587Z
draft: false
---

## 先備知識

主網路

1. 以太坊系統的本體是一個點對點網路。
2. 全節點大概要同步個一天以上
3. 全節點大概要吃掉 250 GB 的硬碟空間
4. 主網路 要用真的以太幣才能部署合約
5. 測試網路 有水龍頭可以領測試用的測試幣
6. 「狀態」的讀取，免費
7. 「狀態」的寫入，要送花費 gas 的交易

## 三天前的準備

先同步好一個全節點，當天可以快速展示

## Demo 主網路

步驟：

1. 展示全節點的 Log
2. 展示連接上全節點，並瀏覽合約裡面的資料

決策：要讀什麼合約的資料出來玩比較好玩呢？

## 設定全節點

```
sudo apt install build-essential
```

安裝 golang
```
wget -q -O - https://git.io/vQhTU | bash
```


下載並建置 Geth

```
git clone https://github.com/ethereum/go-ethereum.git
cd go-ethereum
make geth
```

跑主網路

```
geth
```


## Demo 從全節點取得資料


```
geth attach <要找 ipc path>
```

### 瀏覽區塊、交易相關資料

- net.version
    - 解釋主網路和其他測試網路
- eth.getBlockNumber()
- eth.getBlockByNumber(100)
    - 挑幾個區塊裡面重要的欄位解釋

### 瀏覽帳戶餘額

解釋帳戶是什麼，私鑰公鑰數位簽章。EOA 與合約帳戶

- eth.getBalance


### 瀏覽合約資料

- eth.getCode()
    - 選一個合約地址，看 bytecode 與 etherscan 上面的是否吻合

### 呼叫函式與瀏覽合約狀態

(這項看起來需要 js library 配合比較容易做)


## 相關連結

- https://ethstats.net/
- https://www.ethernodes.org/

-----

# 網頁 Demo


## 前言

我知道全節點同步下來全網的狀態

- 區塊鏈怎麼執行我的業務邏輯？
    - 利用部署到區塊鏈的程式碼
    - 利用狀態的資料與
- 我要怎麼更改區塊鏈上面的狀態？
- 我要怎麼讓使用者看到區塊鏈上面的狀態？

在人們偷懶把所有的功能委託給 Infura 與 Metamask ，這些核心的問題很難自行釐清。這個 Demo 的用意在於用最少程式，看到資料怎麼透過網頁與全節點網路互動。

## 節點


跑測試網路

```
geth --goerli
```

水龍頭 https://goerli-faucet.slock.it/


## 部署合約

1. 安裝 Solidity



很簡單的 Solidity
```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;


contract Hello {
     string name = "";
    
    function sayHello() external view returns(string memory){
        return name;
    }
    
    function changeName(string calldata _name) external {
        name = _name;
    }
}

```

## Demo 網頁

ethers.js 套件
```
wget https://cdn.ethers.io/lib/ethers-5.0.esm.min.js
```


## 在網頁上顯示合約內的資料


網頁 code

```
<html>

<head> </head>

<body>
    <script type="module">
        import { ethers } from "./ethers-5.0.esm.min.js";
        // 讓瀏覽器 console 可以拿到 ethers
        window.ethers = ethers;

        // const provider = new ethers.providers.JsonRpcProvider("http://localhost:8545");
        // console.log("provider", provider)
        // const signer = provider.getSigner()
        // console.log("signer", signer)
        // signer.getAddress().then(x => console.log(x))
        // console.log(provider.getBlockNumber())
    </script>
</body>

</html>
```

geth 必須要把權限打開

```
geth --http --http.api personal,eth,net,web3  --http.corsdomain '*'
```