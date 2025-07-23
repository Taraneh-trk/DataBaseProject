# Database Management System

A comprehensive SQLite-based database management system for warehouse and inventory operations, featuring user management, order processing, product cataloging, and advanced analytics.

### Note: This project was created for educational purposes and may not follow all production-level best practices. It serves as a foundation for learning database concepts.

##  Overview

This project implements a complete warehouse management system using Python and SQLite. It handles multiple aspects of business operations including user management, product catalogs, order processing, warehouse locations, and provides advanced analytics for business intelligence.

##  Features

### Core Functionality
- **User Management**: Admin and normal user roles with authentication
- **Product Catalog**: Comprehensive product information with pricing and inventory
- **Order Processing**: Complete order lifecycle management with status tracking  
- **Warehouse Management**: Multi-location warehouse system with container tracking
- **Location Services**: GPS coordinate-based location management

### Advanced Analytics
- **Sales Analytics**: Revenue tracking, profit calculations, and performance metrics
- **Customer Analytics**: Purchase behavior, retention rates, and customer segmentation
- **Inventory Analytics**: Product popularity, warehouse utilization, and stock analysis
- **Time-based Analysis**: Weekly, monthly, and seasonal trend analysis
- **Outlier Detection**: Automatic identification of unusual purchase patterns

##  Database Schema

The system consists of 6 interconnected tables:

### Tables Overview

| Table | Purpose | Key Features |
|-------|---------|--------------|
| `tpl` | Template/Organization management | Primary entity identifier |
| `user` | User account management | Role-based access (admin/normal) |
| `orders` | Order transaction records | Status tracking, gift options |
| `catelog` | Product catalog | Pricing, specifications, inventory |
| `warehouse` | Warehouse facility data | Multi-location, operational status |
| `location` | Geographic location data | GPS coordinates, container tracking |

### Key Relationships
- Users belong to organizations (tpl)
- Orders link customers to products and warehouses
- Products are managed by users and organizations
- Locations are associated with warehouses and organizations

##  Installation

### Prerequisites
- Python 3.6 or higher
- SQLite3 (included with Python)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Taraneh-trk/DataBaseProject.git
   cd DataBaseProject
   ```

2. **Run the application**
   ```bash
   python DataBaseProject.py
   ```

3. **Initial setup**
   - When prompted "run before ?", enter `no` for first-time setup
   - This will create the database schema and populate with sample data
   - For subsequent runs, enter `yes` to skip data initialization

##  Usage

### First Run
```bash
python DataBaseProject.py
# Enter 'no' when prompted to initialize the database with sample data
```

### Subsequent Runs
```bash
python DataBaseProject.py
# Enter 'yes' when prompted to skip data initialization
```

The script will automatically:
1. Create database tables if they don't exist
2. Populate with sample data (if requested)
3. Execute a series of analytical queries
4. Display results for various business metrics

##  Database Operations

### Data Management
- **CRUD Operations**: Complete Create, Read, Update, Delete functionality
- **Bulk Operations**: Efficient batch data insertion using `executemany()`
- **Data Validation**: Check constraints for data integrity
- **Foreign Key Relationships**: Referential integrity maintenance

### Sample Operations
```sql
-- User creation
INSERT INTO user VALUES (1,"john","john@email.com","password123",25,"admin",1);

-- Order placement  
INSERT INTO orders VALUES (1,"2023-01-15",1200,1,1,1,"pending","electronics","Product details","no");

-- Product addition
INSERT INTO catelog VALUES (1,"laptop",NULL,800,1000,"USA",2.5,15.0,"Gaming laptop","SKU001","Dell XPS",1,1,1);
```

##  Query Examples

### Business Intelligence Queries

#### 1. User Purchase History
```sql
SELECT DISTINCT user_name, user_email
FROM user, orders  
WHERE user_id = register_user_id;
```

#### 2. Product Profitability Analysis
```sql
SELECT product_id, SUM(sell_price-built_cost) as profit
FROM catelog 
GROUP BY product_id;
```

#### 3. Customer Retention Analysis
```sql
WITH repeat_customers AS (
    SELECT tpl_id, COUNT(DISTINCT register_user_id) AS repeat_count
    FROM orders
    WHERE register_user_id IN (
        SELECT register_user_id 
        FROM orders 
        GROUP BY register_user_id 
        HAVING COUNT(*) > 1
    )
    GROUP BY tpl_id
)
SELECT * FROM repeat_customers;
```

#### 4. Seasonal Profit Analysis
```sql
SELECT 
    tpl_id,
    strftime('%m', order_date) AS month,
    AVG(sell_price - built_cost) AS avg_monthly_profit
FROM orders
JOIN catelog ON order_user_id = register_user_id
GROUP BY tpl_id, strftime('%m', order_date);
```

##  Project Structure

```
database-management-system/
│
├── DataBaseProject.py   # Main application script
├── database PRESENTATION.pdf          # PRESENTATION
├── README.md            # Project documentation
└── project-statement.pdf     # project statement
```

##  Technical Details

### Database Features
- **SQLite Engine**: Lightweight, serverless database
- **ACID Compliance**: Transaction integrity and consistency
- **Foreign Key Constraints**: Data relationship enforcement
- **Check Constraints**: Data validation at database level
- **Indexed Queries**: Optimized query performance

### Python Features
- **Error Handling**: Robust database connection management
- **Parameterized Queries**: SQL injection prevention
- **Batch Operations**: Efficient bulk data processing
- **Dynamic Data Generation**: Automated test data creation

##  Analytics Capabilities

The system provides 25+ pre-built analytical queries covering:

- **Sales Performance**: Revenue trends, profit margins
- **Customer Behavior**: Purchase patterns, loyalty metrics  
- **Inventory Management**: Stock levels, product popularity
- **Operational Efficiency**: Warehouse utilization, location analysis
- **Temporal Analysis**: Daily, weekly, monthly, and seasonal insights
- **Anomaly Detection**: Outlier identification in purchase behavior

##  Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

### Development Guidelines
- Follow PEP 8 Python style guidelines
- Add comments for complex SQL queries
- Test database operations thoroughly
- Update documentation for new features

- Multi-database support
- User authentication system
- Backup and restore functionality

---

**Note**: This system is designed for educational and small-scale business use. For production environments, consider additional security measures, data validation, and performance optimizations.
