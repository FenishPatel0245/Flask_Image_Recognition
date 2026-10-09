"""Additional tests for supported image colour modes."""

from io import BytesIO

import numpy as np
import pytest
from PIL import Image

from model import preprocess_img


@pytest.mark.parametrize(
    ("mode", "colour"),
    [
        ("RGB", (128, 128, 128)),
        ("L", 128),
        ("RGBA", (128, 128, 128, 255)),
    ],
    ids=["rgb", "grayscale", "rgba"],
)
def test_preprocess_supported_image_modes(mode, colour):
    """Valid images should produce three normalized colour channels."""
    with BytesIO() as upload:
        image = Image.new(mode, (32, 48), colour)
        image.save(upload, format="PNG")
        upload.seek(0)

        processed = preprocess_img(upload)

    assert processed.shape == (1, 224, 224, 3)
    np.testing.assert_allclose(processed, 128 / 255, rtol=1e-6)
