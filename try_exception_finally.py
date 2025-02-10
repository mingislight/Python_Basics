acro = { 'LOL': 'laugh out loud',
        'IDK': "I don't know",
        'TBH': "To be honest"
        }

try: # Code that might cause an exception
    definition = acro['LOL']  
    print('Definition of ', acro['LOL'], " is ", definition)
except: # Print an error message
    print("The key does not exisit.") 
finally: # Used whether the try has an error or not
    print('The acronyms we have defined are:')
    for ac in acro:
        print(ac)


print('The program keeps going...')