from tools import define_tools, run_tool, get_current_time
from agent_add  import add_tool_message, add_assistant_message

def create_messagees(system_promt):
    messages = [
        {
            "role" : "system",
            "content" : system_promt
        }
    ]

def add_user_message(messages, user_text):
    messages.append(
        {
            "role" : "user",
            "content" : user_text
        }
    )

def mock_model_decision(messages):
    last_message = messages[-1]
    user_text = last_message["content"].lower()


    if "time" in user_text:
        return {
            "type": "tool",
            "tool_name": "get_current_time"
        }


    if "what can you do" in user_text:
        return {
            "type": "answer",
            "content": "I can answer simple questions and use tools."
        }


    if "hello" in user_text:
        return {
            "type": "answer",
            "content": "Hello! I am your learning agent."
        }


    return {
        "type": "answer",
        "content": "I do not understand yet, but I am learning."
    }


def agent_step(messages, user_text):
    tools = define_tools()
    messages = add_user_message(messages, user_text)
    decision = mock_model_decision(messages)

    if decision["type"] == "answer":
        response = decision["content"]


    elif decision["type"] == "tool":
        tool_name = decision["tool_name"]
        tool_result = run_tool(tool_name, tools)
        response = f"The result is: {tool_result}"


    else:
        response = "Error: unknown decision type."


    messages = add_assistant_message(messages, response)


    return messages, response


def agent_loop():
    messages = create_messages("You are a simple learning agent.")


    print("Learning agent started. Type 'quit' to exit.")


    while True:
        user_text = input("You: ")


        if user_text.lower() == "quit":
            print("Agent stopped.")
            break


        messages, response = agent_step(messages, user_text)


        print("Agent:", response)





#agent_loop()
messages= create_messagees("Your a simple agent")
tools = define_tools()

tool_name="get_current_time"
tool_result= run_tool(tool_name, tools)

messages = add_tool_message(messages, tool_name, tool_result)
print(messages)