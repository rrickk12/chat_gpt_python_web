import asyncio
from api.test_openai_async import *

def run_api(text):
    message = "quero enviar um email como suporte tecnico utilizando o linguajar do portugues de portugal e quero que você revise este texto : "+text
    response = asyncio.run(test_complete(message))
    # asyncio.run(test_generate_img())
    # test_generate_img()
    # test_chat_complete() 
    return  response