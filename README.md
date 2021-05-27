Docker/Heroku steps:
```
docker build -t airbnb .
docker tag airbnb registry.heroku.com/airbnb-ds-predict/web
docker tag airbnb registry.heroku.com/airbnb-ds-predict/worker
docker push registry.heroku.com/airbnb-ds-predict/web
docker push registry.heroku.com/airbnb-ds-predict/worker
heroku container:release web -a <Name of your heroku app>
heroku container:release worker -a <Name of your heroku app>
```

# Foobar

Foobar is a Python library for dealing with word pluralization.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)