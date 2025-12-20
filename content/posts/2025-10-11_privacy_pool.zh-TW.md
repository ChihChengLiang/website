---
title: "[備份] 隱私池的設計"
date: 2025-10-11
draft: false
---

本文刊載在 [Taipei Ethereum Meetup 專欄](https://medium.com/taipei-ethereum-meetup/privacy-pool-0143430da59c)，此篇為備份。

*感謝 TEM 審稿者 Kevin, Kimi, Nic 的細心審閱。*

最近在參加鐵人賽，寫了有關龍捲風現金（Tornado Cash），以及其繼任者隱私池（Privacy Pool）的文章。 [^ithome_1] [^ithome_2]

鐵人賽的文章比較摘要式的談，但這篇想看一些原始碼的細節。

讀者若有具備龍捲風現金的一些基礎知識，會比較能欣賞隱私池的細節。但如果沒有的話也沒關係，可以看一下簡介。

## 簡介

龍捲風現金是一種打斷幣流的混幣器，目的是讓使用者得到「鏈上」的隱私。合約只有「存款」和「提款」兩個函式。使用者把一筆金額，例如一顆以太幣，存入龍捲風現金合約。過了一段時間之後，也許幾個月，再從合約提款。人們只能知道提款者是眾多存款者之一，但除非有其他已知暴露的資訊，沒辦法知道提款者具體是哪個存款者。

提款的交易中，合約會檢查提款者送出的零知識證明。通過這個檢查，代表提款者曾經存款，且不曾提款過。

背後用到的密碼學就是雜湊函式和零知識證明。

雜湊函式可以用一些合理的方式層層包裝，例如 `f(x) = keccak(keccak(x))` 或 `g(x) = keccak(a, b, c, keccak(x))`（其中 a, b, c 是常數），這些函式 f, g 都會針對 x 產生出不會撞號的雜湊值。雖然 f 和 g 都用了 keccak ，但 f 和 g 可以「視為」兩種不同的雜湊函式。

想像我們有兩種雜湊函式，hash1 和 hash2 。使用者有個秘密的隨機值 `random` 。這個隨機值必須從夠大的空間抽樣（例如： 128 位元），讓攻擊者無法用電腦暴力搜索，從雜湊值反推隨機值的數字。

- 存款：留下 `hash1(random)`
- 提款：留下 `hash2(random)`

外人無法從雜湊值 `hash1(random)` 與 `hash2(random)` 得知兩者的關聯。

因此使用者在提款時：

1. 合約先檢查 `hash2(random)`不曾出現過，確認該使用者尚未提款。
2. 迴路以私密參數接收 `hash1(random)`，以公開參數接收 `hash2(random)`
3. 迴路驗證 `hash1(random)` 與 `hash2(random)` 背後的隨機值是相同的。這樣驗證存提款是同一個人，卻又不揭露存款者的資訊。
4. 最後合約把 `hash2(random)` 記錄在鏈上。這樣重複提款時，在步驟一就會失敗。

`hash2(random)` 像是在存款名單上，把提款過的人的名字劃掉，但劃掉了誰只有提款者知曉。

## 龍捲風現金的問題

龍捲風現金的設計是任何人都可以使用，這造成了一些問題。駭客攻擊完合約或交易所後，盜取的幣會往龍捲風現金跑，造成日後追緝不易。

既然壞人可能從龍捲風現金出來，交易所就不收從龍捲風現金出來的幣。

因應這種現況，龍捲風現金開發團隊提供一個所謂「[合規工具](https://docs.torn.cash/tornado-cash-classic/compliance-tool)」，讓使用者可以對交易所提出零知識證明，去證明自己從龍捲風現金出來的幣，來源是哪個存款地址。讀者可以看出來，使用「合規工具」，就相當於失去使用龍捲風現金的意義。

Vitalik 和 Ameen Soleimani 等人，在 2023 年發表一篇 [論文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4563364)，提出名為 **隱私池（Privacy Pool）** 的設計。其實也就是改良龍捲風現金，並在背後加上一個人工維護的名單，稱作 **關聯集（Association Set）** 。這個名單的設計可以是允許名單或拒絕名單。提款時得先證明自己在允許名單中，或不在拒絕名單中。人們可以去設計自己的名單，看想要美國合規、歐盟合規、或中國合規都可以。

## 隱私池

2025 三月 0xbow 團隊部署了正式版的隱私池 https://privacypools.com/ 。

其中關聯集的運作方式是允許名單，在存款打入隱私池合約之後，需要等一陣子。**關聯集提供者（Association Set Provider, ASP）** 會把存款的標籤加到允許名單中。名單在密碼學中，是以雜湊樹表達，在迴路中用雜湊樹根與成員證明即可。

### 怒退

隱私池因為增加了關聯集，讓提款不再是無條件能發生。這有一個新問題：那萬一使用者存款了，卻被標記無法提款，錢卡在合約裡怎麼辦？

這有兩種情況：一種是使用者存款後，被標記為不合規了，不給放到允許清單裡。另一種可能是，使用者已經存款，並提款數次了，但突然被從允許清單移除。

因應這些情況，隱私池也設計了 **怒退（Ragequit）** 功能。在被清單排除後，使用者可以怒退存款，放棄清理蹤跡並取回自己的餘額。但使用者必須記得第一次存款時是用哪個帳號存的，資產只能回去原來那個地址。否則壞人可以利用怒退來變相清理金流足跡。

### 支持不同存提款金額

龍捲風現金同一個幣種，會分三個固定額度的池子，例如 1 ETH, 10 ETH, 100 ETH，並規定存提款就是該固定的額度。目的是為了避免金額差異暴露存提款者的身份。

在固定額度之下， 假設在 1 ETH 的池子內有 300 人存款，匿名集的大小就是 300 人。 300 人的意思是任何一個最新的提款者，他可能是這 300 人的其中一人，匿名集越大就越難猜中提款者是誰。要挑惕一點的話可以把匿名集扣掉已知曝光的存款者與提款者身份連結。

隱私池解放了這個限制，設計了 **部分提款功能** ，這讓存款和提款都不再是固定的額度。使用者可以存一大筆金額到合約裡，並每次少量取出。這樣每次取出的部分，可以有各自獨立的足跡。以往一筆大金額就只能有一筆足跡，想要有獨立足跡，必須切碎再重新過合約。

缺點也很明顯：假設池裡共五個人，前面四個都存 1 ETH ，就第五個存了 100 ETH 。如果第五個使出部分提款 2 ETH ，那就從這五個裡面曝光了。

曝光小明並不只是害到他本人。原本其他人享有 5 人的匿名集，現在因為小明的行為，匿名集變成 4 人了。

因此，在一個千餘人存款的池子裡，有各種不同存提款的金額之下，要計算匿名集的大小並不如固定額度的龍捲風現金單純容易。

不同提款金額帶來了一些方便，卻也讓理清匿名集有多大這件事變困難了。

## 程式碼實作

這邊的分析會以 [v1.1.1](https://github.com/0xbow-io/privacy-pools-core/tree/v1.1.1) 版本為主。

專案的零知識證明，[仍用](https://github.com/0xbow-io/privacy-pools-core/blob/v1.1.1/packages/circuits/circomkit.json) Circom 語言，配 Groth16 架構，與適用以太坊預編譯能驗證的 bn128 曲線驗證。

### 雜湊函式

主要的雜湊函式用迴路友善的 Poseidon 雜湊函式。最近發現 TACEO 有一個 [推文](https://x.com/TACEO_IO/status/1969371023343784155/photo/1) 講怎麼在五花八門的雜湊函式中選擇想要的。

因為 Groth16 使用的是算數迴路，開發者只能使用整數加法和乘法去表達程式的邏輯。 Poseidon 是專門為算數迴路設計的雜湊函式，因為只有用加法與乘法構成，所以在迴路中使用的成本很低。但有些小個性：他只能吃固定數量的參數，所以會看到有 Poseidon(2) 或 Poseidon(3) 之類的區分，前者只能吃兩個參數，後者三個。

迴路或合約中也會看到 keccak 雜湊函式，目前看起來這是拿來得到標籤用的。keccak 是在 EVM 環境中非常便宜。

從一些前人的 [評測](https://eprint.iacr.org/2023/681.pdf) [來看](https://github.com/chancehudson/poseidon-solidity)：

- 在 EVM 中，也就是合約中，成本以燃氣 gas 計算
  - keccak 起步價 30 gas ，之後每吸收 32 位元輸入 消耗 6 gas
  - poseidon 大概一個參數 10,000 gas （circomlibjs [實作](https://github.com/iden3/circomlibjs/blob/4f094c5be05c1f0210924a3ab204d8fd8da69f49/src/poseidon_gencontract.js#L23) （以 JavaScript 撰寫 EVM 操作碼））
- 在迴路中，成本是消耗多少條限制式
  - keccak      151,357
  - poseidon        240

整體而言，keccak 在合約超便宜，迴路中爆貴。 poseidon 則反過來。

### 雜湊樹

雜湊樹是用 PSE 團隊開發出來的 [LeanIMT](
https://github.com/zk-kit/zk-kit.solidity/blob/main/packages/lean-imt/contracts/InternalLeanIMT.sol) ，主要是可以在鏈上增長樹，並且節省燃氣。

## 迴路

迴路有三個檔案，我們會略過 `merkleTree.circom`

### commmitment.circom

這段就是計算 存款與提款分別留下來的雜湊值。**註銷符（nullifier）** 是一個夠大的隨機數，連結了這兩個雜湊值。

- 存款留下 `Poseiden(value, label, Poseidon(nullifier, secret))` （可以看成 `hash1(nullifier)`）
- 提款留下 `Poesidon(nullifier)`  （可以看成 `hash2(nullifier)`）

其中 label 是拿來辨識這筆存款用的標籤。會有池子的代號 pool_scope 與 第幾個存款 nonce 。label 後面註解為 `keccak256(pool_scope, nonce) % SNARK_SCALAR_FIELD` 。注意 EVM 裡面是 32 位元組為一字，而迴路裡面加減乘除的結果得對一個 254 位元的巨大整數 `SNARK_SCALAR_FIELD` 取餘數。如果一個數字同時要拿來餵合約和迴路，要記得取餘數，不然合約裡面可以有多個數字對應到一樣的迴路數字，有攻擊空間。

```circom
pragma circom 2.2.0;

include "../../../node_modules/circomlib/circuits/poseidon.circom";

/**
 * @title CommitmentHasher template
 * @dev Template for computing commitment hashes, precommitments and nullifier hashes
 */
template CommitmentHasher() {

  //////////////////////// SIGNALS ////////////////////////

  signal input value;              // Value of commitment
  signal input label;              // keccak256(pool_scope, nonce) % SNARK_SCALAR_FIELD
  signal input nullifier;          // Nullifier of commitment
  signal input secret;             // Secret of commitment

  signal output commitment;        // Commitment hash
  signal output nullifierHash;     // Nullifier hash

  ///////////////////// END OF SIGNALS /////////////////////

  // 1. Compute nullifier hash
  component nullifierHasher = Poseidon(1);
  nullifierHasher.inputs[0] <== nullifier;

  // 2. Compute precommitment
  component precommitmentHasher = Poseidon(2);
  precommitmentHasher.inputs[0] <== nullifier;
  precommitmentHasher.inputs[1] <== secret;

  // 3. Compute commitment hash
  component commitmentHasher = Poseidon(3);
  commitmentHasher.inputs[0] <== value;
  commitmentHasher.inputs[1] <== label;
  commitmentHasher.inputs[2] <== precommitmentHasher.out;

  // 4. Populate output signals
  commitment <== commitmentHasher.out;
  nullifierHash <== nullifierHasher.out;
}
```
### withdraw.circom

提款迴路算是迴路中的核心。

部分提款功能的實作，只是單純在存款束縛（Commitment）中，記載存入的金額。提款時做以下事情：

- 檢查提款金額必須小於存款餘額。
- 剩餘的存款，製造一個新的存款束縛，放回存款樹。（後面合約處理）
- 用註銷符雜湊值註銷舊的存款束縛。（合約記得註銷符雜湊值）
- 對於關聯集，也只是在迴路中多放一顆樹，檢查存款標籤的成員證明。

有個有趣的點是提款者的資訊。以往龍捲風現金，有 [四個相關變數](https://github.com/tornadocash/tornado-core/blob/1ef6a263ac6a0e476d063fcb269a9df65a1bd56a/circuits/withdraw.circom#L54-L64)：提款金額的收受地址 `_recipient`、中繼人小費收受者 `_relayer`、小費金額 `_fee` 、還有一個和 ERC20 有關的 `_refund` 。在龍捲風現金的提款迴路結尾，對四個變數做了沒有意義的平方乘法，意圖是用合約綁定四個變數，好像簽章的效果。

龍捲風現金，預設提款者是倚賴第三方中繼人。這是因為和合約互動要繳手續費，因此提款帳戶需要有以太幣。若想要提款到完全空白的新地址，可以請中繼人幫忙。提款者在零知識證明中咬住中繼人的地址與要給他們的小費，這樣可以避免中繼人的小費被中途打劫。

隱私池捨棄龍捲風現金那種把收受地址、中繼人、小費金額等欄位資訊寫死在迴路裡的做法。那些資訊會在合約被檢查，但在迴路內不會用到。隱私池把提款需要的資訊抽象成下列提款結構（`struct Withdrawal`）。在隱私池的提款迴路內，需要「簽章」的資訊變成提款結構的 keccak 雜湊值，賦值給 `context` 變數。

```solidity
struct Withdrawal {
  address processooor;
  bytes data;
}
```

提款結構中，諧謔稱為處理者（processooor）的地址，可以是實際的提款者或某個合約。提款結構有個資料欄位，可以打包任意資訊。隱私池可以自行提款，也能委託中繼人幫忙。我們後面合約可以看到怎麼做。

這樣做的好處有兩種：第一是中繼業務所需要的資訊抽象掉了，不用寫死在迴路裡面。合約裡可以做很靈活的設計。

第二是在合約中，檢查零知識證明所需的公開輸入（Public Input）變少了。在驗證 Groth16 證明的合約中，每多一個公開輸入的參數，會需要多做一個橢圓曲線的常數乘法和加法。（大概消耗 [數千 gas](https://www.evm.codes/precompiled?fork=cancun#0x07) ）

```circom
pragma circom 2.2.0;

include "./commitment.circom";
include "./merkleTree.circom";
include "../../../node_modules/circomlib/circuits/comparators.circom";

/**
 * @title Withdraw template
 * @dev Template for withdrawing value from a commitment
 * @param maxTreeDepth The maximum depth of the Merkle trees
 */
template Withdraw(maxTreeDepth) {

  //////////////////////// PUBLIC SIGNALS ////////////////////////

  // Signals to compute commitments
  signal input withdrawnValue;                   // Value being withdrawn

  // Signals for merkle tree inclusion proofs
  signal input stateRoot;                        // A known state root
  signal input stateTreeDepth;                   // Current state tree depth
  signal input ASPRoot;                          // Latest ASP root
  signal input ASPTreeDepth;                     // Current ASP tree depth
  signal input context;                          // keccak256(IPrivacyPool.Withdrawal, scope) % SNARK_SCALAR_FIELD

  //////////////////// END OF PUBLIC SIGNALS ////////////////////


  /////////////////////// PRIVATE SIGNALS ///////////////////////

  // Signals to compute commitments
  signal input label;                            // keccak256(scope, nonce) % SNARK_SCALAR_FIELD
  signal input existingValue;                    // Value of the existing commitment
  signal input existingNullifier;                // Nullifier of the existing commitment
  signal input existingSecret;                   // Secret of the existing commitment
  signal input newNullifier;                     // Nullifier for the new commitment
  signal input newSecret;                        // Secret for the new commitment

  // Signals for merkle tree inclusion proofs
  signal input stateSiblings[maxTreeDepth];      // Siblings of the state tree
  signal input stateIndex;                       // Indices for the state tree
  signal input ASPSiblings[maxTreeDepth];        // Siblings of the ASP tree
  signal input ASPIndex;                         // Indices for the ASP tree

  /////////////////// END OF PRIVATE SIGNALS ///////////////////


  /////////////////////// OUTPUT SIGNALS ///////////////////////

  signal output newCommitmentHash;               // Hash of new commitment
  signal output existingNullifierHash;           // Hash of the existing commitment nullifier

  /////////////////// END OF OUTPUT SIGNALS ///////////////////

  // 1. Compute existing commitment
  component existingCommitmentHasher = CommitmentHasher();
  existingCommitmentHasher.value <== existingValue;
  existingCommitmentHasher.label <== label;
  existingCommitmentHasher.nullifier <== existingNullifier;
  existingCommitmentHasher.secret <== existingSecret;
  signal existingCommitment <== existingCommitmentHasher.commitment;

  // 2. Output existing nullifier hash
  existingNullifierHash <== existingCommitmentHasher.nullifierHash;

  // 3. Verify existing commitment is in state tree
  component stateRootChecker = LeanIMTInclusionProof(maxTreeDepth);
  stateRootChecker.leaf <== existingCommitment;
  stateRootChecker.leafIndex <== stateIndex;
  stateRootChecker.siblings <== stateSiblings;
  stateRootChecker.actualDepth <== stateTreeDepth;

  stateRoot === stateRootChecker.out;

  // 4. Verify label is in ASP tree
  component ASPRootChecker = LeanIMTInclusionProof(maxTreeDepth);
  ASPRootChecker.leaf <== label;
  ASPRootChecker.leafIndex <== ASPIndex;
  ASPRootChecker.siblings <== ASPSiblings;
  ASPRootChecker.actualDepth <== ASPTreeDepth;

  ASPRoot === ASPRootChecker.out;

  // 5. Check the withdrawn amount is valid
  signal remainingValue <== existingValue - withdrawnValue;
  component remainingValueRangeCheck = Num2Bits(128);
  remainingValueRangeCheck.in <== remainingValue;
  _ <== remainingValueRangeCheck.out;
  component withdrawnValueRangeCheck = Num2Bits(128);
  withdrawnValueRangeCheck.in <== withdrawnValue;
  _ <== withdrawnValueRangeCheck.out;

  // 6. Check existing and new nullifier don't match
  component nullifierEqualityCheck = IsEqual();
  nullifierEqualityCheck.in[0] <== existingNullifier; 
  nullifierEqualityCheck.in[1] <== newNullifier; 
  nullifierEqualityCheck.out === 0;

  // 7. Compute new commitment
  component newCommitmentHasher = CommitmentHasher();
  newCommitmentHasher.value <== remainingValue;
  newCommitmentHasher.label <== label;
  newCommitmentHasher.nullifier <== newNullifier;
  newCommitmentHasher.secret <== newSecret;

  // 8. Output new commitment hash
  newCommitmentHash <== newCommitmentHasher.commitment;
  _ <== newCommitmentHasher.nullifierHash;

  // 9. Square context for integrity
  signal contextSquared <== context * context;
}
```

## 合約

可以直接看到 PrivacyPool.sol

### 存款

存款的部分，使用者把私下算好的雜湊值 `_precommitmentHash = Poseidon(nullifier, secret)` 傳給合約，並繳納存款。

合約會自動幫使用者產生新的標籤。合約會需要把標籤記下來（放 depositors 變數），日後怒退會用到。

其他功能和舊的龍捲風現金差不多，包含把存款束縛放到合約維護的雜湊樹中，以及從使用者身上取得存款。

這邊比較混淆的可能是 PoseidonT4 這個寫法，雖然名稱裡有 4 ，但實際上只吃三個參數。 PoseidonTX 只能收納 X-1 個參數，這是論文留下來的奇怪慣例。

```solidity
  /// PrivacyPool.sol
  function deposit(
    address _depositor,
    uint256 _value,
    uint256 _precommitmentHash
  ) external payable onlyEntrypoint returns (uint256 _commitment) {
    // Check deposits are enabled
    if (dead) revert PoolIsDead();

    if (_value >= type(uint128).max) revert InvalidDepositValue();

    // Compute label
    uint256 _label = uint256(keccak256(abi.encodePacked(SCOPE, ++nonce))) % Constants.SNARK_SCALAR_FIELD;
    // Store depositor
    depositors[_label] = _depositor;

    // Compute commitment hash
    _commitment = PoseidonT4.hash([_value, _label, _precommitmentHash]);

    // Insert commitment in state (revert if already present)
    _insert(_commitment);

    // Pull funds from caller
    _pull(msg.sender, _value);

    emit Deposited(_depositor, _commitment, _label, _value, _precommitmentHash);
  }
```

### 自行提款

這邊的提款函式是給不委託中繼人的提款者使用的。提款人要自己付燃氣手續費。

驗過證明之後，合約記得註銷符雜湊值，以及把剩餘的餘額做一筆新存款。

```solidity
  /// PrivacyPool.sol
  function withdraw(
    Withdrawal memory _withdrawal,
    ProofLib.WithdrawProof memory _proof
  ) external validWithdrawal(_withdrawal, _proof) {
    // Verify proof with Groth16 verifier
    if (!WITHDRAWAL_VERIFIER.verifyProof(_proof.pA, _proof.pB, _proof.pC, _proof.pubSignals)) revert InvalidProof();

    // Mark existing commitment nullifier as spent
    _spend(_proof.existingNullifierHash());

    // Insert new commitment in state
    _insert(_proof.newCommitmentHash());

    // Transfer out funds to procesooor
    _push(_withdrawal.processooor, _proof.withdrawnValue());

    emit Withdrawn(
      _withdrawal.processooor, _proof.withdrawnValue(), _proof.existingNullifierHash(), _proof.newCommitmentHash()
    );
  }
```

驗證的部分，分為迴路的驗證與合約的驗證。前者以另外部署的 `WITHDRAWAL_VERIFIER` 合約，做驗證 groth16 證明必要的橢圓曲線運算。後者以 `validWithdrawal` 修飾子去做。

裡面得檢查：

- 合約交易的發送方，確實是零知識證明中 context 變數所綁定的處理人 processooor 。如果沒檢查這件事，其他人可以複製證明內容，並劫持提款到其他地址。
- 檢查零知識證明中所綁定的存款樹（他們稱狀態樹 state tree）的樹根，有在合約紀錄之中
- 檢查零知識證明中所綁定的關聯集樹根，也有在合約紀錄之中

合約會滾動記錄雜湊樹的樹根。因為提款者在產生提款證明時，可能其他存款者也在存款。因此合約不能只記得一個樹根，而是要記得一段時間的樹根，才不會提款交易發出的時候，樹根都過期了。

```solidity
  /// PrivacyPool.sol
  modifier validWithdrawal(Withdrawal memory _withdrawal, ProofLib.WithdrawProof memory _proof) {
    // Check caller is the allowed processooor
    if (msg.sender != _withdrawal.processooor) revert InvalidProcessooor();

    // Check the context matches to ensure its integrity
    if (_proof.context() != uint256(keccak256(abi.encode(_withdrawal, SCOPE))) % Constants.SNARK_SCALAR_FIELD) {
      revert ContextMismatch();
    }

    // Check the tree depth signals are less than the max tree depth
    if (_proof.stateTreeDepth() > MAX_TREE_DEPTH || _proof.ASPTreeDepth() > MAX_TREE_DEPTH) revert InvalidTreeDepth();

    // Check the state root is known
    if (!_isKnownRoot(_proof.stateRoot())) revert UnknownStateRoot();

    // Check the ASP root is the latest
    if (_proof.ASPRoot() != ENTRYPOINT.latestRoot()) revert IncorrectASPRoot();
    _;
  }
```

### 委託提款

在委託提款的情境中，提款者會指定中繼人，並約定好手續費。產好證明後，由中繼人對合約發起交易。

前述 `Withdrawal` 提款結構中的 processooor 值，會是 `Entrypoint.sol` 的地址，原因我們後面解釋。而 data 欄位值，則是下列中繼資料的序列化。

```solidity
  struct RelayData {
    address recipient; /// The recipient of the funds withdrawn from the pool
    address feeRecipient; /// The recipient of the fee
    uint256 relayFeeBPS; /// The relay fee in basis points
  }
```

`recipient` 會是提款人的地址。`feeRecipient` 則是中繼者。最後費用則是以基點(basis points, bp) 計算。 100 bp 是收提款金額 1% 的意思， 50 bp 是 0.5% 。

中繼提款的函式長在 `Entrypoint.sol` 合約。這個合約管理眾多不同資產的池子。

注意合約開頭有個 `if (_withdrawal.processooor != address(this)) revert InvalidProcessooor();` ，檢查處理者必須是這個合約的地址。

接著 relay 函式會先以合約的身份呼叫池子的提款函式 `_pool.withdraw(_withdrawal, _proof);` 。這一步會先把錢提到合約這邊，然後再切分成小費與剩餘提款額度，分別給予中繼人與提款者。

（那步驟我第一次看時一度卡住，覺得怎麼錢被提了兩次。 withdraw 函式裡 _push 了一次，relay 函式裡又 _transfer 一次）

可以觀察 `_data` 結構是怎麼從提款結構的資料欄位解構出來的。

```solidity
  /// Entrypoint.sol
  function relay(
    IPrivacyPool.Withdrawal calldata _withdrawal,
    ProofLib.WithdrawProof calldata _proof,
    uint256 _scope
  ) external nonReentrant {
    // Check withdrawn amount is non-zero
    if (_proof.withdrawnValue() == 0) revert InvalidWithdrawalAmount();
    // Check allowed processooor is this Entrypoint
    if (_withdrawal.processooor != address(this)) revert InvalidProcessooor();

    // Fetch pool by scope
    IPrivacyPool _pool = scopeToPool[_scope];
    if (address(_pool) == address(0)) revert PoolNotFound();

    // Store pool asset
    IERC20 _asset = IERC20(_pool.ASSET());
    uint256 _balanceBefore = _assetBalance(_asset);

    // Process withdrawal
    _pool.withdraw(_withdrawal, _proof);

    // Decode relay data
    RelayData memory _data = abi.decode(_withdrawal.data, (RelayData));

    if (_data.relayFeeBPS > assetConfig[_asset].maxRelayFeeBPS) revert RelayFeeGreaterThanMax();

    uint256 _withdrawnAmount = _proof.withdrawnValue();

    // Deduct fees
    uint256 _amountAfterFees = _deductFee(_withdrawnAmount, _data.relayFeeBPS);

    uint256 _feeAmount = _withdrawnAmount - _amountAfterFees;

    // Transfer withdrawn funds to recipient
    _transfer(_asset, _data.recipient, _amountAfterFees);
    // Transfer fees to fee recipient
    _transfer(_asset, _data.feeRecipient, _feeAmount);

    // Check pool balance has not been reduced
    uint256 _balanceAfter = _assetBalance(_asset);
    if (_balanceBefore > _balanceAfter) revert InvalidPoolState();

    emit WithdrawalRelayed(msg.sender, _data.recipient, _asset, _withdrawnAmount, _feeAmount);
  }
```

### 怒退

使用者在遲遲沒辦法得到關聯集提供者的許可時，可以怒退款。做法是產生零知識證明，並呼叫 ragequit 函式。

怒退使用了 commitment.circom 這個迴路，並把 `value` 和 `label` 這兩個輸入值 [設為公開](https://github.com/0xbow-io/privacy-pools-core/blob/7bc392dad5fa483f53cf74e25d7ad19f0fc6d85f/packages/circuits/src/index.ts#L12-L16)。輸出值 `commitmentHash` `nullifierHash` 也是公開的。

合約中的 `ProofLib.RagequitProof` 這個參數結構（欄位沒列在本文），裡面檢查 `commitmentHash` `nullifierHash` `value` `label` 四個公開參數。

合約中，要檢查怒退者地址確實是當時的存款地址，用 `depositors[_label]` 這個變數。

注意提款迴路中，新與舊的存款束縛皆會分享同一個標籤。因此即使提款多次，合約中留下來最新的存款束縛，其 `label` 會是一樣的。因此怒退時，可以用帶有最新餘額的存款束縛，與 `depositors[_label]` 作比較。

如果沒有要求原始存款地址這個條件的話，會發生什麼事呢？可以知道的是，怒退者可以使用其他地址進行怒退。但怒退者有沒有辦法變相借怒退，達成清理蹤跡的提款效果？理論上應該不可行，因為有效的零知識證明會咬著 `label` ，暴露當時的存款束縛，也就把當時存款地址的關係綁在一起。

推測要求原始存款地址，可能只是實務上想避免無謂的分析成本。

```solidity
  /// PrivacyPool.sol
  function ragequit(ProofLib.RagequitProof memory _proof) external {
    // Check if caller is original depositor
    uint256 _label = _proof.label();
    if (depositors[_label] != msg.sender) revert OnlyOriginalDepositor();

    // Verify proof with Groth16 verifier
    if (!RAGEQUIT_VERIFIER.verifyProof(_proof.pA, _proof.pB, _proof.pC, _proof.pubSignals)) revert InvalidProof();

    // Check commitment exists in state
    if (!_isInState(_proof.commitmentHash())) revert InvalidCommitment();

    // Mark existing commitment nullifier as spent
    _spend(_proof.nullifierHash());

    // Transfer out funds to ragequitter
    _push(msg.sender, _proof.value());

    emit Ragequit(msg.sender, _proof.commitmentHash(), _proof.label(), _proof.value());
  }
```

合約裡面，有趣的小細節大概是因為從存款樹裡找 commitmentHash 在怒退情境中沒有隱私需求，所以可以直接在 EVM 裡用 mapping 找。

## 關聯集

一直想了解隱私池怎麼處理關聯集和存款樹。

要產出提款迴路的證明，必須做出關聯集和存款樹的雜湊樹成員證明。迴路裡的變數要有樹根、自己的樹葉、以及必要的中間節點。

一般而言，必須先取得所有的葉子，再從所有的葉子算出需要的東西。

存款樹的話，因為其建構都在合約中進行，插入新葉子時，也會釋出事件（Events）。跑節點的人可以監聽事件去取得所有的葉子。沒跑節點的人，印象以往龍捲風現金是跟 web3 提供者（provider）拉事件回來。

關聯集的話，合約中僅有授權人士可以更新樹根，並會附上 IPFS CID。這些都沒什麼嚴格的檢查，全憑良心。

```solidity
  /// Entrypoint.sol
  function updateRoot(uint256 _root, string memory _ipfsCID) external onlyRole(_ASP_POSTMAN) returns (uint256 _index) {
    // Check provided values are non-zero
    if (_root == 0) revert EmptyRoot();
    uint256 _cidLength = bytes(_ipfsCID).length;
    if (_cidLength < 32 || _cidLength > 64) revert InvalidIPFSCIDLength();

    // Push new association set and update index
    associationSets.push(AssociationSetData(_root, _ipfsCID, block.timestamp));
    _index = associationSets.length - 1;

    emit RootUpdated(_root, _ipfsCID, block.timestamp);
  }
```

目前 [網站程式碼](https://github.com/0xbow-io/privacy-pools-website/blob/8d189574e9bca94ab776bc6e420f6f5bd94e6ba5/src/hooks/useASP.ts#L8) 顯示，提款或怒退的時候，會去打一個 API ，取得所有系統現有的存款葉子和關聯集葉子。

實際用網站操作，並觀察開發者工具的網路分頁（Network tab）。結果發現是打 `https://api.0xbow.io/1/public/mt-leaves` 這個 API ，拉回一個 JSON 物件，分別有關聯集葉子近兩千筆，及存款樹葉子近四千筆。一個葉子 32 位元組，數千筆應該就幾 KB 大小，以前端而言應該也不罪過？

這裡最壞的情況是 API 壞掉了，無法透過網頁下載關聯集和存款樹。人們可以自行跑節點取得存款樹葉子，然後怒退。

### 鏈下隱私

隱私池這類工具目的在於清理鏈上蹤跡。但沒管到鏈下的隱私。因此透過網頁傳送提款需求，似乎還是會透漏 IP 資訊。要與其他工具搭配著用。

目前除了網頁之外，似乎也還沒看到可以自己架設的版本。如果有人有知道或是蓋出來可以分享一下。

## 結語

龍捲風現金與隱私池是我很喜歡的專案。他們迴路和合約夠小，讀起來不會太累，能夠思考各種細節。同時又是個已經正在運作的專案，並產生各種社會衝擊。每次重看都會看到一些之前沒看到的東西。




[^ithome_1]: https://ithelp.ithome.com.tw/articles/10382591
[^ithome_2]: https://ithelp.ithome.com.tw/articles/10383520
