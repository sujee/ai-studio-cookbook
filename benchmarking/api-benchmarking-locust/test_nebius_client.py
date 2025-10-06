"""
Simple test script to validate the NebiusAPIClient implementation.
This script tests the basic functionality without running a full Locust test.
"""

import os
import sys
from dotenv import load_dotenv

# Add the current directory to the path so we can import our locust script
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Load environment variables
load_dotenv()

def test_nebius_client():
    """
    Test the NebiusAPIClient implementation.
    """
    try:
        # Import the client from our locust script
        from locust_test_nebius import NebiusAPIClient
        
        print("Testing NebiusAPIClient...")
        
        # Initialize the client
        client = NebiusAPIClient()
        print(f"Client initialized with base URL: {client.base_url}")
        
        # Test that we have an API key
        api_key = os.getenv("NEBIUS_API_KEY")
        if not api_key:
            print("WARNING: NEBIUS_API_KEY not found in environment variables")
            print("Please set the NEBIUS_API_KEY environment variable to test with actual API calls")
            return True
        
        print("NEBIUS_API_KEY found in environment")
        print("Client setup successful!")
        return True
        
    except Exception as e:
        print(f"Error testing NebiusAPIClient: {e}")
        return False

if __name__ == "__main__":
    success = test_nebius_client()
    if success:
        print("\n✓ NebiusAPIClient test passed!")
        print("\nTo run the full Locust test:")
        print("1. Make sure you have set your NEBIUS_API_KEY in the .env file")
        print("2. Run: locust -f locust_test_nebius.py --host https://api.studio.nebius.com/v1/")
    else:
        print("\n✗ NebiusAPIClient test failed!")
        sys.exit(1)
