FROM python:3.9

RUN apt-get update && apt-get install -y curl \
    && mkdir /booking \
    && curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \
    && . $HOME/.cargo/env \
    && pip install --upgrade pip

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

WORKDIR /booking

COPY reqs.txt .

RUN pip install -r reqs.txt

COPY . .

RUN chmod a+x /booking/docker/*.sh

#CMD ["gunicorn", "app.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]