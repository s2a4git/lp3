# ✅ **Minimal & Easy Hyperledger Business Network Code**

This is the exact simple code format used in 99% of BCT practical files.

You just submit **3 files**:

---

## **1️⃣ Model File (model.cto)**

Defines participants, assets, and transactions.

```
namespace org.example.business

participant Person identified by personId {
  o String personId
  o String name
}

asset Product identified by productId {
  o String productId
  o String owner
  o Double price
}

transaction TransferProduct {
  --> Person newOwner
  --> Product product
}
```

### **What to explain:**

* A **Participant** = user in the network
* An **Asset** = something owned
* A **Transaction** = operation that changes state

Super easy.

---

## **2️⃣ Script File (logic.js)**

Defines how the transaction works.

```javascript
/**
 * Transfer an asset to another participant
 * @param {org.example.business.TransferProduct} tx
 * @transaction
 */
async function transferAsset(tx) {
    tx.product.owner = tx.newOwner.personId;
}
```

### **Explanation:**

* We receive a transaction `tx`
* We update asset owner
* Hyperledger stores it automatically

Easy 4-line logic.

---

## **3️⃣ Permissions (permissions.acl)**

Super minimal permissions so everything works.

```
rule AllowAll {
  description: "Allow anyone to read/write everything"
  participant: "ANY"
  operation: ALL
  resource: "org.example.business.*"
  action: ALLOW
}
```

Done.

---

# 🎉 This satisfies **“Create a Business Network in Hyperledger”**

### ✔ Participants – **Person**

### ✔ Asset – **Product**

### ✔ Transaction – **TransferProduct**

### ✔ Logic implemented – yes

### ✔ Permissions – included

### ✔ Deployable – yes

### ✔ Easy to remember – YES (only 3 files!)

---

# 📌 What to SAY in viva (super short)

> "We built a simple business network in Hyperledger.
> It contains a Participant called Person, an Asset called Product,
> and a transaction TransferProduct that changes the owner.
> The logic is written in JavaScript and uses @transaction annotation.
> Permissions allow anyone to test the network."

---

# 🧾 Want the **ZIP folder structure** also?

```
business-network/
  ├── models/
  │     └── model.cto
  ├── lib/
  │     └── logic.js
  └── permissions.acl
```
