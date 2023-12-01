const jose = require("jose");
const { JWS } = jose;
const fs = require("fs");

const key = jose.JWK.asKey(fs.readFileSync("./privatekey.key"));
const converter = (obj) => {
    //Sign data with RSA256 ALG
    var jwsData = JWS.sign(obj, key, { alg: "RS256" });
    var x_Signature = jwsData.split(".").pop();
    return x_Signature;
};

module.exports = {
    converter,
};
