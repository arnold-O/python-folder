# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from fastapi import FastAPI
from scalar_fastapi import  get_scalar_api_reference

app = FastAPI()


@app.get("/shipment/{id_one}")
def get_shipment(id_one):
    return {
        "id": id_one,
        "name":"The black cinderella dress",
        "price": 2520,
        "date": "Friday the 13th of Someday 2026"
    }

@app.get("/shipment/latest")
def shipment_id():
    return {
        "id": 1234,
        "name": "The black cinderella dress",
        "price": 2520,
        "date": "Friday the 13th of Someday 2026"
    }



@app.get("/scalar", include_in_schema=False)
def get_scalardocs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",

    )

