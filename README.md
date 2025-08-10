# Court-Data Fetcher & Mini Dashboard

This Flask web app allows users to search for Indian court case metadata using case type, number, and filing year.

## Example Usage

**Input:**
- Case Type: CIVIL
- Case Number: 123
- Filing Year: 2023

**Output:**
- Case Number: 123  
- Parties: John Doe vs State  
- Filing Date: 2023-06-14  
- Next Hearing Date: 2025-08-10  
- Download Latest Order: [Click here](https://delhihighcourt.nic.in/sample-judgment.pdf)

---

## Screenshots

### Search Form
![Search Form]  http://127.0.0.1:5000/
https://github.com/Deepak1804322/court-data-fetcher-dashboard/blob/main/screenshots/Screenshot%202025-08-10%20123932.png



### Search Result
![Search Result] https://github.com/Deepak1804322/court-data-fetcher-dashboard/blob/main/screenshots/Screenshot%202025-08-10%20123948.png

---

## Local Setup Instructions

1. Clone the Repository
```bash
git clone https://github.com/Deepak1804322/court-data-fetcher-dashboard
cd court-dashboard
```

2. Set up Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On macOS/Linux
```

3. Install Dependencies
```bash
pip install flask requests beautifulsoup4
```

4. Run the App
```bash
python app.py
```

Then open your browser and visit:  
`http://127.0.0.1:5000`

---

## Folder Structure
```
court_data_fetcher_dashboard/
│
├── app.py
├── scraper.py
├── templates/
│   ├── index.html
│   └── result.html
├── README.md
├── LICENSE
└── queries.db (auto-created after form use)
```

---

📄 **License**  
This project is licensed under the MIT License.

