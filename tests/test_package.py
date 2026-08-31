"""Static package checks, NOT evaluations of agent behavior or user comprehension."""

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "shared-understanding"


class SkillPackageTests(unittest.TestCase):
    def test_required_frontmatter(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        parts = text.split("---", 2)
        self.assertEqual(parts[0], "")
        fields = dict(
            line.split(":", 1) for line in parts[1].strip().splitlines()
        )
        self.assertEqual(fields["name"].strip(), SKILL.name)
        description = fields["description"].strip()
        self.assertTrue(20 <= len(description) <= 1024)
        self.assertIn("Present", description)

    def test_core_is_bounded_and_self_contained(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertLess(len(text.splitlines()), 250)
        self.assertLess(len(text.encode("utf-8")), 24000)
        self.assertNotRegex(text, r"\b(?:TODO|TBD|FIXME)\b")

    def test_optional_codex_metadata(self):
        text = (SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn('display_name: "认知外显 · Shared Understanding"', text)
        self.assertIn("$shared-understanding", text)
        self.assertIn("allow_implicit_invocation: true", text)

    def test_skill_local_links_stay_in_package_and_exist(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        links = re.findall(r"\]\(([^)]+)\)", text)
        self.assertIn("references/examples.md", links)
        for link in links:
            with self.subTest(link=link):
                self.assertNotIn("://", link)
                target = (SKILL / link).resolve()
                self.assertIn(SKILL.resolve(), target.parents)
                self.assertTrue(target.is_file())

    def test_evaluation_case_schema(self):
        data = json.loads((ROOT / "evals" / "cases.json").read_text(encoding="utf-8"))
        self.assertEqual(data["schema_version"], 1)
        self.assertEqual(data["skill"], SKILL.name)
        self.assertEqual(data["execution_status"], "not_run")
        cases = data["cases"]
        self.assertEqual(len(cases), 12)
        self.assertEqual(len({case["id"] for case in cases}), len(cases))
        for case in cases:
            with self.subTest(case=case["id"]):
                self.assertRegex(case["id"], r"^SU-\d{2}$")
                self.assertTrue(case["coverage"])
                self.assertIsInstance(case["context"], str)
                self.assertGreaterEqual(len(case["turns"]), 1)
                for turn in case["turns"]:
                    self.assertEqual(turn["role"], "user")
                    self.assertTrue(turn["content"])
                self.assertGreaterEqual(len(case["must"]), 2)
                self.assertGreaterEqual(len(case["must_not"]), 1)

    def test_evaluation_coverage(self):
        data = json.loads((ROOT / "evals" / "cases.json").read_text(encoding="utf-8"))
        actual = {tag for case in data["cases"] for tag in case["coverage"]}
        required = {
            "opening", "low-risk", "mid-task", "correction", "continuation",
            "handoff", "delegation", "audience", "trivial", "evidence",
            "reasoning-boundary", "authorization",
        }
        self.assertTrue(required <= actual, required - actual)
        self.assertTrue(any(len(case["turns"]) > 1 for case in data["cases"]))

    def test_handoff_docs_exist(self):
        for name in ("README.md", "evals/README.md", "skills/shared-understanding/references/examples.md"):
            with self.subTest(name=name):
                self.assertGreater(len((ROOT / name).read_text(encoding="utf-8")), 300)

    def test_skill_contains_no_machine_specific_paths(self):
        self.assertTrue((SKILL / "SKILL.md").is_file())
        for path in SKILL.rglob("*"):
            if path.is_file():
                with self.subTest(path=str(path)):
                    self.assertNotRegex(path.read_text(encoding="utf-8"), r"/Users/|/home/|[A-Z]:\\Users\\")


if __name__ == "__main__":
    unittest.main()
