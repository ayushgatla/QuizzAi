from uuid import uuid4
sessions={}
def create_session():
    chat_id = str(uuid4())
    sessions[chat_id]={
        "crew_session_id": str(uuid4()),
        "pdf_text":None,
        "processed":False
    }
    return chat_id,sessions[chat_id]

def get_session(chat_id):
    return sessions.get(chat_id,None)
