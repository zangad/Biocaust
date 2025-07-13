import os

# Folder with JSON fragments
PARTS_FOLDER = "json_parts"
OUTPUT_FILE = "data/minecraft/worldgen/noise_settings/overworld.json"

def merge_json_parts():
    parts = sorted(os.listdir(PARTS_FOLDER))
    full_json = ""

    for filename in parts:
        if filename.endswith(".json"):
            with open(os.path.join(PARTS_FOLDER, filename), "r", encoding="utf-8") as f:
                full_json += f.read().strip()
                
    # Wrap the file with curly braces to make it a JSON file.
    full_json = "{" + full_json + "}"
    
    # Optional: prettify indentation and check JSON validity
    try:
        import json
        json_obj = json.loads(full_json)
        with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
            json.dump(json_obj, out, indent=2)
        print(f"Merged JSON written to {OUTPUT_FILE}")
    except Exception as e:
        print("❌ Error combining parts into valid JSON:", e)

if __name__ == "__main__":
    merge_json_parts()
