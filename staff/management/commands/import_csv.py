import csv
from staff.models import StaffData  # Replace 'staff' with your app name
a=1
with open('D:/database_anime/cleaned_file_staff.txt', 'r') as file:
    reader = csv.DictReader(file)  # Read CSV file as a dictionary
    for row in reader:
        def clean_value(value):
            return value.strip() if value and value.strip() else None
        print(a+1)
        # Create and save the Staff object
        StaffData.objects.create(
            id=clean_value(row.get('StaffId')),
            name_full=clean_value(row.get('name_full')),
            name_native=clean_value(row.get('name_native')),
            name_alternative=clean_value(row.get('name_alternative')),
            language=clean_value(row.get('language')),
            description=clean_value(row.get('description')),
            image=clean_value(row.get('image')),  # Adjust the field as needed (for file paths or URLs)
            site_url=clean_value(row.get('site_url')),
            staff_media=clean_value(row.get('staff_media')),
        occupation=clean_value(row.get('Occupation')),
        )

