# pyez_test
Juniper PyEZ test script

## ssh config file
* https://www.juniper.net/documentation/en_US/junos-pyez/topics/task/program/junos-pyez-connection-methods.html
* Junos PyEZ automatically queries the default SSH configuration file at `~/.ssh/config`, if one exists.
* However, starting with Junos PyEZ Release 1.2, you can specify a different SSH configuration file when you create the device instance by including the `ssh_config` parameter in the Device argument list.

## ssh key
* https://github.com/Juniper/py-junos-eznc#notices
* As of release 2.0.0, Junos PyEZ requires ncclient version 0.5.2 or later.
* When using the `ssh_private_key_file` argument of the Device constructor on MacOS Mojave and higher, ensure that the SSH keys are in the RSA format, and not the newer OPENSSH format.
  * New key: `ssh-keygen -p -m PEM -f ~/.ssh/id_rsa`
  * Convert an existing OPENSSH key: `ssh-keygen -p -m PEM -f ~/.ssh/private_key`
  * Check if a given key is RSA or OPENSSH format: `head -n1 ~/.ssh/private_key`
    * RSA: `-----BEGIN RSA PRIVATE KEY-----`
    * OPENSSH: `-----BEGIN OPENSSH PRIVATE KEY-----`

## OUTPUT

```bash
$ python3 pyez_test.py
True
dcr1
{'re0': {'text': '18.2R3.4', 'object': junos.version_info(major=(18, 2), type=R, minor=3, build=4)}}
False
```

## nornir_pyez

hi ...
I tried to open pull request but I got permission denied, probably don't have permission to create a new branch.

PYEZ supports optional parameters for path to `ssh_key` and `ssh_config`, i tested it here: https://github.com/patrikh-dev/pyez_test

Below is update which should add support for these optional parameters also in `nornir_pyez`.  

pls have a look and if possible add it to your package, thanks

```bash
--- a/nornir_pyez/plugins/connections/__init__.py
+++ b/nornir_pyez/plugins/connections/__init__.py
@@ -27,6 +27,8 @@ class Pyez:
             "password": password,
             "port": port,
             "optional_args": {},
+            "ssh_config": extras["ssh_config"] if "ssh_config" in extras.keys() else None,
+            "ssh_private_key_file": extras["ssh_private_key_file"] if "ssh_private_key_file" in extras.keys() else None,
         }
```

## Custom SSH config file or path to ssh key

* definition inside `hosts.yaml`

```yaml
hostname:
    ...
    connection_options:
        pyez:
            extras:
                ssh_config: "path_to_ssh_config"
                ssh_private_key_file: "path_to_ssh_key"
```

* definition inside `groups.yaml`

```yaml
group_name:
    ...
    connection_options:
        pyez:
            extras:
                ssh_config: "path_to_ssh_config"
                ssh_private_key_file: "path_to_ssh_key"
```

* definition inside code
  * requires to have definition of connection_options/pyez/extras under host or group (depends which definition is used inside the code) otherwise `KeyError: 'pyez'` is generated

```yaml
host / group:
    connection_options:
        pyez:
            extras: {}
```

```python
# per host definition
nr.inventory.hosts['hostname'].connection_options['pyez'].extras['ssh_config'] = "path_to_ssh_config"
nr.inventory.hosts['hostname'].connection_options['pyez'].extras['ssh_private_key_file'] = "path_to_ssh_key"
# per group definition
nr.inventory.groups['group_name'].connection_options['pyez'].extras['ssh_config'] = "path_to_ssh_config"
nr.inventory.groups['group_name'].connection_options['pyez'].extras['ssh_private_key_file'] = "path_to_ssh_key"
```
