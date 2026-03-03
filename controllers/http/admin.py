from fastapi import APIRouter


router = APIRouter()


@router.get('/components')
def get_components():
    ...


@router.post('/components')
def create_components():
    ...


@router.put('/components')
def update_components():
    ...


@router.delete('/components')
def delete_components():
    ...