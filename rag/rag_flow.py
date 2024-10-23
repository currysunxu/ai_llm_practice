import os
from pathlib import Path
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from rag.embedding import embedding_model_local_bge_small
from structured_data_demo.llms import deepseek_llm
from structured_data_demo.structured_data_extract_method import openai_pydantic_api_data_extract

project_root = Path().resolve()
Settings.embed_model = embedding_model_local_bge_small()
Settings.llm = deepseek_llm()
# to resolve the warning TOKENIZERS_PARALLELISM
os.environ["TOKENIZERS_PARALLELISM"] = "false"


reader = SimpleDirectoryReader(input_files=[project_root.parent /'data'/'EV_local_prediction_PRD.pdf'])

# 1 . load data
docs = reader.load_data()

# 2. vector data, docs -> index (store to memory instead of disk)
# No API key found for OpenAI error , solution: to set Global Settings.embed_model from embedding model local or online
index = VectorStoreIndex.from_documents(docs)
print(f"Loaded {len(docs)} documents")

# 3. mock user to query
# No API key fro llm openai , solution: to set global Settings.llm from deepseek_llm method
chat_engine = index.as_chat_engine()

# normal query
# response = chat_engine.query("introduce an ev local prediction")
# print(response)

#streaming output
response = chat_engine.stream_chat("introduce an ev local prediction")
for token in response.response_gen:
    openai_pydantic_api_data_extract(token)