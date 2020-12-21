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
