<p align="center">
    <img src="./assets/kafka.png" alt="Apache Kafka" width="70%">
</p>

# Dive into Kafka

### Table of Contents:
- [Getting Started](#getting-started)
- [Kafka Connect](#kafka-connect)

### Getting Started
Apache Kafka is an open-source fault-tolerant messaging system based on the publish-subscribe model. Kafka is known for its speed, scalability, and distributed architecture by design.
Use cases:
- Microservices Communication: It's often used as a communication backbone for microservices architectures, ensuring reliable and asynchronous communication between services.
- Log and Event Streaming: Kafka is ideal for collecting and processing log and event data from various sources, making it valuable for monitoring, analytics, and auditing.
- Data Integration: Many organizations use Kafka to connect disparate data systems, enabling efficient data sharing and integration between applications.
- Real-time Analytics: Kafka enables real-time data streaming, supporting applications for real-time analytics, dashboarding, and decision-making.
- IoT and Sensor Data: It's an excellent choice for managing data from Internet of Things (IoT) devices and sensors, allowing for the real-time processing of vast amounts of data.
- Machine Learning and AI: Kafka can be integrated into machine learning and artificial intelligence pipelines to facilitate real-time data ingestion and model training.

![Kafka message broker](https://github.com/a-m-farahani/kafka-tutorial/blob/master/assets/kafka-producer-consumer.png?raw=true)

In this context, we are setting up a Kafka server within a Docker environment. To streamline the process, we'll create a bash script responsible for pulling and launching "kafka-server" and "kafka-topic-creator" services.
