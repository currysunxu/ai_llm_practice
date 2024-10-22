from llama_index.llms.openai import OpenAI

# need to add deepseek models in source code .venv/lib/python3.11/site-packages/llama_index/llms/openai/utils.py
def deepseek_llm(**kwargs):
    llm = OpenAI(api_key="sk-829818565b6f4634abfb8cc2c8031400",
                 model="deepseek-chat",
                 api_base="https://api.deepseek.com")
    return llm