print("hello whats your name")
name = input()
print(f"nice to meet you{name}")
print("how are you feeling(good/bad)")
mood = input().lower()
if mood == "good":
    print("i'm glad to hear that")
elif mood == "bad":
    print("i'm sorry to hear that")
else:
    print("i understand it is sometimes hard to share your feelings")
print(f"it was nice chatting with you{name}bye")   