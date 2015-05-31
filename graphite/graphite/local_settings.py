## Graphite local_settings.py
# Edit this file to customize the default Graphite webapp settings
#
# Additional customizations to Django settings can be added to this file as well

#####################################
# General Configuration #
#####################################
# Set this to a long, random unique string to use as a secret key for this
# install. This key is used for salting of hashes used in auth tokens,
# CRSF middleware, cookie storage, etc. This should be set identically among
# instances if used behind a load balancer.
SECRET_KEY = 'YOUR_SECRET_KEY'

# In Django 1.5+ set this to the list of hosts your graphite instances is
# accessible as. See:
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-ALLOWED_HOSTS
#ALLOWED_HOSTS = [ '*' ]

# Set your local timezone (Django's default is America/Chicago)
# If your graphs appear to be offset by a couple hours then this probably
# needs to be explicitly set to your local timezone.
TIME_ZONE = 'UTC'

# Override this to provide documentation specific to your Graphite deployment
#DOCUMENTATION_URL = "http://graphite.readthedocs.org/"

# Logging
#LOG_RENDERING_PERFORMANCE = True
#LOG_CACHE_PERFORMANCE = True
#LOG_METRIC_ACCESS = True

# Enable full debug page display on exceptions (Internal Server Error pages)
#DEBUG = True

# If using RRD files and rrdcached, set to the address or socket of the daemon
#FLUSHRRDCACHED = 'unix:/var/run/rrdcached.sock'

# This lists the memcached servers that will be used by this webapp.
# If you have a cluster of webapps you should ensure all of them
# have the *exact* same value for this setting. That will maximize cache
# efficiency. Setting MEMCACHE_HOSTS to be empty will turn off use of
# memcached entirely.
#
# You should not use the loopback address (127.0.0.1) here if using clustering
# as every webapp in the cluster should use the exact same values to prevent
# unneeded cache misses. Set to [] to disable caching of images and fetched data
#MEMCACHE_HOSTS = ['10.10.10.10:11211', '10.10.10.11:11211', '10.10.10.12:11211']
#DEFAULT_CACHE_DURATION = 60 # Cache images and data for 1 minute


#####################################
# Filesystem Paths #
#####################################
# Change only GRAPHITE_ROOT if your install is merely shifted from /opt/graphite
# to somewhere else
#GRAPHITE_ROOT = '/opt/graphite'

# Most installs done outside of a separate tree such as /opt/graphite will only