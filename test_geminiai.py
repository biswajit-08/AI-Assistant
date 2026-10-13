from google import genai
import os

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

interaction = client.interactions.create(
    model="gemini-3.5-flash-lite",
    input="Say hello to my AI assistant in one sentence."
)

print(interaction.output_text)