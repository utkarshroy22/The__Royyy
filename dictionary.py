# Library Management using Nested Dictionary
library_data = {
    "Rahul": {"books": ["Python Basics", "DSA"], "due_date": "2026-03-20", "fine": 50},
    "Priya": {"books": ["Cloud Computing", "Algorithms"], "due_date": "2026-03-15", "fine": 0},
    "Aman": {"books": ["Python Basics"], "due_date": "2026-03-10", "fine": 200},
    "Sneha": {"books": ["Web Dev"], "due_date": "2026-03-25", "fine": 0}
}

print("Library Records:")
for student, details in library_data.items():
    print(f"{student}: Books - {', '.join(details['books'])}, Due - {details['due_date']}, Fine - ₹{details['fine']}")

# Total fine calculate
total_fine = sum(details['fine'] for details in library_data.values())
print(f"Total Fine Collected: ₹{total_fine}")

# Overdue students (fine > 0)
overdue = {s: d for s, d in library_data.items() if d['fine'] > 0}
print("Overdue Students:", overdue)

# All unique books
all_books = set()
for details in library_data.values():
    all_books.update(details['books'])
print("All Unique Books:", list(all_books))

# Most popular book
book_count = {}
for details in library_data.values():
    for book in details['books']:
        book_count[book] = book_count.get(book, 0) +1