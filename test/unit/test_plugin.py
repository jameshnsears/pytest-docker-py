def test_hello(testdir):
    testdir.makeconftest(
        """
        import pytest

        @pytest.fixture(params=[
            "Brianna",
            "Andreas",
            "Floris",
        ])
        def name(request):
            return request.param
    """
    )

    testdir.makepyfile(
        """
        import pytest
        from plugin import hello

        @pytest.mark.timeout(30)
        def test_hello_default(hello):
            assert hello() == "Hello World!"

        @pytest.mark.timeout(30)
        def test_hello_name(hello, name):
            assert hello(name) == "Hello {0}!".format(name)
    """
    )

    result = testdir.runpytest()
    result.assert_outcomes(passed=4)
