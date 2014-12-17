FROM ubuntu:trusty
MAINTAINER Tobias Schmid <toashd@gmail.com>

# Update the sources list
RUN apt-get update

# Install Python and basic Python tools
RUN apt-get install -y python python-dev python-distribute python-pip

# Install server tools
RUN apt-get install -y nginx supervisor

# Copy application resources
ADD ./app /var/www/peanut/app
ADD ./requirements.txt /var/www/peanut/requirements.txt

# Create directory for uwsgi log files
RUN mkdir /var/log/uwsgi

# Install app requirements
RUN pip install -r /var/www/peanut/requirements.txt

# Configure nginx and supervisor
ADD ./conf /var/www/peanut/conf
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /var/www/peanut/conf/peanut_nginx.conf /etc/nginx/sites-enabled/
RUN ln -s /var/www/peanut/conf/peanut_supervisor.conf /etc/supervisor/conf.d/

# Expose ports
EXPOSE 80

# Start server
CMD ["supervisord", "-n"]
