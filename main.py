import subprocess
import json


def call_node_function(function_name, *args):
    command = ['node', 'index.js', function_name, *args]
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode().strip()


function_name = 'converter'
data = {
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

args = [json.dumps(data)]
result = call_node_function(function_name, *args)
print(result)