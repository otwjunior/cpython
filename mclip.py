#! python3
#mclip.py - a multiclipboard program.

TEXT={'agree':"""Yes, I agree. That sound fine to me.""",
    'busy':"""Sorry, can we do this later or next week""",
    'upsell':"""Would you consider making this a monthly donation?"""}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] #first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for'+ keyphrase+ 'copied to clipboard.')
else:
    print('There is not text for' + keyphrase)
