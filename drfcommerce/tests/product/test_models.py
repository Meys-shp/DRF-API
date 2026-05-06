from unittest import TestCase

import pytest

pytestmark= pytest.mark.django_db

class TestProductModel:
    def test_str_method(self, product_factory):
        # Arrange
        x = product_factory(name="test_Product")
        assert x.__str__() == "test_Product"



class TestBrandModel:
    def test_str_method(self, brand_factory):
        # Arrange
        x = brand_factory(name="test_Brand")
        assert x.__str__() == "test_Brand"


class TestCategoryModel:
    def test_str_method(self, category_factory):
        # Arrange
        x = category_factory(name="test_Category")
        assert x.__str__() == "test_Category"
