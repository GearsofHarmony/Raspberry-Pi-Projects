FROM scratch
ADD files/2024-11-19-raspios-bookworm-arm64-lite.tar.gz /

ENV USER=piusr

RUN sudo adduser ${USER} && \
    usermod -a -G adm,dialout,cdrom,sudo,audio,video,plugdev,games,users,input,netdev,gpio,i2c,spi ${USER} && \
    sudo su - ${USER}

USER ${USER}
WORKDIR /home/${USER}

CMD ["bash"]
