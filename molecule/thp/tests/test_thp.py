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
        ("enable-transparent-hugepages", False),
    ],
)
def test_service_enabled_and_running(host, name, running):
    service = host.service(name)
    assert service.is_enabled
    # some services are one-shot
    if running:
        assert service.is_running


def test_huge_page_support_enabled(host):
    assert host.file("/proc/meminfo").contains("^AnonHugePages:[ ]*[0-9]* kB$")


def test_pymongo_is_installed(host):
    py_ver = host.file("/opt/mongodb_venv/lib/").listdir()[0]
    pymongo_path = "/opt/mongodb_venv/lib/" + py_ver + "/site-packages/pymongo"
    assert host.file(pymongo_path).is_directory


def test_service_tcp_port(host):
    socket = host.socket("tcp://127.0.0.1:27018")
    assert socket.is_listening
