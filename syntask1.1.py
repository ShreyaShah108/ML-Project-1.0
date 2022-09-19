modern_family = ['CLaiRe_DunPhY', 'PHiL_dUnpHY', 'GLoRiA_PriTCheTt', 'CaMErOn_TuCKEr',
'StELLa']
print('step1:\n')
indices = []
characters = []
for x,element in enumerate(modern_family):
    indices.append(x)
    characters.append(element)
print("indices: "+ str(indices))
print("characters: " + str(characters))

print('\nstep2:\n')
for i in range(len(characters)):
    characters[i] = characters[i].lower()
    characters[i] = characters[i].replace('_','-')
print("characters: " + str(characters))

print('\nstep3:\n')
# def lamda(n):
#     return len(n)
temp = list(map(lambda n: len(n),characters))
print("temp: " + str(temp))

print('\nstep4:\n')
for x,y in zip(indices,temp):
    a = [x,y]
    indices[x] = sum(a)
print("indices: "+str(indices))
print('\nstep5:\n')
indices.sort()
indices.reverse()
print("indices: "+str(indices))
print('\nstep6:\n')
Phew_finally = {}
for i in range(len(indices)):
    Phew_finally[indices[i]] = characters[i]
print("Phew_finally: "+str(Phew_finally))
