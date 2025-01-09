maping = [
    {
        "heading": "Item borrowed (Select Item and Quantity)  [Wheelchair]",
        "id": 1
    },
    {
        "heading": "Item borrowed (Select Item and Quantity)  [Transporter Chair]",
        "id": 2
    },
    {
        "heading": "Item borrowed (Select Item and Quantity)  [Metal Walker]",
        "id": 3
    },
    {
        "heading": "Item borrowed (Select Item and Quantity)  [Rollator]",
        "id": 4
    },
    {
        "heading": "Item borrowed (Select Item and Quantity)  [Bed side Commode]",
        "id": 5
    },
    {
        "heading": "Item borrowed (Select Item and Quantity)  [Toilet Riser]",
        "id": 6
    },
    {
        "heading": "Item borrowed (Select Item and Quantity)  [Shower Bench/Chair]",
        "id": 7
    },
    {
        "heading": "Item borrowed (Select Item and Quantity)  [Hospital Bed]",
        "id": 8
    },
    {
        "heading": "Item borrowed (Select Item and Quantity)  [Hoyer Lift]",
        "id": 9
    },
    {
        "heading": "Item borrowed (Select Item and Quantity)  [Crutches]",
        "id": 10
    },
    {
        "heading": "Item borrowed (Select Item and Quantity)  [Cane]",
        "id": 11
    },
    {
        "heading": "Item borrowed (Select Item and Quantity)  [Bed rails]",
        "id": 12
    },
    {
        "heading": "Item borrowed (Select Item and Quantity)  [Toilet rails]",
        "id": 13
    },
    {
        "heading": "Item borrowed (Select Item and Quantity)  [House oxygen concentrator]",
        "id": 14
    },
    {
        "heading": "Item borrowed (Select Item and Quantity)  [Portable oxygen concentrator]",
        "id": 15
    }
]

# Supplies mapping helper functions
def get_dme_id(heading):
    for item in maping:
        if item["heading"] == heading:
            return item["id"]
    return None
