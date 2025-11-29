from crewai import Memory
def get_agent(pdf_text:str):
    agent = Agent(
        role="MCQ Agent",
        goal="Generate MCQs/short questions/long questions from the given PDF text",
        backstory="You are a helpful assistant that generates MCQs/short questions/long questions from the given PDF text",
        verbose=True,
        model="deepseek/deepseek-chat",
        tools=[],
        input=pdf_text,
    )
    return agent