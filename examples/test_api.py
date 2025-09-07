#!/usr/bin/env python3
"""
Test script for Flask API endpoints
Usage: python test_api.py
"""

import requests
import json

BASE_URL = "http://localhost:5000"

def test_health_check():
    """Test root endpoint"""
    print("\n1. Testing Health Check...")
    response = requests.get(f"{BASE_URL}/")
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.text}")
    return response.status_code == 200

def test_hello():
    """Test hello endpoint"""
    print("\n2. Testing Hello Endpoint...")
    response = requests.get(f"{BASE_URL}/hello")
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.text}")
    return response.status_code == 200

def test_radius_calculation():
    """Test radius calculation endpoint"""
    print("\n3. Testing Radius Calculation...")
    
    # POST request
    radius_data = {"radius": 10}
    response = requests.post(
        f"{BASE_URL}/radius",
        json=radius_data,
        headers={"Content-Type": "application/json"}
    )
    print(f"   POST Status: {response.status_code}")
    print(f"   POST Response: {json.dumps(response.json(), indent=2)}")
    
    # GET request
    response = requests.get(f"{BASE_URL}/radius")
    print(f"   GET Status: {response.status_code}")
    print(f"   GET Response: {json.dumps(response.json(), indent=2)}")
    
    return True

def test_book_crud():
    """Test book CRUD operations"""
    print("\n4. Testing Book CRUD Operations...")
    
    # Create book
    book_data = {
        "id": 1,
        "title": "Docker for Beginners",
        "author": "Student Developer"
    }
    response = requests.post(
        f"{BASE_URL}/book",
        json=book_data,
        headers={"Content-Type": "application/json"}
    )
    print(f"   CREATE Status: {response.status_code}")
    print(f"   CREATE Response: {json.dumps(response.json(), indent=2)}")
    
    # Read books
    response = requests.get(f"{BASE_URL}/book")
    print(f"   READ Status: {response.status_code}")
    print(f"   READ Response: {json.dumps(response.json(), indent=2)}")
    
    return True

def main():
    """Run all tests"""
    print("="*50)
    print("Flask API Test Suite")
    print("="*50)
    
    try:
        # Check if API is running
        requests.get(BASE_URL, timeout=1)
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Cannot connect to API at", BASE_URL)
        print("   Make sure the Docker container is running:")
        print("   docker-compose up")
        return
    
    tests = [
        test_health_check,
        test_hello,
        test_radius_calculation,
        test_book_crud
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"   ❌ Error: {e}")
            results.append(False)
    
    print("\n" + "="*50)
    print("Test Results Summary:")
    passed = sum(results)
    total = len(results)
    print(f"✅ Passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 All tests passed!")
    else:
        print("⚠️  Some tests failed")

if __name__ == "__main__":
    main()