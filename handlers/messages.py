from settings import *

router = Router()

@router.message(F.text)
async def _(message: types.Message):
   ...