#!/usr/bin/python3
"""unittest for models/engine/file_storage.py"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        models.storage._FileStroage__objects = {}
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        objs = models.storage.all()
        self.assertEqual(type(objs), dict)
        self.assertEqual(str, type(list(objs.keys())[0]))
        self.assertIsInstance(list(objs.values())[0], BaseModel)

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        bm = BaseModel()
        models.storage.new(bm)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        us = User()
        models.storage.new(us)
        self.assertIn("User." + us.id, models.storage.all().keys())
        self.assertIn(us, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)
            
    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        bm = BaseModel(name="ALX")
        us = User(name="Yidne")
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("User." + us.id, save_text)
        bm = BaseModel(name="Mission")
        us = BaseModel(name="Street")
        models.storage.new(bm)
        models.storage.save()
        with open("file.json", "r") as f:
            self.assertNotEqual(save_text, f.read())
           
    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(1)

    def test_reload(self):
        bm = BaseModel(id="98", name="Mission")
        with open("file.json", "w") as f:
            json.dump({"BaseModel.98": bm.to_dict()}, f)
        models.storage.reload()
        self.assertIn("BaseModel.98", models.storage.all().keys())
        us = User(id="98", name="Mission")
        with open("file.json", "w") as f:
            json.dump({"User.98": us.to_dict()}, f)
        models.storage.reload()
        self.assertIn("User.98", models.storage.all().keys())
        
    def test_reload_no_file(self):
        objs = models.storage.all()
        models.storage.reload()
        self.assertEqual(objs, models.storage.all())
        
    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(1)


if __name__ == "__main__":
    unittest.main()
