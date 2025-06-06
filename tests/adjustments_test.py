from operations.adjustments.brightness_adjustment import BrightnessAdjustment
from core.image_data import ImageData
from operations.filters.box_blur_filter import BoxBlurFilter


def test_brightness():
    # Insert your image path here
    image_path = "/Users/ronlevin/PycharmProjects/Lightricks_HA/tests/imgs/mona_lisa.jpg"

    # Load image
    for factor in [0.1, 0.5, 1, 2, 3]:
        brightness_adj = BrightnessAdjustment(factor)
        img = ImageData.load(image_path)
        result = brightness_adj.apply(img)
        result.show()

    # # Configure box blur dimensions
    # width = 20   # e.g., change as needed
    # height = 40  # e.g., change as needed
    #
    # # Apply BoxBlurFilter
    # blur_filter = BoxBlurFilter(width=width, height=height)
    # result = blur_filter.apply(img)


def test_adj_w_blur_chain():
    # Insert your image path here
    image_path = "/Users/ronlevin/PycharmProjects/Lightricks_HA/tests/imgs/mona_lisa.jpg"

    # Configure box blur dimensions
    width = 25  # e.g., change as needed
    height = 25  # e.g., change as needed
    factor = 0.5

    # Load image
    img = ImageData.load(image_path)
    blur = BoxBlurFilter(width, height)
    chain = BrightnessAdjustment(factor, next_filter=blur)

    result = chain.apply(img)
    result.show()


if __name__ == "__main__":
    # unittest.main()
    # test_brightness()
    test_adj_w_blur_chain()
