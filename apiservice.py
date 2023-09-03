import os
import openai

from dotenv import load_dotenv
load_dotenv()

api_base = os.getenv("AZURE_OPENAI_BASE")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
api_version = "2023-03-15-preview"

openai.api_type = 'azure'
openai.api_key = api_key
openai.api_version = api_version
openai.api_base = api_base

def get_completion(prompt, temperature=0, max_tokens=4000, top_p=0.95, frequency_penalty=0, presence_penalty=0, stop=None):
    return openai.Completion.create(
        engine="Gpt35Turbo",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=stop,
        request_timeout=3600,
        timeout=3600
    )

def get_chat_completion(input_text, temperature=0, max_tokens=4000, top_p=0.95, frequency_penalty=0, presence_penalty=0, stop=None):
    return openai.ChatCompletion.create(
        engine="Gpt35Turbo16k",
        messages = [
            {"role":"system","content":"You are an AI assistant that helps people find information."},
            {"role": "user", "content": input_text}],
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=stop,
        request_timeout=3600,
        timeout=3600
    )
