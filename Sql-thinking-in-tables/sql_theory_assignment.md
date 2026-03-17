Q1: Why databases are important in real-world AI systems
Databases are essential because AI systems depend on large volumes of structured data for training, predictions, and decision-making.
- They ensure organized storage, fast retrieval, and consistency.
- Examples of data stored:
- User profiles (names, emails, preferences)
- Transaction records (e-commerce, banking)
- Sensor data (IoT devices, medical monitors)
- Why structured storage matters: Without structured tables, AI models would struggle to process and learn patterns efficiently.

Q2: Relational database mental model
Relational databases follow a table-based model.
- Table → Represents an entity (e.g., Users, Orders).
- Row (Tuple) → Represents a single record (e.g., one user).
- Column (Attribute) → Represents a property of the entity (e.g., Name, Email).
- Each table should represent only one entity to avoid confusion and redundancy.
Example Table (Users):
| UserID | Name   | Email            |
|--------|--------|------------------|
| 1      | Ansh   | ansh@example.com |
| 2      | Freya  | freya@example.com |

Q3: Concept of a Primary Key
A Primary Key uniquely identifies each record in a table.
- Must be unique (no duplicates).
- Must be non-null (every record must have a value).
- Helps in searching, indexing, and linking records.
Example:
In the Users table, UserID can be the primary key.
- UserID = 1 → Ansh
- UserID = 2 → Freya

Q4: Database Schema
A Schema defines the structure of the database.
- It specifies tables, columns, data types, and relationships.
- Ensures consistency across the database.
- Acts like a blueprint for how data is organized.
Example Schema (simplified):
- Table: Users (UserID INT, Name VARCHAR, Email VARCHAR)
- Table: Orders (OrderID INT, UserID INT, Amount DECIMAL)

Q5: Relationships between tables
Relationships connect data across tables using foreign keys.
- A Foreign Key in one table refers to the Primary Key in another.
- This allows linking related data.
Example:
- Users table has UserID as primary key.
- Orders table has UserID as foreign key.
So, we can connect:
- UserID = 1 (Ansh) → Orders placed by Ansh.
- UserID = 2 (Freya) → Orders placed by Freya.
