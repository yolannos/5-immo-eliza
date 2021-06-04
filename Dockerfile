FROM python:3.7-stretch
LABEL Yolann Sabaux <yolann.sabaux@gmail.com>

# install build utilities
RUN apt-get update && apt-get install -y gcc make apt-transport-https ca-certificates build-essential

# check our python environment
RUN python3 --version
RUN pip3 --version

# set the working directory for containers
WORKDIR  /usr/src/5-IMMO-ELIZA

# Installing python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the files from the project’s root to the working directory (Le point, je prends le src et le mets là où je suis)
COPY src/ . 
RUN ls -la /usr/src/*

# Running Python Application
EXPOSE 8501
ENTRYPOINT ["streamlit","run"]
CMD ["/usr/src/main.py"]
