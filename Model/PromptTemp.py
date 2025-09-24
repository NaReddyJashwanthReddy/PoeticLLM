from langchain.prompts import PromptTemplate

class SimpleTemplate:
    def __init__(self, template: str = "Rewrite the following text in a {type} style: {input_text}"):
        self.template = template
        self.prompt = PromptTemplate(input_variables=["type", "input_text"], template=self.template)
        
    def get_prompt(self, **kwargs):
        print(self.prompt)
        print("*"*20)
        return self.prompt
        
class ConversationalTemplate:
    def __init__(self, template: str = "User: Can you take this text and make it sound more {type}? Here is the text: {input_text}"):
        self.template = template
        self.prompt = PromptTemplate(input_variables=["type", "input_text"], template=self.template)
        
    def get_prompt(self, **kwargs):
        return self.prompt
class RoleplayingTemplate:
    def __init__(self, template: str = "You are a {type} expert tasked with rewriting text. Your goal is to make the tone of the following text {type}. Text to be rewritten: {input_text}"):
        self.template = template
        self.prompt = PromptTemplate(input_variables=["type", "input_text"], template=self.template)
        
    def get_prompt(self, **kwargs):
        return self.prompt