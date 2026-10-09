# Hand Digit Image Recognition

This Flask web application predicts the digit shown in an uploaded hand-sign image. It uses a saved Keras deep learning model.

![Python](https://img.shields.io/badge/python-8338ec)
![Keras](https://img.shields.io/badge/keras-219ebc)
![Numpy](https://img.shields.io/badge/numpy-ffafcc)
![Pillow](https://img.shields.io/badge/pillow-00bbf9)
![Flask](https://img.shields.io/badge/flask-f72585)
![Bootstrap](https://img.shields.io/badge/bootstrap-57cc99)

## Project Source

This repository is a fork of the original project by Sachin-crypto.

- Original project: https://github.com/Sachin-crypto/Flask_Image_Recognition
- Assignment fork: https://github.com/FenishPatel0245/Flask_Image_Recognition

The original application, saved model, and existing tests were retained. Assignment improvements include clearer error handling, support for grayscale and RGBA images, additional tests, pre-commit checks, and GitHub Actions.

## Original Demonstration

https://user-images.githubusercontent.com/72191416/201943098-c8f5fd8b-ec7d-4e5d-883d-8b69109b946f.mp4

## Requirements

- Windows with Python 3.10 (64-bit)
- Git
- A browser

The local environment was tested with Python 3.10.11. GitHub Actions uses Python 3.10 on Ubuntu.

The application uses Flask, TensorFlow, Keras, NumPy, and Pillow. Bootstrap provides the user interface styling.

## Get Started

Clone this fork and open the project folder:

```powershell
git clone https://github.com/FenishPatel0245/Flask_Image_Recognition.git
cd Flask_Image_Recognition
```

Create a virtual environment:

```powershell
py -3.10 -m venv .venv
```

Install the runtime and development dependencies:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pip check
```

`requirements-dev.txt` includes `requirements.txt`, Pylint, and pre-commit.

Werkzeug is pinned to version 2.2.3 for compatibility with Flask 2.2.1. Python 3.10 is used with the project's TensorFlow 2.10 dependency.

The commands use the virtual environment's Python directly, so activating the environment is optional.

## Run the Application

Run this command from the project folder:

```powershell
.\.venv\Scripts\python.exe app.py
```

Open http://127.0.0.1:9000 in a browser.

Keep the terminal running while using the application. Use another terminal for quality checks.

The application must run from the project folder so it can find `digit_model.h5`. It starts in debug mode for local development.

## Try an Image

1. Open the application in your browser.
2. Choose a hand-sign image from the `test_images` folder.
3. Check the image preview and filename.
4. Click Submit.
5. View the predicted digit.

Missing files, empty filenames, and unreadable images display:

```text
File cannot be processed.
```

Valid images are converted to RGB, resized to 224 × 224 pixels, and normalized before prediction.

## Main Components

| File or folder | Purpose |
|---|---|
| `app.py` | Creates the Flask application and handles the home and prediction routes. |
| `model.py` | Loads the saved model, preprocesses images, and returns the predicted digit. |
| `digit_model.h5` | Stores the trained Keras model. |
| `templates/index.html` | Contains the image upload form. |
| `templates/layout.html` | Provides the shared page layout and links to CSS and JavaScript. |
| `templates/result.html` | Displays the predicted digit or an error message. |
| `static/css/custom.css` | Provides custom page styling. |
| `static/js/image_upload.js` | Displays the selected image preview and filename. |
| `test_images` | Contains sample images for testing. |
| `requirements.txt` | Lists the runtime dependencies and pytest. |
| `requirements-dev.txt` | Includes the runtime requirements and development tools. |

## Run Pylint

```powershell
.\.venv\Scripts\python.exe -m pylint --rcfile=.pylintrc app.py model.py
```

The `.pylintrc` configuration targets Python 3.10, uses a maximum line length of 100, and sets a minimum score of 10. It excludes `.venv` and `__pycache__` from directory discovery.

The verified application code received a Pylint score of 10.00/10.

## Run Automated Tests

```powershell
.\.venv\Scripts\python.exe -m pytest -q --tb=short
```

The verified suite contains 26 passing test cases: 17 inherited cases and 9 additional cases.

The additional tests cover:

- Home-page loading.
- Valid upload processing and prediction display.
- Empty files, corrupted images, and text-file uploads.
- Empty filenames.
- RGB, grayscale, and RGBA image preprocessing.

The valid-upload route test mocks the predictor to check route behavior independently of model accuracy.

## Install and Run Pre-commit

Install the Git hooks after setting up the environment:

```powershell
.\.venv\Scripts\python.exe -m pre_commit install
```

Run all hooks manually:

```powershell
.\.venv\Scripts\python.exe -m pre_commit run --all-files
```

The hooks check:

- Trailing whitespace.
- File endings.
- YAML syntax.
- Python syntax.
- Merge-conflict markers.

Some hooks automatically fix formatting. If files are modified, review the changes and run the checks again before staging and committing.

## Continuous Integration

The workflow is stored in `.github/workflows/ci.yml`.

GitHub Actions runs on:

- Pushes to `main`.
- Pull requests targeting `main`.
- Manual workflow runs.

The workflow checks out the repository, sets up Python 3.10, installs dependencies, checks dependency compatibility, and runs Pylint and pytest.

The pytest step also runs after a Pylint failure when dependency installation succeeded.

Workflow results are available at:

https://github.com/FenishPatel0245/Flask_Image_Recognition/actions
