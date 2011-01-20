from paver.easy import *

import sphinxtools

options(
    sphinx=Bunch(
        # Sphinx configuration file, which is passed to searchd and
        # indexer in the tasks. Mandatory.
        config='sphinx.conf',

        # Sphinx configuration file template, which can be used to
        # build the Sphinx configuration file in `config` option. Mandatory.
        config_template='sphinx.conf.tpl',

        # Searchd process ID filename. Mandatory.
        pid_file='searchd.pid',

        # All options in here can be accessed in the configuration
        # template with standard ``str.format`` syntax. You can put
        # whatever options you need in here, for example your database
        # settings.
        database=Bunch(
            type='mysql',
            host='localhost',
            port='',
            user='root',
            password='very_secret',
            name='blog'
        ),
        host='127.0.0.1',
        port=9312,
        index_path='data',
        log_path='log',
    )
)