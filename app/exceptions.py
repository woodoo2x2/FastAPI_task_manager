class UserNotFoundException(Exception):
    detail = "User not found"


class UserNotCorrectPasswordException(Exception):
    detail = "Password is incorrect"


class TokenExpiredException(Exception):
    detail = "Token expired"


class TokenNotCorrectException(Exception):
    detail = "Token is incorrect"


class TaskNotFoundException(Exception):
    detail = "Task not found"
