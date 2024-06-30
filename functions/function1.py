def password():
    passcode ='food'
    secretcode=""
    countattempt=0
    while passcode != secretcode:
         print('What is the secretcode?')
         secretcode = input()
         print('Yes, the password is ' + secretcode + '. You may enter.')
         countattempt=+1
         print(countattempt)
         if countattempt==4:
             print("many failed attempt")
         else:
             continue
       
         
password()