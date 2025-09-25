import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    database=os.getenv("DB_NAME")
)
cursor = conn.cursor()

def save_deployment(data):
    sql = "INSERT INTO deployments (id, status, appName) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE status=%s"
    val = (data['deploymentInfo']['deploymentId'], data['deploymentInfo']['status'], data['deploymentInfo']['applicationName'], data['deploymentInfo']['status'])
    cursor.execute(sql, val)
    conn.commit()

def save_pipeline(data):
    sql = "INSERT INTO pipelines (name, version) VALUES (%s, %s) ON DUPLICATE KEY UPDATE version=%s"
    val = (data['pipeline']['name'], data['pipeline']['version'], data['pipeline']['version'])
    cursor.execute(sql, val)
    conn.commit()
