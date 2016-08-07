"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *
from sqlalchemy import or_
init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.

brand = Brand.query.filter(Brand.id == 8).all()

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

models = Model.query.filter_by(name="Corvette", brand_name="Chevrolet").all()

# Get all models that are older than 1960.

models = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.

brands = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".

models = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.

brands = Brand.query.filter(Brand.founded == 1903, Brand.discontinued is 'Null').all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.

brands = Brand.query.filter(or_(Brand.founded < 1950, Brand.discontinued is not None)).all()


# Get any model whose brand_name is not Chevrolet.

models = Model.query.filter(Model.brand_name is not "Chevrolet").first()

# Fill in the following functions. (See directions for more info.)


def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models = Model.query.filter(Model.year == year).all()
    for model in models:

        return (model.name, model.brand_name, model.brand[0].headquarters)


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''
    
    brands = db.session.query(Brand).all()
    for brand in brands:
        if brand.model is not None:
            print(brand.name, brand.model.name)

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
#      Returned value will be list of brand objects having name 'Ford'. Data type is List.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
#      Association table is like a middle table between two tables that are not connected to each other.
#      It associates those two tables. 
#      Asoociation table manages Many to Many relatioship.  
# -------------------------------------------------------------------
# Part 3


def search_brands_by_name(mystr):
    brands = Brand.query.filter(Brand.name == mystr).all()
    return brands


def get_models_between(start_year, end_year):
    models = Model.query.filter(Model.year >= start_year, Model.year < end_year).all()
    return models



