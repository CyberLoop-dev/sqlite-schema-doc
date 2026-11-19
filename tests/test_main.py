import sqlite3
import unittest
from main import inspect_schema, render_html

class SchemaDocTests(unittest.TestCase):
    def test_lists_columns_indexes_and_foreign_keys(self):
        db = sqlite3.connect(":memory:")
        db.execute("CREATE TABLE parent(id INTEGER PRIMARY KEY)")
        db.execute("CREATE TABLE child(id INTEGER PRIMARY KEY, parent_id INTEGER REFERENCES parent(id))")
        db.execute("CREATE INDEX child_parent_idx ON child(parent_id)")
        objects = inspect_schema(db)
        child = next(item for item in objects if item["name"] == "child")
        self.assertEqual(child["columns"][1][1], "parent_id")
        self.assertTrue(child["indexes"])
        self.assertTrue(child["foreign_keys"])
    def test_html_escapes_database_names(self):
        output = render_html([], "<unsafe>.db")
        self.assertIn("&lt;unsafe&gt;", output)

if __name__ == "__main__":
    unittest.main()
