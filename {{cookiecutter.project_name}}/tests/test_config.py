from pathlib import Path

import pytest
from marshmallow import ValidationError

from {{cookiecutter.project_name}}.config import load_config


@pytest.mark.parametrize("content", [])
def test_load_config_exception(make_tmp_config_file, content):
    path = make_tmp_config_file(content)
    with pytest.raises(ValidationError):
        load_config(Path(path))


@pytest.mark.parametrize("content, expected", [])
def test_load_config(make_tmp_config_file, content, expected):
    path = make_tmp_config_file(content)
    assert load_config(Path(path)) == expected
