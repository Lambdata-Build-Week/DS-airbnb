# AIRBNB RECOMMENDER - A tool that recommends listing price


![GitHub repo size](https://img.shields.io/github/repo-size/Build-Week-ft-airbnb-2/DS)
![GitHub contributors](https://img.shields.io/github/contributors/Build-Week-ft-airbnb-2/DS)
![GitHub license](https://img.shields.io/github/license/Build-Week-ft-airbnb-2/DS)
![GitHub forks](https://img.shields.io/github/forks/Build-Week-ft-airbnb-2/DS?style=social)
![Github stars](https://img.shields.io/github/stars/Build-Week-ft-airbnb-2/DS?style=social)
![Github follow](https://img.shields.io/github/followers/Build-Week-ft-airbnb-2?style=social)


AirBnB Price Recommender is an `<APP>` that allows an `<AirBnb host>` to quickly get a `<Best Listing Price>` with minimal effort.

[AirBnb Recommender Website](https://airbnb-ds-predict.herokuapp.com/)

[Product Vision Document](https://www.notion.so/Product-Vision-Document-a52320ed951a4682aed8bb12f77a1778)

This web app is built on Fast API. The app uses Machine Learning to generate a prediction.

## Duplicate the project
You can clone this project and try yourself.

Clone the repo
```
git clone https://github.com/Build-Week-ft-airbnb-2/DS.git

cd YOUR-REPO-NAME
```

You can use either pipenv using Pipfile 
```
pipenv install --dev
```

Activate the virtual environment
```
pipenv shell
```

Launch the app
```
uvicorn app.main:app --reload
```

Go to `localhost:8000` in your browser.

![image](https://user-images.githubusercontent.com/7278219/87965040-c18ba300-ca80-11ea-894f-d51a69d52f8a.png)

Or Docker to rebuild this project using Dockerfile 

### Docker/Heroku steps:
```
docker build -t airbnb .
docker tag airbnb registry.heroku.com/airbnb-ds-predict/web
docker tag airbnb registry.heroku.com/airbnb-ds-predict/worker
docker push registry.heroku.com/airbnb-ds-predict/web
docker push registry.heroku.com/airbnb-ds-predict/worker
heroku container:release web -a <Name of your heroku app>
heroku container:release worker -a <Name of your heroku app>
```



## Contributing to Airbnb Recommender
<!--- If your README is long or you have some specific process or steps you want contributors to follow, consider creating a separate CONTRIBUTING.md file--->
To contribute to Airbnb Recommender, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contributors

Thanks to the following people who have contributed to this project:

* [@Brody Osterbuhr](https://github.com/BOsterbuhr) :beers:
* [@Ryan Fikejs](https://github.com/RyanFikejs) :baby_bottle:
* [@Minh Nguyen](https://github.com/minh14496) :high_brightness:
* [@Jack Stanley](https://github.com/Jack4589) ⌨
* [@Dennis Smith](https://github.com/domoreburpees) 😙

## License
[MIT](https://choosealicense.com/licenses/mit/)
