from fastapi import APIRouter

router = APIRouter(prefix='/admin', tags=['Admin'])


@router.get('/components')
def get_components():
    ...


@router.post('/components')
def create_components():
    ...
