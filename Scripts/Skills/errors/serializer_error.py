class SerializerError(Exception):
    def __init__(self, message, original_exception: Exception = None):
        """
        Generalised exception for errors encountered while serializing or deserializing JSON with the json module.
        :type original_exception: Exception
        """
        assert isinstance(message, str)
        assert original_exception is None or isinstance(original_exception, Exception)

        super().__init__(message, original_exception)
