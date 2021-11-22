

```python
def analyze_spells_distribution(csv_path: Path, book_file_name: str):
    with open(csv_path, 'r', encoding='utf8') as spell_by_line_file:
        spell_by_line_csv = reader(spell_by_line_file, delimiter=',')
        # skip headers
        next(spell_by_line_csv)

        # lines = []
        # spells = []
        # for row in spell_by_line_csv:
        #     lines.append(row[0])
        #     spells.append(row[1])
        lines, spells = zip(*(
            (int(row[0]), row[1])
            for row in spell_by_line_csv
        ))
```
