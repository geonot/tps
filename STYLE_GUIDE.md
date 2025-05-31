# Tacoma Parking Services - Design and Style Guide

## 1. Logo

A simple, modern logo featuring the initials "TPS" and a stylized parking symbol or a subtle outline of Mount Rainier. Color: Primary Blue.

## 2. Color Palette

*   **Primary Blue:** `#005A9C` (Used for branding, primary buttons, active links)
*   **Secondary Teal:** `#40B0A6` (Used for secondary actions, highlights, call-to-action sections)
*   **Accent Orange:** `#F08C00` (Used for alerts, important notices, or tertiary calls to action)
*   **Neutral Dark Gray:** `#333333` (Used for body text, headings)
*   **Neutral Medium Gray:** `#767676` (Used for secondary text, borders)
*   **Neutral Light Gray:** `#F5F5F5` (Used for backgrounds, card backgrounds)
*   **White:** `#FFFFFF` (Used for text on dark backgrounds, content areas)
*   **Success Green:** `#28A745`
*   **Error Red:** `#DC3545`

## 3. Typography

*   **Headings Font:** "Montserrat", sans-serif (Modern, clean, and slightly geometric)
    *   Import via Google Fonts: `<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700&display=swap" rel="stylesheet">`
*   **Body Font:** "Open Sans", sans-serif (Highly legible for body text)
    *   Import via Google Fonts: `<link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">`

## 4. UI Elements

*   **Buttons:**
    *   Primary: Solid Primary Blue background, white text. Rounded corners.
    *   Secondary: Solid Secondary Teal background, white text. Rounded corners.
    *   Outline: Transparent background, Primary Blue border and text. Rounded corners.
*   **Forms:** Clean and simple input fields with clear labels. Use Neutral Medium Gray borders, focusing on Primary Blue.
*   **Cards:** Use Neutral Light Gray background with subtle shadows.

## 5. Wireframes (Textual Description)

### 5.1. Home Page

*   **Header:** Logo (left), Navigation (Home, About, Services, Parking, Contact, Login/User Account) (right).
*   **Hero Section:** Large background image (e.g., Tacoma cityscape or modern parking facility). Catchy headline (e.g., "Parking in Tacoma, Simplified."), brief introductory text, and a primary call-to-action button (e.g., "Find Parking" or "Purchase Permit").
*   **Services Overview:** Section with 2-3 cards highlighting key services (e.g., Daily Parking, Monthly Permits, QR Code Payments).
*   **How it Works:** Simple 3-4 step visual/text explanation of using the QR code payment system.
*   **Call to Action (Secondary):** Section encouraging users to create an account or explore monthly permits.
*   **Footer:** Copyright, links to Privacy Policy, Terms of Service, Contact.

### 5.2. About Page

*   **Header:** Consistent with Home Page.
*   **Main Content:**
    *   "Our Mission" section.
    *   "Who We Are" - Information about Tacoma Parking Services.
    *   Perhaps a "Why Choose Us?" section with key benefits.
*   **Footer:** Consistent with Home Page.

### 5.3. Services Page

*   **Header:** Consistent with Home Page.
*   **Main Content:**
    *   Detailed descriptions of each service offered:
        *   **Daily Parking:** How it works, benefits, link to find lots.
        *   **Monthly Permits:** Types of permits, pricing, benefits, link to purchase.
        *   **QR Code Payments:** Explanation of the system, how to use it.
        *   (Potentially other services like event parking, business accounts).
*   **Footer:** Consistent with Home Page.

### 5.4. Parking Page (Lot Finder / Purchase)

*   **Header:** Consistent with Home Page.
*   **Guest View / Initial View:**
    *   Search/Filter options (e.g., by location, availability - future).
    *   Map view (placeholder for future integration, initially a list).
    *   List of parking lots with brief details (name, address, daily rate, monthly rate if available).
    *   Each lot has a "Pay for Daily Parking" and "Inquire about Monthly Permit" button/link.
*   **Daily Parking Purchase Flow (Modal or New Page Section):**
    *   Lot Name/ID (pre-filled if coming from a specific lot).
    *   License Plate Number input.
    *   Duration (e.g., hours, full day).
    *   Price calculation.
    *   "Proceed to Payment" button (leads to PayPal).
*   **Monthly Permit Purchase Flow:**
    *   Information about available monthly permits for a selected lot.
    *   Application/purchase form.
*   **Footer:** Consistent with Home Page.

### 5.5. Contact Page

*   **Header:** Consistent with Home Page.
*   **Main Content:**
    *   Contact Form (Name, Email, Subject, Message).
    *   Contact Information (Address, Phone Number, Email Address).
    *   Map (embedded Google Map placeholder).
*   **Footer:** Consistent with Home Page.

### 5.6. User Account Pages (Post-Login)

*   **Dashboard:** Overview of recent activity, current permits.
*   **Profile Settings:** Update personal information, password.
*   **Payment History:** List of past transactions.
*   **Manage Permits:** View active permits, renew.
