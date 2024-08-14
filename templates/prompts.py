from langchain_core.prompts import ChatPromptTemplate

summarize_template = ChatPromptTemplate.from_template(
    "Summarize the following content:\n\n{content}"
)
