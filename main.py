import argparse
import html
import sqlite3
from pathlib import Path

def quote_identifier(value):
    return '"' + value.replace('"', '""') + '"'

def inspect_schema(connection):
    objects = connection.execute(
        "SELECT type, name, sql FROM sqlite_master WHERE type IN ('table','view') AND name NOT LIKE 'sqlite_%' ORDER BY type, name"
    ).fetchall()
    result = []
    for kind, name, sql in objects:
        identifier = quote_identifier(name)
        columns = connection.execute(f"PRAGMA table_info({identifier})").fetchall()
        indexes = connection.execute(f"PRAGMA index_list({identifier})").fetchall() if kind == "table" else []
        foreign_keys = connection.execute(f"PRAGMA foreign_key_list({identifier})").fetchall() if kind == "table" else []
        result.append({"type":kind,"name":name,"sql":sql or "","columns":columns,"indexes":indexes,"foreign_keys":foreign_keys})
    return result

def render_html(objects, database_name):
    parts = ["<!doctype html><html lang='en'><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>",
             "<title>SQLite Schema Documentation</title><style>body{font:16px/1.5 system-ui;max-width:1100px;margin:40px auto;padding:0 20px;background:#0b1220;color:#e2e8f0}h1,h2{color:#5eead4}section{background:#111c2e;padding:20px;margin:18px 0;border:1px solid #334155;border-radius:12px}table{border-collapse:collapse;width:100%}td,th{text-align:left;padding:8px;border-bottom:1px solid #334155}code,pre{color:#a7f3d0;overflow-wrap:anywhere}small{color:#94a3b8}</style>",
             f"<h1>SQLite Schema Documentation</h1><p><small>Database: {html.escape(database_name)} · {len(objects)} objects</small></p>"]
    for item in objects:
        parts.append(f"<section><h2>{html.escape(item['type'].title())}: {html.escape(item['name'])}</h2>")
        parts.append("<h3>Columns</h3><table><tr><th>Name</th><th>Type</th><th>Not null</th><th>Default</th><th>Primary key</th></tr>")
        for col in item["columns"]:
            parts.append("<tr>" + "".join(f"<td>{html.escape(str(value if value is not None else ''))}</td>" for value in (col[1],col[2],bool(col[3]),col[4],bool(col[5]))) + "</tr>")
        parts.append("</table>")
        if item["indexes"]:
            parts.append("<h3>Indexes</h3><ul>" + "".join(f"<li>{html.escape(str(index[1]))} ({'unique' if index[2] else 'non-unique'})</li>" for index in item["indexes"]) + "</ul>")
        if item["foreign_keys"]:
            parts.append("<h3>Foreign keys</h3><ul>" + "".join(f"<li>{html.escape(str(fk[3]))} → {html.escape(str(fk[2]))}.{html.escape(str(fk[4]))}</li>" for fk in item["foreign_keys"]) + "</ul>")
        if item["sql"]:
            parts.append(f"<details><summary>SQL definition</summary><pre>{html.escape(item['sql'])}</pre></details>")
        parts.append("</section>")
    parts.append("</html>")
    return "\n".join(parts)

def main():
    parser = argparse.ArgumentParser(description="Generate HTML documentation for a SQLite schema.")
    parser.add_argument("database", type=Path)
    parser.add_argument("--output", type=Path, default=Path("schema-report.html"))
    args = parser.parse_args()
    uri = args.database.resolve().as_uri() + "?mode=ro"
    with sqlite3.connect(uri, uri=True) as connection:
        objects = inspect_schema(connection)
    args.output.write_text(render_html(objects,args.database.name),encoding="utf-8")
    print(f"Wrote {args.output} ({len(objects)} tables/views).")

if __name__ == "__main__":
    main()
