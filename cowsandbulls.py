import random
s='abcdefghijklmnopqrstuvwxyz'
l=int(input('how many characters do you want guess?'))

word=''.join(random.sample(s,l))

letters=tuple(word)
x=len(word)

print(x,'is the length of the word')



while True:
    guess=input('guess the word ')
    
    if guess==word:
        break
    
    y=len(guess)
    gletters=tuple(guess)

    bulls=0
    cows=0
    
    try:
        for x1 in range(x):
        
            if gletters[x1] ==letters[x1]:
                bulls=bulls+1
        
            for y1 in range(y):
                if gletters[x1]==letters[y1] and x1!=y1:
                    cows=cows+1
    
        print('bulls',bulls)
        print('cows',cows)
    
    except:
        print('guess words with',x,'letters')

    

print('great u made it')