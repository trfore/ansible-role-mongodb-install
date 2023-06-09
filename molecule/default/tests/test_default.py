import os


def test_package_version(host):
    pkg = host.package("mongodb-org")
    assert pkg.is_installed
    assert pkg.version == os.environ["MOLECULE_MONGODB_VERSION"]


def test_service_running_and_enabled(host):
    service = host.service("mongod")
    assert service.is_running
    assert service.is_enabled


def test_service_tcp_port(host):
    socket = host.socket("tcp://127.0.0.1:27017")
    assert socket.is_listening
