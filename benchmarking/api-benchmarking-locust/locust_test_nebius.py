"""
Locust test script for Nebius AI Studio API endpoints.

This script tests the performance of Nebius AI Studio API by sending
concurrent requests to the API and measuring response times.


Example of how to run this script:

    locust -f locust_test_nebius.py --host https://api.studio.nebius.com/v1/ --users 10 --spawn-rate 1
"""

import os
import logging
import time
import random
from dotenv import load_dotenv
from locust import task, events, HttpUser, constant_pacing
from openai import OpenAI

# Load environment variables
load_dotenv()

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
# logger.setLevel(logging.DEBUG)

# Configuration
class MyConfig:
    pass
MyConfig.MODELS_TO_TEST = [model.strip() for model in os.getenv('MODELS_TO_TEST', '').split(',') if model.strip()]
MyConfig.TEMPERATURE = float(os.getenv("TEMPERATURE", "0.5"))
MyConfig.MAX_TOKENS = int(os.getenv("MAX_TOKENS", "1000"))
MyConfig.API_BASE_URL = os.getenv("API_BASE_URL", "https://api.studio.nebius.com/v1/")
MyConfig.NEBIUS_API_KEY = os.getenv("NEBIUS_API_KEY")
if not MyConfig.NEBIUS_API_KEY:
    raise ValueError("NEBIUS_API_KEY environment variable is required")


class NebiusAPIClient:
    """
    Client for interacting with Nebius AI Studio API.
    """

    def __init__(self, host=None):
        """
        Initialize the client with API configuration.
        
        Args:
            host (str): Base URL for the API endpoint
        """
        self.base_url = host or MyConfig.API_BASE_URL
        self.client = OpenAI(
            base_url=self.base_url,
            api_key=MyConfig.NEBIUS_API_KEY,
        )

    def send_completion_request(self, request_type, model, prompt, temperature=None, max_tokens=None):
        """
        Send a completion request to the Nebius API.
        
        Args:
            model (str): Model identifier
            prompt (str): Input prompt
            temperature (float): Sampling temperature
            max_tokens (int): Maximum number of tokens to generate
            
        Returns:
            dict: Response from the API
        """
        temperature = temperature or MyConfig.TEMPERATURE
        max_tokens = max_tokens or MyConfig.MAX_TOKENS

        logger.debug(f"Sending request to model: {model} (temp={temperature}, max_tokens={max_tokens}) with prompt: {prompt[:100]}...")

        request_meta = {
            "request_type": request_type,
            "name": f"{model}",
            "start_time": time.time(),
            "response_length": 0,
            "response": None,
            "context": {"model": model, "prompt": prompt},
            "exception": None,
        }
        
        start_perf_counter = time.perf_counter()

        try:
            # Send request to Nebius API
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            # Calculate response length
            content = response.choices[0].message.content
            request_meta["response_length"] = len(content.encode('utf-8'))
            request_meta["response"] = response
            
            logger.debug(f"Response: {content[:1000]}...")
            
        except Exception as e:
            logger.error(f"Exception: {e}")
            request_meta["exception"] = e

        end_perf_counter = time.perf_counter()
        request_meta["response_time"] = (end_perf_counter - start_perf_counter) * 1000

        # Fire the request event for Locust to track
        events.request.fire(**request_meta)
        
        return request_meta


class NebiusUser(HttpUser):
    """
    Locust User class for testing Nebius API endpoints.
    """
    
    # Wait time between tasks (1 second between requests per user)
    wait_time = constant_pacing(1)
    
    def on_start(self):
        """
        Initialize client when user starts.
        """
        self.api_client = NebiusAPIClient(host=self.host)

    @task
    def test_simple_completion(self):
        """
        Test a simple completion request.
        """
        for model in MyConfig.MODELS_TO_TEST:
            self.api_client.send_completion_request(
                request_type="completion_simple",
                model=model,
                prompt="What is the capital of France?",
                max_tokens=100
            )

    @task
    def test_explanation(self):
        """
        Test completion requests with longer explanation.
        """
        prompt = "Explain quantum computing in simple terms."
        # prompt =  "Write a haiku about cats.",
        # prompt =  "What are the benefits of renewable energy?"

        for model in MyConfig.MODELS_TO_TEST:
            self.api_client.send_completion_request(
                request_type="explanation",
                model=model,
                prompt=prompt,
                max_tokens=1000
            )

    @task
    def test_creative_writing_short(self):
        """
        Test completion requests with creative writing.
        """
        prompt = "Write a haiku about cats."

        for model in MyConfig.MODELS_TO_TEST:
            self.api_client.send_completion_request(
                request_type="creative_short",
                model=model,
                prompt=prompt,
                temperature=0.9, # higher temperature for creativity
                max_tokens=200,
            )
