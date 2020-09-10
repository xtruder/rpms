FROM fedora:latest

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=100

RUN useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

RUN dnf install -y nodejs && dnf clean all

RUN dnf install -y fedora-packager fedora-review copr-cli && \
    dnf clean all

RUN usermod -a -G mock $USERNAME