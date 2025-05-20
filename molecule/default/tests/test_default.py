import os
import pytest
import re
from pathlib import Path

mongodb_version = os.environ["MOLECULE_MONGODB_VERSION"]
mongodb_version_maj = re.search(r"\d+", mongodb_version).group()


def test_config_file(host):
    if mongodb_version_maj >= "7":
        filename = "default_mongo7+.conf"
    else:
        filename = "default_mongo6.conf"
    expected = Path(__file__).with_name(filename)
    assert (
        expected.read_text(encoding="utf-8")
        == host.file("/etc/mongod.conf").content_string
    )


def test_package_version(host):
    pkg = host.package("mongodb-org")
    assert pkg.is_installed
    assert pkg.version == mongodb_version


def test_service_running_and_enabled(host):
    service = host.service("mongod")
    assert service.is_running
    assert service.is_enabled


@pytest.mark.xfail(reason="github runners have huge pages enabled")
def test_huge_page_support_disabled(host):
    assert host.file("/proc/meminfo").contains("^AnonHugePages:[ ]*0 kB$")


def test_service_tcp_port(host):
    socket = host.socket("tcp://127.0.0.1:27017")
    assert socket.is_listening
