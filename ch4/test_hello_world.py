

from  hello_world import hello

def test_hello_without_fixture():
    hello()
    path = "hello.txt"
    with open(path) as f:
        assert f.readline()  == "Hello World!\n"

def test_hello_with_fixture(monkeypatch,tmp_path):
    monkeypatch.chdir(tmp_path)

    hello()

    path = "hello.txt"
    with open(path) as f:
        assert f.readline()  == "Hello World!\n"

    print(tmp_path,path)