import os

def get_ip_address(url):
    command = "host " + url
    process = os.popen(command)
    result = str(process.read())
    marker = result.find('has address') + 12
    return result[marker:].splitlines()[0]
    return result

print(get_ip_address('thenewboston.com'))