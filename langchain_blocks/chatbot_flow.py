from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

def create_qa_chain():
    prompt = PromptTemplate(
        input_variables=["context"],
        template="Generate a list of questions that can be asked based on the following content:\n{context}"
    )
    llm = OpenAI(temperature=0.5)
    return LLMChain(prompt=prompt, llm=llm)
