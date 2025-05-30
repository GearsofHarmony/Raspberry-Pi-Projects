#!/bin/bash

cd ./files/

IMG_REPO=https://downloads.raspberrypi.com/raspios_lite_arm64/images/raspios_lite_arm64-2024-11-19/
IMG_NAME=2024-11-19-raspios-bookworm-arm64-lite.img

MOUNT_PATH=$(mktemp -p "$PWD" -d)
OFFSET="offset=$((1056768*512))"

for download in ${IMG_NAME}.xz ${IMG_NAME}.xz.sha256 ;do 
	if [ ! -f "${download}" ] ;then
		echo "Downloading ${download}"
		if ! curl -s -o ${download} ${IMG_REPO}${download} ;then
			exit 20
		fi
	fi
done

if ! echo "$(cat ${IMG_NAME}.xz.sha256)" | sha256sum --check ;then
	echo "sha256 failed"
	exit 30
fi

if [ -f ${IMG_NAME}.xz -a ! -f ${IMG_NAME} ] ;then
	echo "unpacking image"
	if ! unxz --keep ${IMG_NAME}.xz ;then
		echo "unpack image failed"
		exit 40
	fi
fi

if mount -o loop,${OFFSET} ./2024-11-19-raspios-bookworm-arm64-lite.img ${MOUNT_PATH} ;then
	if ! tar -czf 2024-11-19-raspios-bookworm-arm64-lite.tar.gz -C "${MOUNT_PATH}" . ;then
		echo "mount failed"
		exit 50
	fi
	umount ${MOUNT_PATH}
	rm -d ${MOUNT_PATH}
fi