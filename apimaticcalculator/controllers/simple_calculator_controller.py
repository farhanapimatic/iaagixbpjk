# -*- coding: utf-8 -*-

"""
    apimaticcalculator

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration

class SimpleCalculatorController(BaseController):

    """A Controller to access Endpoints in the apimaticcalculator API."""


    def get_calculate(self,
                      options=dict()):
        """Does a GET request to /{operation}.

        Calculates the expression using the specified operation.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    operation -- OperationTypeEnum -- The operator to apply on
                        the variables
                    x -- float -- The LHS value
                    y -- float -- The RHS value

        Returns:
            float: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/{operation}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'operation': options.get('operation', None)
        })
        _query_parameters = {
            'x': options.get('x', None),
            'y': options.get('y', None)
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.get(_query_url)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return float(_context.response.raw_body)
