This a repo to follow the FASTAPI [tutorial](https://fastapi-tutorial.readthedocs.io/en/latest/).


### Rerun - Docker compose
Most of the times you need to remove old volumes in order the compose to run successfully:

`docker-compose down --volumes`

### Pytest fixture
A pytest fixture is a function that provides a fixed baseline for tests, ensuring consistent and repeatable results by setting up services, state, or environments. Fixtures are requested by test functions through arguments and can be modular, reusable, and composable, making test writing easier and more organized.
Resource: [pytest web](https://docs.pytest.org/en/6.2.x/fixture.html)