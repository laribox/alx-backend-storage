#!/usr/bin/env python3
"""
This module provides displays log stats about Nginx logs stored in MongoDB.

Database: logs
Collection: nginx
Display:
    - First line: x logs where x is the number of documents in this collection
    - Second line: Methods:
        5 lines with the count of documents with method = [
            "GET", "POST", "PUT", "PATCH", "DELETE",
        ] in this order (with a tab before each line)
    - One line with the number of documents with:
        method=GET and path=/status
"""

from pymongo import MongoClient

ALLOWED_METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

def display_logs(collection):
    """Prints log statistics for the specified MongoDB collection."""
    
    # Total document count
    log_count = collection.count_documents({})
    print(f"{log_count} logs")

    # Method counts
    print("Methods:")
    for method in ALLOWED_METHODS:
        method_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    # Specific GET /status count
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

def main():
    """Main function that connects to MongoDB and displays logs."""
    client = MongoClient("mongodb://localhost:27017/")
    collection = client.logs.nginx
    display_logs(collection)

if __name__ == "__main__":
    main()

