import openai
import pytest
from api.openai_async import *
import os
from api.test_utils import *

_OPEN_AI_API_KEY = os.getenv("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")
my_key = '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'
openai.api_key = my_key

async def test_complete(prompt):
    response = await complete(
        my_key,
        timeout=100,
        payload={
            "model": "gpt-3.5-turbo",
            "messages":[{"role": "user", "content":prompt}],
            "temperature": 0.5,
        },
    )
    response_json = response.json()
    # print(response_json['choices'][0]['message']['content'])
    # print(response_json)
    return response_json


async def test_generate_img():
    response = await openai_async.generate_img(
        my_key,
        timeout=8,
        payload={
            "prompt": "raposa de rabo vermelho com chapeu de natal ",
            "n": 1,
            "size": "256x256"
        },
    )
    print(response.json()["data"][0]["url"])
    # print(response)


async def test_embeddings():
    response1 = await openai_async.embeddings(
        _OPEN_AI_API_KEY,
        timeout=2,
        payload={"model": "text-embedding-ada-002", "input": "tooth doctor"},
    )
    response2 = await openai_async.embeddings(
        _OPEN_AI_API_KEY,
        timeout=2,
        payload={"model": "text-embedding-ada-002", "input": "dentist"},
    )
    assert (
        test_utils.cosine_similarity(
            response1.json()["data"][0]["embedding"],
            response2.json()["data"][0]["embedding"],
        )
        > 0.9
    )


async def test_chat_complete():
    response = await openai_async.chat_complete(
        _OPEN_AI_API_KEY,
        timeout=2,
        payload={
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": "Hello!"}],
            "temperature": 0.0,
        },
    )
    print(response.json()["choices"][0]["message"])
