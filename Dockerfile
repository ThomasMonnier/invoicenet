FROM ubuntu:20.04 

# Install Python dependencies
RUN apt-get update && apt-get upgrade -y
RUN apt-get install ffmpeg libsm6 libxext6 libgeos-dev -y
RUN apt-get install python3 python3-pip -y
RUN apt-get install tesseract-ocr poppler-utils libxext-dev libsm-dev libxrender-dev -y
ENV LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libgomp.so.1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install wheel https://github.com/diyor28/tf-docker-m1/releases/download/v1.0.0/tensorflow-2.8.0-cp38-cp38-linux_aarch64.whl
RUN pip install https://github.com/diyor28/tf-docker-m1/releases/download/v1.0.0/tensorflow_addons-0.16.1-cp38-cp38-linux_aarch64.whl

COPY . .

ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]
