#!/usr/bin/env python3
import shutil
import psutil
import socket
import emails

def check_cpu_usage():
  """Returns True if the cpu is having too much usage, false otherwise."""
  return psutil.cpu_percent(1) > 80

def check_disk_space():
  usage = shutil.disk_usage('/')
  # Calculate the percentage of free space
  percent_free = 100 * usage.free / usage.total
  return percent_free < 20

def check_memory():
  mem = psutil.virtual_memory()
  return mem.available < 500

def check_localhost():
  """returns True if it fails to resolve 127.0.0.1, False otherwise"""
  localhost = "127.0.0.1"
  try:
    socket.gethostbyname("localhost")
    return False
  except:
    return True

def generate_error_report(subject_line):
  body = "Please check your system and resolve the issue as soon as possible."
  sender = "automation@example.com"
  recipient = "student-04-60d33f0099c9@example.com"
  subject = subject_line
  gen_err_email = emails.generate_error_report(sender, recipient, subject, body)
  emails.send(gen_err_email)


if check_cpu_usage() == True:
  subject_line = "Error - CPU usage is over 80%"
  generate_error_report(subject_line)
if check_disk_space() == True:
  subject_line = "Error - Available disk space is less than 20%"
  generate_error_report(subject_line)
if check_memory() == True:
  subject_line = "Error - Available memory is less than 500MB"
  generate_error_report(subject_line)
if check_localhost() == True:
  subject_line = "Error - localhost cannot be resolved to 127.0.0.1"
  generate_error_report(subject_line)
