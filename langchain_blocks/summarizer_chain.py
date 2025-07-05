from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

def create_summarizer_chain():
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Summarize the following text into key points:\n{text}"
    )
    llm = OpenAI(temperature=0.3)
    return LLMChain(prompt=prompt, llm=llm)
