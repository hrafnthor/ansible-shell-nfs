# Ansible SystemD mount
A Ansible task specifically for mounting NFS via the shell module

Requirements
------------

This role requires two separate tools be installed.

First it requires the 'ansible.utils' collection be installed from Ansible-Galaxy via:

```shell
ansible-galaxy collection install ansible.utils
```

Secondly it requires the `jsonschema` Python package be installed via:

```shell
pip install jsonschema
```


Role Variables
--------------

```yaml
nfs_mount:
  path:			<string>	The path where unit files will be created
  packages:		<array>		Any packages needed for NFS support
  mounts:
  - host: 		<string>	The host who exposes the NFS
    host_path: 	<string>	The path on the NFS host for the NFS share
    mount_path: <string>	The local path where the NFS share should be mounted
    description: <string>	A human readable description for the mount
    requires: 	<array>		A list of services that are required
    before:		<array>		A list of services who this mount should start before
    after:		<array>		A list of services who this mount should start after
    wantedby: 	<string>	Defines how the unit is linked to a target or other units
    isv4: 		<bool>		Indicates if this is a v4 NFS
    state: 	<started/stopped/restarted/reloaded>
    enabled: 	<bool>		Indicates if the service should be enabled, causing it to persist between reboot.
```

### Example

The following definition will create a unit mount file at path `/storage/.config/system.d` which mounts a network NFS from host 192.168.1.237 to local path `/storage/nfs/nas/media`:

```yaml
nfs_mount:
  path: "/storage/.config/system.d"
  mounts:
  - host: "192.168.1.237"
    host_path: "/volume1/media"
    mount_path: "/storage/nfs/nas/media"
    description: "Mounts NAS media NFS"
    requires:
      - "network-online.service"
    before:
      - "kodi.service"
    after:
      - "network-online.service"
    wantedby: "multi-user.target"
    isv4: true
    state: "started"
    enabled: true
```