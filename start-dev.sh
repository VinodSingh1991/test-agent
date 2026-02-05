#!/bin/bash
# Start the Design System Agent API

cd "$(dirname "$0")"

echo "Starting Design System Agent API..."
echo "===================================="

# Check if .env file exists
if [ ! -f .env ]; then
    echo "Warning: .env file not found. Copying from .env.example"
    cp .env.example .env
    echo "Please update .env with your API keys"
fi

# Start the API server
cd design_system_agent/api
uvicorn main:app --reload --host 0.0.0.0 --port 8000
