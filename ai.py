import os

def get_openai_client():
    from openai import OpenAI
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None
    return OpenAI(api_key=api_key)

def summarize(text):
    if not text:
        return "No content to summarize."
        
    client = get_openai_client()
    if not client:
        return "[Error] OPENAI_API_KEY environment variable is not set."
        
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"Summarize this open source issue or PR in 2-3 short sentences. Keep it extremely concise and helpful for a maintainer:\n\n{text}"}],
            timeout=10
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[Error summarizing] {str(e)}"