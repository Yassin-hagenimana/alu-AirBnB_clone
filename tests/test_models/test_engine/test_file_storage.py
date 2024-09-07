#!/usr/bin/python3
"""Unittest for the FileStorage Class."""

import os
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models


class TestFileStorageInstantiation(unittest.TestCase):
    """Test instantiation of the FileStorage class."""

    def test_instantiation_no_args(self):
        self.assertIsInstance(FileStorage(), FileStorage)

    def test_instantiation_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_private_file_path(self):
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)

    def test_private_objects_dict(self):
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_storage_initialization(self):
        self.assertIsInstance(models.storage, FileStorage)


class TestFileStorageMethods(unittest.TestCase):
    """Test methods of the FileStorage class."""

    @classmethod
    def setUp(cls):
        if os.path.exists("file.json"):
            os.rename("file.json", "tmp")

    @classmethod
    def tearDown(cls):
        if os.path.exists("file.json"):
            os.remove("file.json")
        if os.path.exists("tmp"):
            os.rename("tmp", "file.json")
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertIsInstance(models.storage.all(), dict)

    def test_all_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        objects = [BaseModel()]
        for obj in objects:
            models.storage.new(obj)
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.assertIn(key, models.storage.all())

    def test_new_with_invalid_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        objects = [BaseModel()]
        for obj in objects:
            models.storage.new(obj)
        models.storage.save()
        with open("file.json", "r") as f:
            save_text = f.read()
            for obj in objects:
                self.assertIn(f"{obj.__class__.__name__}.{obj.id}", save_text)

    def test_save_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        objects = [BaseModel()]
        for obj in objects:
            models.storage.new(obj)
        models.storage.save()
        models.storage.reload()
        for obj in objects:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.assertIn(key, models.storage.all())

    def test_reload_no_file(self):
        self.assertRaises(FileNotFoundError, models.storage.reload)

    def test_reload_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
