def print_send_to_controller(header,breachType):
    print(f'{header}, {breachType}')

def print_send_to_email(recepient,text):
    print(f'To: {recepient}')
    print("Hi, the temperature is " + text)