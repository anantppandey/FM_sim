#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/anant/FM_sim/src/catvehicle"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/anant/FM_sim/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/anant/FM_sim/install/lib/python2.7/dist-packages:/home/anant/FM_sim/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/anant/FM_sim/build" \
    "/usr/bin/python2" \
    "/home/anant/FM_sim/src/catvehicle/setup.py" \
     \
    build --build-base "/home/anant/FM_sim/build/catvehicle" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/anant/FM_sim/install" --install-scripts="/home/anant/FM_sim/install/bin"
