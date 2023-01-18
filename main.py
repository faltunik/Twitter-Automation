from dotenv import dotenv_values
from chatgpt import ChatGPTClient
config = dotenv_values("cred.env") # config is ordered dictionary

if __name__ == "__main__":
    chatgpt_client = ChatGPTClient(config)
    que = "How to use Internet?"
    que_response = chatgpt_client.ask(que)
    print(que_response)



