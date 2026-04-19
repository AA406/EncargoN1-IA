import json
from pathlib import Path
import unittest

from src.rag_pipeline import HelpdeskRAGPipeline

class TestHelpdeskRAGPipeline(unittest.TestCase):
    def setUp(self) -> None:
        self.pipeline = HelpdeskRAGPipeline()

    def test_cases_from_json(self) -> None:
        path = Path(__file__).parent / "casos_prueba.json"
        cases = json.loads(path.read_text(encoding="utf-8"))

        for case in cases:
            result = self.pipeline.process_query(case["query"])

            if "expected_category" in case:
                self.assertEqual(result["category"], case["expected_category"])
            if "expected_confidence" in case:
                self.assertEqual(result["confidence"], case["expected_confidence"])
            if "expected_escalate" in case:
                self.assertEqual(result["escalate"], case["expected_escalate"])

if __name__ == "__main__":
    unittest.main()
