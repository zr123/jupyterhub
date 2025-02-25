FROM tensorflow/tensorflow:tensorflow:2.14.0-gpu-jupyter

# install jupyterhub for compatability
RUN pip3 install jupyterhub

# overwrite / set some required env variables
ENV JUPYTER_PORT=8888
EXPOSE $JUPYTER_PORT
ENV JUPYTERHUB_SERVICE_URL=http://127.0.0.1:5555

# run jupyterhub
CMD ["jupyterhub-singleuser", "--allow-root"]
