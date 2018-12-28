from tempfile import NamedTemporaryFile

import pytest
import yaml


@pytest.fixture
def make_tmp_config_file():
    with NamedTemporaryFile(mode="w") as tmp:

        def _make_tmp_config_file(content):
            yaml.dump(content, tmp)
            return tmp.name

        yield _make_tmp_config_file
