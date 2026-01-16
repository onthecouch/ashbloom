import json
import sys

def validate_report(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)

        if not isinstance(data, list):
            print("Error: Root element must be a list")
            sys.exit(1)

        if len(data) == 0:
            print("Report is empty (valid)")
            return

        required_fields = {
            "title", "description", "deepLink", "filePath",
            "lineNumber", "confidence", "rationale", "context",
            "language", "category", "estimatedImpact"
        }

        valid_categories = {
            "n+1-query", "caching", "async-io",
            "loop-optimization", "data-structure", "other"
        }

        for i, item in enumerate(data):
            # Check required fields
            missing = required_fields - item.keys()
            if missing:
                print(f"Error: Item {i} missing fields: {missing}")
                sys.exit(1)

            # Validate types and values
            if not isinstance(item["confidence"], int) or not (1 <= item["confidence"] <= 3):
                print(f"Error: Item {i} has invalid confidence: {item.get('confidence')}")
                sys.exit(1)

            if item["category"] not in valid_categories:
                print(f"Error: Item {i} has invalid category: {item.get('category')}")
                sys.exit(1)

            if not isinstance(item["estimatedImpact"], int) or not (1 <= item["estimatedImpact"] <= 3):
                print(f"Error: Item {i} has invalid estimatedImpact: {item.get('estimatedImpact')}")
                sys.exit(1)

        print("Validation successful")

    except json.JSONDecodeError:
        print("Error: Invalid JSON format")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    validate_report("performance_report.json")
