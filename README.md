# fresh_flow_order

At Freshflow, we calculate how much supermarkets and other grocery retailers should order of every item, every day.

Your task is to output a list of orders (per item, per day) by joining various tables together from this SQLite database that contains information about items, inventory, what’s orderable that day, and how much we think they will sell of each item in a specific day.

The output of your microservice should be a list of dicts, in JSON.

Each dict represents an order, for an item, for a day.

An order is a collection of information about the item, when it can be ordered, when it will be delivered, what’s the suggested retail price, what’s the profit margin, the purchase price, in which categories this item is in, any labels, how much there’s in a case of this stuff, how much they should order, and how much do they have in the inventory.

Here’s how this list of dicts should look like:

[
  {  # an order
    'item_number': int,  # uniquely identifies the item
    'ordering_day': datetime.date,  # the day this item can be ordered
    'delivery_day': datetime.date,  # the day this item will be delivered
    'sales_price_suggestion': float,  # supplier's suggested retail price per unit
    'profit_margin': float,  # profit margin at the sales price suggestion
    'purchase_price': float,  # supplier official purchase price per unit
    'item_categories': List<str>,  # any of the categories the item is in
    'labels': List<str>,  # a list that can contain any of `new`, `on_sale` and `price_change`, plus all categories extracted from the item name
    'case': {
      'quantity': float,  # represents how many items (in `case.unit`) a case contains
      'unit': str  # the unit of the `case.quantity`
    },
    'order': {
      'quantity': int,  # represents how many items (in `order.unit`) the user should order given the formula below (look below)
      'unit': str  # the unit of the `order.quantity` (it's always 'CS')
    },
    'inventory': {
      'quantity': float,  # the inventory quantity of the item that day
      'unit': str  # the unit of that quantity
    }
  },  # end of order
  {...}, # another order
  ...  # etcetera
]
