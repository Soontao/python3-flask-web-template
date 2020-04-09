from flask import Flask, jsonify


class FlaskBaseError(Exception):
    """
    application base error, use this error, you can define the response code & message
    """

    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        """
        convert to dict
        """
        return {
            "error_type": self.__class__.__name__,
            "error": self.message,
            "code": self.status_code
        }


class ParameterError(FlaskBaseError):
    """
    parameter related error
    """

    status_code = 400


class ParameterLostError(ParameterError):
    """
    parameter lost error
    """

    def __init__(self, param_name):
        ParameterError.__init__(self, f"{param_name} must be provided.")


def set_error_handler(app: Flask):
    """
    set flask app error handler
    """
    @app.errorhandler(Exception)
    def handle_invalid_usage(e: Exception):
        """
        handle invalid message
        """

        if isinstance(e, FlaskBaseError):
            response = jsonify(e.to_dict())
            response.status_code = e.status_code
            return response

        response = jsonify({
            "code": 500,
            "error_type": e.__class__.__name__,
            "error": str(e),
        })
        response.status_code = 500
        return response
