from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize client with API key
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def run_example3():
    """
    Main function to run Example 3 demonstrations
    This function will be called from main.py
    """
    try:
        print("🚀 Running Example 3 - Responses API Demo")
        print("=" * 50)
        
        #       Using instruction in the response creation
        #         The reasoning parameter is only available for OpenAI's reasoning models like:
        # o1-preview
        # o1-mini
        # o3-mini
        # These are specialized reasoning models, not the standard GPT models.
        response = client.responses.create(
            model="gpt-3o-mini",
            reasoning={"effort": "low"},
            instructions="Talk like a pirate.",
            input="Are semicolons optional in JavaScript?",
        )
        print("\n🏴‍☠️ Response with instructions:")
        print(response.output_text)

        # Put instruction inside input array as Developer role and user question as User role
        response = client.responses.create(
            model="gpt-3o-mini",
            reasoning={"effort": "low"},
            input=[
                {
                    "role": "developer",
                    "content": "Talk like a pirate."
                },
                {
                    "role": "user", 
                    "content": "Are semicolons optional in JavaScript?"
                }
            ]
        )   
        print("\n🏴‍☠️ Response with developer role in input:")
        print(response.output_text)
        
        print("\n✅ Example 3 completed successfully")
        
    except Exception as e:
        print(f"❌ Error in Example 3: {str(e)}")
        print("Make sure your OpenAI API key is set in the .env file")





