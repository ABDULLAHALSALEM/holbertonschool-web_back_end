# NoSQL - MongoDB

This project introduces **NoSQL databases** with a focus on **MongoDB**, a document-oriented database. You'll learn how to perform CRUD operations, query data, and use Python with MongoDB through PyMongo.

---

## What is NoSQL?

**NoSQL** (Not Only SQL) databases are designed to handle large volumes of unstructured or semi-structured data. Unlike traditional relational databases (SQL), NoSQL databases:

- Don't require fixed table schemas
- Scale horizontally (distributed across multiple servers)
- Are optimized for specific data models (document, key-value, graph, etc.)
- Handle big data and real-time applications efficiently

### MongoDB Overview

**MongoDB** is a document-oriented NoSQL database that stores data in flexible, JSON-like documents called BSON (Binary JSON). Key features:

- **Flexible Schema**: Each document can have different fields
- **Scalability**: Horizontal scaling through sharding
- **High Performance**: Optimized for read/write operations
- **Rich Query Language**: Powerful querying and aggregation
- **Indexing**: Support for various index types

---

## Learning Objectives

By the end of this project, you will be able to:

- Understand what NoSQL databases are and when to use them
- Explain the differences between SQL and NoSQL
- Perform CRUD operations in MongoDB
- Use MongoDB shell commands
- Work with MongoDB using Python and PyMongo
- Query and filter documents effectively
- Update and delete documents
- Aggregate and analyze data

---

## Project Structure

```
NoSQL/
├── 0-list_databases              # MongoDB: List all databases
├── 1-use_or_create_database      # MongoDB: Create/use database
├── 2-insert                      # MongoDB: Insert document
├── 3-all                         # MongoDB: List all documents
├── 4-match                       # MongoDB: Query with filter
├── 5-count                       # MongoDB: Count documents
├── 6-update                      # MongoDB: Update documents
├── 7-delete                      # MongoDB: Delete documents
├── 8-all.py                      # Python: List all documents
├── 9-insert_school.py            # Python: Insert document
├── 10-update_topics.py           # Python: Update document
├── 11-schools_by_topic.py        # Python: Query by topic
├── 12-log_stats.py               # Python: Nginx log statistics
└── README.md                     # Project documentation
```

---

## Files Description

### MongoDB Shell Scripts

#### 0-list_databases
Lists all databases in MongoDB.
```javascript
show dbs
```

#### 1-use_or_create_database
Creates or switches to the database `my_db`.
```javascript
use my_db
```

#### 2-insert
Inserts a document into the `school` collection.
```javascript
db.school.insert({name: "Holberton school"})
```

#### 3-all
Lists all documents in the `school` collection.
```javascript
db.school.find()
```

#### 4-match
Finds documents matching specific criteria.
```javascript
db.school.find({name: "Holberton school"})
```

#### 5-count
Counts the number of documents in the collection.
```javascript
db.school.count()
```

#### 6-update
Updates documents by adding a new field.
```javascript
db.school.update(
    {name: "Holberton school"},
    {$set: {address: "972 Mission street"}},
    {multi: true}
)
```

#### 7-delete
Deletes all documents matching the criteria.
```javascript
db.school.deleteMany({name: "Holberton school"})
```

---

### Python Scripts (PyMongo)

#### 8-all.py
Function to list all documents in a collection.
```python
def list_all(mongo_collection):
    """Returns list of all documents"""
    return list(mongo_collection.find())
```

#### 9-insert_school.py
Inserts a new document based on keyword arguments.
```python
def insert_school(mongo_collection, **kwargs):
    """Inserts and returns new document ID"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
```

#### 10-update_topics.py
Updates all topics of a school document.
```python
def update_topics(mongo_collection, name, topics):
    """Updates topics for a school"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
```

#### 11-schools_by_topic.py
Returns schools that have a specific topic.
```python
def schools_by_topic(mongo_collection, topic):
    """Returns list of schools with specific topic"""
    return list(mongo_collection.find({"topics": topic}))
```

#### 12-log_stats.py
Provides statistics about Nginx logs stored in MongoDB.
- Counts total logs
- Counts each HTTP method (GET, POST, PUT, PATCH, DELETE)
- Counts status check requests

---

## Installation

### Install MongoDB on Ubuntu/Debian
```bash
# Import MongoDB public key
wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -

# Create list file
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list

# Update and install
sudo apt-get update
sudo apt-get install -y mongodb-org

# Start MongoDB
sudo systemctl start mongod
sudo systemctl enable mongod
```

### Install MongoDB on Windows
1. Download MongoDB from [mongodb.com](https://www.mongodb.com/try/download/community)
2. Run the installer
3. Add MongoDB to system PATH
4. Start MongoDB service

### Install PyMongo
```bash
pip install pymongo
```

---

## Usage

### MongoDB Shell Commands

```bash
# Start MongoDB shell
mongo

# Or connect to specific database
mongo my_db

# Run a script file
mongo < 0-list_databases

# Or using mongosh (modern shell)
mongosh < 0-list_databases
```

### Python Scripts

```bash
# Make scripts executable
chmod +x *.py

# Run Python scripts
python3 8-all.py
python3 12-log_stats.py
```

---

## MongoDB Basic Commands

### Database Operations
```javascript
show dbs                    // List all databases
use database_name           // Switch to database
db.dropDatabase()          // Delete current database
```

### Collection Operations
```javascript
show collections           // List all collections
db.createCollection("name") // Create collection
db.collection.drop()       // Delete collection
```

### CRUD Operations

**Create (Insert)**
```javascript
db.collection.insertOne({field: "value"})
db.collection.insertMany([{}, {}, {}])
```

**Read (Query)**
```javascript
db.collection.find()                    // Find all
db.collection.find({field: "value"})    // Find with filter
db.collection.findOne({field: "value"}) // Find single document
db.collection.find().limit(5)           // Limit results
db.collection.find().sort({field: 1})   // Sort (1=asc, -1=desc)
```

**Update**
```javascript
db.collection.updateOne({filter}, {$set: {field: "new value"}})
db.collection.updateMany({filter}, {$set: {field: "new value"}})
db.collection.replaceOne({filter}, {new document})
```

**Delete**
```javascript
db.collection.deleteOne({filter})
db.collection.deleteMany({filter})
```

---

## PyMongo Basics

### Connect to MongoDB
```python
from pymongo import MongoClient

# Connect to local MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Access database
db = client['database_name']

# Access collection
collection = db['collection_name']
```

### Perform Operations
```python
# Insert
result = collection.insert_one({"name": "John", "age": 30})
print(result.inserted_id)

# Find all
for doc in collection.find():
    print(doc)

# Find with filter
for doc in collection.find({"age": {"$gt": 25}}):
    print(doc)

# Update
collection.update_many(
    {"age": {"$lt": 30}},
    {"$set": {"status": "young"}}
)

# Delete
collection.delete_many({"age": {"$lt": 18}})

# Count
count = collection.count_documents({})
print(f"Total documents: {count}")
```

---

## MongoDB Query Operators

### Comparison Operators
- `$eq`: Equal to
- `$ne`: Not equal to
- `$gt`: Greater than
- `$gte`: Greater than or equal to
- `$lt`: Less than
- `$lte`: Less than or equal to
- `$in`: Matches any value in array
- `$nin`: Matches none of the values in array

### Logical Operators
- `$and`: Joins conditions with AND
- `$or`: Joins conditions with OR
- `$not`: Inverts the effect of a query
- `$nor`: Joins conditions with NOR

### Example:
```javascript
db.collection.find({
    $and: [
        {age: {$gte: 18}},
        {status: "active"}
    ]
})
```

---

## SQL vs NoSQL

| Feature | SQL (Relational) | NoSQL (MongoDB) |
|---------|------------------|-----------------|
| **Data Model** | Tables with rows & columns | Documents (JSON-like) |
| **Schema** | Fixed schema | Flexible/dynamic schema |
| **Scalability** | Vertical (more powerful server) | Horizontal (more servers) |
| **Relationships** | Foreign keys, JOINs | Embedded documents, references |
| **Best For** | Complex queries, transactions | Large-scale data, flexibility |
| **Examples** | MySQL, PostgreSQL | MongoDB, Cassandra, Redis |

---

## When to Use NoSQL?

✅ **Use NoSQL when:**
- Handling large volumes of unstructured data
- Need rapid development with changing requirements
- Horizontal scaling is required
- Working with real-time big data applications
- Schema flexibility is important

❌ **Use SQL when:**
- Need complex transactions (ACID compliance)
- Data relationships are complex and well-defined
- Strong consistency is critical
- Working with structured data with clear schema

---

## Common MongoDB Use Cases

1. **Content Management**: Blogs, articles with varying fields
2. **Real-time Analytics**: User behavior tracking
3. **IoT Applications**: Sensor data collection
4. **Mobile Applications**: User profiles, preferences
5. **Catalogs**: Product catalogs with diverse attributes
6. **Logging**: Application logs, event tracking

---

## Best Practices

1. **Design Schema for Your Queries**: Structure data based on how you'll query it
2. **Use Indexes**: Create indexes on frequently queried fields
3. **Avoid Deep Nesting**: Limit embedded document depth to 2-3 levels
4. **Use Embedding for One-to-Few**: Embed related data when there are few items
5. **Use References for One-to-Many**: Use references for large related datasets
6. **Monitor Performance**: Use `explain()` to analyze query performance
7. **Handle Connections Properly**: Reuse MongoDB connections

---

## Requirements

- **MongoDB**: 4.4 or higher
- **Python**: 3.7 or higher
- **PyMongo**: Latest version
- Ubuntu 20.04 LTS or Windows 10/11
- All Python files must be executable
- All files must end with a newline
- First line of Python files: `#!/usr/bin/env python3`
- Code must follow `pycodestyle` (version 2.5)

---

## Testing

### Test MongoDB Shell Scripts
```bash
# Test listing databases
mongo < 0-list_databases

# Test inserting data
mongo < 1-use_or_create_database
mongo < 2-insert
mongo < 3-all
```

### Test Python Scripts
```bash
# Create test file
cat > test.py << 'EOF'
from pymongo import MongoClient
from 8_all import list_all

client = MongoClient('mongodb://127.0.0.1:27017')
print(list_all(client.my_db.school))
EOF

python3 test.py
```

---

## Troubleshooting

### MongoDB Connection Issues
```bash
# Check if MongoDB is running
sudo systemctl status mongod

# Start MongoDB
sudo systemctl start mongod

# Check MongoDB logs
sudo tail -f /var/log/mongodb/mongod.log
```

### Port Already in Use
```bash
# Find process using port 27017
sudo lsof -i :27017

# Kill the process
sudo kill -9 <PID>
```

### Permission Issues
```bash
# Fix data directory permissions
sudo chown -R mongodb:mongodb /var/lib/mongodb
sudo chown mongodb:mongodb /tmp/mongodb-27017.sock
```

---

## Resources

- [MongoDB Official Documentation](https://docs.mongodb.com/)
- [PyMongo Documentation](https://pymongo.readthedocs.io/)
- [MongoDB University](https://university.mongodb.com/) - Free courses
- [NoSQL vs SQL Explained](https://www.mongodb.com/nosql-explained/nosql-vs-sql)
- [Data Modeling in MongoDB](https://docs.mongodb.com/manual/core/data-modeling-introduction/)

---

## Author

**Holberton School** - Web Backend Development Project

---

## License

This project is part of the Holberton School curriculum.