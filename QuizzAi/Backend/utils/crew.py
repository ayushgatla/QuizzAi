from crewai import Agent
from typing import Dict, Optional
import json
import os
class AgentManager:
    def __init__(self):
        self.agents: Dict[str, Agent] = {}
        self.context_storage: Dict[str, Dict[str, str]] = {}  # Store context manually
    
    def create_agent(self, session_id: str) -> Agent:
        if session_id in self.agents:
            print(f"Using existing agent for session: {session_id}")
            return self.agents[session_id]
        
        self.context_storage[session_id] = {}
        
        agent = Agent(
            role="Educational AI Assistant",
            goal="""Generate high-quality educational questions (MCQs, short answer, long answer) 
                   from PDF content and help students learn through intelligent conversation.""",
            backstory="""You are an expert educational assistant with deep knowledge across multiple subjects.
                        You excel at creating challenging yet fair questions that test understanding.
                        You have access to PDF content and can reference it to create questions.
                        
                        When generating questions, ensure they are:
                        - Clear and unambiguous
                        - Based on the actual PDF content
                        - At an appropriate difficulty level
                        - Well-structured with correct answers
                        
                        IMPORTANT: When asked to generate questions, you MUST respond ONLY with valid JSON.
                        Do not include any explanatory text, markdown formatting, or code blocks.
                        Just pure JSON that can be parsed directly.""",
            verbose=True,
            llm="deepseek/deepseek-chat",  # Changed from 'model' to 'llm'
            tools=[],
            allow_delegation=False,
        )
        
        self.agents[session_id] = agent
        print(f"Created new agent for session: {session_id}")
        return agent

    def add_to_context(self, session_id: str, content: str, content_type: str = "pdf_content"):
       
        if session_id not in self.context_storage:
            self.context_storage[session_id] = {}
        
        context_key = f"{content_type}_{len(self.context_storage[session_id])}"
        self.context_storage[session_id][context_key] = content
        
        print(f"Added {len(content)} characters to context for session: {session_id}")
        print(f"Total context items: {len(self.context_storage[session_id])}")

    def get_context(self, session_id: str) -> str:
        if session_id not in self.context_storage:
            return ""
        
        context_parts = []
        for key, value in self.context_storage[session_id].items():
            context_parts.append(f"[{key}]\n{value}\n")
        
        return "\n".join(context_parts)

    def run_agent(self, prompt: str, session_id: str, include_context: bool = True) -> str:
    
        if session_id not in self.agents:
            raise ValueError(
                f"No agent found for session: {session_id}\n"
                f"Available sessions: {list(self.agents.keys())}\n"
                f"Did you forget to create the agent first?"
            )
        
        try:
            agent = self.agents[session_id]
            
            # Build the full prompt with context
            full_prompt = prompt
            if include_context:
                context = self.get_context(session_id)
                if context:
                    full_prompt = f"""Context Information:
{context}


{prompt}"""
            
            print(f"Running agent for session: {session_id}")
            print(f"Prompt preview: {full_prompt[:100]}...")
            
            response = agent.execute_task(full_prompt)
            
            return response
        
        except Exception as ex:
            print(f"Error running agent: {str(ex)}")
            raise

    def get_agent_info(self, session_id: str) -> Optional[dict]:
        """Get information about an agent session."""
        if session_id in self.agents:
            return {
                "session_id": session_id,
                "has_agent": True,
                "has_context": session_id in self.context_storage,
                "context_items": len(self.context_storage.get(session_id, {})),
                "agent_role": self.agents[session_id].role,
                "agent_goal": self.agents[session_id].goal
            }
        return {"error": f"No agent found for session: {session_id}"}

    def clear_session(self, session_id: str) -> bool:
       
        found = False
        
        if session_id in self.agents:
            print(f"Deleting agent for session: {session_id}")
            del self.agents[session_id]
            found = True
        
        if session_id in self.context_storage:
            print(f"Deleting context for session: {session_id}")
            del self.context_storage[session_id]
            found = True
        
        if not found:
            print(f"No data found for session: {session_id}")
        
        return found

    def get_active_sessions(self) -> list:
       
        return list(self.agents.keys())

    def get_stats(self) -> dict:
     
        return {
            "total_agents": len(self.agents),
            "total_contexts": len(self.context_storage),
            "active_sessions": self.get_active_sessions()
        }


agent_maneger = AgentManager()


