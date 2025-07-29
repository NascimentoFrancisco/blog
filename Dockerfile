# Usando uma imagem base Python
FROM python:3.12-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Define variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Instala as dependências do sistema necessárias para psycopg2
# RUN apt-get update && apt-get install -y libpq-dev gcc

# Instala as dependências do sistema necessárias para psycopg2 e netcat
RUN apt-get update && apt-get install -y libpq-dev gcc netcat

# Copia o arquivo requirements.txt e instala as dependências Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação para o contêiner
COPY . /app/

# Garante que o script entrypoint seja executável
RUN chmod +x /app/entrypoint.sh

# Expõe a porta que o Gunicorn vai usar
EXPOSE 8000

# Define o comando de entrada que será executado quando o contêiner iniciar
ENTRYPOINT ["/app/entrypoint.sh"]
