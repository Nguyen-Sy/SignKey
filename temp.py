from main import call_node_function
import json

args = {
    "trace": {
        "clientTransId": "a009e24f7dcc0d20596adece715f0c18",
        "clientTimestamp": "20190530113020123"
    },
    "data": {
        "virtualAccountInfo": {
            "vaId": "VNM",
            "subId": "ABC12345",
            "vaName": "VNM 001",
            "bankAccountNo": "0001100012473007"
        }
    }
}
result = call_node_function(*[json.dumps(args)])
print(result)