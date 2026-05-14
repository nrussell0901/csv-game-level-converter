import csv
import json
import os

def level_converter():
    print("=== Game Level Data Converter ===")
    print("Converts CSV level designs to game-ready JSON formats.")

    # Auto-test mode for VS Code (no input required)
    test_mode = False
    if not test_mode:  # Change to True for auto-test in VS Code
        try:
            # Get input file
            input_file = input("Enter CSV file path: ").strip()
            if not os.path.exists(input_file):
                print("File not found")
                return

            output_file = os.path.splitext(input_file)[0] + '.json'
            conversion_type = input("Conversion type (basic/tilemap/entity): ").strip().lower()

        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return
    else:
        # AUTO-TEST MODE (for VS Code testing)
        print("Running in test mode...")
        input_file = "sample_level.csv"
        output_file = "test_output.json"
        conversion_type = "tilemap"

        # Create sample file if it doesn't exist
        if not os.path.exists(input_file):
            create_sample_csv(input_file)

    try:
        # Read CSV
        with open(input_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        if not rows:
            print("CSV file is empty")
            return

        print(f"Read {len(rows)} rows from {input_file}")

        # Conversion logic
        output_data = convert_data(rows, conversion_type)

        # Save output
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2)

        print(f"\n✅ Conversion complete!")
        print(f"Input: {input_file}")
        print(f"Output: {output_file}")
        print(f"Type: {conversion_type}")
        if conversion_type == "basic":
            print(f"Total objects converted: {len(output_data)}")
        else:
            print(f"Total objects converted: {len(output_data.get('tiles', output_data.get('entities', [])))}")

    except Exception as e:
        print(f"An error occurred: {e}")

def create_sample_csv(filename):
    """Creates a simple sample CSV file for testing."""
    print(f"Creating sample CSV: {filename}")
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['x', 'y', 'type', 'id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'x': '0', 'y': '0', 'type': 'wall', 'id': 'wall_1'})
        writer.writerow({'x': '1', 'y': '0', 'type': 'floor', 'id': 'floor_1'})
        writer.writerow({'x': '2', 'y': '1', 'type': 'enemy', 'id': 'enemy_1'})
        writer.writerow({'x': '3', 'y': '2', 'type': 'coin', 'id': 'coin_1'})
        writer.writerow({'x': '4', 'y': '2', 'type': 'exit', 'id': 'exit_1'})

def convert_data(rows, conversion_type):
    """Converts list of rows to specified JSON format."""
    if conversion_type == "basic":
        return rows
    elif conversion_type == "tilemap":
        tilemap = {'tiles': []}
        for row in rows:
            try:
                tilemap['tiles'].append({
                    'x': int(row.get('x', 0)),
                    'y': int(row.get('y', 0)),
                    'type': row.get('type', 'empty')
                })
            except ValueError:
                print(f"Warning: Skipping row with invalid x or y: {row}")
                continue
        return tilemap
    elif conversion_type == "entity":
        entities = {'entities': []}
        for row in rows:
            entity_data = {}
            for key, value in row.items():
                 entity_data[key] = value
            # Attempt to convert x and y to float
            if 'x' in entity_data:
                try:
                    entity_data['x'] = float(entity_data['x'])
                except ValueError:
                    pass
            if 'y' in entity_data:
                try:
                    entity_data['y'] = float(entity_data['y'])
                except ValueError:
                     pass
            entities['entities'].append(entity_data)
        return entities
    else:
        print(f"Error: Unknown conversion type '{conversion_type}'")
        return None

if __name__ == "__main__":
    level_converter()