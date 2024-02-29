class TestA:
    def setup_method(self):
        print("connection to database")
        self.data = 10

    def teardown_method(self):
        print("close database")

    def test_1(self):
        print("test_1 run")
        assert self.data == 10

    def test_2(self):
        print("test_2 run")
        assert self.data == 10

def test_3(database):
    print("test_3 run")
    assert database == 10