class AppException(Exception):
    def __init__(
            self,
            message:str, 
            code:str, 
            status_code: int,

    ):
        self.message= message
        self.code = code
        self.status_code = status_code

# user stuff 
class UserNotFoundError(AppException):
    def __init__(self):
        super().__init__("User Not Found", "USER_NOT_FOUND", 404)

class UserAlreadyExistsError(AppException):
    def __init__(self):
        super().__init__("User Already Exists", "USER_ALREADY_EXISTS", 409)
        
class UserInactiveError(AppException):
    def __init__(self):
        super().__init__("User Inactive", "USER_INACTIVE", 400)

# auth stuff
class InvalidCredentialsError(AppException):
    def __init__(self):
        super().__init__("Invalid Credentials", "INVALID_CREDENTIALS", 401)

class InvalidTokenError(AppException):
    def __init__(self):
        super().__init__("Invalid Token", "INVALID_TOKEN", 401)


class UnAuthorizedAssess(AppException):
    def __init__(self):
        super().__init__("UnAuthorized Access", "UNAUTHORIZED_ACCESS", 403)



# task stuff 
class InvalidTaskStatusError(AppException):
    def __init__(self):
        super().__init__("Invalid Task Status", "INVALID_TASK_STATUS", 400)

class TaskNotFoundError(AppException):
    def __init__(self):
        super().__init__("Task Not Found", "TASK_NOT_FOUND", 404)

class TaskAlreadyExistsError(AppException):
    def __init__(self):
        super().__init__("Task Already Exists", "TASK_ALREADY_EXISTS", 409)



# server stuff 
class InternalServerError(AppException):
    def __init__(self):
        super().__init__("Internal Server Error", "INTERNAL_SERVER_ERROR", 500)


