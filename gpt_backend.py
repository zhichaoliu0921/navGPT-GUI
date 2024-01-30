from openai import OpenAI
from dotenv import load_dotenv, find_dotenv, set_key
import os

# Path to your .env file
env_file = find_dotenv('.env')
if env_file == '':
    env_file = '.env'

# Your OpenAI API key
openai_api_key = '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'

# Load existing .env file or create it if it doesn't exist
load_dotenv(env_file)

# Set the OPENAI_API_KEY in the .env file, updating it if it already exists
set_key(env_file, 'OPENAI_API_KEY', openai_api_key)

print(f'OPENAI_API_KEY has been set in {env_file}')

# Load environment variables from .env file
load_dotenv()

# Read OPENAI_API_KEY from .env
openai_api_key = os.getenv('OPENAI_API_KEY')

# Make sure the API key is available
if openai_api_key is None:
    raise ValueError("OPENAI_API_KEY is not set in the .env file.")

# Set the OpenAI API key for making API calls
OpenAI.api_key = openai_api_key

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ],
temperature=0.7,
max_tokens=2048,
top_p=1

)

print(completion.choices[0].message.content)