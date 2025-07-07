# RAG Example with LLama-Index + Nebius

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nebius/ai-studio-cookbook/blob/main/rag/rag-pdf-llama-index/rag_pdf_query.ipynb)
[![](https://img.shields.io/badge/Powered%20by-Nebius%20AI-orange?style=flat&labelColor=orange&color=green)](https://nebius.com/ai-studio)

This example shows querying a PDF using  [llama index](https://docs.llamaindex.ai/en/stable/) framework and running LLM on [Nebius AI Studio](https://studio.nebius.com/)


## References and Acknoledgements

- [llamaindex documentation](https://docs.llamaindex.ai/en/stable/)
- [Nebius AI Studio](https://studio.nebius.com/)
- [Nebius AI Studio documentation](https://docs.nebius.com/studio/inference/quickstart)

## Pre requisites

- Nebius API key.  Sign up for free at [AI Studio](https://studio.nebius.com/)


## Running the Code on Google Colab

No setup required.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nebius/ai-studio-cookbook/blob/main/rag/rag-pdf-llama-index/rag_pdf_query.ipynb)

## Run the example locally

### Option-1 (Preferred): Using `uv`

Install dependencies

```bash
uv  sync
```

Run notebook

```bash
uv run jupyter lab  rag_pdf_query.ipynb
```

### Option-2: Using pip

```bash
pip install -r requirements.txt
```

```bash
jupyter lab  rag_pdf_query.ipynb
```


