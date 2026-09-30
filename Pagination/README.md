# ⚡ FastAPI Pagination API

A simple and practical **Pagination API built with FastAPI** that demonstrates how to efficiently retrieve large datasets using `skip` and `limit` parameters.

The API returns user data along with pagination metadata such as the total number of records and whether more records are available.

## 🚀 Features

- ⚡ FastAPI-based REST API
- 📄 Pagination using `skip` and `limit`
- 📊 Total record count
- 🔍 Easy-to-use query parameters
- ✅ `has_more` indicator for additional records
- 📦 Clean and structured JSON response
- 📚 Automatic Swagger/OpenAPI documentation

## 📦 API Response

The API returns a response in the following format:

```json
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
