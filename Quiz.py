score = 0
print('Welcome to Quiz on python')
begin = input('Would you like to begin?: ')
print('')
if begin == "yes":
    print('A)  case sensitive')
    print('B)  user can be typo :p')
    print('C)  no idea')
    q1 = input('Is python is case sensitive lang?: ')
    if q1 == "a" or q1 == "A":
        print('')
        print('Well done!')
        score += 1
    else:
        print('Sorry you are Wrong!')
    print('')
    print('A)  acidic')
    print('B)  normal')
    print('C)  base')
    print('')
    q2 = input ('Honey is ___ in nature ?: ')
    if q2 == "a" or q2 == "A":
        print('')
        print('Well done!')
        score += 1
    else:
        print('Wrong answer try to learn Chemistry :)')
    print('')
    print('A)  yes')
    print('B)  no')
    print('C)  oftenly')
    print('')
    q3 = input ('Do you like playing game?: ')
    if q3 == "a" or q3 == "A" or q3 == "c" or q3 == "C":
        print('')
        print('Good')
        score += 1
    #elif q3 == "c" or q3 == "C":
        print('')
        print("that's good :)")
        
    else:
        print('GOD BLESS YOU :p')
    print('')
    print("you Got", str(score)+"/3 right :)")
else:
    print('Thanks for trying Goodbye ;)')
    
