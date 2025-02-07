acro = {'LOL': "laugh out loud",
        'IDK': "I don't know",
        'TBH': "To be Honest"}

acro['TBH'] = 'Honestly'

definition = acro.get('BTW')

if definition:
    print(definition)
else:
    print("Key doesn't exist.")


sentence = 'IDK' + ' what happened ' + 'TBH'
translation = acro.get('IDK') + ' what happened ' + acro.get('TBH')

print('sentence: ', sentence)
print('translation: ', translation)