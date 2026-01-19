#!/bin/bash

echo "========================================"
echo " Agentic AI System"
echo " National-Scale Decision Making"
echo "========================================"
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "ERROR: .env file not found!"
    echo ""
    echo "Please create .env file first:"
    echo "  1. Copy .env.example to .env"
    echo "  2. Add your API key"
    echo ""
    echo "For FREE setup, see FREE_SETUP.md"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies if needed
echo "Checking dependencies..."
pip install -q -r requirements.txt

# Run the application
echo ""
echo "Starting Agentic AI System..."
echo ""
python main.py
