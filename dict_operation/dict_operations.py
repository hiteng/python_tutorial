


from pprint import pprint

def get_car_details(details, model_no):
    return details[model_no]


def get_model_location(details, model_no):
    return details[model_no]["manu_location"]

def get_model_loc_street(details, model_no):
    return details[model_no]["manu_location"]["Los Angeles"]

def update_price_by_value(details, price_value):
    for model_no, value in details.iteritems():
        #print model_no,value
        details[model_no]["price"] =  details[model_no]["price"] + price_value
    print details

def pop_details(details,model_no):
    try:

        details.pop(model_no)
    except KeyError:
        print "{} Model Does not exist.".format(model_no)
    except Exception as e:
        print "Error occured while deleting {} from data.".format(model_no)
        print "Error msg : {}".format(e)
    pprint (details)

# Give me all the models whose price are less than 300000
def model_price_less_than(details, price_val):
    for model_no in details:

        if details[model_no]["price"] < price_val:
            print model_no

def model_price_more_than(details, price_val):

    model_no_list = []
    for model_no in details:

        if details[model_no]["price"] > price_val:
            model_no_list.append(model_no)
            print model_no
    return model_no_list


def change_name(details):
    details["a2"]["name"] = "Audi RS"
    print car_details

def key_name(details):
    # for key in details:
    #     print(key)
    print details.keys()

def value_name(details,model_no):
    # for value in details:
    #     print(details[value]["name"])
    print details[model_no].values()


if __name__ == '__main__':

    car_details = {"a1": {"name": "Audi1", "manu_date": "01/01/2015", "price": 100000, "manu_location": ["New york","San Francisco","Los Angeles"]},
                   "a2": {"name": "Audi2", "manu_date": "02/01/2015", "price": 200000, "manu_location": ["New york","San Francisco","Los Angeles"]},
                   "a3": {"name": "Audi3", "manu_date": "03/01/2015", "price": 300000, "manu_location": ["New york","San Francisco","Los Angeles"]},
                   "a4": {"name": "Audi4", "manu_date": "04/01/2015", "price": 400000, "manu_location": ["New york","San Francisco","Los Angeles"]},
                   "a6": {"name": "Audi6", "manu_date": "06/01/2015", "price": 600000, "manu_location": ["New york","San Francisco","Los Angeles"]},
                   "a5": {"name": "Audi5", "manu_date": "05/01/2015", "price": 500000, "manu_location": {"New york": ["George st", "King st","Queen st"],
                   "San Francisco": ["River st", "Pitt st","May st"],"Los Angeles":["William st", "Grote st","Flinders st"]}}}



    print""
    print get_car_details(car_details, "a5")
    print""
    print get_model_location(car_details, "a2")
    print""
    print get_model_loc_street(car_details, "a5")
    print""
    print update_price_by_value(car_details,1000)
    print""
    print pop_details(car_details,"a9")
    print pop_details(car_details, "a6")
    print""
    print model_price_less_than(car_details, 300000)
    print""
    print model_price_more_than(car_details, 400000)
    print""
    print change_name(car_details)
    print""
    key_name(car_details)
    print""
    value_name(car_details,"a2")
