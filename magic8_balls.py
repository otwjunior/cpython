import random

messages = ['It is certain',
'it is decidely so',
'yes definitely',
'reply hazy try again',
'ask again later',
'concentrate  and ask  again',
'my reply is no', 'outlook no so good',
'very doubtful']
print(messages[random.randint(0, len(messages)- 1)])