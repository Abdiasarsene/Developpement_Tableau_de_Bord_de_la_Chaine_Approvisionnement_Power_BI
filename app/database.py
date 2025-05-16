# Importation des librairie
import mysql.connector
import logging

def insert_data(data, Delivery_Status):
    try: 
        connection = mysql.connector.conect(
            host ="localhost",
            user ="root",
            password ="",
            database = "logistik_data"
        )
        cursor = connection.cursor()
        
        insert_query="""
        INSERT INTO logistic_chain (
            Stock_Level, 
            Sales, 
            Transportation_Cost,
            Region, 
            Delivey_Urgency,
            Estimated_Day) 
        VALUES (%s,%s,%s,%s,%s,%s)
        """
        
        values =(
            data.Stock_Level,
            data.Sales,
            data.Transportation_Cost,
            data.Region, 
            data.Delivery_Urgency,
            data.Estimated_Day,
            Delivery_Status
        )
        
        cursor.execute(insert_query, values)
        connection.commit()
        cursor.close()
        connection.close()
        
        print("✅ Nouvelles données enrégistrées avec succès")
    except mysql.connector.Error as err:
        logging.error(f"❌ Erreur lors de l'insertion dans la base de données : {err}")
    except Exception as e: 
        logging.error(f"❌ Erreur générale : {e}")
        print(f"❌ Erreur lors de l'insertion dans la base de données : {e}")