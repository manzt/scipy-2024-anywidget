FROM mcr.microsoft.com/vscode/devcontainers/python:3.11

COPY ../requirements.txt /

RUN apt-get update -y && export DEBIAN_FRONTEND=noninteractive

RUN python3 -m pip install -r requirements.txt
