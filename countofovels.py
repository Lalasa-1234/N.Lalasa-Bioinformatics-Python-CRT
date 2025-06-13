str=input("enter the string:")
u_vowel=l_vowel=u_con=l_con=0
for ch in str:
    if(ch.isalpha and ch.isupper):
        if ch in 'AEIOU':
            u_vowel+=1
        else:
            u_con+=1
    if(ch.isalpha() and ch.islower):
        if ch in 'aeiou':
            l_vowel+=1
        else:
            l_con+=1
print("coun of upper case vowels",u_vowel)
print("coun of upper case consonants",u_con)
print("coun of loer case vowels",l_vowel)
print("coun of lower case consonants",u_con)