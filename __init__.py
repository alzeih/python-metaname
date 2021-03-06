"""Module for accessing metaname.net api

  Documentation for the Metaname API is at:
  https://metaname.net/api/1.1/doc

Usage::

    >>> client = Client("account_reference", "api_key")
    >>> client.domain_names()
    >>> client.dns_zone("example.com")
    >>> client.create_dns_record("example.com",
            {"name":"www",
                "type":"A",
                "aux":None,
                "ttl":86400,
                "data":"93.184.216.119"})

"""

