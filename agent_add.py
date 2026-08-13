def add_assistant_message(messages, assistant_text):
    messages.append(
        {
            "role": "assistant",
            "content": assistant_text
        }
    )
    return messages


def add_tool_message(messages, tool_name, tool_result):
    messages.append(
        {
            "role":"tool",
            "name": tool_name,
            "content":str(tool_result)
        }
    )
    return messages