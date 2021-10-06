#!/bin/sh

#Colors
RED='\033[0;31m'
LIGTH_RED='\033[1;31m'
Black='\033[0;30m'
Blue='\033[0;34m'
Green='\033[0;32m'
Cyan='\033[0;36m'
Purple='\033[0;35m'
Brown='\033[0;33m'
Blue='\033[0;34m'
Green='\033[0;32m'
Cyan='\033[0;36m'
Purple='\033[0;35m'
Brown='\033[0;33m'
NC='\033[0m' # No Color

# Variables
app=""
sqlalchemy_url=""
build_img=false
run_img=false


# Help
print_usage() {
    echo "$package - attempt to capture frames"
    echo " "
    echo "$package [options] application [arguments]"
    echo " "
    echo "options:"
    echo "-h, --help                                show brief help"
    echo "-b, --build                               build docker image"
    echo "-r, --run                                 run docker image"
    echo "-a <NAME_APP>, --app <NAME_APP>           specify a name of run container (like as Tag)"
    echo "-s <URL>, --sql-alchemy <URL>             specify a url for Enviroment variable to excecute success"
}

# Read flags
while test $# -gt 0; do
    case "$1" in
        -h|--help)
            print_usage
            exit 0
            ;;
        -a|--app*)
            shift
            app=`echo $1 | sed -e 's/^[^=]*=//g'`
            shift
            ;;
        -s|--sql-alchemy*)
            shift
            if test $# -gt 0; then
                sqlalchemy_url=`echo $1 | sed -e 's/^[^=]*=//g'`
            else
                echo "No URL SQLALCHEMY are specified"
                exit 1
            fi
            shift
            ;;
        -b|--build)
            build_img=true
            shift
            ;;
        -r|--run)
            run_img=true
            shift
            ;;
        *)
            print_usage
            exit 1
            break
            ;;
    esac
done

if [[ ! -z "$app" ]]; then
    if [ $build_img = true ]; then
        docker build -t ${app} .
        sleep 1
        echo -e "${Green}Building Image '${app}' Success${NC}"
    fi
    if [ $run_img = true ]; then
        opts=""
        if [[ ! -z "${sqlalchemy_url}" ]]; then
            opts="--env SQLALCHEMY_DATABASE_URL=${sqlalchemy_url}"
        fi

        docker run -d -p 56733:80 ${opts} ${app}
    fi
else
    echo -e "${LIGTH_RED}\n-a, --app         Is required\n\n\n${NC}"
    print_usage
    exit 1
fi