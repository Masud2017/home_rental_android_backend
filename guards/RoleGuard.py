class RoleGuard:
    def __init__(self,role:str):
        self.role = role

    def __call__(self,func):
        decorator_self = self
        def wrapper(*args,**kwargs):
            

            return func(args,kwargs)

            # logic should be written here
            print("Yo checking the logic")

        
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
        
        return wrapper