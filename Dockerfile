FROM alicek106/python-vim-devel:0.1
LABEL maintainer=alice_k106@naver.com

RUN git clone https://github.com/alicek106/available_stores_frontend.git
WORKDIR /available_stores_frontend
RUN  pip3 install -r requirements.txt
CMD ["python3", "/available_stores_frontend/main.py"]
