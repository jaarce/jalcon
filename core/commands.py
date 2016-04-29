import subprocess


def createproject(project_name):
    """
    A simple method that runs a ManagementUtility.
    """
    app_clone_script = 'git clone https://github.com/famoraes/falcon-api.git %s' % project_name
    subprocess.call(app_clone_script.split(' '))
