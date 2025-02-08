---
title: Docker Debian Install
Modified: 2025-02-08T14:39:25-06:00
tags:
  - debian
  - docker
---
#### Add Docker's official GPG key:
```copy
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

#### Add the repository to Apt sources:
```copy
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

#### Install latest version
```copy
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
 
#### Verify that the installation is successful by running the `hello-world` image:

```copy
sudo docker run hello-world
```

 This command downloads a test image and runs it in a container. When the container runs, it prints a confirmation message and exits.


