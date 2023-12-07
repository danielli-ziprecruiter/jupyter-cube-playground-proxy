import setuptools
from glob import glob

setuptools.setup(
    name="jupyter-cube-proxy",
    version='1.0.1',
    url="https://github.com/yuvipanda/jupyter-sparkui-proxy",
    author="Yuvi Panda",
    license="BSD 3-Clause",
    packages=setuptools.find_packages(),
    install_requires=['jupyter-server-proxy>=1.0.1'],
    python_requires='>=3.5',
    classifiers=[
        'Framework :: Jupyter',
    ],
    data_files=[
        ('etc/jupyter/jupyter_notebook_config.d', ['jupyter_cube_proxy/etc/jupyter-cube-proxy-notebookserverextension.json']),
        ('etc/jupyter/jupyter_server_config.d', ['jupyter_cube_proxy/etc/jupyter-cube-proxy-jupyterserverextension.json']),
    ],
    include_package_data=True,
    zip_safe=False
)
