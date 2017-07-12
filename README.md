# JupyterHub Http authenticator

Verify username and password by checking against a http account server.

## Installation

```
pip install jupyterhub_http_authenticator
```

You can then enable it in `jupyterhub_config.py`:

```
c.JupyterHub.authenticator_class = 'jupyterhub_http_authenticator.HttpAuthenticator'
```

## Configuratian
