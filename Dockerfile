FROM ubuntu:16.04
LABEL maintainer=alice_k106@naver.com
RUN sed -i 's/archive.ubuntu.com/ftp.daum.net/g' /etc/apt/sources.list
RUN apt update && \
  apt install python3 python3-pip git -y && \
  apt clean autoclean && \
  apt autoremove --yes && \
  rm -rf /var/lib/{apt,dpkg,cache,log}

RUN git clone https://github.com/alicek106/available_stores_frontend.git
WORKDIR /available_stores_frontend
RUN  pip3 install -r requirements.txt
CMD ["python3", "/available_stores_frontend/run.py"]
