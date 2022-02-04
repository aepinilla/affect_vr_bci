import {Client, Config, Document, KeyPair, KeyType} from '@iota/identity-wasm/node/identity_wasm.js';

async function createDid(clientConfig) {
    // Create a default client configuration from the parent config network.
    const config = Config.fromNetwork(clientConfig.network);
    
    // Create a client instance to publish messages to the Tangle.
    const client = Client.fromConfig(config);

    // Generate a new ed25519 public/private key pair.
    const key = new KeyPair(KeyType.Ed25519);

    // Create a DID Document (an identity) from the generated key pair.
    const doc = new Document(key, clientConfig.network.toString());

    // Sign the DID Document with the generated key.
    doc.signSelf(key, doc.defaultSigningMethod().id.toString());

    // Publish the Identity to the IOTA Network, this may take a few seconds to complete Proof-of-Work.
    const receipt = await client.publishDocument(doc);

    const createDidResponse = {
        Key: {
            Public: key.public,
            Private: key.private
        },
        Doc: {
            Id: doc.id.tag
        },
        Receipt: {
            MessageId: receipt.messageId,
            NetworkId: receipt.networkId
        }
    }

    // Return the results.
    return createDidResponse;
}

export {createDid};
