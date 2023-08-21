FROM python:3.11.2-slim-bullseye

SHELL ["/bin/bash", "-c"]

RUN mkdir -p /home/syneto-lab-dark-side/src
COPY src/pyproject.toml /home/syneto-lab-dark-side
WORKDIR /home/syneto-lab-dark-side

RUN apt-get update
RUN python3 -m venv .venv/
RUN .venv/bin/python3 -m pip install --upgrade pip
RUN .venv/bin/python3 -m pip install poetry
RUN .venv/bin/python3 -m poetry install

ENTRYPOINT [ ".venv/bin/python3", "-m", "uvicorn", "--host", "0.0.0.0", "src.main:app", "--reload" ]

# Build command: docker build -t isyneto .

# Start container: docker run -p 8000:8000 -d --name ctracker --mount type=bind,source="$(pwd)/src",target=/home/syneto-lab-dark-side/src tracker

#  Enter container: docker exec -it csyneto /bin/bash ; once inside, execute 
# `source .venv/bin/activate` and you are ready to code

# uvicorn main:app --reload --host 0