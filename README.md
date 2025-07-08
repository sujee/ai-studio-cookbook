# Nebius AI Studio Cookbook

The Nebius AI Studio Cookbook is a collection of guides and examples for working with open models using Nebius AI Studio. Use these recipes to build and deploy intelligent applications faster.

## Contributing

We welcome your contributions!

### [See Community Contributions](community/README.md)


## Resources

- [Nebius AI Studio Docs](https://docs.nebius.com/studio)
- [Nebius AI Blog](https://nebius.com/blog)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Getting Started

**1 - Prerequisites**

- You’ll need a Nebius AI Studio account and API key. Sign up for free [here](https://studio.nebius.com/).
- Python runtime (local, Google Colab etc.)
- Git

**2 - Follow the [setup guide](setup-dev-env.md)**

**3 - Follow project-specific instructions**

## [APIs](api/)

Access AI Studio using various APIs.

| Code                                       | Description           |
|--------------------------------------------|-----------------------|
| [api_native.ipynb](api/api_native.ipynb)         | OpenAI compatible API |
| [api_litellm.ipynb](api/api_litellm.ipynb)       | Using LiteLLM API     |
| [api_aisuite.ipynb](api/api_aisuite.ipynb)       | Using aisuite API     |
| [api_llamaindex.ipynb](api/api_llamaindex.ipynb) | Using llama-index API |



## Embeddings


## [RAG](rag/)

| Example                             | Description                                         | Tech Stack                         |
|-------------------------------------|-----------------------------------------------------|------------------------------------|
| [PDF RAG](rag/rag-pdf-llama-index/) | Simple PDF RAG application                          | LLamaindex + Nebius AI     |
| [Chat with Documents](rag/chat-with-pdf)  | UI Web app to chat interactively with PDF documents | LLamaindex + Nebius AI + Streamlit |

## [Agents](agents/)


| Framework | Name                                          | Description           |
|-----------|-----------------------------------------------|-----------------------|
| **CrewAI**    | [Research agent](agents/crewai/starter-agent) | Single research agent |
|           | [All CrewAI examples](agents/crewai/)    

## Vision Modes


## Observability

## MCP

## Finetuning

## Distillation

## LORA

---
© Nebius BV, 2025

