FROM python:3.10

RUN pip install -r requirements.txt

WORKDIR /app

RUN echo 'alias norminette="flake8"' >> /root/.bashrc

CMD ["top", "-b"]