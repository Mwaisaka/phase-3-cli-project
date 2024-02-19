# Inventory Management CLI

The Inventory Management CLI application is designed to help businesses efficiently manage their inventory. It provides a user-friendly command-line interface (CLI) to monitor stock levels, track sales, and manage orders.

## Overview

- **Functionality:**
  - Add, update, and remove products from the inventory.
  - Update product information.
  - Basic search feature by name or category.
  - Check stock levels.
  - View the entire inventory.

- **Importance:**
  - Crucial for businesses selling products.
  - Prevents stockouts, overstocking, and related issues.

**Commands:**

### 1. Adding, Updating, and Removing Products
   - inventory add <product_name> <quantity> <price>
   - inventory update <product_id> <new_quantity> <new_price>
   - inventory remove <product_id>

### 2. Updating Product Information
    inventory update-info <product_id>

### 3. Basic Search Feature
    inventory search --name <product_name>
    
### 4. Checking Stock Levels
    inventory check-stock <product_id>
    inventory check-all-stock

### 5. Checking the Entire Inventory
    inventory show-all
    

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone git@github.com:Mwaisaka/phase-3-cli-project.git
   cd phase-3-cli-project

2. **Install dependencies:**
    npm install

3. **Run the application:**
    npm start