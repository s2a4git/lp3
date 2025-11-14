# ✅ **BCT PRACTICAL VIVA NOTES (SPPU BE – LP3)**

**Option B – Medium Detailed, Easy to Remember, Viva-friendly**

---

# **🔵 Practical 1 — Install MetaMask & Study Ether Transaction Cost**

## **Aim**

To install MetaMask browser wallet, connect to a test network, and analyze how much Ether is spent per blockchain transaction.

---

## **Concept Summary**

### **What is MetaMask?**

* A crypto wallet
* A browser extension
* Allows interaction with Ethereum & other EVM blockchains

### **Steps to Install MetaMask**

1. Go to **metamask.io** → Download extension
2. Click **Create Wallet**
3. Set password
4. **Save Secret Recovery Phrase (12 words)**
5. Login

### **Connect to Test Network**

Because real ETH costs money, we use free test ETH.

1. Settings → Networks → Show test networks
2. Select: **Sepolia / Holesky**
3. Use a **Faucet** to get free ETH
   Example: Google *“Sepolia Faucet”*

### **Study Transaction Cost**

Every transaction costs **Gas**, which is paid in Ether.

Formula:

```
Transaction Cost = Gas Used × Gas Price
```

Example:

* Gas used: 21,000
* Gas price: 2 Gwei
  → Cost = 21,000 × 2 Gwei = 42,000 Gwei
  Convert Gwei → ETH → ~0.000042 ETH

---

## **Why Gas is required?**

* To pay miners/validators for computation
* Prevents infinite loops
* Protects network from spam

---

## **Viva Questions**

**Q1. What is MetaMask?**
A browser-based crypto wallet for Ethereum.

**Q2. What is Gas in Ethereum?**
A unit that measures computational cost.

**Q3. Why are test networks used?**
To develop & test without spending real money.

**Q4. What is Gwei?**
A smaller denomination of Ether:
1 ETH = 1,000,000,000 Gwei

**Q5. What affects gas cost?**
Network congestion & complexity of transaction.

---

---

# **🔵 Practical 2 — Create a Wallet Using MetaMask**

## **Aim**

To create a crypto wallet using MetaMask and understand address, public key, private key.

---

## **Concept Summary**

### **Wallet Creation Steps**

1. Install MetaMask
2. Click **Create Wallet**
3. Choose password
4. Backup **Secret Recovery Phrase** safely
5. Wallet is ready → you get a **public address**

---

## **Key Concepts**

### **Public Key**

* Your wallet "username"
* Safe to share
  Example:
  `0xA14b3F…92cF`

### **Private Key**

* Your wallet "password"
* MUST be kept secret
* Anyone who has it can steal your funds

### **Seed Phrase**

* 12-word backup
* Can restore wallet anywhere
* Store offline (never share online)

---

## **Viva Questions**

**Q1. Public vs. Private key?**
Public key is for receiving; private key is for signing transactions.

**Q2. What is a seed phrase?**
A human-readable backup for your wallet.

**Q3. What happens if private key is lost?**
You lose access permanently.

**Q4. Can MetaMask store multiple accounts?**
Yes, unlimited accounts inside the same wallet.

**Q5. Is MetaMask custodial?**
No — user controls private keys.

---

---

# **🔵 Practical 3 — Smart Contract (Bank Account) on Test Network**

## **Aim**

To write and deploy a smart contract that supports:

* Deposit money
* Withdraw money
* Check balance

---

## **Minimal, Easy-to-Remember Code**

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Bank {
    mapping(address => uint256) public balance;

    function deposit() public payable {
        balance[msg.sender] += msg.value;
    }

    function withdraw(uint256 amt) public {
        require(balance[msg.sender] >= amt, "Not enough balance");
        balance[msg.sender] -= amt;
        payable(msg.sender).transfer(amt);
    }

    function getBalance() public view returns(uint256) {
        return balance[msg.sender];
    }
}
```

---

## **Deployment Steps (Remix + MetaMask)**

1. Open **remix.ethereum.org**
2. Create a new `.sol` file
3. Paste contract
4. Compile
5. Deploy using “Injected Provider” (MetaMask)
6. Use Sepolia test ETH to run deposit/withdraw

---

## **Viva Questions**

**Q1. What is `msg.sender`?**
Address of the user calling the function.

**Q2. What is `msg.value`?**
Amount of Ether sent with a transaction.

**Q3. Why use `payable`?**
Allows function to receive Ether.

**Q4. What is `mapping`?**
Data structure for key–value storage.

**Q5. Why require() is used?**
To validate conditions and revert on error.

---

---

# **🔵 Practical 4 — Student Data Contract (Structures, Arrays, Fallback)**

## **Aim**

To create a smart contract with:

* Structure
* Array
* Fallback function

---

## **Minimal Easy Code**

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {

    struct Student {
        string name;
        uint256 roll;
        uint256 marks;
    }

    Student[] public students;

    function addStudent(string memory name, uint256 roll, uint256 marks) public {
        students.push(Student(name, roll, marks));
    }

    // Fallback function (runs when no function matches)
    fallback() external payable {}

    // Receive Ether
    receive() external payable {}
}
```

---

## **Gas Analysis**

When deployed:

* Deployment cost = high (creates contract storage)
* addStudent() → costs more because writing to storage is expensive
* fallback() → cheapest

---

## **Viva Questions**

**Q1. What is `struct`?**
User-defined data type grouping multiple fields.

**Q2. Why arrays in smart contracts?**
To store multiple student entries.

**Q3. What is a fallback function?**
Runs when:

* function doesn't exist
* wrong data sent

**Q4. Difference: fallback vs. receive?**

* **receive()** → called when ETH is sent without data
* **fallback()** → called when data is present or no receive()

**Q5. Why gas increases when modifying storage?**
Storage operations cost more than memory operations.

---

---

# **🔵 Practical 6 — Hyperledger Business Network**

## **Aim**

To create a simple business network using Hyperledger Fabric / Composer.

---

## **Concept Summary**

### **What is Hyperledger?**

A permissioned blockchain framework for enterprise-level solutions.

### **Components of Hyperledger Fabric**

* **Peers** – maintain ledger
* **Orderer** – handles transaction ordering
* **Chaincode** – smart contract logic
* **Channel** – private blockchain between participants
* **CA (Certificate Authority)** – identity management

---

# **Steps to Create a Business Network Using Hyperledger Composer**

1. **Install prerequisites**

   * Node.js
   * Docker
   * Hyperledger Fabric binaries
   * Composer CLI

2. **Create a Business Model File (`.cto`)**
   Example:

   ```
   namespace org.store

   asset Product identified by productId {
     o String productId
     o String name
     o Double price
   }

   participant User identified by userId {
     o String userId
     o String name
   }

   transaction Purchase {
     --> User buyer
     --> Product product
   }
   ```

3. **Write Transaction Logic (`logic.js`)**

   ```
   async function Purchase(tx) {
       console.log(tx.buyer.name + " bought " + tx.product.name);
   }
   ```

4. **Deploy Network**

   * `composer network install`
   * `composer network start`

5. **Interact Using Playground GUI**

   * Create assets
   * Add participants
   * Submit transactions

---

## **Viva Questions**

**Q1. What is Hyperledger Fabric?**
A permissioned blockchain for enterprise use cases.

**Q2. What is Chaincode?**
Smart contract code in Fabric.

**Q3. What is a Channel?**
Private communication layer between specific members.

**Q4. Difference between Ethereum & Hyperledger?**

* Ethereum → public, crypto-based
* Hyperledger → private, enterprise, permissioned

**Q5. Why does Fabric not use cryptocurrency?**
Because enterprises want predictable cost and controlled access.
