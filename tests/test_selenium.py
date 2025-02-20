def test_connection(selenium):
    result = selenium.get('http://jupyterhub:8000')
    assert(selenium.title == 'JupyterHub')
