a = input('Geef een woord: ')
b = input('Geef nog een woord: ')

if len (a) > len (b):     
    print('Woord 1 heeft meer letters dan woord 2')
elif len (a) < len (b):   
    print('Woord 1 heeft minder letters dan woord 2')
else:                   
    print('Woord 1 en woord 2 hebben evenveel letters')