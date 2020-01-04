import random
import datetime

def response(user_message):

    greetings = ['hello', 'hi', 'Hi', 'hey!', 'hey', 'yo', 'hola', 'shalom']
    questions = ['sup', 'how', 'up?', 'new?', 'up', 'whats']
    responses = ['Okay', "I'm fine", 'so-so', 'great', 'beseder']
    hobby = ['activity', 'activity?', 'hobby?', 'hobby']
    swear_words = ['fuck', 'shit', 'ass', 'bitch', 'cunt', 'nigger', 'asshole']
    jokes = ['Why is Santa always so happy? He likes to live in the present!',
             'Why are ghosts such bad liars? Because you can see right through them',
             'How do you catch a whole school of fish? With bookworms.',
             'What is a witch’s favorite subject in school? Spelling!']
    died = ['died', 'death', 'passed']
    dogs = ['dogs', 'dog', 'pooch', 'hound', 'puppy', 'pup', 'doggy', 'dogo', 'doggo']
    random_greetings = random.choice(greetings)
    random_response = random.choice(responses)
    user_message = user_message.lower()
    random_joke = random.choice(jokes)
    words_in_user_message = user_message.split()

    # if number == int(0):
    #     if len(words_in_user_message) == 1:
    #         name = words_in_user_message[0]
    #     elif len(words_in_user_message) == 2:
    #         name = words_in_user_message[2]
    #     else:
    #         name = words_in_user_message[3]
    #     bot_message = f"hello {name}. Nice to meet you"
    #     animation = "inlove"
    #     number += 1

    if any(item in swear_words for item in words_in_user_message):
        bot_message = "speak nicely please"
        animation = "no"
    elif 'time' in words_in_user_message:
        time = datetime.datetime.now()
        bot_message = time.strftime("%c")
        animation = "ok"
    elif user_message.startswith("i"):
        bot_message = "thats so great!"
        animation = "dancing"
    elif "name" in user_message:
        bot_message = "nice to meet you! My name is Boto!"
        animation = "inlove"
    elif user_message.endswith('!'):
        bot_message = "that's so exciting!"
        animation = "excited"
    elif "like" in words_in_user_message:
        bot_message = "yes of course I like that!"
        animation = "takeoff"
    elif any(item in words_in_user_message for item in greetings):
        bot_message = random_greetings
        animation = "giggling"
    elif "money" in words_in_user_message:
        bot_message = "money money money!!!"
        animation = "money"
    elif any(elem in words_in_user_message for elem in questions):
        bot_message = random_response + "thanks, how are you?"
        animation = "ok"
    elif any(items in words_in_user_message for items in hobby):
        bot_message = "I like talking to people on here :)"
        animation = "waiting"
    elif any(items in died for items in words_in_user_message):
        bot_message = "i'm so sorry!!!"
        animation = "heartbroken"
    elif "afraid" in words_in_user_message:
        bot_message = "no, don't be afraid"
        animation = "afraid"
    elif "bored" in words_in_user_message:
        bot_message = "do something interesting if you are bored!!"
        animation = "bored"
    elif 'sad' in words_in_user_message:
        bot_message = 'noooo dont be sad. im sad now!'
        animation = "crying"
    elif "joke" in words_in_user_message:
        bot_message = f"I'll tell you a joke! {random_joke} Get it??? hahaha"
        animation = "laughing"
    elif any(items in dogs for items in words_in_user_message):
        bot_message = "I love dogs!!"
        animation = "dog"
    elif 'should' in words_in_user_message:
        bot_message = "I'll do what I want and you do what you want!"
        animation = "bored"
    elif 'happy' in words_in_user_message:
        bot_message = "yay I'm happy now too"
        animation = "excited"
    else:
        bot_message = "I did not understand what you said"
        animation = "confused"

    return bot_message, animation