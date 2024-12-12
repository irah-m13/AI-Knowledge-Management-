# Knowledge Base Application

## Overview

The **Knowledge Base Application** is a modular and scalable system designed to provide AI-driven responses and manage knowledge efficiently. This project leverages a structured folder system to separate concerns and ensure maintainability.

---

## Project Structure

```plaintext
knowledge base/
├── .env                     # Environment variables
├── main.py                  # Entry point of the application
├── app/
│   ├── src/                 # Main source code
│   │   ├── ai_service/      # AI/ML service logic
│   │   ├── database_conf/   # Database configuration and connections
│   │   ├── models/          # Data models and schemas
│   │   ├── routers/         # API route definitions
│   │   └── service/         # Business logic and utilities
│   ├── utils/               # Utility scripts
│       ├── logging/         # Logging configuration
│       └── prompts/         # AI/ML prompts and templates
└── .idea/                   # IDE configuration (optional)
```

---

## Features

1. **AI Service**: AI/ML logic for inference and integrations.
2. **Database Configuration**: Centralized database setup for storage and retrieval.
3. **API Routing**: Organized routers to define application endpoints.
4. **Data Models**: Schemas for structured data management.
5. **Prompts and Logging**: Modularized utility scripts for custom prompts and logging.

---

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- Required Python packages (`requirements.txt` not provided but assumed)

### Steps

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd knowledge base
   ```

2. **Set Up Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   Install necessary Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**

   Update the `.env` file with appropriate values:
   ```env
   DATABASE_URL=<your-database-url>
   API_KEY=<your-api-key>
   ```

5. **Run the Application**

   Start the FastAPI application:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

---

## Key Modules

### `src/`

- **`ai_service/`**: Handles AI model integration and inference.
  - Example: `azure_model.py`
- **`database_conf/`**: Configures database connections.
  - Example: `database.py`
- **`models/`**: Manages schemas for storing and validating data.
  - Example: `gpt_record.py`
- **`routers/`**: Defines RESTful API endpoints.
  - Example: `answer_router.py`
- **`service/`**: Contains business logic for processing requests.
  - Example: `llm_service.py`

### `utils/`

- **`logging/`**: Centralized logging configuration.
  - Example: `logging.py`
- **`prompts/`**: Templates and AI model prompts.
  - Example: `chatbot_prompts.py`

---

