FROM python:3.10
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
ADD . /app/
CMD ["watchmedo", "auto-restart", "--patterns=*.py", "--recursive", "--", "python", "-u", "booking.py"]