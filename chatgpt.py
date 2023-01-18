from revChatGPT.ChatGPT import Chatbot

class ChatGPTClient:

    def __init__(self, cred):
        self.session_token = cred['CHATGPT_SESSION_TOKEN']
        self.chatbot = Chatbot({"session_token": self.session_token}, conversation_id=None, parent_id=None)

    def ask(self, que ="tell me one interesting fact about dogs"):
        response = self.chatbot.ask(que, conversation_id=None, parent_id=None) 
        print(response)
        return response

    def create_mcq_website(self, url):
        pass


    
