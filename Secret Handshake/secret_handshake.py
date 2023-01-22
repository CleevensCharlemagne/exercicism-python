def commands(binary_str):
    # the message to dispay
    msg = []
    # The secret mesaages
    secret = ['jump', 'close your eyes', 'double blink', 'wink']

    # Adding the appropriate secret message
    for i in range(4, 0, -1):
        if binary_str[i] == '1':
            msg.append(secret[i-1])

    # Reverse the order of the list if the bynary number starts by one
    if binary_str[0] == '1':
        msg.reverse()

    return msg


