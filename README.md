# 🚀 FastAPI Employee Management System

A comprehensive employee management system built with [FastAPI](https://fastapi.tiangolo.com/) that meets enterprise-grade requirements. This project demonstrates best practices for building scalable, secure, and well-tested RESTful APIs.

## ✅ Functional Requirements Met

- ✅ **Containerized Service**: Full Docker support with docker-compose
- ✅ **OpenAPI Documentation**: Auto-generated interactive API documentation
- ✅ **Comprehensive Unit Testing**: Full test coverage with pytest
- ✅ **Custom Rate Limiting**: Proprietary implementation without external libraries
- ✅ **Data Security**: Multi-tenant architecture preventing data leaks between organizations
- ✅ **Python/FastAPI**: Built entirely with Python and FastAPI framework

## 🔒 Security Features

- **Multi-tenant Architecture**: Complete data isolation between organizations
- **Custom Rate Limiting**: Proprietary sliding window implementation
- **Field-level Access Control**: Dynamic field masking based on organization configuration
- **Input Validation**: Comprehensive Pydantic schema validation
- **SQL Injection Protection**: SQLAlchemy ORM with parameterized queries

---

## 📁 Project Structure

```
app/
├── api/                # Route definitions and API endpoints
├── config/             # App configuration and settings
├── constant/           # Application constants and enums
├── core/               # Core utilities (rate limiting, dependencies)
├── db/                 # Database connection and session management
├── schemas/            # Pydantic schemas for request/response validation
├── utils/              # Utility functions and database helpers
├── model/              # SQLAlchemy ORM models
├── repository/         # Data access layer (CRUD operations)
├── services/           # Business logic and use cases
├── main.py             # FastAPI application entry point
migrations/             # Alembic database migration scripts
alembic.ini             # Alembic configuration
requirements.txt        # Python dependencies
README.md               # Project documentation
```

## 🏗️ Architecture Overview

### Multi-Tenant Design
- **Organization-based Isolation**: All data is scoped to specific organizations
- **Dynamic Field Access**: Employee fields are dynamically masked based on organization configuration
- **Secure Data Access**: Repository layer enforces organization boundaries

### Custom Rate Limiting
- **Sliding Window Algorithm**: Proprietary implementation using in-memory storage
- **Thread-safe Design**: Handles concurrent requests safely
- **Configurable Limits**: Different limits for search vs general operations
- **No External Dependencies**: Pure Python implementation

---

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.12+
- PostgreSQL 16+
- Docker & Docker Compose (for containerized deployment)

### 🍎 MacOS

```bash
# Install PostgreSQL dependencies
brew install libpq && brew link --force libpq

# Create virtual environment
python3 -m venv venv && source venv/bin/activate

# Install dependencies
pip3 install -r requirements.txt
```

### 🐧 Linux

```bash
# Install PostgreSQL dependencies
sudo apt-get install libpq-dev

# Create virtual environment
python3 -m venv venv && source venv/bin/activate

# Install dependencies
pip3 install -r requirements.txt
```

### Environment Configuration

Create a `.env` file in the root directory:

```bash
# Database Configuration
DB_URL=postgresql+psycopg://admin:password@localhost:5432/db_dev

# Rate Limiting Configuration
SEARCH_RATE_LIMIT=1000
GENERAL_RATE_LIMIT=100
RATE_LIMIT_WINDOW=3600

# Application Configuration
LOG_LEVEL=INFO
MAX_PAGE_SIZE=100
ALLOWED_ORIGINS=["*"]
```

---

## 🧬 Database Migration (Alembic)

### Create a new migration

```bash
alembic revision --autogenerate -m "your migration message"
```

### Apply latest migrations

```bash
alembic upgrade head
```

### Roll back one migration

```bash
alembic downgrade -1
```

---

## 🌱 Seeding Initial Data

To populate the database with test data (e.g., 1,000,000 employees), run the following command:

```bash
PYTHONPATH=. python3 app/config/seed.py
```

> **Note:** Make sure your database
> is running and all migrations have been applied before executing the seed script.

---

## 🚀 Running the Application

### Development Mode

```bash
# Start the FastAPI development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Production Mode

```bash
# Using Gunicorn with Uvicorn workers
gunicorn app.main:app --bind 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker -w 8
```

## 📚 API Documentation

Once the application is running, you can access:

- **Interactive API Docs (Swagger UI)**: http://localhost:8000/docs

### API Endpoints

| Endpoint | Method | Description | Rate Limit |
|----------|--------|-------------|------------|
| `/organization/` | GET | Search organizations | General |
| `/department/` | GET | Search departments | General |
| `/position/` | GET | Search positions | General |
| `/location/` | GET | Search locations | General |
| `/employee/` | GET | Search employees | Search (higher limit) |

### Example API Usage

```bash
# Search employees in an organization
curl "http://localhost:8000/employee/?organization_id=1&keyword=john&limit=10&offset=0"

# Search departments
curl "http://localhost:8000/department/?keyword=engineering&limit=5"

# Get API documentation
curl "http://localhost:8000/openapi.json"
```

---

## 🧪 Testing

### Test Coverage
- **Unit Tests**: Comprehensive test coverage for all components
- **API Tests**: End-to-end API endpoint testing
- **Rate Limiting Tests**: Custom rate limiter functionality testing
- **Security Tests**: Data isolation and field masking validation

### Running Tests

#### Prerequisites
Create a test database manually:
```sql
CREATE DATABASE db_test;
```

#### Run All Tests
```bash
pytest
```

#### Run Specific Test Categories
```bash
# API tests only
pytest tests/api/

# Employee API tests only
pytest tests/api/test_employee_api.py -v

# Rate limiter tests
pytest tests/core/test_rate_limiter.py -v

# All tests with coverage report
pytest --cov=app --cov-report=html
```

#### Test Examples

```bash
# Test employee search with rate limiting
pytest tests/api/test_employee_api.py::TestSearchEmployee::test_employee_search_rate_limit -v

# Test data isolation between organizations
pytest tests/api/test_employee_api.py::TestSearchEmployee::test_search_employees -v

# Test custom rate limiter functionality
pytest tests/core/test_rate_limiter.py::test_is_allowed_within_limit -v
```

## 🐳 Containerized Deployment

### Docker Features
- **Multi-stage Build**: Optimized production image
- **Health Checks**: Database and application health monitoring
- **Environment Configuration**: Flexible configuration via environment variables
- **Production Ready**: Gunicorn with multiple workers for high performance

### Quick Start with Docker

#### 1. Build and Run with Docker Compose
```bash
# Build the application
docker compose build

# Start all services (PostgreSQL + FastAPI)
docker compose up --profile prod -d

# Check service status
docker compose ps

# View logs
docker compose logs -f fastapi
```

#### 2. Stop Services
```bash
# Stop and remove containers
docker compose down

# Remove volumes (database data)
docker compose down -v
```

### Manual Docker Commands

#### Build Image
```bash
docker build -t fastapi-employee-system .
```

#### Run Container
```bash
# Run with PostgreSQL
docker run -d \
  --name fastapi-app \
  -p 8000:8000 \
  -e DB_URL=postgresql+psycopg://admin:password@host.docker.internal:5432/db_dev \
  fastapi-employee-system
```

### Production Deployment

#### Environment Variables for Production
```bash
# Database
DB_URL=postgresql+psycopg://user:pass@prod-db:5432/prod_db

# Rate Limiting (adjust based on traffic)
SEARCH_RATE_LIMIT=5000
GENERAL_RATE_LIMIT=500
RATE_LIMIT_WINDOW=3600

# Security
ALLOWED_ORIGINS=["https://yourdomain.com"]
LOG_LEVEL=WARNING
```

#### Docker Compose for Production
```yaml
version: '3.8'
services:
  fastapi:
    build: .
    environment:
      - DB_URL=postgresql+psycopg://admin:password@postgres:5432/prod_db
      - SEARCH_RATE_LIMIT=5000
      - GENERAL_RATE_LIMIT=500
    ports:
      - "8000:8000"
    depends_on:
      postgres:
        condition: service_healthy
    restart: unless-stopped
```

---

## 🛡️ Security & Rate Limiting

### Custom Rate Limiting Implementation

This project implements a proprietary rate limiting solution without external dependencies:

#### Features
- **Sliding Window Algorithm**: More accurate than fixed window counters
- **Thread-safe Design**: Handles concurrent requests safely
- **Configurable Limits**: Different limits for different endpoint types
- **Memory Efficient**: Automatic cleanup of expired requests
- **Real-time Statistics**: Track usage and reset times

#### Implementation Details
```python
# Rate limiter configuration
SEARCH_RATE_LIMIT = 1000    # Requests per hour for search endpoints
GENERAL_RATE_LIMIT = 100    # Requests per hour for general endpoints
RATE_LIMIT_WINDOW = 3600    # Time window in seconds (1 hour)
```

#### Rate Limiting Headers
The API returns rate limiting information in response headers:
```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 2024-01-01T12:00:00Z
```

### Data Security & Multi-tenancy

#### Organization-based Data Isolation
- **Complete Data Separation**: All queries are scoped to organization_id
- **Field-level Access Control**: Employee fields are dynamically masked
- **No Data Leakage**: Impossible to access data from other organizations

#### Field Masking Example
```json
// Organization A configuration allows: ["first_name", "last_name", "email"]
{
  "id": 1,
  "first_name": "John",
  "last_name": "Doe", 
  "email": "john.doe@company.com",
  "allowed_fields": ["first_name", "last_name", "email", "id"]
}

// Organization B configuration allows: ["first_name", "last_name", "phone", "department"]
{
  "id": 2,
  "first_name": "Jane",
  "last_name": "Smith",
  "phone": "+1234567890",
  "department": "Engineering",
  "allowed_fields": ["first_name", "last_name", "phone", "department", "id"]
}
```

#### Security Measures
- **Input Validation**: All inputs validated with Pydantic schemas
- **SQL Injection Protection**: SQLAlchemy ORM with parameterized queries
- **CORS Configuration**: Configurable cross-origin resource sharing
- **Environment-based Configuration**: Secure configuration management

---

## 📖 OpenAPI Documentation

### Auto-generated API Documentation
FastAPI automatically generates comprehensive OpenAPI documentation:

#### Available Documentation Formats
- **Swagger UI**: Interactive API explorer at `/docs`

#### Documentation Features
- **Interactive Testing**: Test API endpoints directly from the browser
- **Request/Response Examples**: Auto-generated examples for all endpoints
- **Schema Validation**: Real-time validation of request/response schemas
- **Authentication Support**: Ready for future authentication implementation

#### API Schema Export
```bash
# Export OpenAPI schema to file
curl http://localhost:8000/openapi.json > api-schema.json

# Share API documentation
# The OpenAPI schema can be imported into tools like:
# - Postman
# - Insomnia
# - Swagger Editor
# - API Gateway services
```

### API Response Format
All API endpoints follow a consistent response format:

```json
{
  "items": [
    {
      "id": 1,
      "first_name": "John",
      "last_name": "Doe",
      "email": "john.doe@company.com",
      "allowed_fields": ["first_name", "last_name", "email", "id"]
    }
  ],
  "total": 1,
  "limit": 10,
  "offset": 0
}
```

### Error Handling
The API provides consistent error responses:

```json
{
  "detail": "Rate limit exceeded. Try again at 2024-01-01T12:00:00Z."
}
```

Common HTTP status codes:
- `200`: Success
- `400`: Bad Request (validation errors)
- `404`: Not Found
- `429`: Too Many Requests (rate limit exceeded)
- `500`: Internal Server Error
