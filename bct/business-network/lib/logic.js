/**
 * Transfer an asset to another participant
 * @param {org.example.business.TransferProduct} tx
 * @transaction
 */
async function transferAsset(tx) {
    tx.product.owner = tx.newOwner.personId;
}
