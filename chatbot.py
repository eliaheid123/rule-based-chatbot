# Chatbot
import random

PHRASES = [
    "That's exciting.",
    "Tell me more about it!",
    "I don't quite understand you—could you explain it again?"
]

print("Chatbot: Hi, I'm your chatbot. What is on your mind?")

user_input = "x"

while user_input != "":
    user_input = input("You: ").lower()

    if "hello" in user_input:
        print("Chatbot: Hi, what's up?")
    elif "hi" in user_input:
        print("Chatbot: Hello")
    elif "work" in user_input:
        print("Chatbot: I hope you enjoy the work.")

    elif "car" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "cars" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "vehicle" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "vehicles" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "truck" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "trucks" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "motorcycle" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "bicycle" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "bike" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "bus" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "train" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "airplane" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "plane" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "ship" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "boat" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "travel" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "trip" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "journey" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "vacation" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "holiday" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "beach" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "ocean" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "sea" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "river" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "lake" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "mountain" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "forest" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "park" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "city" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "town" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "village" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "country" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "world" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "home" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "house" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "apartment" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "room" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "kitchen" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "bedroom" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "bathroom" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "garden" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "yard" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "door" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "window" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "wall" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "floor" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "ceiling" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "roof" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "table" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "chair" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "desk" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "bed" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "sofa" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "lamp" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "light" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "water" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "food" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "bread" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "rice" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "pasta" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "pizza" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "cheese" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "fruit" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "apple" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "banana" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "orange" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "vegetable" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "meat" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "chicken" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "fish" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "egg" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "milk" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "coffee" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "tea" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "juice" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "breakfast" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "lunch" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "dinner" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "restaurant" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "school" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "teacher" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "student" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "class" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "lesson" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "book" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "paper" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "pen" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "pencil" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "computer" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "laptop" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "phone" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "smartphone" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "internet" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "website" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "email" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "message" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "friend" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "family" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "mother" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "father" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "parent" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "child" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "baby" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "brother" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "sister" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "people" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "person" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "man" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "woman" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "boy" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "girl" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "dog" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "cat" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "horse" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "bird" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "animal" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "pet" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "music" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "song" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "dance" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "movie" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "film" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "game" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "sport" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "football" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "soccer" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "basketball" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "tennis" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "baseball" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "swimming" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "running" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "walking" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "exercise" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "health" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "doctor" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "nurse" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "hospital" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "medicine" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "money" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "bank" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "shop" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "store" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "market" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "job" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "office" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "business" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "company" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "meeting" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "plan" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "idea" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "question" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "answer" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "problem" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "solution" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "story" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "language" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "english" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "word" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "sentence" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "conversation" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "talk" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "listen" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "hear" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "speak" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "read" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "write" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "learn" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "study" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "understand" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "think" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "know" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "remember" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "forget" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "feel" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "love" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "happy" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "sad" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "angry" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "tired" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "excited" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "afraid" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "calm" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "beautiful" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "funny" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "interesting" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "important" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "easy" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "difficult" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "new" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "old" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "big" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "small" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "little" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "long" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "short" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "fast" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "slow" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "hot" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "cold" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "warm" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "cool" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "rain" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "snow" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "sun" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "moon" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "star" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "sky" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "cloud" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "weather" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "season" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "spring" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "summer" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "autumn" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "winter" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "monday" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "tuesday" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "wednesday" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "thursday" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "friday" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "saturday" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "sunday" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "time" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "day" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "night" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "morning" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "afternoon" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "evening" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "today" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "tomorrow" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "yesterday" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "week" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "month" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "year" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "hour" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "minute" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "second" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "clock" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "date" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "birthday" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "party" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "gift" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "present" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "clothes" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "shirt" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "pants" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "shoes" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "dress" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "jacket" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "hat" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "bag" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "color" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "red" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "blue" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "green" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "yellow" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "black" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "white" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "purple" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "pink" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "brown" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "gray" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "gold" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "silver" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "art" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "drawing" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "picture" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "photo" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "design" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "science" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "math" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "history" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "geography" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "nature" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "energy" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "power" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "technology" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "robot" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "machine" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "tool" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "guitar" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "piano" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "drum" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "melody" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "sound" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "voice" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "actor" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "actress" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "theater" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "television" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "radio" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "news" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "sports" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "team" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "player" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "coach" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "ball" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "goal" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "race" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "competition" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "winner" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "lose" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "win" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "practice" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "hobby" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "plant" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "flower" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "tree" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "grass" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "seed" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "earth" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "space" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "planet" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "universe" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "experiment" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "dream" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "hope" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "future" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "past" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "memory" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "feeling" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "emotion" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "thought" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "mind" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "choice" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "decision" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "change" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "start" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "finish" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "begin" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "end" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "stop" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "move" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "stay" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "come" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "leave" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "arrive" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "drive" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "ride" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "fly" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "swim" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "walk" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "run" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "jump" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "climb" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "sit" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "stand" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "sleep" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "wake" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "eat" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "drink" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "cook" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "bake" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "clean" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "wash" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "build" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "fix" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "create" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "make" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "use" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "open" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "close" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "turn" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "push" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "pull" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "carry" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "bring" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "send" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "receive" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "buy" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "sell" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "pay" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "save" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "spend" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "count" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "measure" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "compare" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "choose" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "decide" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "explain" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "describe" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "show" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "help" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "share" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "teach" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "ask" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "reply" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "respond" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "react" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "smile" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "laugh" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "cry" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "worry" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "relax" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "enjoy" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "prefer" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "need" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "want" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "like" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "dislike" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "hate" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "believe" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "trust" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "agree" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "disagree" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "grow" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "improve" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "try" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "succeed" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "fail" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "rest" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "play" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "explore" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "discover" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "invent" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "imagine" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "prepare" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "visit" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "return" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "meet" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "join" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "follow" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "lead" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "protect" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "support" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "care" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "respect" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "kindness" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "courage" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "patience" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "honesty" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "truth" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "peace" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "freedom" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "safety" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "comfort" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "style" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "fashion" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "beauty" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "shape" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "size" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "number" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "letter" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "taste" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "smell" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "touch" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "sight" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "culture" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "aaa" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "aaberg" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "aachen" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "aachener" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "aaker" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "aalborg" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "aalburg" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "aalen" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "aaliyah" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "aalseth" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "aalsmeer" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "aalto" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "aamodt" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "aancor" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "aardema" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "aardvark" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "aardvarks" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "aargh" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "aarhus" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "aaron" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "aarons" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "aaronson" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "aarti" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "aase" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "aasen" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "aba" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "ababa" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "abacha" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "aback" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "abaco" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "abacus" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "abad" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "abadaka" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "abadi" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "abadie" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "abair" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "abalkin" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "abalone" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "abalones" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "abalos" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "abandon" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "abandoned" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "abandoning" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "abandonment" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "abandonments" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "abandons" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "abanto" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "abarca" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "abare" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "abascal" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "abash" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "abashed" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "abasia" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "abate" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "abated" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "abatement" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "abatements" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "abates" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "abating" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "abattoir" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "abba" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "abbado" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "abbas" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "abbasi" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "abbate" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "abbatiello" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "abbe" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "abbenhaus" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "abbett" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "abbeville" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "abbey" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "abbie" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "abbitt" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "abbot" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "abbotstown" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "abbott" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "abbottstown" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "abboud" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "abbreviate" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "abbreviated" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "abbreviates" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "abbreviating" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "abbreviation" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "abbruzzese" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "abbs" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "abby" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "abc" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "abco" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "abcotek" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "abcs" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "abd" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "abdalla" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "abdallah" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "abdel" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "abdella" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "abdicate" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "abdicated" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "abdicates" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "abdicating" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "abdication" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "abdnor" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "abdo" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "abdollah" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "abdomen" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "abdominal" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "abduct" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "abducted" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "abductee" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "abductees" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "abducting" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "abduction" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "abductions" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "abductor" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "abductors" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "abducts" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "abdul" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "abdulaziz" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "abdulla" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "abdullah" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "abe" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "abed" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "abedi" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "abee" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "abel" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "abela" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "abelard" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "abele" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "abeles" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "abell" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "abella" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "abeln" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "abelow" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "abels" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "abelson" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "abend" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "abendroth" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "aber" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "abercrombie" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "aberdeen" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "aberford" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "aberg" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "aberle" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "abermin" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "abernathy" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "abernethy" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "aberrant" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "aberration" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "aberrational" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "aberrations" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "abert" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "abet" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "abetted" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "abetting" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "abex" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "abeyance" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "abeyta" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "abhor" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "abhorred" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "abhorrence" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "abhorrent" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "abhors" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "abiam" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "abid" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "abide" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "abided" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "abides" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "abiding" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "abidjan" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "abie" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "abigail" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "abila" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "abilene" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "abilities" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "ability" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "abimael" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "abimaels" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "abingdon" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "abington" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "abio" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "abiola" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "abiomed" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "abiquiu" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "abitibi" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "abitz" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "abject" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "abkhazia" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "abkhazian" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "abkhazians" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "ablate" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "ablation" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "ablaze" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "able" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "abled" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "abler" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "ables" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "ablest" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "abloom" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "ablution" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "ablutions" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "ably" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "abnegation" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "abner" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "abney" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "abnormal" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "abnormality" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "abnormally" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "abo" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "aboard" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "abode" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "abohalima" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "abolish" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "abolished" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "abolishes" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "abolishing" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "abolition" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "abolitionism" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "abolitionist" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "abominable" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "abomination" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "abominations" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "abood" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "aboodi" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "abor" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "aboriginal" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "aborigine" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "aborigines" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "aborn" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "abort" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "aborted" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "aborting" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "abortion" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "abortionist" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "abortionists" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "abortions" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "abortive" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "aborts" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "abott" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "abou" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "aboud" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "abouhalima" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "abound" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "abounded" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "abounding" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "abounds" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "about" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "above" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "aboveboard" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "abplanalp" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "abra" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "abracadabra" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "abrade" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "abraded" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "abrades" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "abraham" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "abrahamian" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "abrahams" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "abrahamsen" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "abrahamson" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "abram" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "abramczyk" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "abramo" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "abramovitz" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "abramowicz" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "abramowitz" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "abrams" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "abramson" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "abrasion" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "abrasions" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "abrasive" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "abrasives" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "abraxa" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "abraxas" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "abreast" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "abrego" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "abreu" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "abridge" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "abridged" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "abridgement" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "abridges" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "abridging" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "abril" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "abroad" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "abrogate" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "abrogated" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "abrogating" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "abrogation" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "abrol" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "abron" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "abrupt" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "abruptly" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "abruptness" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "abrutyn" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "abruzzese" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "abruzzo" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "abs" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "absalom" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "absaraka" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "abscam" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "abscess" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "abscond" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "absconded" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "absconding" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "absconds" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "absecon" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "absence" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "absences" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "absent" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "absentee" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "absenteeism" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "absentees" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "absentia" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "absher" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "abshier" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "abshire" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "absinthe" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "abso" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "absolom" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "absolut" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "absolute" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "absolutely" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "absoluteness" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "absolutes" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "absolution" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "absolutism" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "absolutist" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "absolve" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "absolved" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "absolves" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "absolving" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "absorb" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "absorbed" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "absorbency" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "absorbent" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "absorber" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "absorbers" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "absorbing" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "absorbs" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "absorption" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "abstain" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "abstained" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "abstaining" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "abstention" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "abstentions" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "abstinence" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "abstinent" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "abston" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "abstract" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "abstracted" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "abstraction" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "abstractions" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "abstracts" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "abstruse" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "absurd" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "absurdist" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "absurdities" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "absurdity" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "absurdly" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "abt" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "abts" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "abu" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "abudrahm" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "abuellah" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "abuladze" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "abundance" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "abundant" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "abundantly" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "aburto" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "abuse" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "abused" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "abuser" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "abusers" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "abuses" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "abusing" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "abusive" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "abut" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "abuts" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "abutted" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "abutting" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "abuzz" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "abysmal" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "abysmally" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "abyss" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "abyssinia" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "abyssinian" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "abzug" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "aca" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "acacia" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "academe" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "academia" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "academic" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "academically" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "academician" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "academicians" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "academics" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "academies" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "academy" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "acadia" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "acaena" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "acampo" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "acampora" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "acampsia" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "acantha" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "acapulco" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "acary" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "acc" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "accardi" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "accardo" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "accede" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "acceded" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "accedes" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "acceding" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "accel" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "accelerant" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "accelerants" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "accelerate" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "accelerated" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "accelerates" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "accelerating" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "acceleration" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "accelerator" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "accelerators" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "accent" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "accented" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "accenting" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "accents" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "accentuate" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "accentuated" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "accentuates" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "accentuating" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "accenture" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "accept" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "acceptable" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "acceptably" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "acceptance" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "acceptances" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "accepted" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "accepting" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "accepts" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "access" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "accessed" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "accessible" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "accessing" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "accession" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "accessories" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "accessorize" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "accessorized" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "accessory" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "accetta" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "accident" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "accidental" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "accidentally" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "accidently" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "accidents" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "accion" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "accival" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "acclaim" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "acclaimed" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "acclaiming" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "acclaims" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "acclamation" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "acclimate" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "acclimated" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "acclimation" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "acco" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "accokeek" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "accola" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "accolade" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "accolades" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "accomando" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "accommodate" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "accommodated" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "accommodates" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "accompanied" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "accompanies" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "accompanist" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "accompany" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "accompanying" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "accompli" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "accomplice" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "accomplices" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "accomplish" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "accomplished" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "accomplishes" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "accor" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "accord" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "accordance" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "accorded" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "according" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "accordingly" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "accordion" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "accordions" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "accords" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "accost" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "accosted" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "accosting" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "account" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "accountable" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "accountancy" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "accountant" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "accountants" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "accounted" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "accountemp" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "accountemps" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "accounting" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "accounts" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "accouterment" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "accoutrement" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "accra" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "accredit" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "accredited" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "accrediting" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "accreted" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "accretion" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "accrual" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "accruals" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "accrue" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "accrued" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "accrues" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "accruing" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "accu" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "accuhealth" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "accumulate" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "accumulated" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "accumulates" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "accumulating" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "accumulation" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "accumulative" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "accumulator" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "accumulators" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "accuracies" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "accuracy" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "accurate" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "accurately" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif "accuray" in user_input:
        print("Chatbot: That sounds interesting. What makes you think about it?")
    elif "accuride" in user_input:
        print("Chatbot: I'd like to hear a little more about that.")
    elif "accursed" in user_input:
        print("Chatbot: How does that make you feel?")
    elif "accurso" in user_input:
        print("Chatbot: What do you enjoy most about it?")
    elif "accusation" in user_input:
        print("Chatbot: That could be worth exploring. Tell me more.")
    elif "accusations" in user_input:
        print("Chatbot: Why is that on your mind today?")
    elif "accusative" in user_input:
        print("Chatbot: That sounds like something you have thought about.")
    elif "accusatory" in user_input:
        print("Chatbot: What would you like to happen next?")
    elif "accuse" in user_input:
        print("Chatbot: Have you had a good experience with that?")
    elif "accused" in user_input:
        print("Chatbot: What is the most important part of that for you?")
    elif "accuser" in user_input:
        print("Chatbot: I see. Can you tell me a little more?")
    elif "accusers" in user_input:
        print("Chatbot: That gives me something to think about. What else?")
    elif "accuses" in user_input:
        print("Chatbot: What first got you interested in that?")
    elif "accusing" in user_input:
        print("Chatbot: Would you say that matters a lot to you?")
    elif "accusingly" in user_input:
        print("Chatbot: How long have you felt that way?")
    elif "accustom" in user_input:
        print("Chatbot: What do you think is the best thing about it?")
    elif "accustomed" in user_input:
        print("Chatbot: Is there a particular reason you mention that?")
    elif "accutane" in user_input:
        print("Chatbot: That sounds personal to you. Would you like to explain?")
    elif "ace" in user_input:
        print("Chatbot: What comes to mind when you think about it?")
    elif "acecomm" in user_input:
        print("Chatbot: Let's talk about that a little more.")
    elif user_input != "":
        text = random.choice(PHRASES)
        print("Chatbot:", text)

print("Chatbot: It was wonderful talking to you. Goodbye!")
