FROM pypy:latest
WORKDIR /app
COPY . /app
CMD python financial-calc.py