# Bus Ticket Booking System - Tkinter GUI Project

## Overview

This is a desktop-based GUI application developed using Python's Tkinter library. It simulates a basic **Bus Ticket Booking System** with interactive components, allowing users to book tickets between pre-defined locations, view routes, learn about the services, and provide reviews.

---

## Features

### 🚌 Bus Information

* Displays the **bus number** (e.g., 90A)
* Routes available: Gandhipuram, Saibaba Colony, Thottipalayam, R.S. Puram, Ramnagar, Lakshmi Mills, Hopes College, Neelambur, Sitra-Airport

### 📅 Ticket Booking

* Select **From** and **To** destinations with search-enabled dropdowns
* Choose a **travel date** using a calendar picker
* Select number of tickets
* Calculates and displays **total fare** based on location pair

### ℹ️ About Page

* Displays features with images:

  * Safety
  * On-Time Performance
  * Comfortable Ride

### ⭐ Reviews

* User can rate their travel experience: Very Good, Good, Bad, Very Bad
* Feedback is acknowledged with a thank-you message

### ☰ Menu Options

* Bus Info
* About
* Reviews
* Exit

---

## Technologies Used

* Python 3.x
* Tkinter (GUI)
* Pillow (`PIL.Image`) for image processing
* `tkcalendar` for date selection

---

## Setup Instructions

1. **Clone the Repository or Copy Files**
2. Ensure you have Python 3.x installed
3. Install required packages:

```bash
pip install pillow tkcalendar
```

4. Update file paths in code:

   * Icons (e.g., `bus-stop.ico`)
   * Images (`safety.jpg`, `time.png`, `seat.png`)
5. Run the application:

```bash
python your_file_name.py
```

---

## Folder Structure Example

```
BusBooking/
├── bus_booking.py
├── bus-stop.ico
├── safety.jpg
├── time.png
├── seat.png
```

---

## Screenshots

> Add screenshots of the main window, booking screen, and review form for better understanding.

---

