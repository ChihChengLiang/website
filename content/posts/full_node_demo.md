---
title: "ðå¨ç¯é» Demo"
date: 2021-02-28T13:35:56.587Z
draft: false
---

## ååç¥è­

ä¸»ç¶²è·¯

1. ä»¥å¤ªåç³»çµ±çæ¬é«æ¯ä¸åé»å°é»ç¶²è·¯ã
2. å¨ç¯é»å¤§æ¦è¦åæ­¥åä¸å¤©ä»¥ä¸
3. å¨ç¯é»å¤§æ¦è¦åæ 250 GB çç¡¬ç¢ç©ºé
4. ä¸»ç¶²è·¯ è¦ç¨ççä»¥å¤ªå¹£æè½é¨ç½²åç´
5. æ¸¬è©¦ç¶²è·¯ ææ°´é¾é ­å¯ä»¥é æ¸¬è©¦ç¨çæ¸¬è©¦å¹£
6. ãçæãçè®åï¼åè²»
7. ãçæãçå¯«å¥ï¼è¦éè±è²» gas çäº¤æ

## ä¸å¤©åçæºå

ååæ­¥å¥½ä¸åå¨ç¯é»ï¼ç¶å¤©å¯ä»¥å¿«éå±ç¤º

## Demo ä¸»ç¶²è·¯

æ­¥é©ï¼

1. å±ç¤ºå¨ç¯é»ç Log
2. å±ç¤ºé£æ¥ä¸å¨ç¯é»ï¼ä¸¦çè¦½åç´è£¡é¢çè³æ

æ±ºç­ï¼è¦è®ä»éº¼åç´çè³æåºä¾ç©æ¯è¼å¥½ç©å¢ï¼

## è¨­å®å¨ç¯é»

```
sudo apt install build-essential
```

å®è£ golang
```
wget -q -O - https://git.io/vQhTU | bash
```


ä¸è¼ä¸¦å»ºç½® Geth

```
git clone https://github.com/ethereum/go-ethereum.git
cd go-ethereum
make geth
```

è·ä¸»ç¶²è·¯

```
geth
```


## Demo å¾å¨ç¯é»åå¾è³æ


```
geth attach <è¦æ¾ ipc path>
```

### çè¦½åå¡ãäº¤æç¸éè³æ

- net.version
    - è§£éä¸»ç¶²è·¯åå¶ä»æ¸¬è©¦ç¶²è·¯
- eth.getBlockNumber()
- eth.getBlockByNumber(100)
    - æå¹¾ååå¡è£¡é¢éè¦çæ¬ä½è§£é

### çè¦½å¸³æ¶é¤é¡

è§£éå¸³æ¶æ¯ä»éº¼ï¼ç§é°å¬é°æ¸ä½ç°½ç« ãEOA èåç´å¸³æ¶

- eth.getBalance


### çè¦½åç´è³æ

- eth.getCode()
    - é¸ä¸ååç´å°åï¼ç bytecode è etherscan ä¸é¢çæ¯å¦å»å

### å¼å«å½å¼èçè¦½åç´çæ

(éé çèµ·ä¾éè¦ js library éåæ¯è¼å®¹æå)


## ç¸éé£çµ

- https://ethstats.net/
- https://www.ethernodes.org/

-----

# ç¶²é  Demo


## åè¨

æç¥éå¨ç¯é»åæ­¥ä¸ä¾å¨ç¶²ççæ

- åå¡éæéº¼å·è¡æçæ¥­åéè¼¯ï¼
    - å©ç¨é¨ç½²å°åå¡éçç¨å¼ç¢¼
    - å©ç¨çæçè³æè
- æè¦æéº¼æ´æ¹åå¡éä¸é¢ççæï¼
- æè¦æéº¼è®ä½¿ç¨èçå°åå¡éä¸é¢ççæï¼

å¨äººåå·æ¶æææçåè½å§è¨çµ¦ Infura è Metamask ï¼éäºæ ¸å¿çåé¡å¾é£èªè¡éæ¸ãéå Demo çç¨æå¨æ¼ç¨æå°ç¨å¼ï¼çå°è³ææéº¼ééç¶²é èå¨ç¯é»ç¶²è·¯äºåã

## ç¯é»


è·æ¸¬è©¦ç¶²è·¯

```
geth --goerli
```

æ°´é¾é ­ https://goerli-faucet.slock.it/


## é¨ç½²åç´

1. å®è£ Solidity



å¾ç°¡å®ç Solidity
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

## Demo ç¶²é 

ethers.js å¥ä»¶
```
wget https://cdn.ethers.io/lib/ethers-5.0.esm.min.js
```


## å¨ç¶²é ä¸é¡¯ç¤ºåç´å§çè³æ


ç¶²é  code

```
<html>

<head> </head>

<body>
    <script type="module">
        import { ethers } from "./ethers-5.0.esm.min.js";
        // è®çè¦½å¨ console å¯ä»¥æ¿å° ethers
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

geth å¿é è¦ææ¬éæé

```
geth --http --http.api personal,eth,net,web3  --http.corsdomain '*'
```