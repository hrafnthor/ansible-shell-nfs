#!/usr/bin/env python3

import json
import jsonschema
import pytest
from pathlib import Path

base_path = Path(__file__).parent
schema = json.load(open(base_path / '../../files/assertions/criteria/nfs_mount_criteria.json'))

def test_missing_required_field_path():
	data = json.load(open(base_path / './data/missing_field_path.json'))

	with pytest.raises(Exception, match=r"'path' is a required property"):
		jsonschema.validate(instance=data, schema=schema)

def test_missing_required_mount_field_host():
	data = json.load(open(base_path / './data/missing_mount_field_host.json'))

	with pytest.raises(Exception, match=r"'host' is a required property"):
		jsonschema.validate(instance=data, schema=schema)

def test_missing_required_mount_field_host_path():
	data = json.load(open(base_path / './data/missing_mount_field_host_path.json'))

	with pytest.raises(Exception, match=r"'host_path' is a required property"):
		jsonschema.validate(instance=data, schema=schema)

def test_missing_required_mount_field_mount_path():
	data = json.load(open(base_path / './data/missing_mount_field_mount_path.json'))

	with pytest.raises(Exception, match=r"'mount_path' is a required property"):
		jsonschema.validate(instance=data, schema=schema)

def test_empty_field_path():
	data = json.load(open(base_path / './data/empty_field_path.json'))

	with pytest.raises(Exception, match=r"'' should be non-empty"):
		jsonschema.validate(instance=data, schema=schema)

def test_empty_mount_field_host():
	data = json.load(open(base_path / './data/empty_mount_field_host.json'))

	with pytest.raises(Exception, match=r"'' should be non-empty"):
		jsonschema.validate(instance=data, schema=schema)

def test_empty_mount_field_host_path():
	data = json.load(open(base_path / './data/empty_mount_field_host_path.json'))

	with pytest.raises(Exception, match=r"'' should be non-empty"):
		jsonschema.validate(instance=data, schema=schema)

def test_empty_mount_field_mount_path():
	data = json.load(open(base_path / './data/empty_mount_field_mount_path.json'))

	with pytest.raises(Exception):
		jsonschema.validate(instance=data, schema=schema)

def test_empty_mount_field_after():
	data = json.load(open(base_path / './data/empty_mount_field_after.json'))

	with pytest.raises(Exception, match=r"\[\] should be non-empty"):
		jsonschema.validate(instance=data, schema=schema)

def test_empty_mount_field_before():
	data = json.load(open(base_path / './data/empty_mount_field_before.json'))

	with pytest.raises(Exception, match=r"\[\] should be non-empty"):
		jsonschema.validate(instance=data, schema=schema)

def test_empty_mount_field_requires():
	data = json.load(open(base_path / './data/empty_mount_field_requires.json'))

	with pytest.raises(Exception, match=r"\[\] should be non-empty"):
		jsonschema.validate(instance=data, schema=schema)

def test_non_array_mount_field_after():
	data = json.load(open(base_path / './data/non_array_field_after.json'))

	with pytest.raises(Exception, match=r"'' is not of type 'array'"):
		jsonschema.validate(instance=data, schema=schema)

def test_non_array_mount_field_before():
	data = json.load(open(base_path / './data/non_array_field_before.json'))

	with pytest.raises(Exception, match=r"'' is not of type 'array'"):
		jsonschema.validate(instance=data, schema=schema)

def test_non_array_mount_field_requires():
	data = json.load(open(base_path / './data/non_array_field_requires.json'))

	with pytest.raises(Exception, match=r"'' is not of type 'array'"):
		jsonschema.validate(instance=data, schema=schema)

def test_known_enum_value_started_mount_field_state():
	data = json.load(open(base_path / './data/started_enum_value_field_state.json'))

	jsonschema.validate(instance=data, schema=schema)

def test_known_enum_value_stopped_state():
	data = json.load(open(base_path / './data/stopped_enum_value_field_state.json'))

	jsonschema.validate(instance=data, schema=schema)

def test_known_enum_value_restarted_mount_field_state():
	data = json.load(open(base_path / './data/restarted_enum_value_field_state.json'))

	jsonschema.validate(instance=data, schema=schema)

def test_known_enum_value_reloaded_mount_field_state():
	data = json.load(open(base_path / './data/reloaded_enum_value_field_state.json'))

	jsonschema.validate(instance=data, schema=schema)

def test_unknown_enum_value_mount_field_state():
	data = json.load(open(base_path / './data/unknown_enum_value_field_state.json'))

	with pytest.raises(Exception, match=r"'unknown value' is not one of \['started', 'stopped', 'restarted', 'reloaded'\]"):
		jsonschema.validate(instance=data, schema=schema)

