import logging
import os 
import ConfigParser

import airflow
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from datetime import timedelta

default_args = {
    'retries': 1,
    'start_date': airflow.utils.dates.days_ago(0)
}

dag = DAG(
    'trst_bq_fin_divn_lookup_ini',
    default_args=default_args,
    description='DAG to look up financial division number for prop & co-branded cards',
    schedule_interval=None)

#dummyOp = DummyOperator(task_id='dummy_task',
#    dag=dag)
	
sqlDir = 'bq-sql/'

createcustomerdetails = BigQueryOperator(
    task_id='load_data',
    sql=sqlDir+'load_data.sql',
    use_legacy_sql=False,
    destination_dataset_table=None,
    dag=dag)


removetheduplicates= BigQueryOperator(
    task_id='remove_dup',
    sql=sqlDir+'remove_dup.sql',
    use_legacy_sql=False,
    destination_dataset_table=None,
    dag=dag)
 
avgsalarywithconstraint = BigQueryOperator(
    task_id='avg_sal',
    sql=sqlDir+'avg_sql.sql',
    use_legacy_sql=False,
    destination_dataset_table=None,
    dag=dag
)
createcustomerdetails>>removetheduplicates>>avgsalarywithconstraint