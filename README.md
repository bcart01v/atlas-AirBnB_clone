
# Atlas - AirBnB Clone

This is the beginning of the Atlas - Airbnb Clone. It's the foundation of re-creating Air-BnB, starting with the backend. 

![hbnb logo with old school name and mascot](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240206%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240206T185348Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b199eff9b9ada959b79786874f4fa126c6a278344c58c32ac864ce12d9db83ea)



## Project Description

#### AirBnB - Console

This is our AirBnB clone project. This repository contains the first step towards constructing our very own full-stack web application, which is essentially recreating the AirBnB platform. This is the first phase, known as "The Console," is a command interpreter designed to manage the core functionalities of our AirBnB application and lay the groundwork for the subsequent web development stages.
## Features


 **Command Interpreter:** To manage objects for the AirBnB clone, including:

- Creating new instances of BaseModel (e.g., new User or new Place)
- Retrieving an object from storage
- Performing operations on objects (e.g., count, compute stats)
- Updating attributes of an object
- Destroying an object

###
- **Serialization and Deserialization:** Conversion of instances into a JSON file and vice versa, enabling persistent storage of our data.
###
- **BaseModel Class:** A base class to take care of initialization, serialization, and deserialization of future instances.
###
- **User Authentication:** Basic user authentication management to create new users and manage their information.
###
- **Storage Management:** A simple file storage system to persist data between sessions, ensuring that our objects' data remains intact.


## How to Start

To start the console, simply navigate to the root directory and type 

``` ./console.py ```

