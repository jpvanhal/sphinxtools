"""This module contains Paver tasks for managing Sphinx Search server."""

import os
import time

from paver.easy import error, info, needs, options, path, sh, task


def is_process_running(pid):
    """Return True if a process with given process id is running."""
    # TODO: Windows version of this function
    try:
        # Sending signal 0 to a process will raise an OSError if the
        # process is not running, and do nothing otherwise.
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True


def is_sphinx_daemon_running():
    """Return True if Sphinx search daemon is running."""
    pid = get_sphinx_daemon_pid()
    return pid and is_process_running(pid)


def get_sphinx_daemon_pid():
    """Return Sphinx search daemon process id, or None if not found."""
    try:
        return int(path(options.sphinx.pid_file).text().strip())
    except (IOError, ValueError):
        return None


@task
@needs('sphinx_configure', 'sphinx_index', 'sphinx_daemon_restart')
def sphinx_bootstrap():
    """Configure Sphinx, index everything and start search daemon."""
    pass


@task
def sphinx_index():
    """Update all indices."""
    path(options.sphinx.index_path).makedirs()
    command = 'indexer --all --config %s' % options.sphinx.config
    if is_sphinx_daemon_running():
        command += ' --rotate'
    sh(command)


@task
def sphinx_daemon_start():
    """Start the search daemon."""
    path(options.sphinx.log_path).makedirs()
    if is_sphinx_daemon_running():
        error('Search daemon is already running.')
    else:
        sh('searchd --config %s' % options.sphinx.config)
        time.sleep(2)


@task
def sphinx_daemon_stop():
    """Stop the search daemon."""
    sh('searchd --stop --config %s' % options.sphinx.config)
    time.sleep(2)


@task
def sphinx_daemon_restart():
    """Restart the search daemon."""
    if is_sphinx_daemon_running():
        sphinx_daemon_stop()
    sphinx_daemon_start()


@task
def sphinx_daemon_status():
    """Check if the search daemon is running"""
    if is_sphinx_daemon_running():
        info('Search daemon is running.')
    else:
        info('Search daemon is stopped.')


@task
def sphinx_configure():
    """Builds the Sphinx configuration file.

    This task uses standard Python string formatting to transform the template
    file in ``options.sphinx.config_template`` into a Sphinx configuration
    file. The formatting operations uses the contents of
    ``options.sphinx.config`` as keyword arguments. Finally, the built Sphinx
    configuration file is written to the file in ``options.sphinx.config``.

    """
    template = path(options.sphinx.config_template).text()
    output = template.format(**options.sphinx)
    path(options.sphinx.config).write_text(output)
    info('Wrote Sphinx configuration to %s' %
         path(options.sphinx.config).relpath())
