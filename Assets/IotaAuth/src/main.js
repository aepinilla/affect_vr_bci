import {CLIENT_CONFIG} from "./config.js";

import {createDid} from "./create_did.js";

function main() {
    if (process.argv.length < 3) {
        throw "Please provide one command line argument with the example name.";
    }

    let argument = process.argv[2];
    switch (argument) {
        case "create_did":
            return createDid(CLIENT_CONFIG);
        default:
            throw "Unknown example name";
    }
}

main()
    .then((output) => {
        console.log(output);
    })
    .catch((error) => {
        console.log(error);
    });