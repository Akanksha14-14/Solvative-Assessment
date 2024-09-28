#!/usr/bin/python3

import paramiko
import os
import subprocess
import datetime
hosts=["test2"]
db_host="localhost"
db_user="admin"
password="mysql@14"
now = datetime.datetime.now()
timestamp = str(now.strftime("%Y%m%d_%H:%M:%S"))

for i in hosts:
  name =i
  command = ['ping', '-c', '2', i]
  p= subprocess.Popen(command, stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
  p.wait()
  if p.poll():
    print(f'{i} server is down')
  else:
    ssh_client=paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=i,username=user_name)

def mysql_dump():

  print("Taking MYSQL DB Backup")
  cmd = "mysqldump -h %s -u %s -p%s --all-databases --single-transaction --flush-logs --master-data=2 | gzip > mysql_full_bkup_%s.gz | aws s3 cp - s3://backup_bucket/%s/dump/mysql/mysql_full_bkup_%s.gz " % (db_host, db_user, password, timestamp, name, timestamp)
  stdin,stdout,stderr=ssh_client.exec_command(cmd)
  x = stdout.channel.recv_exit_status()
  if x==0:
    print("MYSQL Backup Successful")
  else:
    print("MYSQL Backup Failed")

if __name__ == "__main__":
  mysql_dump()

#AWS role is attached to the mysql server which have aws s3 access  for that bucket



