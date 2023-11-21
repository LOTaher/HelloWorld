import argparse
import os
import aiohttp
from dotenv import load_dotenv
from utils import get_file_extension

load_dotenv()
openai_key = os.environ.get("OPENAI_API_KEY")

async def translate_code(source_code, target_language):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_key}"
    }

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": f"Translate the following code to {target_language}. Provide any necessary imports."
            },
            {
                "role": "user",
                "content": source_code
            }
        ],
    }

    async with aiohttp.ClientSession() as session:
        async with session.post("https://api.openai.com/v1/chat/completions", json=payload, headers=headers) as response:
            return await response.json()


def read_file_contents(file_path):
    with open(file_path, 'r') as file:
        return file.read()

async def main():
    parser = argparse.ArgumentParser(description='Code Translator CLI Tool')
    parser.add_argument('file_path', help='Path to the file containing source code')
    parser.add_argument('target_language', help='Target programming language')
    args = parser.parse_args()

    source_code = read_file_contents(args.file_path)
    target_language = args.target_language

    response = await translate_code(source_code, target_language)
    translated_code = response['choices'][0]['message']['content']

    file_dir, file_name = os.path.split(args.file_path)
    name, ext = os.path.splitext(file_name)

    new_file_name = f"{name}.{get_file_extension(target_language)}"

    new_file_path = os.path.join(file_dir, new_file_name)
    with open(new_file_path, 'w') as new_file:
        new_file.write(translated_code)

    print(f"Your code has been translated to {new_file_path}! 🎉") 


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
