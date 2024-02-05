from typing import List, Optional
from fastapi import APIRouter, Cookie, Form, Header
from fastapi.responses import  PlainTextResponse, Response, HTMLResponse

router = APIRouter(
    prefix='/product',
    tags=['product']
)

products = ['watch', 'cemara', 'phone']

@router.post('/new')
def create_product(name:str = Form(...)):
    products.append(name)
    return products

@router.get('/all')
def get_all_products():
    # return products
    data = ", ".join(products) #leave it blank for making a string without comma
    response = Response(content=data, media_type="text/plain")
    response.set_cookie(key="test_cookie", value="test_cookie_value")
    return Response(content=data, media_type='text/plain')

@router.get('/withheader')
def get_products(
    response: Response,
    custom_header: List[str] = Header(None),  #request headers 
    test_cookie: Optional[str]= Cookie
):
    if custom_header:
        response.headers['custom_response_header'] = "and ".join(custom_header)
    return {
        'data': products,
        'custom_header': custom_header,
        'my_cookie': test_cookie
    }

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