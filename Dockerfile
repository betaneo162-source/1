FROM ubuntu:22.04
RUN apt update && apt install -y gcc python3 python3-pip
COPY neo.c /app/
COPY neo1.c /app/
COPY app.py /app/
WORKDIR /app

# Compile both binaries
RUN gcc -pthread -O3 -o flame neo.c
RUN gcc -pthread -O3 -o neo neo1.c

RUN pip3 install flask
EXPOSE 5001
CMD ["python3", "app.py"]
