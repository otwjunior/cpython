#find email and phone numbers on clipboard

import re, pyperclip

#phone regex
phonergx =re.compile(r'(+254)\d\d\d\d\d\d\d\d\d')
#email regex
emailrgx = re.compile(r'''(
    [a-zA-Z0-9._%+-] + #username
    @
    [a-zA-z0-9.-]+ #domain name
    (\.[a-zA-Z]{2,4}) #dot something
    )''', re.VERBOSE)

    #find matches in clpboard text.
    text = str(pyperclip.paste())

    matches = []
    for groups in phonergx.findall(text):
        phoneNum = '-'.join([groups[1], groups[3],groups[5]])
        if groups[8] != '':
            phoneNum += ' x' + groups[8]
        matches.append(phoneNum)
    for groups in emailrgx.findall(text):
        matches.append(groups[0])
        