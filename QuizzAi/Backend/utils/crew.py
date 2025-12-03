from crewai import Memory,Agent
memory = Memory()
agent = Agent(
        role="MCQ Agent",
        goal="Generate MCQs/short questions/long questions from the given PDF text",
        backstory="You are a helpful assistant that generates MCQs/short questions/long questions from the given PDF text",
        verbose=True,
        model="deepseek/deepseek-chat",
        tools=[],
        memory = memory
    )
def add_to_memory(sessionid , content):
    memory.add(key=sessionid,value=content)
def run_agent(prompt,sessionid):
    response = agent.run(
        prompt,
        memory_key = sessionid

    )
    return response