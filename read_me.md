Real-Time Device Communication System
=====================================

Introduction
------------
This project implements a system for real-time communication with multiple devices using various protocols. The primary features include:

1. TCP/IP communication support for reading and writing values.
2. Simultaneous communication with multiple devices.
3. Extensible architecture for adding new communication protocols.
4. Stub implementation for testing TCP/IP communication.
5. Code-driven unit tests.

The system is designed with asyncio for efficient handling of concurrent operations.

File Structure
--------------
- protocols.py: Contains the base CommunicationProtocol class and its implementations.
- device_manager.py: Implements the DeviceManager for handling multiple devices.
- stubs.py: Includes stub implementations for testing.
- tests.py: Contains unit tests for the system.
- main.py: The entry point for running tests.

Requirements
------------
- Python 3.7 or higher

How to Run
----------
1. Ensure you have Python 3.7+ installed on your system.

2. Navigate to the project directory in your terminal:
   cd path/to/project_directory

3. Run the main script to execute the tests:
   python main.py

   This will run all the unit tests and display the results.

4. To use the system in your own code, import the necessary classes:
   from device_manager import DeviceManager
   from protocols import TCPIPProtocol

   Then create a DeviceManager and add devices as needed:
   manager = DeviceManager()
   device = TCPIPProtocol("192.168.1.1", 8080)
   manager.add_device("device1", device)

Extending the System
--------------------
To add a new communication protocol:
1. Create a new class in protocols.py that inherits from CommunicationProtocol.
2. Implement the read() and write() methods for your new protocol.
3. Use your new protocol class when adding devices to the DeviceManager.

Note: This system is a prototype and may require additional error handling and optimization for production use.