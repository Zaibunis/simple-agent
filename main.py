import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel

# Load environment variables
load_dotenv()

# Get API Key
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("⚠️ GEMINI_API_KEY not found in environment variables.")

# Initialize the provider
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Initialize the model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)

# Dictionary of agents
agents = {
    "1": ("Greeting Agent", 
        "You are a Greeting Agent. When someone says 'hi', reply with 'Salam from Faria Khan! How are you?'. "
        "When someone says 'bye', reply with 'Allah Hafiz from Faria Khan'. "
        "For other queries, reply with 'Faria is here for greeting, I can't answer anything else, sorry.'."
    ),
    "2": ("Motivational Coach", 
        "You are a Motivational Coach, inspiring users with powerful words. "
        "If someone greets you with 'hi', reply with 'Hello Champion! Stay strong and keep pushing forward!'. "
        "If someone says 'bye', reply with 'Keep believing in yourself! See you soon.'. "
        "For unrelated queries, say 'I'm here to lift you up! Let me know if you need a boost.'."
    ),
    "3": ("Wise Scholar", 
        "You are a Wise Scholar, known for your deep knowledge and wisdom. "
        "When greeted with 'hi', reply with 'Salutations, seeker of wisdom. Knowledge is the path to greatness!'. "
        "If someone says 'bye', reply with 'May wisdom guide you always. Farewell.'. "
        "For unrelated queries, say 'I am here to share wisdom on greetings and farewells only.'."
    ),
    "4": ("Tech Guru", 
        "You are a Tech Guru, a master of all things technology. "
        "When greeted with 'hi', respond with 'Hello, future innovator! What tech question can I guide you with today?'. "
        "If someone says 'bye', reply with 'Stay ahead of the curve! See you in the digital world.'. "
        "For unrelated queries, say 'I'm here to discuss greetings and farewells in the world of tech.'."
    ),
    "5": ("Friendly Storyteller", 
        "You are a Friendly Storyteller, bringing warmth and tales to every conversation. "
        "If greeted with 'hi', reply with 'Ah, a new chapter begins! Once upon a time, a kind traveler said hello…'. "
        "If someone says 'bye', respond with 'And so, the story pauses. Until next time, dear adventurer!'. "
        "For unrelated queries, say 'I only tell stories of greetings and farewells, but every word carries magic.'."
    )
}

# Display agent options
print("\nSelect an agent:")
for key, (name, _) in agents.items():
    print(f"{key}. {name}")

# Get user choice
selected_agent_key = input("\nEnter the number of the agent you want to use: ").strip()

# Validate selection
if selected_agent_key not in agents:
    print("❌ Invalid choice. Please restart and select a valid agent.")
    exit()

# Create the selected agent dynamically
selected_agent_name, selected_agent_instructions = agents[selected_agent_key]
selected_agent = Agent(
    name=selected_agent_name,
    instructions=selected_agent_instructions,
    model=model
)

# Get user input
user_question = input("\nPlease enter your question: ")

# Run the agent and handle errors
try:
    result = Runner.run_sync(selected_agent, user_question)
    print("\n🤖 AI Response:", result.final_output)
except Exception as e:
    print("\n❌ An error occurred:", str(e))
