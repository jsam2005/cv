#!/bin/bash
set -e
cd "$(dirname "$0")"

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

echo ""
echo "Setup complete. Run an experiment like this:"
echo "  source .venv/bin/activate"
echo "  python exp/ex_01.py path/to/your/image.jpg"
