# API End Point Testing with Locust

## Running the Code

### 1 - Setup the env

with `uv` 

```bash
uv sync
source .venv/bin/activate
```

with `pip`

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 2 - Create .env file

Create a `.env` file in the project root and add your Nebius API key:

```bash
cp env.example .env
```

Edit the `.env` file and add
- your actual API key
- model to test

```
NEBIUS_API_KEY=your_actual_api_key_here
MODEL_TO_TEST = "Qwen/Qwen3-30B-A3B-Instruct-2507"
```

### 3 - Run the benchmark


```bash
# Run with default settings (1 user, 1 spawn rate)
locust -f locust_test_nebius.py --host https://api.studio.nebius.com/v1/

# Run with custom settings
locust -f locust_test_nebius.py --host https://api.studio.nebius.com/v1/ --users 10 --spawn-rate 1 --run-time 5m

# Run with configuration file
locust --config locust-nebius.conf
```

You can see the results on browser UI at : http://localhost:8089


## Dev Notes

### Project Setup

```bash
uv init 
uv add locust python-dotenv openai

# run this if we update requirements
uv pip freeze > requirements.txt
```

## References 

- [Locust docs](https://docs.locust.io/en/stable/index.html)
- [Load Testing SageMaker Real-time Inference Endpoints with Locust](https://garystafford.medium.com/finding-your-llms-breaking-point-load-testing-sagemaker-real-time-inference-endpoints-with-locust-5b60cd1dfbf5) and [github repo](https://github.com/garystafford/sagemaker-locust-load-testing-demo)
