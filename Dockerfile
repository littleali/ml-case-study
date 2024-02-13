FROM tensorflow/tensorflow:2.15.0.post1

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["bash"]
