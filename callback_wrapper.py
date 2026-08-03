
from support_assistant import generate_reply

async def my_target_wrapper(input:str) ->str :
    reply,context,tool_called = generate_reply(input)
    return reply
