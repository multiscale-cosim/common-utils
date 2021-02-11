import unittest
import os
import logging
from pathlib import Path
# TODO: relative import instead of absolute import
from python.configuration_manager.configurations_manager import ConfigurationsManager
import shutil


class ConfigurationsManagerTest(unittest.TestCase):
    """Tests the behavior of ConfigurationsManager class."""
    @classmethod
    def setUpClass(cls) -> None:
        """set-up the common resources."""
        cls.configurations_manager = ConfigurationsManager()

    @classmethod
    def tearDownClass(cls) -> None:
        """clean up the common resources."""
        # TODO: clean up -- directories
        #   e.g shutil.rmtree(cls.configurations_manager.get_directory('output'))
        # to prevent the side effects such as memory leaks
        del cls.configurations_manager

    def test_make_directory(self):
        """Case: whether a directory is successfully created."""
        # make a test directory
        temp_dir = self.configurations_manager.make_directory('temp_dir')
        # test: whether the directory is successfully created
        self.assertTrue(os.path.isdir(temp_dir))
        shutil.rmtree(temp_dir)  # clean up

    def test_make_directory_location_correctness(self):
        """Case: whether the directory is created at the target location."""
        # make a test directory
        temp_dir = self.configurations_manager.make_directory('temp_dir_location_test')
        # test: whether the location is correct
        path = Path(self.configurations_manager.get_directory('temp_dir_location_test'))
        self.assertEqual(Path(self.configurations_manager.get_directory('output')), path.parent)
        shutil.rmtree(temp_dir)  # clean up

    def test_get_directory_exists(self, target_directory=None):
        """Case: the target_directory exists.
        It should return the path to that."""
        if target_directory is None:
            target_directory = 'output'  # default directory
        # test: whether the return path exists and is an directory.
        self.assertTrue(os.path.isdir(self.configurations_manager
                                      .get_directory(target_directory)))

    def test_get_directory_not_exists(self):
        """Case: the target_directory does not exist.
        It should raise an exception."""
        target_dir = 'not_exists'
        # test: it should raise an exception if directory does not exist
        with self.assertRaises(Exception) as context:
            self.configurations_manager.get_directory(target_dir)
        self.assertTrue('directory not found' in str(context.exception))

    def test_get_component_configuration_settings_exists(self):
        """Case: the target ``component configuration settings`` exists.
        It should return the configuration settings for that."""
        target_component_configuration_settings = 'log_configurations'
        # Test: it returns the configurations settings that exist for the target component
        self.assertIsNotNone(self.configurations_manager.
                             get_configuration_settings(target_component_configuration_settings))
        print(self.configurations_manager.
              get_configuration_settings(target_component_configuration_settings))

    def test_get_component_configuration_settings_data_type_correctness(self):
        """Case: the return data type for the existing target
         configuration settings is 'correct'."""
        target_component_configuration_settings = 'log_configurations'
        target_data_type = dict
        # Test: it returns the correct data type
        self.assertIsInstance(self.configurations_manager.
                              get_configuration_settings(target_component_configuration_settings),
                              target_data_type)

    def test_get_component_configuration_settings_not_exists(self):
        """Case: the target ``component configuration settings``
        does not exist. It should raise an exception."""
        target_component = 'not_exists'
        # Test: it should raise an 'LookupError' exception when the
        # target component configuration settings do not exist.
        with self.assertRaises(LookupError) as context:
            self.configurations_manager.get_configuration_settings(target_component)
        # Test: the captured exception is the one that is raised.
        self.assertTrue("configuration settings not found!" in str(context.exception))

    def test_load_log_configurations(self):
        """Case: the logger is 'properly' configured. It should return
        the instance of Logging.Logger class with user defined name and
         settings, and should emit the logs at the user specified levels."""
        test_logger_name = __name__
        with self.assertLogs(__name__, level='INFO') as context:
            logger = self.configurations_manager.load_log_configurations(test_logger_name)
            # test: whether the logger is created
            self.assertIsNotNone(logger)
            # test: whether the logger is an instance of class ``Logger``
            self.assertIsInstance(logger, logging.Logger)
            # test: whether the logger is created with user defined name
            self.assertEqual(logger.name, test_logger_name)
            # emit two test log messages
            logger.info("TEST INFO log")
            logger.error("TEST ERROR log")
        # test: whether all log messages are emitted successfully
        self.assertEqual(len(context.records), 2)
        # test: correctness of the log messages i.e. whether the captured log
        # messages are the ones that were emitted.
        self.assertEqual(context.records[0].getMessage(), "TEST INFO log")
        self.assertEqual(context.records[1].getMessage(), "TEST ERROR log")
        # test: correctness of the level of emitted log messages
        self.assertEqual(context.records[0].levelno, logging.INFO)
        self.assertEqual(context.records[1].levelno, logging.ERROR)


if __name__ == '__main__':
    unittest.main()
