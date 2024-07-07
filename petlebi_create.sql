CREATE TABLE IF NOT EXISTS petlebi (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    brand VARCHAR(63),
    price DECIMAL(10, 2),
    stock VARCHAR(31),
    category VARCHAR(127),
    sku VARCHAR(63),
    barcode VARCHAR(63),
    description TEXT,
    url TEXT,
    images JSON
)