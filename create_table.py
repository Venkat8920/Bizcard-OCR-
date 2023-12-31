from sqlalchemy import create_engine, text

# Create engine using SQLAlchemy
engine = create_engine('mysql+pymysql://root:Venkat1585#@127.0.0.1/')

with engine.connect() as conn:
    # Execute the SQL statements to create the database and table
    conn.execute(text("CREATE DATABASE IF NOT EXISTS proj_bizcard"))
    conn.execute(text("USE proj_bizcard"))
    conn.execute(text('''
        CREATE TABLE IF NOT EXISTS BUSINESS_CARD(
            NAME VARCHAR(50), 
            DESIGNATION VARCHAR(100), 
            COMPANY_NAME VARCHAR(100), 
            CONTACT VARCHAR(35), 
            EMAIL VARCHAR(100), 
            WEBSITE VARCHAR(100), 
            ADDRESS TEXT, 
            PINCODE VARCHAR(100)
        )
    '''))



