FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn pydantic
EXPOSE 8000
CMD ["python", "main.py"]
