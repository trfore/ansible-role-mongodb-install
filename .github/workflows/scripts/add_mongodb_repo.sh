#!/usr/bin/env bash
#
# Depends: curl, gpg, lsb_release
# Description: Add MongoDB repositories and update APT index
# Note: This script is simple with few checks and designed to work on github
# runners.

VERSION=(4.4 5.0 6.0 7.0 8.0) # default MongoDB versions

if [ "$(id -u)" -ne 0 ]; then
    echo 'Error: script not running as root'
    exit 1
fi

# add GPG keys
for i in "${VERSION[@]}"; do
    curl -fsSL https://pgp.mongodb.com/server-${i}.asc |
        gpg --yes -o /usr/share/keyrings/mongodb-server-${i}.gpg --dearmor
done

# add source repos
for i in "${VERSION[@]}"; do
    echo "deb [ arch=amd64 signed-by=/usr/share/keyrings/mongodb-server-${i}.gpg ] https://repo.mongodb.org/apt/ubuntu $(lsb_release -cs)/mongodb-org/${i} multiverse" |
        tee /etc/apt/sources.list.d/mongodb-org-${i}.list >/dev/null
done

# update sources.list.d repos
apt-get update -o Dir::Etc::sourcelist="/etc/apt/sources.list.d/"

exit 0
