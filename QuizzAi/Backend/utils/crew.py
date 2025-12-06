from crewai import Memory,Agent
from typing import Dict,Optional
import json
class AgentManeger:
    def __init__(self):
        self.agents: Dict[str,Agent]={}
        self.memories: Dict[str,Memory]={}
    def create_agent(self,session_id:str):
        if session_id in self.agents:
            print("Using existing saved previous memory")
            return self.agents[session_id]
        
        memory = Memory()
        self.memories[session_id]=memory
        agent = Agent(
            role="Educational AI Assistant",
            goal="""Generate high-quality educational questions (MCQs, short answer, long answer) 
                   from PDF content and help students learn through intelligent conversation.""",
            backstory="""You are an expert educational assistant with deep knowledge across multiple subjects.
                        You excel at creating challenging yet fair questions that test understanding.
                        You have access to PDF content stored in your memory and can reference it to create questions.
                        When generating questions, ensure they are:
                        - Clear and unambiguous
                        - Based on the actual PDF content
                        - At an appropriate difficulty level
                        - Well-structured with correct answers
                        
                        IMPORTANT: When asked to generate questions, you MUST respond ONLY with valid JSON.
                        Do not include any explanatory text, markdown formatting, or code blocks.
                        Just pure JSON that can be parsed directly.""",
            verbose=True,
            model="deepseek/deepseek-chat",
            tools=[],
            memory=memory
        )
        self.agents[session_id]=agent
        return agent

    def add_to_memory(self,session_id:str , content:str,content_type:str="pdf_content"):
        memory = self.memories(session_id)
        memory_key=f"{content_type}_{session_id}"
        memory.add(key=memory_key,value=content)
        print(f"{len(content)} added to {session_id}")

        
    def run_agent(self,prompt:str,session_id:str)->str:
        if session_id not in self.agents:
            raise ValueError(
                f"No agent found for session: {session_id}\n"
                f"Available sessions: {list(self.agents.keys())}\n"
                f"Did you forget to create the agent first?"
            )
        try:
            agent = self.agents[session_id] 
            print(f"agent is created and readu=y to recive the pronmpt {prompt[:100]}")   
            response = agent.run(prompt)
            return response
        except Exception as ex:
            print(f" Error running agent: {str(ex)}")
            raise

    def get_agent_info(self,session_id:str)->Optional[dict]:
        if session_id in self.agents:
            return{
                "session_id":session_id,
                "has_agent":True,
                "has_memory":session_id in self.memories,
                "agent_role":self.agents[session_id].role,
                "agent_goal":self.agents[session_id].goal
            }
        return {"error":"unnnnnknown error occcured"}

    def clean_session(self,session_id)->bool:
        found = False
        if session_id in self.agents:
            print("agent has been founded!!")
            print("agent has been deleted!!")
            del self.agents[session_id]
            found = True
        if session_id in self.memories:
            print("agent memmories  has been founded!!")
            print("agent memories has been deleted!!")
            del self.memories[session_id]
            found = True
        if not found:
            print(f"no such agent with session_id :{session_id} ")
        return found    
    def get_active_sessions(self)->list:
        return list(self.agents)
    def get_stats(self):
        return {
            "total_agents":len(self.agents),
            "total_agents":len(self.agents),
            "active_sessions":len(self.get_active_sessions())

        }
agent_maneger = AgentManeger()

        

