<!-- PROJECT LOGO -->

<div align="center" id="readme-top">
  <a href="https://github.com/bkctrl/watstreet-backend-onboarding">
    <br /><br />
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/flask/flask-original.svg" alt="Logo" width="120" height="120" style="border-radius: 50%;">
  </a>

<h3 align="center">Travel Wishlist API</h3>

<p align="center"><b>Wat Street Backend Onboarding</b></p>

  <p align="center">
    Flask REST API for travel wishlists.
<br /><br />

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
</div> 

## Getting Started
To set up the project locally and get a local copy up and running:

### Installation & Setup

1. Clone the repository: <br />

   ```bash
   git clone https://github.com/bkctrl/watstreet-backend-onboarding
   ```
2. Create & activate a Python virtual environment: <br />

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install the dependencies in the virtual environment: <br />

   ```bash
   pip install -r requirements.txt
   ```
4. Establish a database connection: <br />

   ```bash
   python3 create_db.py
   ```
5. Run the API on a local server: <br />

   ```bash
   python3 api.py
   ```
   The API should be running on `http://127.0.0.1:5000`!



## API Endpoints
  ### GET /
  This is the root endpoint.

  <img width="1538" alt="Screenshot 2025-01-22 at 7 38 40 AM" src="https://github.com/user-attachments/assets/7a50a288-0399-44d3-84c1-22283d542159" />

  ### POST /api/wishlist
  Given a JSON format:
  ```
  placeFields = {
    'id': fields.Integer,
    'name': fields.String,
    'attractions': fields.String,
    'best_time_to_visit': fields.String,
    'visited': fields.Boolean,
  }
  ```
 we POST a placeField into our database.
  
  Example placeFields (1):

  <img width="1538" alt="Screenshot 2025-01-22 at 7 39 06 AM" src="https://github.com/user-attachments/assets/cecc3f3c-2c9f-46db-9ddf-c68068609d09" />

  Example placeFields (2):

  <img width="1537" alt="Screenshot 2025-01-22 at 7 39 22 AM" src="https://github.com/user-attachments/assets/c09febd2-6163-4151-a0c9-50ded398faa9" />

  Example placeFields (3):

  <img width="1538" alt="Screenshot 2025-01-22 at 7 39 33 AM" src="https://github.com/user-attachments/assets/e66b8460-b400-4376-936f-5521690645b5" />

  <br />
  
  <img width="1532" alt="Screenshot 2025-01-22 at 7 39 55 AM" src="https://github.com/user-attachments/assets/32fb2f68-aff1-4438-848d-ed67236ff16d" />
  <img width="1542" alt="Screenshot 2025-01-22 at 7 40 08 AM" src="https://github.com/user-attachments/assets/69c34c72-b225-4417-b83f-ead8797f27d8" />
  <img width="1538" alt="Screenshot 2025-01-22 at 7 40 25 AM" src="https://github.com/user-attachments/assets/855ae9a8-fa01-414c-b720-09f67ab8e7bb" />
  <img width="1540" alt="Screenshot 2025-01-22 at 7 40 50 AM" src="https://github.com/user-attachments/assets/265bdfce-2524-4d22-a5c8-f4fd9d0980c0" />
  <img width="1539" alt="Screenshot 2025-01-22 at 7 41 41 AM" src="https://github.com/user-attachments/assets/3ae4b92d-0799-48c4-8d5d-b54a9e61f95d" />

