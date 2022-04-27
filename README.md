# README

Simple:
- [Simple Python without deps](Dockerfile)
- [Sleep to inspect with exec](Dockerfile.sleep) - show root dir and root user
- [Workdir + user](Dockerfile.workdir_user) - show normal user (install procps)

With deps:
- slim-bullseye - uses wheels
- slim-bullseye-compile - failure due to missing buildpack-deps
- bullseye-compile - build from source works but huge image
- multistage - FTW

To build a Docker image from one of the Dockerfiles, specify its path:

    docker build -t hellopy -f more_pip/Dockerfile.multistage .
