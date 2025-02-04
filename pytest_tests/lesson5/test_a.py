class TestA1:
    def test_A11(self, fixture_class, fixture_package, fixture_module, fixture_func, fixture_session):
        print("test_A11")
        assert True

    def test_A12(self, fixture_class, fixture_package, fixture_module, fixture_func, fixture_session):
        print("test_A12")
        assert True


class TestA2:
    def test_A21(self, fixture_class, fixture_package, fixture_module, fixture_func, fixture_session):
        print("test_A21")
        assert True

    def test_A22(self, fixture_class, fixture_package, fixture_module, fixture_func, fixture_session):
        print("test_A22")
        assert True