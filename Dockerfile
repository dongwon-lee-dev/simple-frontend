FROM python:3.9-slim
RUN pip install streamlit requests
WORKDIR /app
COPY . /app
CMD ["streamlit", "run", "app.py", "--server.port=5000", "--server.address=0.0.0.0"]
