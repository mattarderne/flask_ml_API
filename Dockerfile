FROM jupyter/datascience-notebook
RUN pip install flask
COPY models/* /home/jovyan/work/models/
COPY service.py /home/jovyan/work
WORKDIR /home/jovyan/work
ENV FLASK_APP=service.py
ENV FLASK_DEBUG=0
CMD [“flask”, “run”, “ — host=0.0.0.0”]