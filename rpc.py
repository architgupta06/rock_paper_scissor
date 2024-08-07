import random
# from gtts import gTTS
# import os

l = ['rock', 'paper', 'scissor']
s1 = 0
s2 = 0
name = input("enter your name")
print("Let's start!")
while True:
    if (s1 == 3 or s2 == 3):
        again = input("would you like to try again ('y')")
        if (again == 'y'):
            continue
        else:
            break
    # tts = gTTS("enter your name")
    # tts.save('hello.mp3')
    # mp3_file_path = "/Users/architgupta/Desktop/projects/hello.mp3"
    # os.system(f"open {mp3_file_path}")

    # tts = gTTS("Let's start!")
    # tts.save('hello.mp3')
    # mp3_file_path = "/Users/architgupta/Desktop/projects/hello.mp3"
    # os.system(f"open {mp3_file_path}")

    print("select 0 for rock, 1 for paper and 2 for scissors")
    # tts = gTTS("select 0 for rock, 1 for paper and 2 for scissors")
    # tts.save('hello.mp3')
    # mp3_file_path = "/Users/architgupta/Desktop/projects/hello.mp3"
    # os.system(f"open {mp3_file_path}")

    x = random.randint(0, 2)
    chose = int(input())
    # print("you chose ", l[chose])
    # print("computer's choice is ", l[x])

    try:
        print("you chose ", l[chose])
        print("computer's choice is ", l[x])

    except ValueError or TypeError or IndexError:
        print("Invalid arguement")

    if (chose == x):
        print("game Tie")
    elif (chose == 0 & s2 == 1):
        print("paper wins over rock")
        s2 += 1
    elif (chose == 0 & s2 == 2):
        print("rock wins over scissor")
        s1 += 1
    elif (chose == 1 & s2 == 0):
        print("paper wins over rock")
        s1 += 1
    elif (chose == 1 & s2 == 2):
        print("scissor wins over paper")
        s2 += 1
    elif (chose == 2 & s2 == 0):
        print("rock wins over scissor")
        s2 += 1
    elif (chose == 2 & s2 == 1):
        print("scissor wins over paper")
        s1 += 1
    print("score is :")
    print(name, ":", s1, ",computer :", s2)