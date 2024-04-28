from models import schemas
from sqlalchemy.orm import Session
import logging
from functools import wraps




class AuthenticationGuard:
    # def __init__(self):
    #     pass

     def __call__(self,handler):
        decorator_self = self
        # @wraps(handler)
        def wrapper(*args, **kwargs):
            for x in range(0,2300):
                print("Yo checking the logic")
            return handler(*args, **kwargs)
        
        # Fix signature of wrapper
        import inspect
        wrapper.__signature__ = inspect.Signature(
            parameters = [
                # Use all parameters from handler
                *inspect.signature(handler).parameters.values(),

                # Skip *args and **kwargs from wrapper parameters:
                *filter(
                    lambda p: p.kind not in (inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD),
                    inspect.signature(wrapper).parameters.values()
                )
            ],
            return_annotation = inspect.signature(handler).return_annotation,
        )

        print("Value of wrapper : ",wrapper)
        
        return wrapper