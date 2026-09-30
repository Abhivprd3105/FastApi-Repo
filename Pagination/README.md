⚡ FastAPI Pagination API

A simple and practical FastAPI Pagination API demonstrating how to efficiently fetch and navigate through large datasets using skip and limit parameters.

The API returns paginated user data along with useful metadata such as the total number of records and whether more results are available.

📦 Response Structure
{
  "data": [
    {
      "id": 1,
      "name": "User 1",
      "email": "user1@example.com",
      "status": "ACTIVE"
    }
  ],
  "total": 100,
  "skip": 0,
  "limit": 1,
  "has_more": true
}

🔑 Response Fields

data — List of users returned for the current request.

total — Total number of available records.

skip — Number of records skipped before returning results.

limit — Maximum number of records returned.

has_more — Indicates whether additional records are available.

🎯 Purpose

This project demonstrates a clean approach to implementing pagination in FastAPI and designing API responses that provide both data and pagination metadata.

It can serve as a starting point for APIs that need to handle large datasets efficiently without returning all records in a single response.
