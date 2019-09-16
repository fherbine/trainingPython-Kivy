import re

phone = input('enter your phone number: ')
phone = phone.strip()

if re.search(r'^([-. ]?[0-9]{2}){5}$', phone):
    print(repr(phone), 'ok')
else:
    print('nok')

email = input('enter an email: ')
email = email.strip()

if re.search(
        r'^([a-zA-Z\.\-0-9])+@([a-z]|[A-Z])+\.([a-z]|[A-Z]){1,10}$',
        email,
    ):
    print(repr(email), 'valid')
else:
    print('nok')
