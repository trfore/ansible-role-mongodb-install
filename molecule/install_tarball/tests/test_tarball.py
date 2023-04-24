def test_service_running_and_enabled(host):
    service = host.service("mongod")
    assert service.is_running
    assert service.is_enabled


def test_service_tcp_port(host):
    socket = host.socket("tcp://127.0.0.1:27017")
    assert socket.is_listening
