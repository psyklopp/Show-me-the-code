# 🐋 Docker for Dummies

I have used Docker but never bothered to go through the official documentation. After reading the following pages, I can definitely say that the concepts are much more clear!

## What is a container?
A container is a sandboxed process running on a host machine that is isolated from all other processes running on that host machine.

According to [Docker](https://docs.docker.com/get-started/workshop/), a container:

- Is a runnable instance of an image. You can create, start, stop, move, or delete a container using the Docker API or CLI.
- Can be run on local machines, virtual machines, or deployed to the cloud.
- Is portable (and can be run on any OS).
- Is isolated from other containers and runs its own software, binaries, configurations, etc.

## What is an image?

A running container uses an isolated filesystem. This isolated filesystem is provided by an image

The image must contain everything needed to run an application - all dependencies, configurations, scripts, binaries, etc. The image also contains other configurations for the container, such as environment variables, a default command to run, and other metadata.

## :one: Containerize an application
  
[Part 1: Containerize an application](https://docs.docker.com/get-started/workshop/02_our_app/)

## :two: Updating the application

[Part 2: Update the application](https://docs.docker.com/get-started/workshop/03_updating_app/)

## 3️⃣ Share the application

[Part 3: Share the application](https://docs.docker.com/get-started/workshop/04_sharing_app/)

## :four: Setup the DB to persist

[Part 4: Persist the DB](https://docs.docker.com/get-started/workshop/05_persisting_data/)

## :five: Share host's filesystem with container

[Part 5: Use bind mounts](https://docs.docker.com/get-started/workshop/06_bind_mounts/)

## :six: Using multiple containers

[Part 6: Multi-container apps](https://docs.docker.com/get-started/workshop/07_multi_container/)

## 7️⃣ Docker Compose

[Part 7: Use Docker Compose](https://docs.docker.com/get-started/workshop/08_using_compose/)

## :eight: Resources

<details><summary>Other links and pages</summary>
<br>
  
- [Play with Docker](https://training.play-with-docker.com/)
- [Image-building best practices](https://docs.docker.com/get-started/workshop/09_image_best/)
</details>

## Verdict ⤵️

Straightforward and beginner friendly - approved ☑️
