from rest_framework.response import Response


def response(data, message='', status=1):
    """
    Method to standardize the response
    :param data: dictionary with the data of the response
    :param message: message to add to the response
    :param status: status code, no HTTP code
    :return:
    """
    return Response({'data': data, 'message': message, 'status': status})
