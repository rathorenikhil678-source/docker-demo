from kafka import KafkaConsumer
import json


def user_login_and_listen():
    print("=== Transaction Monitoring System ===")

    user_id_input = input("Enter your User ID: ")

    try:
        user_id = int(user_id_input)
    except ValueError:
        print("Invalid User ID.")
        return

    print(f"Logged in as User {user_id}")
    print("Listening for transactions above ₹500...\n")

    consumer = KafkaConsumer(
        'transaction-above-500',
        bootstrap_servers=['kafka:9092'],
        auto_offset_reset='latest',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    for message in consumer:

        tx_data = message.value

        if tx_data.get('userId') == user_id:

            print("\nTRANSACTION ALERT ")
            print(f"Name      : {tx_data.get('name')}")
            print(f"User ID   : {tx_data.get('userId')}")
            print(f"Tx ID     : {tx_data.get('tx_id')}")
            print(f"Amount    : ₹{tx_data.get('amount'):.2f}")
            print(f"Timestamp : {tx_data.get('timestamp')}")
            print("-" * 40)


if __name__ == "__main__":
     user_login_and_listen()
# from kafka import KafkaConsumer
# import json


# def user_login_and_listen():
#     print("=== Fraud Alert System ===")

#     user_id_input = input("Enter your userId to login: ")

#     try:
#         user_id = int(user_id_input)
#     except ValueError:
#         print("Invalid ID. Exiting.")
#         return

#     print(f"Logged in as User {user_id}. Listening for alerts...")

#     consumer = KafkaConsumer(
#         'fraud-notification',
#         bootstrap_servers=['kafka:9092'],
#         auto_offset_reset='latest',
#         value_deserializer=lambda x: json.loads(x.decode('utf-8'))
#     )

#     for message in consumer:

#         alert_data = message.value

#         if alert_data.get('userId') == user_id:

#             print("\n🚨 CRITICAL FRAUD ALERT 🚨")
#             print(f"Name      : {alert_data.get('name')}")
#             print(f"User ID   : {alert_data.get('userId')}")
#             print(f"Tx ID     : {alert_data.get('tx_id')}")
#             print(f"Amount    : ₹{alert_data.get('amount'):.2f}")
#             print(f"Timestamp : {alert_data.get('timestamp')}")
#             print("-" * 40)


# if __name__ == "__main__":
#     user_login_and_listen()