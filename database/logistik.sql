-- Active: 1746494190621@@localhost@3306@logistik_data
CREATE TABLE logistic_chain(
    Id INT AUTO_INCREMENT PRIMARY kEY,
    Stock_Level  INT,
    Sales INT,
    Transportation_Cost FLOAT,
    Region CHAR(50),
    Delivery_Urgency CHAR(50),
    Estimated_Day INT
)