# Chatbot-using-hugging-face

- This chatbot takes in a URL of a webpage, learns from it and then answers your queries from the data on that webpage.
- Scrapes data from website using beautifulsoup4 and passes it to chatbot model as context for user input
- Uses Meta-Llama-3-8B-Instruct model for text generation.

## How to use:
- Clone this repository
  ```
  git clone https://github.com/manish7696/Chatbot-using-hugging-face.git
  ```
- Replace your hugging face api key with the placeholder
- Replace the website url in the main function which you want to scrape
- Run the following command in terminal:
  ```
  python chat.py
  ```
