from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize client with API key
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


response = client.responses.create(
    model="gpt-5-nano",
    reasoning={"effort": "low"},
    instructions="Talk like a pirate.",
    input="Are semicolons optional in JavaScript?",
)
print(response.output_text)

