import openai
import json
from aiohttp import ClientSession
import asyncio
my_key = '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'
openai.api_key = my_key
openai.aiosession.set(ClientSession())

async def chat_with_chatgpt(prompt, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        # prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
        messages=[ {"role": "system", "content": "You are a helpful assistant."}, 
                  {"role": "user", "content": "Im a software developer can you help me?"}, 
                  {"role": "assistant", "content": "Sure i'm here to help"},
                  {"role": "user", "content": prompt}, ],

    )

    message = json.loads(json.dumps(response))['choices'][0]['message']

    await openai.aiosession.get().close()

    return message

user_prompt = "Can you generate a mock testimony for a murder witness."
chatbot_response = asyncio.run(chat_with_chatgpt(user_prompt))

chatbot_response_content = chatbot_response['content']
print(chatbot_response_content)
