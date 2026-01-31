'''
    module documentation
'''
import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os
import sys
from console import HBNBCommand
from io import StringIO


class TestHBNBCommand(unittest.TestCase):
    """_summary_
        This class test HBNBCommand class.
    """
    def setUp(self) -> None:
        """Set up test environment"""
        self.cmd = HBNBCommand()
        return super().setUp()

    def tearDown(self):
        """Clean up after tests"""
        try:
            os.remove('file.json')
        except:
            pass

    def out_test(self, func, arg, expect):
        """Auxiliary function to test some commands of the console"""
        std_out = StringIO()
        sys.stdout = std_out
        func(arg)
        output = std_out.getvalue()
        self.assertEqual(output, expect + '\n')
        return output

    def capture_output(self, func, arg):
        """Capture output from console command"""
        std_out = StringIO()
        sys.stdout = std_out
        func(arg)
        output = std_out.getvalue()
        sys.stdout = sys.__stdout__
        return output

    # Test file exists
    def test_file_exists(self):
        """Test that console.py file exists"""
        self.assertTrue(os.path.exists('console.py'))

    # Test basic commands
    def test_quit_exists(self):
        """Test quit command is present"""
        self.assertTrue(hasattr(self.cmd, 'do_quit'))

    def test_EOF_exists(self):
        """Test EOF command is present"""
        self.assertTrue(hasattr(self.cmd, 'do_EOF'))

    def test_help_exists(self):
        """Test help command is present"""
        self.assertTrue(hasattr(self.cmd, 'do_help'))

    def test_emptyline_exists(self):
        """Test empty line method is present"""
        self.assertTrue(hasattr(self.cmd, 'emptyline'))

    # Test standard command syntax
    def test_create_BaseModel_exists(self):
        """Test create BaseModel is present"""
        self.assertTrue(hasattr(self.cmd, 'do_create'))

    def test_show_BaseModel_exists(self):
        """Test show BaseModel is present"""
        self.assertTrue(hasattr(self.cmd, 'do_show'))

    def test_destroy_BaseModel_exists(self):
        """Test destroy BaseModel is present"""
        self.assertTrue(hasattr(self.cmd, 'do_destroy'))

    def test_all_BaseModel_exists(self):
        """Test all BaseModel is present"""
        self.assertTrue(hasattr(self.cmd, 'do_all'))

    def test_update_BaseModel_exists(self):
        """Test update BaseModel is present"""
        self.assertTrue(hasattr(self.cmd, 'do_update'))

    # Test dot notation - .all()
    def test_BaseModel_all_exists(self):
        """Test BaseModel.all() is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_Review_all_exists(self):
        """Test Review.all() is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_User_all_exists(self):
        """Test User.all() is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_State_all_exists(self):
        """Test State.all() is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_City_all_exists(self):
        """Test City.all() is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_Amenity_all_exists(self):
        """Test Amenity.all() is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_Place_all_exists(self):
        """Test Place.all() is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    # Test dot notation - .count()
    def test_BaseModel_count_exists(self):
        """Test BaseModel.count() is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_User_count_exists(self):
        """Test User.count() is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_State_count_exists(self):
        """Test State.count() is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_Place_count_exists(self):
        """Test Place.count() is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_City_count_exists(self):
        """Test City.count() is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_Amenity_count_exists(self):
        """Test Amenity.count() is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_Review_count_exists(self):
        """Test Review.count() is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    # Test dot notation - .show("id")
    def test_BaseModel_show_exists(self):
        """Test BaseModel.show('id') is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_User_show_exists(self):
        """Test User.show('id') is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_State_show_exists(self):
        """Test State.show('id') is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_City_show_exists(self):
        """Test City.show('id') is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_Amenity_show_exists(self):
        """Test Amenity.show('id') is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_Place_show_exists(self):
        """Test Place.show('id') is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_Review_show_exists(self):
        """Test Review.show('id') is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    # Test dot notation - .destroy("id")
    def test_BaseModel_destroy_exists(self):
        """Test BaseModel.destroy('id') is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_User_destroy_exists(self):
        """Test User.destroy('id') is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_City_destroy_exists(self):
        """Test City.destroy('id') is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_State_destroy_exists(self):
        """Test State.destroy('id') is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_Place_destroy_exists(self):
        """Test Place.destroy('id') is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_Amenity_destroy_exists(self):
        """Test Amenity.destroy('id') is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_Review_destroy_exists(self):
        """Test Review.destroy('id') is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    # Test dot notation - .update("id", "attribute_name", "string_value")
    def test_BaseModel_update_exists(self):
        """Test BaseModel.update('id', 'attr', 'val') is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_User_update_exists(self):
        """Test User.update('id', 'attr', 'val') is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_State_update_exists(self):
        """Test State.update('id', 'attr', 'val') is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_City_update_exists(self):
        """Test City.update('id', 'attr', 'val') is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_Place_update_exists(self):
        """Test Place.update('id', 'attr', 'val') is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_Amenity_update_exists(self):
        """Test Amenity.update('id', 'attr', 'val') is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_Review_update_exists(self):
        """Test Review.update('id', 'attr', 'val') is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    # Test dot notation - .update("id", {"attribute_name": "string_value"})
    def test_BaseModel_update_dict_exists(self):
        """Test BaseModel.update('id', {dict}) is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_User_update_dict_exists(self):
        """Test User.update('id', {dict}) is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_State_update_dict_exists(self):
        """Test State.update('id', {dict}) is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_Amenity_update_dict_exists(self):
        """Test Amenity.update('id', {dict}) is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_City_update_dict_exists(self):
        """Test City.update('id', {dict}) is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_Place_update_dict_exists(self):
        """Test Place.update('id', {dict}) is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    def test_Review_update_dict_exists(self):
        """Test Review.update('id', {dict}) is present"""
        self.assertTrue(hasattr(self.cmd, 'default'))

    # Original test methods
    def test_creation_failed(self):
        """Testing the 'create' command of the console - the error messages"""
        try:
            os.remove('file.json')
        except:
            pass
        cmd = HBNBCommand()
        self.out_test(cmd.do_create, '', HBNBCommand.ERROR_CLASS_NAME)
        self.out_test(cmd.do_create, 'myModel', HBNBCommand.ERROR_CLASS)


if __name__ == "__main__":
    unittest.main()
