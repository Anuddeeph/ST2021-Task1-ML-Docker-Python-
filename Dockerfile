FROM centos:latest
RUN yum install python3 -y
RUN pip3 install sklearn
RUN pip3 install pandas
RUN pip3 install numpy

RUN mkdir /MLpy_WS

WORKDIR /MLpy_WS

COPY Salary_Data.csv /MLpy_WS
COPY ML_code.py /MLpy_WS
CMD ["python3","/MLpy_WS/ML_code.py"]


