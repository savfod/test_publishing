from test_package_savabcfod.hello import hw


def test_hw() -> None:
    assert hw() == "Hello World"