#

## 1) Minimal chaincode: `business-network/contract/lib/businessNetwork.js`

```javascript
'use strict';

const { Contract } = require('fabric-contract-api');

class BusinessNetworkContract extends Contract {

    // Initialize ledger with a demo asset (optional)
    async initLedger(ctx) {
        const asset = {
            assetId: 'asset1',
            owner: 'PARTICIPANT1',
            value: 1000
        };
        await ctx.stub.putState('ASSET_asset1', Buffer.from(JSON.stringify(asset)));
        return 'Initialized';
    }

    // Create a participant (simple representation)
    async createParticipant(ctx, participantId, name) {
        const participant = { participantId, name };
        await ctx.stub.putState('PART_' + participantId, Buffer.from(JSON.stringify(participant)));
        return participant;
    }

    // Read participant
    async readParticipant(ctx, participantId) {
        const data = await ctx.stub.getState('PART_' + participantId);
        if (!data || data.length === 0) {
            throw new Error(`Participant ${participantId} does not exist`);
        }
        return JSON.parse(data.toString());
    }

    // Create an asset owned by a participant
    async createAsset(ctx, assetId, ownerId, value) {
        // check owner exists (optional)
        const ownerData = await ctx.stub.getState('PART_' + ownerId);
        if (!ownerData || ownerData.length === 0) {
            throw new Error(`Owner ${ownerId} not found`);
        }
        const asset = { assetId, owner: ownerId, value: Number(value) };
        await ctx.stub.putState('ASSET_' + assetId, Buffer.from(JSON.stringify(asset)));
        return asset;
    }

    // Read an asset
    async readAsset(ctx, assetId) {
        const data = await ctx.stub.getState('ASSET_' + assetId);
        if (!data || data.length === 0) {
            throw new Error(`Asset ${assetId} does not exist`);
        }
        return JSON.parse(data.toString());
    }

    // Transfer asset to another participant
    async transferAsset(ctx, assetId, newOwnerId) {
        const assetKey = 'ASSET_' + assetId;
        const assetBytes = await ctx.stub.getState(assetKey);
        if (!assetBytes || assetBytes.length === 0) {
            throw new Error(`Asset ${assetId} not found`);
        }
        // check new owner exists
        const ownerBytes = await ctx.stub.getState('PART_' + newOwnerId);
        if (!ownerBytes || ownerBytes.length === 0) {
            throw new Error(`New owner ${newOwnerId} not found`);
        }
        const asset = JSON.parse(assetBytes.toString());
        asset.owner = newOwnerId;
        await ctx.stub.putState(assetKey, Buffer.from(JSON.stringify(asset)));
        return asset;
    }

    // Simple query: list all assets (range query)
    async queryAllAssets(ctx) {
        const startKey = 'ASSET_';
        const endKey = 'ASSET_\uffff';
        const iterator = await ctx.stub.getStateByRange(startKey, endKey);
        const results = [];
        while (true) {
            const res = await iterator.next();
            if (res.value && res.value.value.toString()) {
                const record = JSON.parse(res.value.value.toString('utf8'));
                results.push(record);
            }
            if (res.done) {
                await iterator.close();
                break;
            }
        }
        return results;
    }
}

module.exports = BusinessNetworkContract;
```

> Save file under `business-network/contract/lib/businessNetwork.js`

---

## 2) Minimal `package.json` for the chaincode

```json
{
  "name": "business-network-contract",
  "version": "1.0.0",
  "description": "Minimal Business Network chaincode",
  "main": "lib/businessNetwork.js",
  "scripts": {},
  "dependencies": {
    "fabric-contract-api": "^2.2.0",
    "fabric-shim": "^2.2.0"
  }
}
```

> Place `package.json` in `business-network/contract/`, run `npm install` there before packaging.

---

## 3) Quick deploy & test steps (using Fabric samples `test-network`)

These are the **short, typical commands** to deploy this chaincode to the local test network shipped with Fabric samples. (If you use a managed testnet, use that environment’s deploy steps.)

1. Start test network (from `fabric-samples/test-network`):

```bash
cd fabric-samples/test-network
./network.sh up createChannel -c mychannel -ca
```

2. Package & install chaincode (from your chaincode root where `package.json` is):

```bash
# set variables for convenience (adjust paths)
CC_NAME="businessnetwork"
CC_VERSION="1.0"
CC_LANG="node"
CC_LABEL="${CC_NAME}_${CC_VERSION}"
CC_PATH="/full/path/to/business-network/contract"  # absolute or relative

# create tar.gz package (Fabric v2 packaging format)
peer lifecycle chaincode package ${CC_LABEL}.tar.gz --path ${CC_PATH} --lang ${CC_LANG} --label ${CC_LABEL}
```

3. Install on peer, approve and commit — easiest is to use the `network.sh` deployexample helper or follow Fabric sample steps:

```bash
# The test-network repo includes scripts; a short approach:
# Use the provided script to deploy (example mode) or run the sequence:
./network.sh deployCC -ccn ${CC_NAME} -ccv ${CC_VERSION} -ccl javascript -ccp ${CC_PATH}
```

`network.sh deployCC` handles packaging, installing, approving and committing for you in the sample network.

4. Invoke and query with peer CLI (example):

```bash
# create participant
peer chaincode invoke -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com \
  --tls --cafile "$ORDERER_CA" -C mychannel -n businessnetwork \
  --peerAddresses localhost:7051 --tlsRootCertFiles "$PEER0_ORG1_CA" \
  -c '{"Args":["createParticipant","PARTICIPANT1","Alice"]}'

# create asset
peer chaincode invoke -C mychannel -n businessnetwork -c '{"Args":["createAsset","asset2","PARTICIPANT1","500"]}'

# read asset
peer chaincode query -C mychannel -n businessnetwork -c '{"Args":["readAsset","asset2"]}'

# transfer asset
peer chaincode invoke -C mychannel -n businessnetwork -c '{"Args":["transferAsset","asset2","PARTICIPANT2"]}'
```

> In the `test-network` environment the scripts set environment variables like `ORDERER_CA`. Use the sample `scripts/env.sh` or the `network.sh` helpers to simplify commands. The goal for the practical is to be able to show `createParticipant`, `createAsset`, `readAsset`, and `transferAsset` invocations and their results.

---

## 4) What to explain in viva (short & clear)

* **Contract purpose:** simple Business Network managing participants and assets.
* **Key constructs:**

  * `ctx.stub.putState(key, value)` to write world-state,
  * `ctx.stub.getState(key)` to read world-state,
  * `getStateByRange` used for simple listing.
* **Transactions implemented:**

  * `createParticipant(participantId, name)`
  * `createAsset(assetId, ownerId, value)`
  * `readAsset(assetId)`
  * `transferAsset(assetId, newOwner)`
  * `queryAllAssets()` (list assets)
* **Security / checks:** we check existence (throw error if missing). Production would add access control (ACLs / client identity checks).
* **Deploy & test:** use Fabric test network scripts (`network.sh up` + `deployCC`) and peer invoke/query to show transactions and gas-equivalent info (in Fabric check endorsement / read/write sets and transaction response/gas is not applicable since Fabric isn’t Ethereum — instead show transaction proposal response and block inclusion).
* **Observe network effects:** for Fabric you discuss transaction latency, endorsement policy, block commit, and resource usage. (If they ask for transaction fee/gas, note: Fabric uses no gas — but you can report transaction latency and block size.)

---

## 5) Minimal testing script (optional) — using Fabric Node SDK

If you want to show a simple Node script that submits transactions (instead of peer CLI), I can add a 30-line example. Say yes and I’ll include it.

---

## Quick memory-primer (one-liner notes to memorize)

* `putState` = write world state, `getState` = read.
* Participant keys: `PART_<id>`, Asset keys: `ASSET_<id>`.
* `createX` → `putState`, `readX` → `getState`, `transfer` → modify object + `putState`.
* Deploy with `test-network` → `network.sh up` → `deployCC` → `peer chaincode invoke/query`.
