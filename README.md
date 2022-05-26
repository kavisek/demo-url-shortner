# url-shortner

### environment prerequisites

create an `./app/.env` file in the root directory of the repo.

```bash
ENV_NAME="Development"
BASE_URL="http://127.0.0.1:8000"
DB_URL="sqlite:///./shortener.db"
```

### Endpoints

- / (GET) : Returns a Hello, World! string
- /url (POST) : Shows the created url_key with additional info, including a secret_key
- /{url_key} (GET) : Forwards to your target URL
- /admin/{secret_key} (GET): Shows administrative info about your shortened URL
- /admin/{secret_key} (GET) : Shows administrative info about your shortened URL
- /admin/{secret_key} (DELETE) : Deletes your shortened URL



### URL Body Request

```json
{
  "target_url": "https://realpython.com",
  "is_active": true,
  "clicks": 0,
  "url": "JNPGB",
  "admin_url": "MIZJZYVA"
}
```

the above turns into the following...

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/url' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "target_url": "https://realpython.com",
  "is_active": true,
  "clicks": 0,
  "url": "JNPGB",
  "admin_url": "MIZJZYVA"
}'
```

### references

- https://realpython.com/build-a-python-url-shortener-with-fastapi/
