from typing import List, Optional
from fastapi import APIRouter, Header
from fastapi.responses import  PlainTextResponse, Response, HTMLResponse

router = APIRouter(
    prefix='/product',
    tags=['product']
)

products = ['watch', 'cemara', 'phone']

@router.get('/all')
def get_all_products():
    # return products
    data = ", ".join(products) #leave it blank for making a string without comma
    return Response(content=data, media_type='text/plain')

@router.get('/withheader')
def get_products(
    response: Response,
    custom_header: Optional[List[str]] = Header(None)    
):
    return products

@router.get('/{id}', responses={
    200: {
        "content": {
            "text/html": {
                "example":"<div>Product</div>"
            }
        },
        "description": "Returns the HTML for an object"
    },
    404: {
        "content": {
            "text/plain": {
                "example": "Product with{id} not available"
            }
        },
        "description": "A cleartext error message"
    }
})
def get_product(id: int):
    if id > len(products):
        out = 'Product not available'
        return PlainTextResponse(status_code=404, content=out, media_type="text/plain")
    else: 
        product = products[id]
        out = f"""
        <head>
            <style>
            .product {{
                width: 500px;
                height: 30px;
                border: 2px inset green;
                background-color: lightblue;
                text-align: center;
            }}
            </style>
        </head>
        <div class="product"> {product} </div>
        """
    return HTMLResponse(content=out, media_type="text/html")