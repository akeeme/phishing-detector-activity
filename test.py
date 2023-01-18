import json
from spellchecker import SpellChecker

spellchecker = SpellChecker()

def check_for_word(string):
    phishing_words = ['click', 'link', 'account', 'confirm', 'update', 'security', 'bank', 'password', 'login', 'verify', 'secure', 'transaction', 'alert',
                      'online', 'bill', 'payment', 'service', 'information', 'personal', 'card', 'activity', 'statement', 'transfer', 'fraud', 'transaction', 'alert', 'fraud']
    count = 0
    for word in phishing_words:
        if word in string:
            count += 1

    return count

def check_for_link(string):
    if 'http' in string:
        return True
    else:
        return False
    
def check_for_misspellings(string):
    misspellings = spellchecker.unknown(string.split())
    if len(misspellings) > 0:
        return True
    else:
        return False

def determine_if_phishing(email):
    if check_for_word(email['subject']) > 3 or check_for_word(email['body']) > 3:
        if check_for_link(email['body']) == True:
            if check_for_misspellings(email['body']) == True:
                print(f"Email with subject {email['subject']} is potentially phishing")
            else:
                print(f"Email with subject {email['subject']} is not phishing")
        else:
            print(f"Email with subject {email['subject']} is not phishing")
    else:
        return print(f"Email with subject {email['subject']} is not phishing")

def main():
    emails = json.load(open('emails.json'))

    for email in emails:
        determine_if_phishing(email)

if __name__ == '__main__':
    main()
            
            

