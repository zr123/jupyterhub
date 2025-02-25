import os

# Auth - allow all linux system users
c.Authenticator.allow_all = True

# Basic Networking
c.JupyterHub.hub_ip = '0.0.0.0'
c.JupyterHub.hub_connect_ip = os.environ['HUB_CONNECT_IP']
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

# DockerSpawner Config
c.DockerSpawner.allowed_images = {
    'scipy': 'jupyter/scipy-notebook:latest',
    'tensorflow-jupyterhub': 'tensorflow-jupyterhub:latest',
}
c.DockerSpawner.network_name = os.environ['NETWORK_NAME']
c.DockerSpawner.remove = True

# directory volume bindings
c.DockerSpawner.notebook_dir = '/home'
c.DockerSpawner.volumes = {
    '/home/{username}': {'bind': '/home/{username}', 'mode': 'rw'},
    os.environ['DATA_DIRECTORY']: {'bind': '/home/data', 'mode': 'rw'},
}
