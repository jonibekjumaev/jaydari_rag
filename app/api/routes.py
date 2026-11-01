from fastapi import APIRouter

router = APIRouter()

@router.get('/health')
def healtgh_check():
    return {'status:' 'OK'}