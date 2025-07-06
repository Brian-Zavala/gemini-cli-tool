import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

api_key = os.environ.get("GEMINI_API_KEY")


def main():

  load_dotenv()
  
  client = genai.Client(api_key=api_key)
  
  args = sys.argv[1:]
  

  user_prompt = " ".join([arg for arg in args if arg != "--verbose"])

  if not args:
    print("Usage: python main.py <prompt>")
    print("Example: python main.py 'What is the capital of France?'")
    sys.exit(1)
  


  messages = [
      types.Content(
          role="user",
          parts=[types.Part(text=user_prompt)]
      )
  ]
  response = client.models.generate_content(
    model="gemini-2.0-flash-001",contents=messages,
  )
  print(response.text)

  if "--verbose" not in args:
    print(user_prompt)

  elif "--verbose" in args:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
   
if __name__ == "__main__":
    main()
