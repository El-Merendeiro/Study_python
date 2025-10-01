FROM python:3.11-slim

WORKDIR /app

# Aggiorna pip
RUN pip install --upgrade pip

# Copia requirements
COPY requirements.txt .

# Installa torch CPU-only + altre dipendenze
RUN pip install --no-cache-dir -r requirements.txt -f https://download.pytorch.org/whl/cpu/torch_stable.html

# Copia tutto il progetto
COPY . .

ENV PORT 8080
EXPOSE 8080

CMD ["python", "app.py"]
