FROM ubuntu:latest

LABEL version="1.0.0" description="Minha imagem" maintainer="Stephanie D Angelo<stephanie.santos@aluno.faculdadeimpacta.com.br>"

RUN apt-get update && apt-get -y --no-install-recommends install htop && rm -rf /var/lib/apt/lists/*

RUN cd / && mkdir STEPHANIE

CMD /bin/bash
