This a repo to follow the FASTAPI [tutorial](https://fastapi-tutorial.readthedocs.io/en/latest/).


### Rerun - Docker compose
Most of the times you need to remove old volumes in order the compose to run successfully:

`docker-compose down --volumes`

### Pytest fixture
A pytest fixture is a function that provides a fixed baseline for tests, ensuring consistent and repeatable results by setting up services, state, or environments. Fixtures are requested by test functions through arguments and can be modular, reusable, and composable, making test writing easier and more organized.
Resource: [pytest web](https://docs.pytest.org/en/6.2.x/fixture.html)

## CRUD Routes
CRUD stands for Create, Read, Update, and Delete, which are the four basic operations you can perform on resources in an API.

 - create -> this operation allows users to add new resources (POST)
 - read -> this operation allows users to retrieve existing resources (GET)
 - update -> this operation modifies an existing resource (in total or partially) (PUT (full update), PATH (partial update))
 - delete -> this operation removes a specified resource (DELETE)

 For example:

 | Operation | HTTP Method | Route | Description |
 |---------- |------------ |------ |------------ |
 | Create | POST | `/items` | Adds a new item to the collection |
 | Read | GET | `/items` | Retrieves all items |
 | Read | GET | `/items/{id}` | Retrieves a specific item by ID |
 | Update | PUT | `/items/{id}` | Updates the entire item with the given ID |
 | Update | PATCH | `/items/{id}`| Partially updates the item with the given ID |
 | Delete | DELETE | `/items/{id}`| Deletes the item with the given ID |

### Implementation Considerations

 - RESTful Design: CRUD operations lend themselves naturally to REST principles. Each operation corresponds to standard HTTP methods, making the API intuitive and easy to follow.
 - Resource Identification: Each resource (like an item, user, etc.) should have a unique identifier (usually an ID) that is used in the routes, especially for Read, Update, and Delete operations.
 - Status Codes: Appropriate HTTP status codes should be returned to indicate the success or failure of each operation (e.g., 201 for successful creation, 404 for resource not found, etc.).
