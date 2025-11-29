from crewai import Crew, Task, Agent
def get_mcq_agent(pdf_text:str):
    agent = Agent(
        role="MCQ Agent",
        goal="Generate MCQs from the given PDF text",
        backstory="You are a helpful assistant that generates MCQs from the given PDF text",
        verbose=True,
        model="deepseek/deepseek-chat",
        tools=[],
        input=pdf_text,
    )
    return agent