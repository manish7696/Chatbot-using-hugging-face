from bs4 import BeautifulSoup
import requests
from huggingface_hub import InferenceClient

# Initialize HuggingFace client
client = InferenceClient(api_key="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")

def scrape_website(url):
    # Send a request to the website
    response = requests.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract relevant information (e.g., all paragraph texts)
    paragraphs = soup.find_all('p')
    content = ' '.join([para.get_text() for para in paragraphs])
    
    return content

def preprocess_content(content):
    # Basic cleaning (e.g., removing newlines or excessive spaces)
    content = content.replace('\n', ' ').strip()
    
    # You can add more specific processing logic here
    
    return content

def generate_chatbot_response(prompt, content):
    # Create a system message to instruct the model on the context
    system_message = f"The following information was scraped from a website:\n\n{content}"
    
    # Concatenate user input and scraped content as a conversation
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
    ]
    
    # Generate response using the Meta-Llama-3-8B-Instruct model
    response = ""
    for message in client.chat_completion(
        model="meta-llama/Meta-Llama-3-8B-Instruct",
        messages=messages,
        max_tokens=500,
        stream=True
    ):
        # Build the response stream
        response += message.choices[0].delta.content

    return response.strip()

def chatbot(url):
    # Scrape the website content
    scraped_content = scrape_website(url)
    
    # Preprocess the content
    processed_content = preprocess_content(scraped_content)
    
    print("Chatbot is ready! Ask any question about the website's content.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        
        # Generate a response based on the scraped content
        response = generate_chatbot_response(user_input, processed_content)
        print(f"Bot: {response}")

if _name_ == "_main_":
    website_url = "https://pokeapi.co/"  # Replace with your URL
    chatbot(website_url)
