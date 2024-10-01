import ell
import openai
import sys
import os
import importlib.util

spec = importlib.util.spec_from_file_location("prompts", "/Users/sunnyharris/Documents/GitHub/EM-bot-refresh/prompts.py")
prompts = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prompts)

ell.init(store="./logdir", autocommit=True, verbose=True)

# custom client
client = openai.Client()

system_instructions = prompts.emma_system
system_instructions2 = "write a poem about this case"
case = prompts.test_case2

# print(f"system instructions: {system_instructions}")


@ell.simple(model="gpt-4o")
def test_case(case : str):
    return [
        ell.system(system_instructions),
        ell.user(case)
    ]

import anthropic
# custom client
anthropic_client = anthropic.Anthropic()

@ell.simple(model='claude-3-5-sonnet-20240620', client=anthropic_client, max_tokens=4000)
def test_case2(case : str):
    return [
        ell.system(system_instructions),
        ell.user(case)
    ]

test_case(case)
# test_case2(case)



