import paramiko
from scp import SCPClient
import pandas as pd
import matplotlib.pyplot as plt
import subprocess
import shlex
import sys
import subprocess

def openImage(path):
    imageViewerFromCommandLine = {'linux':'xdg-open',
                                  'win32':'explorer',
                                  'darwin':'open'}[sys.platform]
    subprocess.run([imageViewerFromCommandLine, path])

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

ssh = createSSHClient('192.168.1.30', 22, 'robot', 'maker')
scp = SCPClient(ssh.get_transport())

scp.get('/home/robot/2022_Hooey_Sucker/data.csv')
scp.get('/home/robot/2022_Hooey_Sucker/title.txt')


t = open('title.txt','r')
title = t.readline()
t.close()

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True


df = pd.read_csv('data.csv')


print(title)
print(df)
print(df.dtypes)

df.set_index('Reading').plot()
plt.title(title)
plt.ylim((43,64)) #use this for reverse
#plt.ylim((30,50)) #use this for forward


fname='/home/lauren/Documents/Lego/Graphs/'+ title + '.png'
plt.savefig(fname)

openImage(fname)

# plt.show()

