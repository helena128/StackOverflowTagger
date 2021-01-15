FROM python:3.8

COPY api/ api/
WORKDIR api/

EXPOSE 8080 8080/tcp

RUN pip install --no-cache-dir -r requirements.txt && \
    python -m nltk.downloader stopwords

CMD ["python", "./main.py"]
