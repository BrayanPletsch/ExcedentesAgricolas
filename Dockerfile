FROM python:3.12-slim

# Instale dependências
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta do servidor
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["python", "api/app.py"]