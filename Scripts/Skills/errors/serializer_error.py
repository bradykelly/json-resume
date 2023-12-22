class SerializerError(Exception):

    def __init__(self, message: str = None, original_exception: Exception = None):
        """
        Generalised exception for errors encountered while serializing or deserializing JSON with the json module.
        :type original_exception: Exception
        """

        assert message is None or isinstance(message, str)
        assert original_exception is None or isinstance(original_exception, Exception)

        self.message = message

        super().__init__(message, original_exception)
