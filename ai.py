from config import CLAUDE_API_KEY
import anthropic

client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)

def get_motivation():
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=100,
        messages=[
            {"role": "user", "content": "Give me a short one sentence motivational message to help me stick to my daily habits"}
        ]
    )
    return message.content[0].text


result = get_motivation()
print(result)

'''
1 → from config import CLAUDE_API_KEY
2 → import anthropic
3 → blank line
4 → create client
5 → blank line
6 → def get_motivation():
7 →     create message with client
8 →     return message.content[0].text

'''

