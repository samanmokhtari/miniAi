from learner import learn_topic, ask_question


print("🤖 MINI AI")
print("========================")

while True:

    print("\n1. Learn Topic")
    print("2. Ask Question")
    print("3. Exit")

    choice = input("> ")

    if choice == "1":

        topic = input("🧠 Topic: ")

        print("\n" + learn_topic(topic))

    elif choice == "2":

        q = input("❓ Question: ")

        print("\n🤖 Answer:\n")
        print(ask_question(q))

    elif choice == "3":
        break