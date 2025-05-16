import os
import pytest


def test_package_version(host):
    pkg = host.package("mongodb-org")
    assert pkg.is_installed
    assert pkg.version == os.environ["MOLECULE_MONGODB_VERSION"]


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
