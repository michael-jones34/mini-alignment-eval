#!/bin/bash
# Setup script for Linux/Mac
# Usage: bash setup.sh

echo "Creating Python virtual environment (.venv)..."
python3 -m venv .venv

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Upgrading pip..."
python -m pip install --upgrade pip

echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "=========================================="
echo "Setup complete!"
echo "=========================================="
echo ""
echo "To activate the virtual environment, run:"
echo "  source .venv/bin/activate"
echo ""
echo "To set your OpenAI API key:"
echo "  export OPENAI_API_KEY='sk-...'"
echo ""
echo "To run the experiment:"
echo "  python main.py"
echo ""
