# PYTHON — tool_use_demo.py
import os
from dotenv import load_dotenv

load_dotenv()
import anthropic, json

client = anthropic.Anthropic()

# === Define tools ===
tools = [
    {
        "name": "calculate",
        "description": "Evaluate a mathematical expression. Use for any math.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "The math expression to evaluate, e.g. '2 + 2' or '500000 * 0.2'"
                }
            },
            "required": ["expression"]
        }
    },
    {
        "name": "get_weather",
        "description": "Get current weather for a city.",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "City name, e.g. 'Bangkok'"}
            },
            "required": ["city"]
        }
    }
]

# === Tool implementations ===
def execute_tool(name, inputs):
    if name == "calculate":
        try:
            result = eval(inputs["expression"])  # ⚠️ Use ast.literal_eval in production!
            return str(result)
        except Exception as e:
            return f"Error: {e}"
    elif name == "get_weather":
        # Simulated — replace with real API
        weather_data = {"Bangkok": "32°C, Humid, Partly Cloudy",
                        "Singapore": "30°C, Thunderstorms"}
        return weather_data.get(inputs["city"], "Weather data not available")

# === Conversation loop with tool use ===
def ask(question):
    messages = [{"role": "user", "content": question}]
    
    while True:
        response = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=1024,
            tools=tools,
            messages=messages
        )
        
        # Check if Claude wants to use tools
        tool_calls = [b for b in response.content if b.type == "tool_use"]
        
        if not tool_calls:
            # No tool calls — return text response
            return response.content[0].text
        
        # Execute each tool call
        messages.append({"role": "assistant", "content": response.content})
        
        for tool_call in tool_calls:
            print(f"  🔧 Using tool: {tool_call.name}({tool_call.input})")
            result = execute_tool(tool_call.name, tool_call.input)
            messages.append({
                "role": "user",
                "content": [{"type": "tool_result",
                             "tool_use_id": tool_call.id,
                             "content": result}]
            })

# Test it!
print(ask("What's the weather in Bangkok and what's 45000 * 4.5?"))
print(ask("If Bangkok is 32°C, what is that in Fahrenheit?"))