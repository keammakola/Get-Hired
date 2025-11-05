#!/bin/bash

echo "Starting Get Hired Application..."

if [ ! -f .env ]; then
    echo "Error: .env file not found. Please create one with GEMINI_API_KEY"
    exit 1
fi

echo "Starting backend API..."
cd api
python3 main.py &
API_PID=$!
cd ..

sleep 3

echo "Starting frontend..."
cd frontend
npm run dev &
FRONTEND_PID=$!
cd ..

echo ""
echo "Application started!"
echo "Backend API: http://localhost:8000"
echo "Frontend: http://localhost:5173"
echo ""
echo "Press Ctrl+C to stop both services"

trap "kill $API_PID $FRONTEND_PID; exit" INT

wait
