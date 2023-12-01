const jose = require("jose");
const { JWS } = jose;
const fs = require("fs");
const process = require("process");

const key = jose.JWK.asKey(fs.readFileSync("./privatekey.key"));
function converter(obj) {
    var jwsData = JWS.sign(JSON.stringify(obj), key, { alg: "RS256" });
    var x_Signature = jwsData.split(".").pop();
    return x_Signature;
}

result = converter(JSON.parse(process.argv[3]));
process.stdout.write(result);
