import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from search import search_web


MEMORY_FILE = "memory.json"


def load_memory():

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}


def save_memory(topic, content):

    data = load_memory()
    data[topic] = content

    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)



def learn_topic(topic):

    print("\n🌐 Searching...\n")

    data = search_web(topic)

    if not data:
        return "❌ چیزی پیدا نشد"

    save_memory(topic, data)

    return "✅ یاد گرفته شد"


def ask_question(question):

    memory = load_memory()

    if not memory:
        return "❌ هنوز چیزی یاد نگرفتم"

    texts = list(memory.values())

    texts.append(question)

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(texts)

    similarities = cosine_similarity(vectors[-1], vectors[:-1])

    best_index = similarities.argmax()

    best_answer = texts[best_index]

    return best_answer[:2000]