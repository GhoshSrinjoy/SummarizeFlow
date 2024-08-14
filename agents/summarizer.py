from langchain_community.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage
import time

class SummarizerAgent:
    def __init__(self):
        self.llm = ChatOllama(
            model="llama3.1",
            keep_alive=-1,  # keep the model loaded indefinitely
            temperature=0,
            max_new_tokens=150
        )
        self.prompt_template = ChatPromptTemplate.from_template(
            "Summarize the following content:\n\n{content}"
        )

    def summarize_content(self, content):
        try:
            # Prepare the prompt with the content
            prompt_input = self.prompt_template.format_prompt(content=content)

            # Convert to HumanMessage type
            message = HumanMessage(content=prompt_input.to_string())

            # Invoke the LLM with the prompt input
            response = self.llm([message])

            # Extract the generated text from the response object
            return response.content.strip()
        
        except Exception as e:
            print(f"Error during summarization: {e}")
            return "Summary not available"
