from Model.PromptTemp import SimpleTemplate, ConversationalTemplate, RoleplayingTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from utils.logger import logger,load_config
import os

load_dotenv()
api_key = os.getenv("api_key")
class LLM:
    def __init__(self, model_name="qwen/qwen3-32b", temperature=0.7):
        self.config = load_config()
        self.model_name = self.config.get('model', model_name)
        logger.info(f"Using model: {self.model_name}")
        self.model = ChatGroq(model_name=self.model_name, temperature=temperature, api_key=api_key)
    
    def get_model(self):
        return self.model

    def get_chain(self, prompt_type):
        if prompt_type == "simple":
            prompt = SimpleTemplate()
        elif prompt_type == "conversational":
            prompt = ConversationalTemplate()
        elif prompt_type == "roleplaying":
            prompt = RoleplayingTemplate()
        else:
            raise ValueError("Invalid prompt type. Choose from 'simple', 'conversational', or 'roleplaying'.")
        return  prompt.get_prompt()

    def rewrite_text(self, input_text, style_type, prompt_type="simple"):
        prompt = self.get_chain(prompt_type)
        chain= prompt | self.model
        print(style_type,prompt)
        return chain.invoke({"type": style_type, "input_text": input_text})

