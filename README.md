
# Atlas - AirBnB Clone

This is the beginning of the Atlas - Airbnb Clone. It's the foundation of re-creating Air-BnB, starting with the backend. 

<p align="center">
  <img src="https://github.com/bcart01v/atlas-AirBnB_clone/blob/main/assets/AirBNBLogo.png" alt="Atlas AirBNB Logo logo">
</p>


## Project Description

#### AirBnB - Console

This is our AirBnB clone project. This repository contains the first step towards constructing our very own full-stack web application, which is essentially recreating the AirBnB platform. This is the first phase, known as "The Console," is a command interpreter designed to manage the core functionalities of our AirBnB application and lay the groundwork for the subsequent web development stages.


## Classes 

The AirBnB Project uses the following classes: 

|     | BaseModel | FileStorage | User | State | City | Amenity | Place | Review |
| --- | --------- | ----------- | -----| ----- | -----| ------- | ----- | ------ |
| **PUBLIC INSTANCE ATTRIBUTES** | `id`<br>`created_at`<br>`updated_at` | | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` |
| **PUBLIC INSTANCE METHODS** | `save`<br>`to_dict` | `all`<br>`new`<br>`save`<br>`reload` | "" | "" | "" | "" | "" | "" |
| **PUBLIC CLASS ATTRIBUTES** | | | `email`<br>`password`<br>`first_name`<br>`last_name`| `name` | `state_id`<br>`name` | `name` | `city_id`<br>`user_id`<br>`name`<br>`description`<br>`number_rooms`<br>`number_bathrooms`<br>`max_guest`<br>`price_by_night`<br>`latitude`<br>`longitude`<br>`amenity_ids` | `place_id`<br>`user_id`<br>`text` | 
| **PRIVATE CLASS ATTRIBUTES** | | `file_path`<br>`objects` | | | | | | |


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

### Usage

In interactive mode

``` (hbnb) help ```

#### Commands currently supported:

- ```quit``` and EOF to exit the program
- ```create``` to create a new object (e.g., create BaseModel)
- ```show``` to display an object (e.g., show BaseModel (ID)) - 
- ```destroy``` to delete an object
- ```all``` to display all objects of a class
- ```update``` to update attributes of an object

#### Non-Interactive Mode 

``` echo "help" | ./console.py ```


#### Examples

``` (hbnb) create User ```

``` (hbnb) show User <id> ```

``` (gbnb) destroy User <id> ```

### Testing

All unit testing can be done running the following Command

``` python3 -m unittest discover tests ```

Alternatively, you can run the unit tester on specific files. 

``` python3 -m unittest tests/test_models/test_base_model.py ```



## Installation

To use this project, you will need to follow these steps

#### Prerequisite  
- This project was built with Python 3.8.10. You will need 3.8.x or above to properly use it, as it utilizes some date functions added in Python 3.8 
- git (to clone the repository)

#### Clone the repository

``` git clone https://github.com/bcart01v/atlas-AirBnB_clone.git ```

```cd atlas-AirBnB_clone```

Then follow the steps outlined above for use.





## Authors

- [Benjamin Carter](https://github.com/bcart01v/) 
- [Kyle Headley](https://github.com/Y-T-O-1)

