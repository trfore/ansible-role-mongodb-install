import os
import pytest


def test_package_version(host):
    pkg = host.package("mongodb-org")
    assert pkg.is_installed
    assert pkg.version == os.environ["MOLECULE_MONGODB_VERSION"]


@pytest.mark.parametrize(
    "name,running",
    [
        ("mongod", True),
        ("dev-hugepages.mount", True),
        ("enable-transparent-hugepages", False),
    ],
)
def test_service_enabled_and_running(host, name, running):
    service = host.service(name)
    assert service.is_enabled
    # some services are one-shot
    if running:
        assert service.is_running


def test_service_tcp_port(host):
    socket = host.socket("tcp://127.0.0.1:27018")
    assert socket.is_listening
