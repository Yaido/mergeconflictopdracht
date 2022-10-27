import oldgreeting
import random
print("merge oefening leuk!")

oldgreeting.greet()




def basicHaiku():
<<<<<<< HEAD
    return ["Toward those tall trees","We saw a hawk descending","On a day in spring."]
=======
    return ["Toward those short trees","media college","On a day in spring."]
>>>>>>> origin/feature

#zet hier je haiku functie neer, zie https://github.com/progsen/haikugitopdracht voor ideeen

haikus = [
    basicHaiku()
]

def randomHaiku():
    return random.choice(haikus)

def start():
    print("starting main")
    
    print(randomHaiku())

    pass


start()