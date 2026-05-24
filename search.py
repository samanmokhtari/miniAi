from ddgs import DDGS

def search_web(query):
    try:
        text = ""
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=5)
            for r in results:
                text += r.get("title", "") + "\n"
                text += r.get("body", "") + "\n\n"
        return text
    except:
        return None