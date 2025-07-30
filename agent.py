import os
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType

load_dotenv()

def create_sql_agent():
    # MySQL connection string
    db_uri = f"mysql+mysqlconnector://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DATABASE')}"
    
    # Create SQLDatabase instance
    db = SQLDatabase.from_uri(db_uri)

    # Gemini LLM configuration
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-pro",
        temperature=0.3,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    # Create the SQL toolkit
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)

    # Create the SQL agent using initialize_agent
    agent_executor = initialize_agent(
        tools=toolkit.get_tools(),
        llm=llm,
        agent=AgentType.OPENAI_FUNCTIONS,  # Works with Gemini too
        verbose=True
    )

    return agent_executor
