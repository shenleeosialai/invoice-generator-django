# Invoice Generator (Django)

A modern **Invoice Generator Web App** built with **Django**, featuring a clean, responsive invoice UI, PDF export, and admin-managed invoice data. The project is designed to be simple, extensible, and production-ready.

---

## ✨ Features

*  Create and manage invoices via Django Admin
*  Client billing details (Bill To) editable from Admin
*  Invoice amount tracking and paid/unpaid status
*  Download invoices as PDFs (html2canvas + jsPDF)
*  Modern, responsive invoice design
*  Invoice list and detail views
*  Unique invoice numbers
*  Company logo support (via static files)

---

##  Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, Vanilla JavaScript
* **Database:** SQLite (default, can be swapped)
* **PDF Generation:** html2canvas, jsPDF
* **Styling:** Custom CSS (no Tailwind)

---

##  Project Structure

```
invoice/
├── invoicegen/
│   ├── migrations/
│   ├── static/
│   │   └── invoicegen/
│   │       ├── css/
│   │       │   └── invoice.css
│   │       └── images/
│   │           └── logo.png
│   ├── templates/
│   │   └── invoicegen/
│   │       ├── base.html
│   │       ├── invoice_list.html
│   │       └── invoice_detail.html
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── invoice/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md
```

---

## 🚀 Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/invoice-generator.git
cd invoice-generator
```

### 2️⃣ Create & activate virtual environment

```bash
python -m venv env
source env/bin/activate  # Linux / macOS
env\Scripts\activate     # Windows
```

### 3️⃣ Install dependencies

```bash
pip install django
```

### 4️⃣ Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create admin user

```bash
python manage.py createsuperuser
```

### 6️⃣ Start the server

```bash
python manage.py runserver
```

Visit:

* Admin: `http://127.0.0.1:8000/admin/`
* App: `http://127.0.0.1:8000/`

---

##  Invoice Model Overview

Key fields:

* `invoice_number` (unique)
* `client_name`, `client_address`, `client_city`, `client_country`
* `amount`
* `paid`
* `created_at`

All client billing information is editable from Django Admin and rendered dynamically in the invoice template.

---

##  PDF Export

Invoices can be exported to PDF directly from the browser using:

* `html2canvas`
* `jsPDF`

The generated PDF preserves the invoice layout and logo.

---

##  Planned Improvements (Next Milestones)

### 1️⃣ Authentication & Authorization

Planned enhancements:

* User authentication (login / logout)
* Restrict invoice access per user
* Each user manages their own invoices
* Admin vs regular user roles
* Optional email-based login

Suggested tools:

* Django built-in `auth`
* `LoginRequiredMixin`
* Custom user model (optional)

---

### 2️⃣ Invoice Line Items (Database-backed)

* Add `InvoiceItem` model
* Persist items instead of relying only on JavaScript
* Server-side total calculation

---

### 3️⃣ Server-side PDF Generation

* Use **WeasyPrint** or **ReportLab**
* Generate PDFs without relying on browser JS
* Enable automated emailing of invoices

---

### 4️⃣ Business & UX Improvements

* Lock invoices once marked as PAID
* Company profile management
* Multiple companies / multi-tenant support
* Invoice status history
* Invoice numbering rules

---

##  Status

 **Active Development** – Core features complete, authentication and persistence planned next.

---

## Contributing

Contributions, issues, and feature requests are welcome.

---

##  License

This project is open-source and available under the **MIT License**.

---

## 🙌 Author

**Shenlee osialai**
Django Developer | Backend Engineer

---

> If you’re reviewing this project: authentication and multi-user support are the next major improvements 
