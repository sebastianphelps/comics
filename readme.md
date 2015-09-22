Test Deployment
===============
Using upstart and uwsgi emporer

    apt-get install python-pip
    apt-get install nginx
    pip install uwsgi

    cd /opt
    git clone https://github.com/sebastianphelps/comics.git

    mkdir -p /etc/uwsgi/vassals
    ln -s /opt/comics/conf/uwsgi/test.ini /etc/uwsgi/vassals/comics.ini
    mkdir -p /opt/var/log
    mkdir -p /opt/var/run
    cp /opt/comics/conf/upstart/test.conf /etc/init/uwsgi.conf

    start uwsgi

    cd /etc/nginx/conf.d
    ln -s /opt/comics/conf/nginx/test.conf comics.conf