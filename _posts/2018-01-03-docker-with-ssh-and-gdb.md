---
title: "Docker: GDB, SSH... "
categories:
  - GDB
  - Remote Debugging
  - Docker
  - CLion
tags:
  - Development
  - Tools
  - GDB
  - SSH
  - Docker
  - Remote Debugger
  - CLion
  - MinGW
  - Windows

---

To set remote debugger GDB on docker container we need to setup it as ssh server. 

# Dockerfile

Info:
- based on [cs5450](https://pages.github.coecis.cornell.edu/cs5450/website/assignments/p1/docker.html)
  what I keep locally as [docker-gdb-ssh]{{ "" | absolute_url }}{% post_url 2018-01-03-docker-with-ssh-and-gdb %}
  
  [pdf]("/assets/sets/docker-remote-dev/CS5250-Fall2017 - Remote Development using containers.pdf")

- We expose 3 ports: 22, 9999 and 7777:
-- Port 22 will be used to SSH into the container,
-- Port 9999 can be used to connect to the program from outside
-- Port 7777 is used to run gdbserver program that allows to debug the program remotely.


```Batch
FROM ubuntu:16.04

RUN apt-get update && \
apt-get install -y openssh-server cmake gcc \
build-essential vim python tcpdump telnet byacc \
flex iproute2 gdbserver less bison valgrind firefox

RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22 9999 7777
CMD ["/usr/sbin/sshd", "-D"]
```

## Locally

We build it: ` docker build -t ubuntu-gdb-ssh .`

We run it in powershell (admin) with command:

```powershell
set-variable -name DISPLAY -value 192.168.1.102:0.0
docker run -d -p 3022:22 -p 7777:7777 -p 9999:9999 -h dev --privileged --security-opt seccomp:unconfined --name ubuntu-gdb-ssh-container ubuntu-gdb-ssh
 ```
 
## From docker hub

Pull image: `docker pull robgrzel/ubuntu-gdb-ssh`

Then Run


# Remote connection via ssh:

We may ssh to it with display: `ssh -X -p 3022 root@127.0.0.1`


## Test gdbserver

```bash
cd /tmp
echo "void main(){}" >> mytest.c
gcc mytest.c -o mytest.o
gdbserver 127.0.0.1:7777 mytest.o &
```

## Notes

### Check if docker has opened ports:

```powershell
docker ps -a
```

### Check if tcp works
```bash
telnet localhost 7777 
```

### Kill gdbserver process to release port

```bash
ps -ef
kill -KILL "one or more pid"
```
