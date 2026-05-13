import os

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and a list of attendees.
    """
    # Check input types: template must be a string, attendees must be a list
    if not isinstance(template, str):
        print(f"Error: Invalid input type. Expected string for template, got {type(template).__name__}.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Invalid input type. Expected list of dictionaries for attendees.")
        return

    # Handle empty inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        processed_template = template
        
        # Placeholders to replace
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        for key in placeholders:
            # If a value is missing or None, replace it with "N/A"
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            
            target = "{" + key + "}"
            processed_template = processed_template.replace(target, str(value))
        
        # Generate output files named output_X.txt
        output_filename = f"output_{index}.txt"
        
        try:
            with open(output_filename, 'w', encoding='utf-8') as f:
                f.write(processed_template)
        except Exception as e:
            print(f"Error writing to {output_filename}: {e}")

# Example of how to run the program as shown in image_1e1757.png
if __name__ == "__main__":
    # Ensure template.txt exists for testing
    if os.path.exists('template.txt'):
        with open('template.txt', 'r') as file:
            template_content = file.read()
            
        attendees_list = [
            {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
            {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
            {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
        ]
        
        generate_invitations(template_content, attendees_list)
