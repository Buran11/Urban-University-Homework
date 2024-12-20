from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated

from app.models.products import Product
from sqlalchemy import insert
from app.schemas import CreateProduct

from slugify import slugify

from sqlalchemy import select, update

router = APIRouter(prefix='/product', tags=['product'])


@router.get('/')
async def all_products(db: Annotated[Session, Depends(get_db)]):
    products = db.scalars(select(Product).where(
        Product.is_active == True, Product.stock > 0)).all()
    return products


@router.post('/create')
async def create_product(db: Annotated[Session, Depends(get_db)], create_product: CreateProduct):
    db.execute(insert(Product).values(
        name=create_product.name,
        discription=create_product.description,
        price=create_product.price,
        image_url=create_product.image_url,
        stock=create_product.stock,
        category_id=create_product.category_id,
        rating=0.0,
        slug=slugify(create_product.name)))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'successful'
    }


@router.get('/{category_slug}')
async def prod_by_category(db: Annotated[Session, Depends(get_db)], category_slug: str):
    category = db.scalar(select(Product).where(Product.slug == category_slug))
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Category not found'
        )
    subcategories = db.scalars(select(Product).where(
        Product.parent_id == category.id)).all()
    category_and_subcategories = [category.id] + [i.id for i in subcategories]
    products_category = db.scalars(select(Product).where(Product.category_id.in_(
        category_and_subcategories), Product.is_active == True, Product.stock > 0)).all()
    return products_category


@router.get('/detail/{product_slug}')
async def product_detail(db: Annotated[Session, Depends(get_db)], product_slug: str):
    product = db.scalar(select(Product).where(
        Product.slug == product_slug, Product.is_active == True, Product.stock > 0))
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Ther are no product'
        )
    return product


@router.put('/detail/{product_slug}')
async def update_product(db: Annotated[Session, Depends(get_db)], product_slug: str, update_product_model: CreateProduct):
    product_update = db.scalar(
        select(Product).where(Product.slug == product_slug))
    if product_update is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no product found'
        )
    db.execute(update(Product).where(Product.slug == product_slug).values(
        name=create_product.name,
        discription=create_product.description,
        price=create_product.price,
        image_url=create_product.image_url,
        stock=create_product.stock,
        category_id=create_product.category_id,
        rating=0.0,
        slug=slugify(create_product.name)))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Product update is successful'
    }


@router.delete('/delete')
async def delete_product(db: Annotated[Session, Depends(get_db)], product_id: int):
    product_delete = db.scalar(select(Product).where(Product.id == product_id))
    if product_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no product found'
        )
    db.execute(update(Product).where(Product.id ==
               product_id).values(is_active=False))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Product delete is successful'
    }
