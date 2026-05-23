from learner import learn_topic

print("Mini AI")
print("====================")

topic = input("What should I learn?")

result = learn_topic(topic)

print("\n📚 Learned Summary:\n")
print(result)