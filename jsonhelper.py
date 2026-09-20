import os
import json

def create_zone_structure(zone_name):
    """Create a zone folder with all empty JSON files"""
    
    # Create zone directory
    zone_path = f'data/zones/{zone_name}'
    os.makedirs(zone_path, exist_ok=True)
    
    # Define all JSON files to create
    json_files = {
        'mobs.json': {},
        'loot_tables.json': {},
        'events.json': {},
        'unique_mobs.json': {}
    }
    
    # Create each JSON file
    for filename, content in json_files.items():
        filepath = os.path.join(zone_path, filename)
        with open(filepath, 'w') as f:
            json.dump(content, f, indent=4)
        print(f"Created: {filepath}")
    
    print(f"\nZone '{zone_name}' created successfully!")

def create_multiple_zones(zone_names):
    """Create multiple zones at once"""
    for zone_name in zone_names:
        create_zone_structure(zone_name)

# Usage:
if __name__ == "__main__":
    # Create single zone
    create_zone_structure('template')
    
    # Or create multiple zones
    # create_multiple_zones(['forest', 'cave', 'village', 'dungeon'])