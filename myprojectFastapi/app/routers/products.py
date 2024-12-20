from fastapi import APIRouter

router = APIRouter(prefix='/product', tags=['product'])


@router.get('/all_products')
async def all_products():
    pass


@router.post('/create')
async def create_product():
    pass


@router.get('/products/{category_slug}')
async def prod_by_category():
    pass


@router.get('/products/detail/{product_slug}')
async def product_detail():
    pass


@router.put('/products/detail/{product_slug}')
async def update_product():
    pass


@router.delete('/products/delete')
async def delete_product():
    pass
