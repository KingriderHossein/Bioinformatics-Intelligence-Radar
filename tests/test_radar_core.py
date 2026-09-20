import json
import unittest
from pathlib import Path

from scripts.radar_core import (
    canonical_id, classify_against_state, deduplicate, event_fingerprint,
    peer_review_eligible, process, update_state, validate_item,
)

FIXTURE = Path(__file__).parent / "fixtures" / "items.json"

class RadarCoreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.items = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_durable_identity_and_fingerprint(self):
        item = self.items[0]
        self.assertEqual(canonical_id(item), "paper:10.1000/example.1")
        self.assertEqual(len(event_fingerprint(item)), 20)

    def test_peer_review_is_hard_gate(self):
        self.assertTrue(peer_review_eligible(self.items[0]))
        self.assertFalse(peer_review_eligible(self.items[1]))
        self.assertTrue(any("peer-review gate" in x for x in validate_item(self.items[1])))

    def test_within_run_deduplication(self):
        unique, suppressed = deduplicate([self.items[2], self.items[3]])
        self.assertEqual(len(unique), 1)
        self.assertEqual(len(suppressed), 1)

    def test_processing_excludes_preprint_and_scores(self):
        result = process(self.items)
        self.assertEqual(result["telemetry"]["excluded_ineligible_scholarly"], 1)
        self.assertEqual(len(result["items"]), 2)
        self.assertGreaterEqual(result["items"][0]["news_value"]["score"], result["items"][1]["news_value"]["score"])

    def test_same_fingerprint_is_suppressed_across_runs(self):
        first = process([self.items[0]])
        state = update_state(None, first["items"], {first["items"][0]["canonical_id"]})
        second = process([self.items[0]], state)
        self.assertEqual(second["items"], [])
        self.assertEqual(second["telemetry"]["cross_run_suppressed_no_change"], 1)

    def test_material_change_is_updated(self):
        first = process([self.items[2]])
        state = update_state(None, first["items"], {first["items"][0]["canonical_id"]})
        changed = dict(self.items[2], version="2.1.0", release_tag="v2.1.0")
        changed["identifiers"] = dict(self.items[2]["identifiers"], canonical_url="https://github.com/org/tool/releases/tag/v2.1.0")
        second = process([changed], state)
        self.assertEqual(second["items"][0]["cross_run_action"], "NEW")

if __name__ == "__main__":
    unittest.main()
