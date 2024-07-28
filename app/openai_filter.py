import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def filter_and_categorize(transcript, categories_prompt):
    prompt = f"""
    Given the following transcript and categories:

    Transcript:
    Hello, thank you for calling TechSupport Plus. My name is Sarah. How can I assist you today? ... I understand you're having trouble with your laptop's Wi-Fi connection. Let's troubleshoot this together. First, can you tell me if you see the Wi-Fi icon in your taskbar? ... Okay, great. Now, let's try turning the Wi-Fi off and on again. You can do this by clicking on the Wi-Fi icon and toggling the switch. ... Perfect. Has this resolved the issue? ... I see, it's still not connecting. In that case, let's try resetting your network settings. I'll guide you through the process step by step. ... Excellent! I'm glad we were able to get your Wi-Fi working again. Is there anything else I can help you with today? ... You're welcome! Thank you for choosing TechSupport Plus. Have a great day!

    Categories and Instructions:
    {categories_prompt}

    Please analyze the transcript and:
    1. Determine the most appropriate category for this transcript.
    2. Highlight the specific parts of the transcript that support this categorization by enclosing them in [[ ]].
    3. Provide a brief explanation for your choice.

    Format your response as follows:
    Category: [Selected Category]
    Highlighted Transcript: [Transcript with relevant parts highlighted]
    Explanation: [Your explanation]
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that analyzes and categorizes transcripts."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000
    )

    return response.choices[0].message.content