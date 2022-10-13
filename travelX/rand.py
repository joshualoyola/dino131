import random
import string
dlNum = random.randrange(1000000,9999999,1)
sdlNum = "%s" %dlNum

rndLet = chr(random.randint(ord('A'), ord('Z')))


monthNum = random.randrange(1,12,1)
dayNum = random.randrange(1,28,1)
yearNum = random.randrange(1950,2022,1)

rndBd = "%s" %monthNum +"/" "%s" %dayNum + "/" "%s" %yearNum

print(rndLet+sdlNum)
print (rndBd)