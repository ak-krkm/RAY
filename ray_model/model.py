from openai import OpenAI
import os
RAYToken = os.getenv("RAYToken")
ModelID = "Qwen/Qwen2.5-Coder-32B-Instruct"

def runInference(query, fileContent=""):
    client = OpenAI(
        base_url="https://router.huggingface.co/v1",
        api_key=RAYToken,
    )
    if fileContent:
        query +=f"\n\n{fileContent}"
    messages = [
        {"role": "system", "content": "You are a helpful security assistant named RAY generate ur response in md format."},
        {"role": "user", "content": query}
    ]
    try:
        completion = client.chat.completions.create(
            model=ModelID,
            messages=messages,
            temperature=0.5,
            max_tokens=1000,
            stream=False
        )
        return completion.choices[0].message.content

    except Exception as e:
        return f"system Erorr: {e}"