FROM apache/airflow:2.3.3
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

# install dbt into a venv to avoid package dependency conflicts
WORKDIR "/usr/local/airflow"

COPY ../../  .
COPY dbt-requirements.txt ./
RUN python -m virtualenv dbt_venv && source dbt_venv/bin/activate && \
    PIP_USER=false pip install  --no-cache-dir -r dbt-requirements.txt && deactivate 