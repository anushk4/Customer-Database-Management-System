# Customer-Database-Management-System

This is a project done as a part of the CS curriculum of `CBSE Class 12`.

Python-MySQL connectivity forms the basis of this project. It involves the usage and implementation of function definition, the concept of local and global scope, modules, and the very basic ideology required for Python programming.

- Import statements imports the already existing modules from python library to main program.
- `while` loop runs till the condition is true while `for` loop runs for a certain specified number of times.
- Defined functions run when called from the `__main__`

### Requirements
- Python IDLE
- MySQL
- VS Code

To connect python and MySQL, install `pip` from the command prompt and then install `mysql.connector` or `pymysql`

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
pip install mysql-connector-python
```

## Aims and Objectives
This project helps to store customer check-in data into a [database management system](https://www.ibm.com/docs/en/zos-basic-skills?topic=zos-what-is-database-management-system) which takes input through an [IDE](https://www.redhat.com/en/topics/middleware/what-is-ide). This data is used to maintain customer information, helps to calculate the total expenditure and keeps track of check-in and check-out timings and miscellaneous details. It also used this information for the future purposes of attracting customers on the basis of customized interests. This helps in increasing the revenue of hotels and at the same time helps in easy management of the hotel.