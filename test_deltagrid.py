# test_deltagrid.py
"""
Tests for DeltaGrid module.
"""

import unittest
from deltagrid import DeltaGrid

class TestDeltaGrid(unittest.TestCase):
    """Test cases for DeltaGrid class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DeltaGrid()
        self.assertIsInstance(instance, DeltaGrid)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DeltaGrid()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
