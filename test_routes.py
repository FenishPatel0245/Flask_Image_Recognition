"""Tests for the upload page and prediction route."""

from io import BytesIO
from unittest.mock import Mock

import pytest
from PIL import Image

import app as app_module


@pytest.fixture
def route_client(monkeypatch):
    """Enable testing so unexpected application errors are exposed."""
    monkeypatch.setitem(app_module.app.config, "TESTING", True)
    with app_module.app.test_client() as client:
        yield client


def test_home_page_loads(route_client):
    """The home page should display an HTML upload form."""
    response = route_client.get("/")

    assert response.status_code == 200
    assert response.mimetype == "text/html"
    assert b"<form" in response.data


def test_valid_upload_displays_prediction(route_client, monkeypatch):
    """A valid image should reach the predictor and display its result."""
    predictor = Mock(return_value=4)
    renderer = Mock(wraps=app_module.render_template)
    monkeypatch.setattr(app_module, "predict_result", predictor)
    monkeypatch.setattr(app_module, "render_template", renderer)

    with BytesIO() as upload:
        Image.new("RGB", (32, 48), "white").save(upload, format="PNG")
        upload.seek(0)
        response = route_client.post(
            "/prediction",
            data={"file": (upload, "valid.png")},
            content_type="multipart/form-data",
        )

    assert response.status_code == 200
    assert b"4" in response.data
    predictor.assert_called_once()
    assert predictor.call_args.args[0].shape == (1, 224, 224, 3)
    renderer.assert_called_once_with("result.html", predictions="4")


@pytest.mark.parametrize(
    ("contents", "filename"),
    [
        (b"", "empty.png"),
        (b"broken image data", "corrupted.png"),
        (b"This is a text document.", "notes.txt"),
    ],
    ids=["empty-file", "corrupted-image", "text-file"],
)
def test_invalid_upload_shows_error(
    route_client, monkeypatch, contents, filename
):
    """Invalid uploads should show an error without calling the predictor."""
    predictor = Mock()
    monkeypatch.setattr(app_module, "predict_result", predictor)

    response = route_client.post(
        "/prediction",
        data={"file": (BytesIO(contents), filename)},
        content_type="multipart/form-data",
    )

    assert response.status_code == 200
    assert b"File cannot be processed." in response.data
    predictor.assert_not_called()


def test_empty_filename_shows_error(route_client, monkeypatch):
    """Submitting an empty filename should not call the predictor."""
    predictor = Mock()
    monkeypatch.setattr(app_module, "predict_result", predictor)

    response = route_client.post(
        "/prediction",
        data={"file": (BytesIO(b""), "")},
        content_type="multipart/form-data",
    )

    assert response.status_code == 200
    assert b"File cannot be processed." in response.data
    predictor.assert_not_called()
