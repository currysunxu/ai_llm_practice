from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.embeddings.ollama import OllamaEmbedding


# pre-condition: 1. pip install llama-index-embeddings-huggingface
# 2. pip install llama-index-embeddings-instructor
def embedding_model_local_bge_small(**kwargs):
    # embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-zh-v1.5")
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5",
                                       cache_folder="./embed_cache",
                                       **kwargs)
    return embed_model

# %pip install llama-index-embeddings-ollama
def embedding_model_ollama_online_nomic(**kwargs):
    ollama_embedding = OllamaEmbedding(
        model_name="nomic-embed-text:latest",
        base_url="http://123.60.22.2:11434",
        ollama_additional_kwargs={"mirostat": 0},
    )
    return ollama_embedding