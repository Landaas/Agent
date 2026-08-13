from datetime import datetime

def define_tools():
    tools = {
        "get_current_time": get_current_time
    }
    return tools
    
def run_tool(tool_name, tools):
    if tool_name not in tools:
        return f"Error: unknown tool '{tool_name}'"
        
    tool_function = tools[tool_name]
    result = tool_function()
    
    return result


def get_current_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")