# Backend

    python -m uvicorn app.main:app --host 0.0.0.0 --port 8000

# Frontend

    npx expo start -c

# Database

    psql -U postgres

# tester si ton serveur répond

    Invoke-WebRequest -Uri "http://127.0.0.1:8000/health" -UseBasicParsing
    ou
    Invoke-WebRequest -Uri "http://localhost:8000/health" -UseBasicParsing

# ipconfig(pour trouver ip de mon pc)

    ipconfig
