from modules.okx import withdraw


def start_transfer():
    with open("recipients.txt", "r") as file:
        recipients = file.readlines()
    
    for recipient in recipients:
        withdraw(recipient.strip())
