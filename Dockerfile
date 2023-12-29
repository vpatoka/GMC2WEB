#
FROM python:3.11.1-slim

# 
LABEL maintainer="Vlad Patoka <docker@patoka.org>"

#
EXPOSE 80

#
#VOLUME app_data

#
ENV PYTHONDONTWRITEBYTECODE=1

#
ENV PYTHONUNBUFFERED=1

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app

#
ENV HOME_HOSTNAME=localhost
CMD ["uvicorn", "app.geigerserv:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

