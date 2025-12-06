

import uvicorn
from config import Config

if __name__ == "__main__":
    
    Config.validate()
    
    print("\n🚀 Starting QuizzAI Server...")
    print(f"📍 Server will be available at: http://{Config.HOST}:{Config.PORT}")
    print(f"📚 API docs will be at: http://localhost:{Config.PORT}/docs")
    print(f"🔄 Auto-reload: {'✅ Enabled' if Config.is_dev() else '❌ Disabled'}")
    print("\n💡 Press CTRL+C to stop the server\n")
    
    
    uvicorn.run(
        "main:app",  
        host=Config.HOST,
        port=Config.PORT,
        reload=Config.is_dev(), 
        log_level="info"
    )