# Flask Login with Telegram Login for Websites

Demo application which uses flask, flask-login, flask-sqlalchemy and Telegram Login for Websites.

## Installation

Use the package manager [pipenv](https://pipenv.pypa.io/en/latest/) to install application.

```bash
$ pipenv install
```

## Usage

Set environment variables like this.

```bash
$ pipenv shell
$ export FLASK_APP=project
$ export FLASK_ENV=development
$ export BOT_TOKEN=...
$ export BOT_USERNAME=...
```

Otherwise variables `BOT_TOKEN` and `BOT_USERNAME` could be set in config file `project\config.py`.

Create database.

```bash
$ flask db init
$ flask db migrate -m "Initial commit"
$ flask db upgrade
```

Run application.

```bash
$ flask run
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)