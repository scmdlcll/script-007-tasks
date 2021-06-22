# coding=utf-8
import os
import shutil

import pytest

from server import FileService


class Test_change_dir:

    def test_incorrect_type1(self):
        """Передать None в качестве значения

        Ожидаемый результат: возбуждение исключения TypeError
        """
        assert False

    def test_incorrect_type2(self):
        """Передать значение типа int

        Ожидаемый результат: возбуждение исключения TypeError
        """
        assert False

    def test_dot_dir(self):
        """Передать . в качестве значения,

        Ожидаемый результат: текущая папка не должна измениться
        """
        assert False

    def test_incorrect_value2(self):
        """Передать .. в качестве значения

        Ожидаемый результат: возбуждение исключения ValueError
        """
        assert False

    def test_incorrect_value3(self):
        """Передать ../something в качестве значения

        Ожидаемый результат: возбуждение исключения ValueError
        """
        assert False

    def test_existing_dir_no_create(self):
        """Перейти в каталог, который уже существует и autocreate=False

        Ожидаемый результат: текущая папка имеет имя ExistingDirectory
        """
        assert False

    def test_existing_dir_create(self):
        """Перейти в каталог, который уже существует и autocreate=True

        Ожидаемый результат: текущая папка имеет имя ExistingDirectory
        """
        assert False

    def test_non_existing_dir_no_create(self):
        """Перейти в каталог, который не существует и autocreate=False

        Ожидаемый результат: текущая папка имеет имя отличное от NotExistingDirectory
        """
        assert False

    def test_non_existing_dir_create(self):
        """Перейти в каталог, который не существует и autocreate=True

        Ожидаемый результат: текущая папка имеет имя отличное от NotExistingDirectory
        """
        assert False
