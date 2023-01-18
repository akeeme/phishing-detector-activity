import json
from textblob import TextBlob


def check_for_word(string):
    phishing_words = ['click', 'clicking', 'link', 'account', 'confirm', 'confirming', 'update', 'updating', 'security', 'bank', 'password', 'login', 'verify', 'secure', 'transaction', 'alert',
                      'online', 'bill', 'payment', 'service', 'information', 'personal', 'card', 'activity', 'statement', 'transfer', 'fraud', 'transaction', 'alert', 'fraud']
    count = 0
    for word in phishing_words:
        if word in string.lower():
            count += 1

    return count


def check_for_link(string):
    if 'http' in string.lower():
        return True
    else:
        return False


def check_for_misspellings(string):
    corrected_text = TextBlob(string).correct()

    return string != corrected_text


def determine_if_phishing(email):
    if check_for_word(email['subject']) > 3 or check_for_word(email['body']) > 2:
        if check_for_link(email['body']) == True:
            if check_for_misspellings(email['body']) == True:
                print(f"Email with id {email['id']} is potentially phishing")
    else:
        print(f"Email with id {email['id']} is not phishing")


def main():
    emails = json.load(open('emails.json'))

    for email in emails:
        determine_if_phishing(email)


if __name__ == '__main__':
    main()
