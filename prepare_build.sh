#!/bin/bash
SCRIPT=`realpath $0`
SCRIPTPATH=`dirname $SCRIPT`
SCRIPTPATH_FOLDER=$(basename $SCRIPTPATH)

echo "PREBUILD_IMAGES"
GROUP_ID=$(id -g)
GROUP_NAME=$(id -gn)
USER_ID=$(id -u)
USER_NAME=$(id -un)

rm -rf .env
touch .env

if [ $? -gt 0 ]; then
	echo "UNABLE TO SET DOCKER-COMPOSE ENVIRONMENT FILE"
	exit 1
fi

echo "WORKDIR=$SCRIPTPATH" >> .env
echo "GROUP_ID=$GROUP_ID" >> .env
echo "GROUP_NAME=$GROUP_NAME" >> .env
echo "USER_ID=$USER_ID" >> .env
echo "USER_NAME=$USER_NAME" >> .env
echo "BUILD_FOLDER=$SCRIPTPATH_FOLDER" >> .env

## prebuild OS builder images, not to rebuild them on every push
## OS builder images should be built using separate repo,
## ideally enm-docker every day build


export IMAGE_REPOSITORY=armdocker.rnd.ericsson.se/proj_oss_releases/eric-enm-native-builders-imlib2
export IMAGE_TAG=1.0.1-1
export CONTEXT=builder


echo "IMAGE_REPOSITORY=$IMAGE_REPOSITORY" >> .env
echo "IMAGE_TAG=$IMAGE_TAG" >> .env


## maven version aligned
# MAVEN_VERSION=3.5.3
# wget --output-document=builder/apache-maven.tar.gz https://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz


prebuild_docker_images(){

    local IMAGE_ARTIFACT=$1
    local FULL_IMAGE_PATH="$IMAGE_REPOSITORY/$IMAGE_ARTIFACT:$IMAGE_TAG"
    
    echo "Preparing image for $FULL_IMAGE_PATH"
    docker pull $FULL_IMAGE_PATH
    local pull_result=$?
    echo "PULL RESULT $?"
    ## if image is not found, or unable to pull the image, build it locally
    if [ $pull_result -gt 0 ]; then
        echo "Unable to find image $FULL_IMAGE_PATH in registry, building and trying to push it to registry"
        docker build --force-rm -t "$FULL_IMAGE_PATH" --file "$CONTEXT/Dockerfile_$IMAGE_ARTIFACT" "$CONTEXT"
        docker push "$FULL_IMAGE_PATH"
    fi
    return 0
}
prebuild_docker_images rhel8
exit 0