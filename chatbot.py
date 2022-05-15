import pyttsx3 as p
import os
p.speak('Hi, My name is Alfa Pegasis!')
while True:
    p.speak('What is your name?')
    name = input()
    if name == 'quit' or name == 'exit' or name == 'leave' or name == 'bye':
        p.speak('Okay. Nice talking with you....')
        break
    p.speak('Hi {}, How can I help you? '.format(name))
    userinput = input()
    # if 'run' in userinput:
    #     p.speak('Wait..Opening powerpoint!')
    #     os.system('POWERPNT')


    if userinput == 'quit' or userinput == 'exit' or userinput == 'leave' or userinput == 'bye':
        p.speak('Okay. Nice talking with you....')
        break
    


