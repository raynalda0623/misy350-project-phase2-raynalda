import time

def find_user(users, username, password):
    username = username.strip()
    password = password.strip()
    for u in users:
        if u.get("username") == username and u.get("password") == password:
            return u
    return None


def register_user(users, username, password, confirm):
    username = username.strip()
    password = password.strip()
    confirm = confirm.strip()

    if username == "" or password == "" or confirm == "":
        return None, "Please fill in all fields."
    if password != confirm:
        return None, "Passwords do not match."
    if len(password) < 4:
        return None, "Password must be at least 4 characters."
    if any(u.get("username") == username for u in users):
        return None, "That username is already taken."

    new_user = {"username": username, "password": password, "role": "Employee"}
    users.append(new_user)
    return new_user, "Account created! You can now log in as " + username + "."


def get_low_stock_items(inventory):
    return [item for item in inventory if item.get("stock", 0) < 5]


def get_total_inventory_value(inventory):
    return round(sum(item.get("price", 0) * item.get("stock", 0) for item in inventory), 2)


def add_item(inventory, name, price, stock, category):
    if not name or not str(name).strip():
        return None, "Please enter a product name."
    normalized_name = str(name).strip().lower()
    if any(item.get("name", "").strip().lower() == normalized_name for item in inventory):
        return None, "A product with that name already exists."
    if price <= 0:
        return None, "Price must be greater than 0."
    if stock < 0:
        return None, "Stock cannot be negative."

    next_id = max((item.get("item_id") or 0) for item in inventory) + 1 if inventory else 1
    new_item = {
        "item_id": next_id,
        "name": str(name).strip(),
        "price": round(float(price), 2),
        "stock": int(stock),
        "category": category or "Other",
        "flagged": False,
    }
    inventory.append(new_item)
    return new_item, "Product added successfully."


def update_item(inventory, item_id, updated_price, add_stock, updated_category):
    for item in inventory:
        if item.get("item_id") == item_id:
            if updated_price <= 0:
                return False, "Price must be greater than 0."
            if add_stock < 0:
                return False, "Added stock cannot be negative."
            item["price"] = round(float(updated_price), 2)
            item["stock"] = item.get("stock", 0) + int(add_stock)
            item["category"] = updated_category or item.get("category", "Other")
            return True, "Product updated successfully."
    return False, "Item not found."


def delete_item(inventory, item_id):
    for item in inventory:
        if item.get("item_id") == item_id:
            inventory.remove(item)
            return True, "Product removed successfully."
    return False, "Item not found."


def get_sales_by_employee(sales, username):
    return [sale for sale in sales if sale.get("logged_by") == username]


def place_sale(inventory, sales, item_id, quantity, username):
    if quantity <= 0:
        return None, "Quantity must be at least 1."
    for item in inventory:
        if item.get("item_id") == item_id:
            current_stock = item.get("stock", 0)
            if current_stock < quantity:
                return None, f"Not enough stock - only {current_stock} available."
            item["stock"] = current_stock - quantity
            if item["stock"] < 5:
                item["flagged"] = True
            new_sale = {
                "sale_id": len(sales) + 1,
                "item": item.get("name", ""),
                "item_id": item_id,
                "quantity": int(quantity),
                "unit_price": item.get("price", 0),
                "total": round(quantity * item.get("price", 0), 2),
                "logged_by": username,
                "date": time.strftime("%Y-%m-%d %H:%M"),
            }
            sales.append(new_sale)
            return new_sale, "Sale logged successfully."
    return None, "Item not found."


def toggle_flag(inventory, item_id):
    for item in inventory:
        if item.get("item_id") == item_id:
            item["flagged"] = not item.get("flagged", False)
            return True
    return False
