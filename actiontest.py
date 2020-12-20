import os

if os.environ.get('CI'):
    print('Looks like GitHub!')
else:
    print('Maybe running locally?')
