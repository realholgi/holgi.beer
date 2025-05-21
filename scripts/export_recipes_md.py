import sqlite3
from pathlib import Path
import argparse
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description="Export latest 20 recipes to Markdown from a Kleiner Brauhelfer 2 SQLite database.")
    parser.add_argument("database", help="Path to the SQLite database file")
    parser.add_argument("--table", default="Sud", help="Table name (default: Sud)")
    parser.add_argument("--columns", default="Sudnummer,Sudname,Braudatum,Kategorie", help="Comma-separated column names (default: Sudname,Braudatum,Kategorie)")
    parser.add_argument("--order-by", default="Braudatum", help="Column to order by (default: ID)")
    parser.add_argument("--output-dir", default="content", help="Output directory for the Markdown file")
    parser.add_argument("--output-file", default="sude.md", help="Name of the Markdown file")
    args = parser.parse_args()

    columns = [col.strip() for col in args.columns.split(",")]
    Path(args.output_dir).mkdir(exist_ok=True)

    conn = sqlite3.connect(args.database)
    c = conn.cursor()
    query = f"SELECT {', '.join(columns)} FROM {args.table} WHERE Status >= 2 ORDER BY {args.order_by} DESC LIMIT 20"
    c.execute(query)
    recipes = c.fetchall()
    conn.close()

    # Markdown header
    md = "---\n"
    md += "title: \"Sude\"\n"
    md += "---\n\n"
    md += "Meine letzten 20 Sude:\n\n"
    md += "| " + " | ".join(columns) + " |\n"
    md += "| " + " | ".join(["---"] * len(columns)) + " |\n"

    for row in recipes:
        row_out = []
        for col_name, value in zip(columns, row):
            if col_name.lower() == "braudatum" and value:
                # Try to parse and reformat date
                try:
                    # Adjust the format string if your date format is different!
                    dt = datetime.fromisoformat(value)
                    value = dt.strftime("%d.%m.%Y")
                except Exception:
                    # If parsing fails, leave as is
                    pass
            row_out.append(str(value) if value is not None else "")
        md += "| " + " | ".join(row_out) + " |\n"

    with open(f'{args.output_dir}/{args.output_file}', 'w', encoding='utf-8') as f:
        f.write(md)

if __name__ == "__main__":
    main()
