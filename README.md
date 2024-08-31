

# NixStays

**NixStays** is a web portal designed to simplify the search for hostels, paying guests (PGs), and flats for students, especially those around academic institutions. The platform allows users to explore accommodations, take virtual tours, and reserve properties, making it easier to find the right place to stay.

## Features

- **Property Listings:** Users can browse a curated list of properties near academic institutions. Each listing provides essential details, amenities, and images.
- **Virtual Tours:** Users can take virtual tours of properties to get a real feel of the place before making a decision.
- **Search & Filters:** Users can search properties based on location, amenities, and other tags like pet-friendly, wifi-enabled, food availability, etc.
- **User Accounts:** Users can create accounts to save favorite properties, view their reservations, and more.
- **Hostel Registration:** Hostel owners can register and submit their property listings. All listings are reviewed by admins before being published.
- **Consultation Form:** Users can fill out a consultation form to get personalized recommendations. The form includes fields for Name, Email, Mobile Number, Date & Time, Institute, and a custom message.
- **Admin Dashboard:** The platform leverages Django's customizable admin panel to manage property listings, user accounts, and more.

## Technology Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Django (Python)
- **Database:** SQLite (or any Django-supported database)
- **Hosting:** VPS on Ubuntu Focal with a domain configured via Cloudflare

## Installation

To run this project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/Tanishq84/NixStays.git
   cd NixStays
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Open your browser and navigate to `http://127.0.0.1:8000/` to see the app in action.

## Usage

- **Homepage:** Displays a list of properties and the consultation form.
- **Login/Signup:** Users need to log in to reserve properties.
- **Admin Panel:** Access via `/admin` to manage listings and users.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
