# CrewAI Starter Agent

A simple yet powerful AI research crew built with CrewAI that leverages multiple specialized agents to discover and analyze groundbreaking technologies. 

## References and Acknoledgements

- This example is adopted with thanks from [Arindam200/awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps) repo. [source](https://github.com/Arindam200/awesome-ai-apps/tree/main/starter_ai_agents/crewai_starter)
- [CrewAI documentation](https://docs.crewai.com/en/introduction)
- [Nebius AI Studio documentation](https://docs.nebius.com/studio/inference/quickstart)


## Features

- 🔬 **Specialized Research**: Dedicated researcher agent focused on discovering groundbreaking technologies
- 🤖 **Intelligent Analysis**: Powered by Meta-Llama-3.1-70B-Instruct model for deep insights
- 📊 **Structured Output**: Well-defined tasks with clear expected outputs
- ⚡ **Sequential Processing**: Organized task execution for optimal results
- 💡 **Customizable Crew**: Easy to extend with additional agents and tasks

## Prerequisites

- Nebius API key (get it from [Nebius AI Studio](https://studio.nebius.ai/))
- If running locally, python 3.10 or higher dev environment.

## Tech Stack

- CrewAI agent framework
- Nebius AI for LLM inference

## Task Structure

Tasks are defined with:

- Clear description
- Expected output format
- Assigned agent
- Sequential processing

## Example Tasks

- "Identify the next big trend in AI"
- "Analyze emerging technologies in quantum computing"
- "Research breakthroughs in sustainable tech"
- "Investigate future of human-AI collaboration"
- "Explore cutting-edge developments in robotics"

## Setup

The code can be run locally or on Google colab.  Colab is recommended, as it doesn't need any setup.

### Local env setup

1. Clone the repository:

```bash
git clone   https://github.com/nebius/ai-studio-cookbook/
cd  agents/crewai/starter-agent
```
2. Install dependencies:

Using conda/pip

```bash
pip  install  -r requirements.txt
```

if using `uv` package manager
```bash
uv pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Nebius API key:

```
NEBIUS_API_KEY=your_api_key_here
```

## Video

🎥 [Video tutorial](https://www.youtube.com/watch?v=jth10qwoMq0)

## Code

[agent.ipynb](agent.ipynb) notebook can be run locally or Google Colab.
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nebius/ai-studio-cookbook/blob/main/agents/crewai/starter-agent/agent.ipynb)

[agent.py](agent.py) python script can be run locally.

```bash
python agent.py
```




