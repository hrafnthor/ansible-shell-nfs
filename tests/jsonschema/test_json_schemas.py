#!/usr/bin/env python3

import json
import jsonschema
import pytest

def test_missing_required_field_host():
	schema = json.load(open('/mnt/Hel/dev/ansible/ansible-shell-nfs/mount-nfs-systemd/files/assertions/criteria/nfs_mount_criteria.json'))
	data = json.load(open('/mnt/Hel/dev/ansible/ansible-shell-nfs/mount-nfs-systemd/tests/jsonschema/data/missing_field_host.json'))

	with pytest.raises(Exception):
		jsonschema.validate(instance=data, schema=schema)

def test_missing_required_field_path():
	schema = json.load(open('/mnt/Hel/dev/ansible/ansible-shell-nfs/mount-nfs-systemd/files/assertions/criteria/nfs_mount_criteria.json'))
	data = json.load(open('/mnt/Hel/dev/ansible/ansible-shell-nfs/mount-nfs-systemd/tests/jsonschema/data/missing_field_path.json'))

	with pytest.raises(Exception):
		jsonschema.validate(instance=data, schema=schema)

def test_missing_required_field_destination():
	schema = json.load(open('/mnt/Hel/dev/ansible/ansible-shell-nfs/mount-nfs-systemd/files/assertions/criteria/nfs_mount_criteria.json'))
	data = json.load(open('/mnt/Hel/dev/ansible/ansible-shell-nfs/mount-nfs-systemd/tests/jsonschema/data/missing_field_destination.json'))

	with pytest.raises(Exception):
		jsonschema.validate(instance=data, schema=schema)

def test_empty_field_host():
	schema = json.load(open('/mnt/Hel/dev/ansible/ansible-shell-nfs/mount-nfs-systemd/files/assertions/criteria/nfs_mount_criteria.json'))
	data = json.load(open('/mnt/Hel/dev/ansible/ansible-shell-nfs/mount-nfs-systemd/tests/jsonschema/data/empty_field_host.json'))

	with pytest.raises(Exception):
		jsonschema.validate(instance=data, schema=schema)

def test_empty_field_path():
	schema = json.load(open('/mnt/Hel/dev/ansible/ansible-shell-nfs/mount-nfs-systemd/files/assertions/criteria/nfs_mount_criteria.json'))
	data = json.load(open('/mnt/Hel/dev/ansible/ansible-shell-nfs/mount-nfs-systemd/tests/jsonschema/data/empty_field_path.json'))

	with pytest.raises(Exception):
		jsonschema.validate(instance=data, schema=schema)

def test_empty_field_destination():
	schema = json.load(open('/mnt/Hel/dev/ansible/ansible-shell-nfs/mount-nfs-systemd/files/assertions/criteria/nfs_mount_criteria.json'))
	data = json.load(open('/mnt/Hel/dev/ansible/ansible-shell-nfs/mount-nfs-systemd/tests/jsonschema/data/empty_field_destination.json'))

	with pytest.raises(Exception):
		jsonschema.validate(instance=data, schema=schema)

def test_empty_field_after():
	schema = json.load(open('/mnt/Hel/dev/ansible/ansible-shell-nfs/mount-nfs-systemd/files/assertions/criteria/nfs_mount_criteria.json'))
	data = json.load(open('/mnt/Hel/dev/ansible/ansible-shell-nfs/mount-nfs-systemd/tests/jsonschema/data/empty_field_after.json'))

	with pytest.raises(Exception):
		jsonschema.validate(instance=data, schema=schema)

def test_empty_field_before():
	schema = json.load(open('/mnt/Hel/dev/ansible/ansible-shell-nfs/mount-nfs-systemd/files/assertions/criteria/nfs_mount_criteria.json'))
	data = json.load(open('/mnt/Hel/dev/ansible/ansible-shell-nfs/mount-nfs-systemd/tests/jsonschema/data/empty_field_before.json'))

	with pytest.raises(Exception):
		jsonschema.validate(instance=data, schema=schema)

def test_empty_field_requires():
	schema = json.load(open('/mnt/Hel/dev/ansible/ansible-shell-nfs/mount-nfs-systemd/files/assertions/criteria/nfs_mount_criteria.json'))
	data = json.load(open('/mnt/Hel/dev/ansible/ansible-shell-nfs/mount-nfs-systemd/tests/jsonschema/data/empty_field_requires.json'))

	with pytest.raises(Exception):
		jsonschema.validate(instance=data, schema=schema)

def test_non_array_field_after():
	schema = json.load(open('/mnt/Hel/dev/ansible/ansible-shell-nfs/mount-nfs-systemd/files/assertions/criteria/nfs_mount_criteria.json'))
	data = json.load(open('/mnt/Hel/dev/ansible/ansible-shell-nfs/mount-nfs-systemd/tests/jsonschema/data/non_array_field_after.json'))

	with pytest.raises(Exception):
		jsonschema.validate(instance=data, schema=schema)

def test_non_array_field_before():
	schema = json.load(open('/mnt/Hel/dev/ansible/ansible-shell-nfs/mount-nfs-systemd/files/assertions/criteria/nfs_mount_criteria.json'))
	data = json.load(open('/mnt/Hel/dev/ansible/ansible-shell-nfs/mount-nfs-systemd/tests/jsonschema/data/non_array_field_before.json'))

	with pytest.raises(Exception):
		jsonschema.validate(instance=data, schema=schema)

def test_non_array_field_requires():
	schema = json.load(open('/mnt/Hel/dev/ansible/ansible-shell-nfs/mount-nfs-systemd/files/assertions/criteria/nfs_mount_criteria.json'))
	data = json.load(open('/mnt/Hel/dev/ansible/ansible-shell-nfs/mount-nfs-systemd/tests/jsonschema/data/non_array_field_requires.json'))

	with pytest.raises(Exception):
		jsonschema.validate(instance=data, schema=schema)