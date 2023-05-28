# docker build -t <test_image> .
# docker run --name <tests_container> <tests_image> <pytest_parameters>

docker build -t test-docker:1.0 .
docker run --name teststartdocker test-docker:1.0 pytest --headless -n auto
