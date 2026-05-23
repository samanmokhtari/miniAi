import requests
import json


def search_wikipedia(topic):

    url = f"https://fa.wikipedia.org/api/rest_v1/page/summary/{topic.replace(' ', '_')}"

    headers = {
        "User-Agent": "MiniAI/1.0 (Macintosh; Intel Mac OS X)"
    }

    try:
        response = requests.get(url, headers=headers)

        print("Status Code:", response.status_code)

        if response.status_code != 200:
            return f"❌ Error {response.status_code}"

        data = response.json()

        summary = data.get("extract")

        if not summary:
            return "❌ No summary found."

        save_memory(topic, summary)

        return summary

    except Exception as e:
        return f"❌ Exception: {e}"


def save_memory(topic, content):

    data = {}

    try:
        with open("memory.json", "r") as f:
            data = json.load(f)

    except:
        pass

    data[topic] = content

    with open("memory.json", "w") as f:
        json.dump(data, f, indent=4)


def load_memory(topic):

    try:
        with open("memory.json", "r") as f:
            data = json.load(f)

            if topic in data:
                return data[topic]

    except:
        return None

    return None


def learn_topic(topic):

    saved = load_memory(topic)

    if saved:
        print("\n🧠 Found in memory!\n")
        return saved

    print("\n🌐 Learning...\n")

    return search_wikipedia(topic)