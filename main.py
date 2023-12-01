import subprocess


def call_node_function(*args):
    command = ['node', 'index.js', 'converter', *args]
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode().strip()
