from langchain_ollama import OllamaLLM
from langchain_community.tools import DuckDuckGoSearchRun

from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from langchain.tools import Tool

# === 1. Charger le modèle Ollama ===
llm = OllamaLLM(model="mistral")

# === 2. Outil de recherche DuckDuckGo ===
search = DuckDuckGoSearchRun()

tools = [
    Tool(
        name="search",
        func=search.run,
        description="Recherche d'informations récentes sur internet"
    )
]

# === 3. Prompt ReAct (standard LangChain)
prompt = hub.pull("hwchase17/react")

# === 4. Création de l’agent
agent = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

# === 5. Boucle interactive
print("=== Chatbot IA avec Ollama + recherche web ===")

while True:
    query = input("You: ")

    if query.lower() in ["quit", "exit", "stop"]:
        break

    response = agent_executor.invoke({"input": query})
    print("Bot:", response["output"])