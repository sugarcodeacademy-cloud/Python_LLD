from LLD2.Structural.Facade.OrderContoller import OrderController


class Client:
    '''
    Go to a restaurant

    customer(user) --> waiter(controller-> take the request) --> chef(service-> handles main logic) --> helper(respository) -->ingredients(data)--> pantry(database)
    pantry(database) --> helper(repository) --> chef(sevice) --> waiter(controller) --> customer(user)
    '''

    '''
    place an order
    user -->  controller
    '''
    order_controller = OrderController()
    order_controller.process_order("Laptop", 123, 3, "vinod")
