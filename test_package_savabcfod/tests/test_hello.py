from test_package_savabcfod import hw


def test_hw() -> None:
    assert hw() == "Hello World"


if __name__ == "__main__":
    test_hw()