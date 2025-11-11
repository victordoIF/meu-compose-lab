# Imagem base
FROM python:3.11-slim

# Diretório de trabalho
WORKDIR /app

# Copiar arquivos
COPY app.py .

# Instalar dependências
RUN pip install flask pymysql cryptography

# Porta exposta
EXPOSE 5000

# Comando padrão
CMD ["python", "app.py"]
