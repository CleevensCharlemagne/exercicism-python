def commands(binary_str):
    msg = []
    secret = ['jump', 'close your eyes', 'double blink', 'wink']

    for i in range(4, 0, -1):
        if binary_str[i] == '1':
            msg.append(secret[i-1])

    if binary_str[0] == '1':
        msg.reverse

    return msg


