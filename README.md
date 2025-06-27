# SelfFinance

This repository now includes a React frontend located in the `client` folder.

## Running the React App

1. Install Node dependencies:

   ```bash
   cd client
   npm install
   ```

2. Start the development server:

   ```bash
   npm run dev
   ```

The application will be available at the URL printed by the Vite server (usually `http://localhost:5173`).

## Running the FastAPI Backend

1. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Start the API server:

   ```bash
   uvicorn src.api.main:app --reload
   ```

The API will be available at `http://localhost:8000` by default.

## Running Both Servers Together

Use the provided Click command to launch the React frontend and FastAPI
backend at the same time:

```bash
python main.py start-app
```
