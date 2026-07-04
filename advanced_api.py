import requests
import time

def test_api_performance_and_data():
    url = "https://jsonplaceholder.typicode.com/comments?postId=1"
    
    # Track latency (Performance QA Metric)
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    
    latency = end_time - start_time
    print(f"API Response Time: {latency:.2f} seconds")
    
    # Assertions for performance SLA
    assert latency < 2.0, "FAIL: API response time exceeded performance SLA!"
    assert response.status_code == 200, "FAIL: Unexpected status code"
    
    # Deep data structure validation
    comments = response.json()
    assert len(comments) > 0, "FAIL: Empty payload received"
    assert "email" in comments[0], "FAIL: Key structural field missing in API response"
    
    print("PASSED: Advanced API structural integrity and performance metrics validated.")

if __name__ == "__main__":
    test_api_performance_and_data()
