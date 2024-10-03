import unittest
from unittest.mock import patch, MagicMock
from src.reconstruction.sfm import SfMReconstructor

class TestSfMReconstructor(unittest.TestCase):
    def setUp(self):
        self.config = MagicMock()
        self.sfm = SfMReconstructor(self.config)

    @patch('src.reconstruction.sfm.SomeSfMLibrary')
    def test_run(self, mock_sfm_lib):
        # Set up the mock
        mock_sfm_instance = mock_sfm_lib.return_value
        mock_sfm_instance.run_sfm.return_value = 'sfm_result_mock'

        # Call the method
        result = self.sfm.run('features_mock', 'matches_mock')

        # Assertions
        mock_sfm_instance.run_sfm.assert_called_once_with('features_mock', 'matches_mock')
        self.assertEqual(result, 'sfm_result_mock')

if __name__ == '__main__':
    unittest.main()