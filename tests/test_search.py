# Import unittest framework
import unittest

# Import search function
from src.knowledge_search import search_knowledge


# Create test class
class TestSearch(unittest.TestCase):

    # Test valid search
    def test_azure_search(self):

        knowledge = (
            "Azure is Microsoft's cloud platform"
        )

        result = search_knowledge(
            "azure",
            knowledge
        )

        self.assertEqual(
            result,
            "Azure is Microsoft's cloud platform"
        )


# Run tests
if __name__ == "__main__":
    unittest.main()
