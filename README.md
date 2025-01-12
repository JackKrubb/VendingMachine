[![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-orange.svg)](https://sonarcloud.io/summary/new_code?id=SuphawitWongfu_VendingMachine)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=SuphawitWongfu_VendingMachine&metric=coverage)](https://sonarcloud.io/summary/new_code?id=SuphawitWongfu_VendingMachine)
# VendingMachineTracker
## vending machines
### self-checklist
- [x] CRUD for vending machine
- [x] Table for keeping different types of items in vending machines
- [x] CRUD for stocks in a vending machine
- [x] Can inspect listing of items in a vending machine
### example response
```json 
[
    {
        "id": 2,
        "installed_at": "Mon, 16 Jan 2023 17:30:22 GMT",
        "location": "In front of New Building",
        "name": "muic666"
    },
    {
        "id": 5,
        "installed_at": "Thu, 19 Jan 2023 05:27:21 GMT",
        "location": "somewhere",
        "name": "muic04"
    }
]
```
### add
```/add_vendings/?machine_name=<machine_name>&machine_location=<machine_location>```\
parameters

| Syntax           | Description                                    |
|------------------|------------------------------------------------|
| machine_name     | string<br/>the name of the vending machine     |
| machine_location | string<br/>the location of the vending machine |

### view
```/vendings/```\
this endpoint has no parameters. it is used to get all vending machines

### delete
```/delete_vendings/?id=<id>```

| Syntax           | Description                                               |
|------------------|-----------------------------------------------------------|
| id               | integer<br/> the id of vending machine you wish to delete |

### edit
```/edit_vendings/?id=<id>&machine_name=<machine_name>&machine_location=<machine_location>```

| Syntax           | Description                                             |
|------------------|---------------------------------------------------------|
| id               | integer<br/> the id of vending machine you wish to edit |
| machine_name     | string<br/>the name of the vending machine              |
| machine_location | string<br/>the location of the vending machine          |
## products
### example response
```json 
[
    {
        "id": 6,
        "price_per_unit": 15.0,
        "product_code": 55,
        "product_name": "coke",
        "product_quantity": 55
    },
    {
        "id": 7,
        "price_per_unit": 5.0,
        "product_code": 56,
        "product_name": "lay lean",
        "product_quantity": 50
    }
]
```
### add
```/add_products/?product_name=<product_name>&product_code=<product_code>&product_quantity=<product_quantity>&price_per_unit=<price_per_unit>```\
parameters

| Syntax           | Description                                  |
|------------------|----------------------------------------------|
| product_name     | string<br/>the name of the product           |
| product_code     | integer<br/>the product code of the product  |
| product_quantity | integer<br/>the quantity of the product      |
| price_per_unit   | integer<br/>price of the product per on unit |
### view
```/products/```\
this endpoint has no parameters. it is used to get all products

### delete
```/delete_products/?id=<id>```

| Syntax           | Description                                           |
|------------------|-------------------------------------------------------|
| id               | integer<br/> the id of the product you wish to delete |

### edit
```/edit_products/?id=<id>&product_name=<product_name>&product_code=<product_code>&product_quantity=<product_quantity>&price_per_unit=<price_per_unit>```

| Syntax           | Description                                        |
|------------------|----------------------------------------------------|
| id               | integer<br/>the id of the product you wish to edit |
| product_name     | string<br/>the name of the product                 |
| product_code     | integer<br/>the product code of the product        |
| product_quantity | integer<br/>the quantity of the product            |
| price_per_unit   | integer<br/>price of the product per on unit       |
## stocks
### example response
```json 
[
    {
        "id": 10,
        "machine_id": 2,
        "product_id": 7,
        "quantity": 10
    },
    {
        "id": 11,
        "machine_id": 2,
        "product_id": 6,
        "quantity": 10
    }
]
```
### add
```/add_machine_stocks/?machine_id=<machine_id>>&product_id=<product_id>>&quantity=<quantity>```\
parameters

| Syntax     | Description                                                    |
|------------|----------------------------------------------------------------|
| machine_id | Integer<br/>id of the machine                                  |
| product_id | integer<br/>id of the product                                  |
| quantity   | integer<br/>the initial quantity of the product in the mahcine |
### view
```/machine_stocks/```\
this endpoint has no parameters. it is used to get all stocks in every machine

### delete
```/delete_machine_stocks/?id=<id>>```

| Syntax           | Description                                         |
|------------------|-----------------------------------------------------|
| id               | integer<br/> the id of the stock you wish to delete |

### edit
```/edit_machine_stocks/?id=<id>&machine_id=<machine_d>&product_id=<product_id>>&quantity=<quantity>```

| Syntax         | Description                                            |
|----------------|--------------------------------------------------------|
| id             | integer<br/>the id of the stock you wish to edit       |
| machine_id     | integer<br/>the id of the machine                      |
| product_id     | integer<br/>the id of the product                      |
| quantity       | integer<br/>the quantity of the product in the machine |


### inspect stocks
```/inspect_stocks/?machine_id=<machine_id>```
### example response
```json
{
    "machine_id": 2,
    "machine_name": "muic666",
    "products": [
        {
            "id": 7,
            "price_per_unit": 5.0,
            "product_code": 56,
            "product_name": "lay lean",
            "product_quantity": 10
        },
        {
            "id": 6,
            "price_per_unit": 15.0,
            "product_code": 55,
            "product_name": "coke",
            "product_quantity": 10
        }
    ]
}
```
### parameters

| Syntax     | Description                                                  |
|------------|--------------------------------------------------------------|
| machine_id | integer<br/>the id of the machine you wish to inspect stocks |
���