import ell
import openai
import sys
import os
import importlib.util
from prompt_lists import *

spec = importlib.util.spec_from_file_location("prompts", "/Users/sunnyharris/Documents/GitHub/EM-bot-refresh/prompts.py")
prompts = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prompts)

ell.init(store="./logdir", autocommit=True, verbose=True)

# custom client
client = openai.Client()

system_instructions = prompts.eva_system
vet_system_instructions = prompts.eva_system
system_instructions2 = critical_system
# case = prompts.test_case2 # histoplasmosis case
case = case_thyroid # 3 yo CP and syncope during soccer


# print(f"system instructions: {system_instructions}")

@ell.simple(model="o1-preview")
def test_case_gpto1_preview(case : str):
    return f"""{system_instructions} 
                 Here is the patient case: 
                 <case> 
                 {case} 
                 </case>"""


@ell.simple(model="gpt-4o")
def test_case_gpt4o(case : str):
    return [
        ell.system(system_instructions),
        ell.user(case)
    ]

@ell.simple(model="gpt-4o-mini")
def test_case_gpt4o_mini(case : str):
    return [
        ell.system(system_instructions),
        ell.user(case)
    ]

import anthropic
# custom client
anthropic_client = anthropic.Anthropic()

@ell.simple(model='claude-3-5-sonnet-20240620', client=anthropic_client, max_tokens=4000)
def test_case_claude_3_5s(case : str, system_instructions : str):
    return [
        ell.system(system_instructions),
        ell.user(case)
    ]

# Summarize Case
@ell.simple(model="gpt-4o-mini")
def summarize_case_gpt4o_mini(case : str, system_instructions : str):
    return [
        ell.system(system_instructions),
        ell.user(case)
    ]


# test_case_gpt4o_mini(case)
# test_case_gpt4o(case)
# test_case_gpto1_preview(case)

# testing iterative system prompts
response1 = test_case_claude_3_5s(case_thyroid, default_system_prompt_NDJSON_iterative)
response2 = test_case_claude_3_5s(f"""
<conversation>
    <turn>
        <user>{case_thyroid}</user>
        <ai>{response1}</ai>
    </turn>
    <turn>
        <user>{case_thyroid_user_prompt2}</user>
    </turn>
</conversation>
""",default_system_prompt_NDJSON_iterative)


# response3 = test_case_claude_3_5s(case_thyroid, default_system_prompt_NDJSON_iterative_2)
# response4 = test_case_claude_3_5s(f"""
# <conversation>
#     <turn>
#         <user>{case_thyroid}</user>
#         <ai>{response3}</ai>
#     </turn>
#     <turn>
#         <user>{case_thyroid_user_prompt2}</user>
#     </turn>
# </conversation>
# """,
# default_system_prompt_NDJSON_iterative_2)
