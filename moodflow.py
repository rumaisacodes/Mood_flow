import random
from collections import Counter

#1. Mood database
moods = {
    "low energy": {
        "quotes": ["Do what makes you happy.",
                   "You become what you believe.","Do it for yourself.",
                   "The way you speak to YOURSELF matters.",
                   "Be around people that are good for your soul."],
        "advice": ["Watch the moonlit sky, while lying or sitting outside in a quite place.",
                   "Reading night with snacks & a spotify playlist, nasheed or soft songs whatever you want.",
                   "Go for a small walk or take a hot/cold bath."]
   },
    "sad": {
        "quotes": ["It's okay to feel heavy.",
                    "Crying does not make you weak.",
                    "Everything happens for a reason.", 
                    "Be like a flower, survive the rain but use it to grow."],
        "advice": ["Be gentle with yourself today.", 
                   "Rest without guilt.", 
                   "Do something that helps you feel calm."]
    },

    "stressed": {
        "quotes": ["You don't have to do everything at once.",
                   "Pause. Breathe. Continue.",
                   "Calmness is a skill you can learn.",
                   "Don't stress over things that are out of your control."],
        "advice": ["Drink some water.",
                   "Step away from screens for 5 minutes.",
                   "Stretch your shoulders and neck." ]
    },

    "tired": {
        "quotes": ["Rest is productive.",
                   "Your body is asking for rest.",
                   "Slow days still count."
                   "it's okay to feel this way you are a human afterall."],
        "advice": ["Take a short nap if you can.",
                   "Sleep early tonight.",
                   "Lower your expectations today."]
    },
    "neutral": {
        "quotes": ["Stillness is not emptiness.",
                   "Not every day needs intensity.",
                   "Being okay is enough.",
                   "Be proud of yourself, you are doing great."],
        "advice": ["Check in with yourself.",
                   "Go outside for fresh air.",
                   "Do one small meaningful task."
        ]
    },
    "happy": {
        "quotes": ["It's a great day to have a great day.",
                   "A beautiful day begins with a beautiful mindset.",
                   "Happniess isn't getting all you want, it's enjoying all you have.",
                   "Always focus on the good."],
        "advice": ["Write one thing you're grateful for.",
                   "Share your energy."
                   "Be kind to someone today."]
    },
}

mood_history = []

print("---WELCOME TO MOOD TRACKS🎀---")
print(f"Available moods: {', '.join(moods.keys())}")
print("Type 'exit' to stop.\n")

# 2. The Main Program Loop
while True:
    # .strip() removes accidental spaces, .lower() makes it case-insensitive
    user_mood = input("How are you feeling right now? ").lower().strip()

    if user_mood == "exit":
        print("🌙 You showed up today. That matters. Goodbye!")
        break

    if user_mood not in moods:
        print("Hmm, I don't recognize that mood. Please pick from the list.\n")
        continue

    # 3. Process the mood
    mood_history.append(user_mood)
    
    quote = random.choice(moods[user_mood]["quotes"])
    advice = random.choice(moods[user_mood]["advice"])

    print(f"\n💬 Quote: {quote}")
    print(f"🌱 Suggestion: {advice}")

    # 4. Reflection Logic
    if len(mood_history) >= 3:
        common = Counter(mood_history).most_common(1)[0][0]
        print(f"📊 Reflection: Your most frequent mood so far is '{common}'.")

    print("\n— Take care of yourself —\n")